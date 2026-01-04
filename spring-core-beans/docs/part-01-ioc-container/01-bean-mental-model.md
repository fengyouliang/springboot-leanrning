# 01. Bean 心智模型：BeanDefinition vs Bean 实例

这一章的目标是先把“Bean 到底是什么”这件事说清楚：**Bean 不是对象本身，而是“容器管理对象的一整套机制”**。如果你脑子里只有“Bean = 被 `@Component` 标注的类”，后面一定会在 Scope、生命周期、代理、自动装配上不断踩坑。

## 1. 你要建立的 3 层心智模型

把 Spring 容器（IoC Container）理解成三层：

1) **配置来源（inputs）**：注解、`@Bean` 方法、`@Import`、XML、程序化注册……
2) **定义层（definitions）**：容器把输入解析成 `BeanDefinition`（以及一堆相关元数据）
3) **实例层（instances）**：容器根据定义创建对象、注入依赖、执行回调，并在合适的时机销毁

一句话概括：

- `BeanDefinition` 描述“如何创建一个 Bean”
- Bean instance 是“创建出来的那个对象”

## 2. BeanDefinition 是什么（以及它通常包含什么）

`BeanDefinition` 可以理解为“对象工厂的配方 + 生命周期/依赖元数据”。常见信息包括（不要求记 API，先记概念）：

- beanName：这个 bean 在容器里的名字
- beanClass / factoryMethod / factoryBeanName：用哪种方式创建实例
- scope：`singleton` / `prototype` / 其他 scope
- lazyInit：是否延迟创建（常见于 `@Lazy`）
- dependsOn：依赖顺序（`@DependsOn`）
- propertyValues / constructorArgs：要注入什么
- autowireCandidate、primary 等候选资格信息

这也是为什么“扩展点”通常分两类：

- **在定义层动手**：例如 BFPP（`BeanFactoryPostProcessor`）可以改 `BeanDefinition`
- **在实例层动手**：例如 BPP（`BeanPostProcessor`）可以包一层代理/修改对象

### 面试常问：BeanDefinition / 原始实例 / 最终暴露对象（三层心智模型）

- 题目：`BeanDefinition`、bean instance、最终 `getBean()` 拿到的对象分别是什么？它们之间有什么关系？
- 追问：为什么说“最终拿到的对象可能不是你写的那个类的实例”？这通常发生在容器的哪个阶段？
- 复现入口（建议先跑再下断点）：
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansContainerLabTest.java`
    - `beanDefinitionIsNotTheBeanInstance()`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansProxyingPhaseLabTest.java`
    - `beanPostProcessorCanReturnAProxyAsTheFinalExposedBean_andSelfInvocationStillBypassesTheProxy()`

## 3. BeanFactory vs ApplicationContext：责任边界

很多学习资料把它们混在一起讲，导致初学者误以为它们是“同一个东西的不同名字”。

- `BeanFactory`：最核心的容器能力（Bean 的创建、依赖注入、Scope、生命周期的骨架）
- `ApplicationContext`：在 `BeanFactory` 之上提供更多“应用层能力”
  - 资源加载（Resource）
  - 国际化（MessageSource）
  - 事件发布（ApplicationEventPublisher）
  - 环境（Environment）
  - 更丰富的自动检测与装配逻辑（配合各种后处理器）

### 面试常问：BeanFactory vs ApplicationContext（层次与 refresh 主线）

- 题目：两者核心差异是什么？为什么 `ApplicationContext` 更适合“应用”，而 `BeanFactory` 更偏“底层容器”？
- 追问：
  - `ApplicationContext#refresh` 相比“只用 BeanFactory”，额外做了哪些事？（事件、多语言、资源加载、环境等）
  - 这些能力分别插入到 `AbstractApplicationContext#refresh` 的哪几个步骤？你会怎么下断点证明？
- 复现入口（可断言 + 可断点，建议从这里 step into `refresh()`）：
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansBeanFactoryVsApplicationContextLabTest.java`
    - `beanFactory_isTheCoreContainer_withoutApplicationLevelFacilities()`
    - `applicationContext_addsEventsMessagesAndResources_andHooksThemIntoRefresh()`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.java`
    - `registerAnnotationConfigProcessors_enablesAutowiredAndPostConstruct()`

在 Spring Boot 应用中，你基本总是在使用 `ApplicationContext`（因为 Boot 启动时创建的就是它的某个实现）。

