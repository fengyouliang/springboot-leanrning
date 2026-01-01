# 12. 容器启动与基础设施处理器：为什么注解能工作？

这一章回答一个很容易被忽略的问题：

> 你写的 `@Configuration` / `@Bean` / `@Autowired` / `@PostConstruct` 之所以“能工作”，不是因为注解本身有魔法，而是因为 **容器在启动时注册并运行了一组基础设施 BFPP/BPP**。

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansBootstrapInternalsLabTest.java`
- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansResourceInjectionLabTest.java`

## 1. 现象：同样是 Spring 容器，不同启动方式结果不一样

### 1.1 `GenericApplicationContext` 默认不处理注解

如果你直接用 `GenericApplicationContext` 注册 bean：

- `@Autowired` 不会发生（字段仍然是 `null`）
- `@PostConstruct` 不会运行（回调不会被触发）

这不是 bug，而是：你没有把“注解解析与回调”的那套基础设施装进去。

对应测试：

- `SpringCoreBeansBootstrapInternalsLabTest.withoutAnnotationConfigProcessors_autowiredAndPostConstructAreNotApplied()`

### 1.2 注册 annotation processors 后，注解才会被处理

当你调用：

- `AnnotationConfigUtils.registerAnnotationConfigProcessors(context)`

容器会注册一组核心处理器（简化理解）：

- `AutowiredAnnotationBeanPostProcessor`：处理 `@Autowired` / `@Value`
- `CommonAnnotationBeanPostProcessor`：处理 `@Resource` / `@PostConstruct` / `@PreDestroy`
- `ConfigurationClassPostProcessor`：解析 `@Configuration` / `@Bean` / `@Import` 等

对应测试：

- `SpringCoreBeansBootstrapInternalsLabTest.registerAnnotationConfigProcessors_enablesAutowiredAndPostConstruct()`

## 2. `@Bean` 为什么能“变成 BeanDefinition”？

很多人以为：

- 写了 `@Configuration` + `@Bean`，容器就自然知道要注册这些 bean

但实际上：

- 如果没有 `ConfigurationClassPostProcessor`（一个 BFPP），`@Bean` 方法根本不会被解析成额外的 `BeanDefinition`

对应测试（同一个 config class，两种容器启动方式得到不同结果）：

- `SpringCoreBeansBootstrapInternalsLabTest.configurationClassIsNotParsedWithoutConfigurationClassPostProcessor()`

## 3. 常见坑

- **误解 1：注解是语言特性**
  - 注解只是元数据；让它“生效”的是容器启动阶段注册的处理器。

- **误解 2：以为任何 ApplicationContext 都等价**
  - `AnnotationConfigApplicationContext` 默认就带“注解能力”，而 `GenericApplicationContext` 默认不带。

- **误解 3：把“容器没装处理器”当成业务 bug**
  - 学机制时请优先问：当前容器有没有注册对应的 BFPP/BPP？

## 源码锚点（建议从这里下断点）

- `AbstractApplicationContext#refresh`：容器启动总入口；你能在这里建立“先装处理器、再建实例”的时间线
- `AnnotationConfigUtils#registerAnnotationConfigProcessors`：把让注解生效的一组 BFPP/BPP 注册进容器（本章的关键动作）
- `ConfigurationClassPostProcessor#postProcessBeanDefinitionRegistry`：解析 `@Configuration/@Bean/@Import` 并注册额外的 `BeanDefinition`
- `AutowiredAnnotationBeanPostProcessor#postProcessProperties`：属性填充阶段处理 `@Autowired/@Value`（没注册它就不会注入）
- `InitDestroyAnnotationBeanPostProcessor#postProcessBeforeInitialization`：处理 `@PostConstruct/@PreDestroy`（`CommonAnnotationBeanPostProcessor` 基于它）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansBootstrapInternalsLabTest.java`
  - `withoutAnnotationConfigProcessors_autowiredAndPostConstructAreNotApplied()`
  - `registerAnnotationConfigProcessors_enablesAutowiredAndPostConstruct()`

建议断点（按从“现象”到“机制”的顺序）：

1) `SpringCoreBeansBootstrapInternalsLabTest` 的两段测试方法内：对照“注册 processors 前后”的行为差异
2) `AnnotationConfigUtils#registerAnnotationConfigProcessors`：确认哪些基础设施处理器被注册进了 `BeanDefinitionRegistry`
3) `ConfigurationClassPostProcessor#postProcessBeanDefinitionRegistry`：观察 `@Configuration/@Bean` 是在什么时候被解析成定义的
4) `AutowiredAnnotationBeanPostProcessor#postProcessProperties`：观察 field/method 注入发生在“属性填充阶段”，而不是构造阶段
5) `InitDestroyAnnotationBeanPostProcessor#postProcessBeforeInitialization`：观察 `@PostConstruct` 触发点（发生在 init 回调链里）

