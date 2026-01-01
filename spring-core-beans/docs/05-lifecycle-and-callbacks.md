# 05. 生命周期：初始化、销毁与回调（@PostConstruct/@PreDestroy 等）

这一章解决两个问题：

1) **Bean 从“还不存在”到“可以被使用”经历了什么阶段？**
2) 你写的各种回调（`@PostConstruct` / `@PreDestroy` / `initMethod` …）到底在什么时机执行？

## 1. 一个典型 Bean 的生命周期（高层版）

如果你只记住一句话：**生命周期 = instantiate → populate → initialize → (use) → destroy**。

但读者 C（源码级）需要更具体：你至少要能把“高层版”映射到 Spring 的关键方法名与扩展点，否则一旦遇到代理/循环依赖/后处理器介入，你会完全失去定位能力。

### 1.1 源码级时间线（建议能复述）

下面这条时间线不是为了背源码，而是为了让你在断点里“认路”：

1. **实例化（instantiate）**
   - 入口常见在 `AbstractAutowireCapableBeanFactory#createBean` / `doCreateBean`
   - 关注点：构造器选择、工厂方法、`Supplier`、`FactoryBean` 等
2. **依赖注入/属性填充（populate properties）**
   - 关键方法：`AbstractAutowireCapableBeanFactory#populateBean`
   - 关注点：`@Autowired` 解析、候选选择、`@Value` 占位符解析（见 docs/03、docs/34）
3. **初始化（initialize）**
   - 关键方法：`AbstractAutowireCapableBeanFactory#initializeBean`
   - Aware：`BeanNameAware`/`BeanFactoryAware` 等
   - BPP before-init：`BeanPostProcessor#postProcessBeforeInitialization`
   - `@PostConstruct`：由 `InitDestroyAnnotationBeanPostProcessor` 触发（见 docs/12）
   - `InitializingBean#afterPropertiesSet`
   - `@Bean(initMethod=...)`
   - BPP after-init：`BeanPostProcessor#postProcessAfterInitialization`（**代理通常在这里产生**，见 docs/31）
4. **销毁（destroy）**
   - 发生在容器关闭（或 scope 结束）时
   - 关键路径：`DefaultSingletonBeanRegistry#destroySingletons` → `DisposableBeanAdapter#destroy`
   - `@PreDestroy` / `DisposableBean#destroy` / `@Bean(destroyMethod=...)`

> 重要提醒：`@PostConstruct/@PreDestroy` 不是 Java 语法“自带”的生命周期，它依赖容器注册了对应的后处理器；这也是为什么理解 docs/06（post-processors）与 docs/12（基础设施处理器）非常关键。

把一个 bean 的创建过程粗略拆成：

1) 实例化（constructor）
2) 依赖注入（populate properties / resolve dependencies）
3) 各种 Aware 回调（告诉 bean 容器信息）
4) 初始化前后回调（BPP 可能介入）
5) 初始化方法（`@PostConstruct` / `afterPropertiesSet` / `initMethod`）
6) 初始化后回调（BPP 可能返回代理）

销毁阶段（当容器关闭时）：

1) `@PreDestroy` / `DisposableBean.destroy` / `destroyMethod`

关键点：

- **BPP 可能改变最终暴露给外界的对象**（比如返回代理）
- **prototype 默认不会走销毁回调**（因为容器不负责其生命周期终点）

## 2. 本模块的可观测例子：`LifecycleLogger`

代码：`src/main/java/com/learning/springboot/springcorebeans/LifecycleLogger.java`

- `@PostConstruct`：容器启动初始化时执行
- `@PreDestroy`：容器关闭时执行（例如应用退出）

你可以通过：

- 运行：`mvn -pl spring-core-beans spring-boot:run`
- 观察控制台输出：
  - `LifecycleLogger: @PostConstruct called`

以及通过测试确认：

- `SpringCoreBeansLabTest.postConstructRunsDuringContextInitialization()`

## 3. 常见生命周期回调方式（按“推荐度/常见度”）

### 3.1 `@PostConstruct` / `@PreDestroy`（推荐，最直观）

优点：

- 与业务代码耦合低（不需要实现 Spring 接口）
- 语义清晰

注意：

- 回调方法通常不应有参数
- 不建议做重 IO/长耗时工作（会拉长启动/关闭时间）

### 3.2 `InitializingBean` / `DisposableBean`（了解即可）

优点：Spring 原生接口  
缺点：让业务类依赖 Spring 接口（耦合）

### 3.3 `@Bean(initMethod=..., destroyMethod=...)`（配置级别控制）

适用场景：

- 你不想修改第三方类源码
- 你想集中管理初始化/销毁方法

## 4. 生命周期与 Scope 的交互（重点）

- singleton：通常在容器 refresh 时创建（除非 `@Lazy`）
- prototype：在你向容器请求它时创建（可能发生在注入时、也可能发生在 `ObjectProvider.getObject()` 调用时）

销毁回调：

- singleton：容器关闭时触发
- prototype：容器通常不触发（需要调用方自己管理）

这也是为什么 prototype 更像“容器帮你 new，一次性交付”，而不是“完整托管生命周期”。

## 源码锚点（建议从这里下断点）

想把生命周期“看见”，你至少需要这几个断点入口：

- 创建主线：`AbstractAutowireCapableBeanFactory#doCreateBean`
- 注入主线：`AbstractAutowireCapableBeanFactory#populateBean`
- 初始化主线：`AbstractAutowireCapableBeanFactory#initializeBean`、`invokeInitMethods`
- 销毁主线：`DefaultSingletonBeanRegistry#destroySingletons`、`DisposableBeanAdapter#destroy`

## 断点闭环（用本仓库 Lab/Test 跑一遍）

建议直接跑并断点：

- `SpringCoreBeansLifecycleCallbackOrderLabTest#singletonLifecycleCallbacks_happenInAStableOrderAroundInitialization`
- `SpringCoreBeansLifecycleCallbackOrderLabTest#prototypeBeans_areNotDestroyedByContainerByDefault`

你应该能在断点里明确验证：

- 初始化阶段的“BPP → @PostConstruct → afterPropertiesSet → initMethod → BPP after-init”顺序
- 为什么 prototype 默认不会走销毁回调（见 docs/17 的进一步解释）

## 5. 你应该能回答的 3 个问题

1) `@PostConstruct` 与依赖注入的先后顺序是什么？
2) 为什么 prototype 的 `@PreDestroy` 可能不会被调用？
3) 为什么 BPP 经常与生命周期放在一起讲？

下一章我们专门讲扩展点：BFPP/BPP，它们就是影响“定义层/实例层”的关键入口。
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansLifecycleCallbackOrderLabTest.java`
推荐断点：`AbstractAutowireCapableBeanFactory#initializeBean`、`CommonAnnotationBeanPostProcessor#postProcessBeforeInitialization`、`DisposableBeanAdapter#destroy`