## 4. 容器启动的高层流程（你至少要能复述）

你不需要背源码，但要能说清楚“发生了什么顺序”。一个典型的容器启动可以粗略理解为：

1) **收集配置**（扫描、解析 `@Configuration`、处理 `@Import` 等）
2) **注册 BeanDefinition** 到 `BeanDefinitionRegistry`
3) **执行 BFPP**：允许在实例化之前调整定义（或再注册一些定义）
4) **注册 BPP**：这些会影响后续 Bean 的创建/初始化
5) **创建单例 Bean**（非 lazy 的单例通常会在 refresh 过程中预实例化）
6) **发布容器就绪相关事件**（这是 `ApplicationContext` 的能力）

注意：**“注册定义”与“创建实例”是两个阶段**。这句话会贯穿你对 Spring 的全部理解。

## 5. 在本模块里如何“看见”这件事

你可以用容器内部实验直接确认“定义不等于实例”：

- 对应实验：`src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansContainerLabTest.java`
  - `beanDefinitionIsNotTheBeanInstance()`

这个实验想传达的是：

- 你可以从 `BeanFactory` 拿到 `BeanDefinition`
- 也可以从容器拿到 `ExampleBean` 实例
- 它们是两种不同概念对象

## 6. 一句话自检

读完这一章，你至少要能回答：

1) “BeanDefinition 和 Bean instance 的区别是什么？”
2) “为什么说 BFPP 更像是在改‘配方’，BPP 更像是在改‘做出来的菜’？”
3) “为什么 Spring Boot 的自动装配本质上就是在某个阶段批量注册 BeanDefinition？”

下一章开始我们会从“BeanDefinition 从哪里来”讲起：扫描、`@Bean`、`@Import`、registrar，以及它们和 Spring Boot 自动装配的关系。

## 7. 深入建议：从“概念正确”到“能定位问题”

如果你觉得这一章“太简单”，通常意味着你已经进入下一阶段：你需要的不再是概念本身，而是**把概念落到可验证的流程与观察点**。

建议你沿着两条线把本章吃透：

### 7.1 把 3 层模型映射到“关键参与者”（源码导航）

- **定义层主角**：`DefaultListableBeanFactory`（保存与管理 `BeanDefinition`）
- **实例层主角**：`AbstractAutowireCapableBeanFactory`（`doCreateBean → populateBean → initializeBean`）
- **扩展点介入**：BDRPP/BFPP/BPP（分别在“多早、改定义还是改实例”上不同）
- **循环依赖相关**：`DefaultSingletonBeanRegistry`（单例缓存与 early reference）

不要求你背源码，但建议你知道“该去哪里看”。更系统的断点与路线见：

- [00. 深挖指南：把“Bean 三层模型”落到源码与断点](00-deep-dive-guide.md)

### 7.2 用实验建立“阶段感”（强烈推荐）

本模块的 Labs 已经把“定义 vs 实例”做成了可重复的实验，你可以用它来建立阶段感：

- `SpringCoreBeansContainerLabTest.beanDefinitionIsNotTheBeanInstance()`

如果你愿意再深入一步（开始进入“为什么注解能工作 / 为什么会被代理 / 为什么会短路”），建议按这个顺序继续读：

1) [12. 容器启动与基础设施处理器](12-container-bootstrap-and-infrastructure.md)（注解能力来自哪些处理器）
2) [14. PostProcessor 顺序](14-post-processor-ordering.md)（很多坑的根源是顺序）
3) [15. 实例化前短路](15-pre-instantiation-short-circuit.md)（为什么有时“还没 new”就拿到对象了）
4) [16. early reference 与循环依赖](16-early-reference-and-circular.md)（循环依赖到底怎么救）

到这里为止，你就不再是“懂概念”，而是能把问题定位到：定义层（注册/顺序/条件）还是实例层（注入/代理/回调）。
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansContainerLabTest.java`
推荐断点：`DefaultListableBeanFactory#getBeanDefinition`、`AbstractBeanFactory#getMergedLocalBeanDefinition`、`AbstractAutowireCapableBeanFactory#doCreateBean`

## 8. 源码解析：把“三层心智模型”落到 Spring 主线

这一节的目标是：你不需要背 Spring 源码，但你必须能把“inputs/definitions/instances”准确映射到**哪类类名、哪段主线、哪几个关键方法**，否则遇到代理/循环依赖/后处理器时会迷路。