你应该看到：

- 不注册 processors：上述 3/4/5 的断点不会命中，注入/回调不会发生
- 注册 processors：断点会命中，`@Autowired` 字段被赋值，`@PostConstruct` 被调用

## 排障分流：这是定义层问题还是实例层问题？

- “`@Autowired/@Resource/@PostConstruct` 全都不生效/字段一直是 null” → **优先定义层/基础设施问题**：你是否注册了 annotation processors？（回到本章 Lab）
- “`@Bean` 方法写了但容器里没有这个 bean” → **优先定义层问题**：配置类是否被 `ConfigurationClassPostProcessor` 解析？（可对照 [02](02-bean-registration.md) 与本章断点）
- “注入生效了但选错候选/候选太多” → **优先实例层（依赖解析）问题**：看 `DefaultListableBeanFactory#doResolveDependency`（见 [03](03-dependency-injection-resolution.md) / [33](33-autowire-candidate-selection-primary-priority-order.md)）
- “拿到的对象形态不对（proxy/替身）” → **优先实例层（BPP/代理）问题**：看 [31](31-proxying-phase-bpp-wraps-bean.md) 与 [00](00-deep-dive-guide.md)

## 源码最短路径（call chain）

> 目标：当你怀疑“注解没生效”时，用最短调用链回答两个问题：
>
> 1) 相关处理器有没有被**注册**？（定义层）
> 2) 相关处理器有没有在 bean 创建链路里被**调用**？（实例层）

从 `GenericApplicationContext#refresh()` 走到 `@Autowired/@Resource/@PostConstruct` 的最短主干（只列关键节点）：

- `AbstractApplicationContext#refresh`
  - `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`
    - `ConfigurationClassPostProcessor#postProcessBeanDefinitionRegistry`（如果注册了它：`@Configuration/@Bean/@Import` 才会被解析成更多 `BeanDefinition`）
  - `PostProcessorRegistrationDelegate#registerBeanPostProcessors`
    - **在这里把 `AutowiredAnnotationBeanPostProcessor` / `CommonAnnotationBeanPostProcessor` 等 BPP 注册进 BeanFactory**
  - `AbstractApplicationContext#finishBeanFactoryInitialization`
    - `DefaultListableBeanFactory#preInstantiateSingletons`
      - `AbstractBeanFactory#doGetBean`
        - `AbstractAutowireCapableBeanFactory#doCreateBean`
          - `applyMergedBeanDefinitionPostProcessors`  
            - 一些基础设施 BPP 会在这里“基于 merged BD 缓存元数据”（见 [35](35-merged-bean-definition.md)）
          - `populateBean`
            - `AutowiredAnnotationBeanPostProcessor#postProcessProperties`（`@Autowired/@Value` 注入点解析与赋值，见 [30](30-injection-phase-field-vs-constructor.md)）
            - `CommonAnnotationBeanPostProcessor#postProcessProperties`（`@Resource` 注入）
          - `initializeBean`
            - `InitDestroyAnnotationBeanPostProcessor#postProcessBeforeInitialization`（`@PostConstruct` 触发）

把这条最短链路走通，你会得到一个很稳的定位策略：

- 断点 **没命中 `registerBeanPostProcessors`** → 你根本没走到“装处理器”的阶段（容器启动方式/时机问题）
- 断点命中但 **BPP 列表里没有目标处理器** → 定义层没注册/注册被覆盖/没引入 annotation config processors
- 断点命中且 BPP 列表齐全但 **`postProcessProperties` 没命中** → 你看的 bean 不是走这条创建链路（可能是别的容器/别的 BeanFactory/或已提前创建）