> 说明：这里不粘贴 Spring Framework 的大段源码（噪声大且易过拟合版本）。采用“方法名 + 调用链 + 关键状态 + 精简伪代码”的方式解释机制。

### 8.1 definitions：BeanDefinition 存在哪里、什么时候会“变”

**核心落点：`DefaultListableBeanFactory`（DLBF）是定义层的“仓库”。**

- `BeanDefinition` 的注册入口最终都会落到：`BeanDefinitionRegistry#registerBeanDefinition`
- 对 DLBF 来说，最重要的事实是：它内部维护了“beanName → BeanDefinition”的映射（你不需要背字段名，但要知道它存在且会在早期被大量写入）。

为什么你有时会看到“同一个 beanName 的定义好像变了”？常见原因是：

1) **原始定义（raw definition）会被“合并”**：例如 parent/child、`@Bean` 方法元信息等会合成 `RootBeanDefinition`（对应你在 docs/35 看到的 merged definition）
2) **定义会被 BFPP/BDRPP 改写**：发生在实例化之前（refresh 很早期），因此你在 `doCreateBean` 里看到的可能已经不是“最初注册进去的那份 definition”

一个非常实用的分界线：

- `getBeanDefinition(beanName)` 更像“读原始登记信息”
- `getMergedBeanDefinition(beanName)` 更像“读最终配方（包含合并/补全后的元信息）”

### 8.2 instances：实例创建的主线在哪里（instantiate → populate → initialize）

**实例层主线基本都收敛在：`AbstractAutowireCapableBeanFactory#doCreateBean`。**

你可以把它当作一个非常稳定的“阶段框架”（精简伪代码）：

```text
doCreateBean(beanName, mbd):
  beanInstance = createBeanInstance(...)          // instantiate
  if (isSingleton && allowCircular && inCreation):
     addSingletonFactory(beanName, () -> getEarlyBeanReference(...)) // early exposure
  populateBean(beanName, mbd, beanInstance)       // populate (DI happens here)
  exposedObject = initializeBean(beanName, beanInstance, mbd)        // initialize
  registerDisposableIfNecessary(beanName, beanInstance, mbd)         // destroy hooks
  return exposedObject
```

把这条主线记住，你就能把很多“现象”放回正确阶段：

- 注入报错（NoSuch/NoUnique）通常是在 `populateBean` 的依赖解析过程中爆出来的（见 docs/03）
- 生命周期回调链（Aware/@PostConstruct/afterPropertiesSet/initMethod）发生在 `initializeBean`（见 docs/05）
- 循环依赖的 early reference 发生在“实例已经有了，但还没 initialize 完”的窗口期（见 docs/09、docs/16）

### 8.3 最终暴露对象：为什么 getBean() 拿到的可能不是“原始实例”

**关键结论：容器返回的是“最终暴露对象（exposed object）”，它可能在多个点被替换/包装。**

常见的三类替换点（只记住它们存在即可，后续章节会分别深挖）：

1) **实例化前短路**：`resolveBeforeInstantiation` → `postProcessBeforeInstantiation`（见 docs/15）
2) **early reference**：`getEarlyBeanReference`（循环依赖窗口期，见 docs/16）
3) **初始化后替换**：`postProcessAfterInitialization`（最常见的代理产生点，见 docs/31）

这也是为什么你在排障时不能只问“这个类有没有被 new”，而要问：

- “最终暴露对象是什么类型？（接口代理/类代理/原始类？）”
- “它在哪个阶段被替换的？（pre/early/after-init）”

### 8.4 必要时用仓库 src 代码把它“看见”（最小片段）

**例 1：definition != instance（定义层对象和实例层对象不是一个概念）**

来自 `spring-core-beans/src/test/java/.../SpringCoreBeansContainerLabTest.java`（最小片段）：

```java
try (AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SimpleBeanConfig.class)) {
    BeanDefinition beanDefinition = context.getBeanFactory().getBeanDefinition("exampleBean");
    ExampleBean bean = context.getBean(ExampleBean.class);
}
```

**例 2：最终暴露对象可被 BPP 替换成 proxy（按接口能拿到、按实现类可能拿不到）**

来自 `spring-core-beans/src/test/java/.../SpringCoreBeansBeanCreationTraceLabTest.java`：

- 它会在 after-initialization 阶段返回一个 JDK proxy（只实现接口）
- 因此 `context.getBean(WorkService.class)` 成功，但按具体类取可能失败（典型“最终暴露对象 != 原始实例”）