## 固定观察点（watch list）

> 目标：不靠猜，靠固定观察点在 1–2 分钟内确认“注解能力到底装没装、在哪里断了”。

### 1) 先确认：处理器有没有“进 registry”（定义层）

在 `AnnotationConfigUtils#registerAnnotationConfigProcessors` 里 watch/evaluate：

- `registry.containsBeanDefinition("org.springframework.context.annotation.internalConfigurationAnnotationProcessor")`（`ConfigurationClassPostProcessor`）
- `registry.containsBeanDefinition("org.springframework.context.annotation.internalAutowiredAnnotationProcessor")`（`AutowiredAnnotationBeanPostProcessor`）
- `registry.containsBeanDefinition("org.springframework.context.annotation.internalCommonAnnotationProcessor")`（`CommonAnnotationBeanPostProcessor`）

> 说明：这些是 Spring 内部的 “internal*Processor” beanName。你不需要背全，但用它们能非常快地确认“注解能力有没有被装进来”。

### 2) 再确认：处理器有没有“进 BeanFactory”（实例层）

在 `PostProcessorRegistrationDelegate#registerBeanPostProcessors` 里 watch/evaluate：

- `beanFactory.getBeanPostProcessors()`：看最终列表里是否包含 `AutowiredAnnotationBeanPostProcessor` / `CommonAnnotationBeanPostProcessor`

如果你只记一个判断条件，就记这个：

- **`beanFactory.getBeanPostProcessors()` 里没有对应处理器 ⇒ 注解一定不会生效**（后面所有“注入/回调没发生”都能解释）

### 3) 最后确认：目标注解在创建链路里有没有被触发

在 `AbstractAutowireCapableBeanFactory#populateBean` / `#initializeBean` 附近 watch/evaluate：

- 注入相关：`AutowiredAnnotationBeanPostProcessor#postProcessProperties` / `CommonAnnotationBeanPostProcessor#postProcessProperties` 是否命中
- 回调相关：`InitDestroyAnnotationBeanPostProcessor#postProcessBeforeInitialization` 是否命中（`@PostConstruct`）

## 反例（counterexample）

**反例：我用 `GenericApplicationContext` 注册了 bean，容器也能启动，但 `@Autowired/@Resource/@PostConstruct` 全都不生效（字段是 null、回调没跑）。**

最小复现入口（必现）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansBootstrapInternalsLabTest.java`
  - `withoutAnnotationConfigProcessors_autowiredAndPostConstructAreNotApplied()`
- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansResourceInjectionLabTest.java`
  - `withoutAnnotationConfigProcessors_resourceIsIgnored()`

你在断点里应该看到什么（用于纠错）：

- 你没有调用 `AnnotationConfigUtils.registerAnnotationConfigProcessors(...)`
  - 所以 `registerBeanPostProcessors` 阶段看不到 `AutowiredAnnotationBeanPostProcessor` / `CommonAnnotationBeanPostProcessor`
- 因为 BPP 根本没装上：
  - `@Autowired` 的 `postProcessProperties` 不会命中 ⇒ 字段保持 `null`
  - `@Resource` 的 `postProcessProperties` 不会命中 ⇒ 字段保持 `null`
  - `@PostConstruct` 的 `postProcessBeforeInitialization` 不会命中 ⇒ 回调不执行

正确做法（本章成功路径）：

- 要么用 `AnnotationConfigApplicationContext`（默认自带 annotation processors）
- 要么在 `GenericApplicationContext` 中显式调用 `AnnotationConfigUtils.registerAnnotationConfigProcessors(context)` 再 `refresh()`

## 4. 一句话自检

- 你能解释清楚：`@Autowired`/`@PostConstruct`/`@Bean` 分别依赖哪些处理器让它们生效吗？
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansBootstrapInternalsLabTest.java`
推荐断点：`AnnotationConfigUtils#registerAnnotationConfigProcessors`、`ConfigurationClassPostProcessor#processConfigBeanDefinitions`、`AutowiredAnnotationBeanPostProcessor#postProcessProperties`
