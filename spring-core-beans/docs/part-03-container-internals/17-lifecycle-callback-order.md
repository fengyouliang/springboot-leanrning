# 17. 生命周期回调顺序：Aware / BPP / init / destroy（以及 prototype 为什么不销毁）

很多“容器行为”只有把生命周期顺序看清楚才能解释。

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansLifecycleCallbackOrderLabTest.java`

## 1. 一个可断言的顺序（比看日志更可靠）

读者 C 的目标不是“背顺序”，而是：**当你看到一个对象行为不对时，能判断它到底处在生命周期的哪一段、被哪些扩展点改过**。

下面给一个“够你排障”的顺序表（把它当成 `initializeBean` 周边的时间线）：

1. 实例化（constructor / factory method）
2. 属性填充（依赖注入）→ `populateBean`
3. Aware 回调（`BeanNameAware`/`BeanFactoryAware` 等）
4. `BeanPostProcessor#postProcessBeforeInitialization`
5. `@PostConstruct`（由 `InitDestroyAnnotationBeanPostProcessor` 触发）
6. `InitializingBean#afterPropertiesSet`
7. 自定义 initMethod（`@Bean(initMethod=...)`）
8. `BeanPostProcessor#postProcessAfterInitialization`（代理/包装经常在这里发生，见 docs/31）

销毁阶段（容器关闭时，singleton 才会默认触发）：

1. `DestructionAwareBeanPostProcessor#postProcessBeforeDestruction`
2. `@PreDestroy`（同样由注解后处理器触发）
3. `DisposableBean#destroy`
4. 自定义 destroyMethod（`@Bean(destroyMethod=...)`）

> 注意：顺序表的意义是“能定位”，不是“每次都一模一样”。当 BPP 数量与排序变化时（见 docs/14、docs/25），你看到的实际调用栈会变化，但大方向依然稳定。

对应测试：

- `SpringCoreBeansLifecycleCallbackOrderLabTest.singletonLifecycleCallbacks_happenInAStableOrderAroundInitialization()`

实验使用一个记录器把关键阶段串起来：

- constructor
- BeanNameAware / BeanFactoryAware
- BeanPostProcessor.beforeInit
- `@PostConstruct`
- `InitializingBean.afterPropertiesSet`
- `initMethod`
- BeanPostProcessor.afterInit
-（容器关闭时）`@PreDestroy` → `DisposableBean.destroy` → `destroyMethod`

学习重点：

- init callbacks 都发生在 BPP(before) 与 BPP(after) 之间
- destroy callbacks 发生在 context close 阶段

## 2. prototype 为什么默认不走销毁回调？

对应测试：

- `SpringCoreBeansLifecycleCallbackOrderLabTest.prototypeBeans_areNotDestroyedByContainerByDefault()`

prototype 的语义是：

- 容器帮你创建并注入
- **但容器通常不负责管理它的“生命周期终点”**

所以：

- `@PreDestroy` / destroyMethod 可能不会被调用
- 清理资源需要调用方自己管理（或引入额外机制）

## 3. 常见坑

- **坑 1：在 `@PostConstruct` 做重 IO**
  - 会拉长启动时间；也更难测试。

- **坑 2：误以为 prototype 会自动销毁**
  - 你必须知道：谁负责 close/cleanup。

- **坑 3：BeanPostProcessor 本身也是特殊 bean**
  - BPP 会很早被实例化、很早被注册。
  - 因此在 BPP 的构造器里依赖复杂 bean，可能导致“过早创建”与“错过后续处理器”。

## 源码锚点（建议从这里下断点）

- `AbstractAutowireCapableBeanFactory#doCreateBean`：单个 bean 创建主流程（实例化 → 注入 → 初始化）
- `AbstractAutowireCapableBeanFactory#populateBean`：属性填充阶段（`@Autowired/@Resource` 等注入发生在这一段）
- `AbstractAutowireCapableBeanFactory#initializeBean`：初始化阶段（aware → before-init → init callbacks → after-init）
- `DisposableBeanAdapter#destroy`：销毁链路的统一入口（`@PreDestroy/DisposableBean/destroyMethod` 会在这里串起来）
- `AbstractApplicationContext#doClose`：context close 阶段触发销毁回调（prototype 默认不在这里被销毁）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansLifecycleCallbackOrderLabTest.java`
  - `singletonLifecycleCallbacks_happenInAStableOrderAroundInitialization()`
  - `prototypeBeans_areNotDestroyedByContainerByDefault()`

建议断点：

1) 参与实验的目标 bean 构造器：观察“构造器先执行，但此时注入未发生”
2) `AbstractAutowireCapableBeanFactory#initializeBean`：观察 init 回调链如何被串起来
3) `BeanPostProcessor#postProcessBeforeInitialization`（例如 `CommonAnnotationBeanPostProcessor`）：观察 `@PostConstruct` 的触发时机
4) `BeanPostProcessor#postProcessAfterInitialization`：观察它一定发生在 init callbacks 之后（本章自检题的答案）
5) `DisposableBeanAdapter#destroy`：在测试里 close context 时命中，观察销毁回调顺序

你应该看到：

- singleton 的 init callbacks 稳定发生在 BPP(before) 与 BPP(after) 之间
- prototype 在容器 close 时不会被自动 destroy（除非你自己显式管理）

## 排障分流：这是定义层问题还是实例层问题？

- “`@PostConstruct` 没触发/注入为 null” → **优先定义层/基础设施问题**：容器是否具备注解处理器？（见 [12](12-container-bootstrap-and-infrastructure.md)）
- “`@PreDestroy` 没触发” → **优先实例层/生命周期语义问题**：是不是 prototype？context 是否真的 close？（本章第 2 节）
- “BPP 里依赖复杂 bean 导致顺序怪异” → **实例层 + 顺序问题**：BPP 本身会很早创建/注册，必要时拆分依赖（对照 [14](14-post-processor-ordering.md)、[25](25-programmatic-bpp-registration.md)）
- “我以为 destroy 回调一定会执行” → **实例层 + scope 语义问题**：prototype 的销毁不由容器托管（本章第 2 节）

## 4. 一句话自检

- 你能解释清楚：为什么 `postProcessAfterInitialization` 一定发生在 init callbacks 之后吗？
- 你能解释清楚：为什么 prototype 默认不会触发 `@PreDestroy` 吗？
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansLifecycleCallbackOrderLabTest.java`
推荐断点：`AbstractAutowireCapableBeanFactory#initializeBean`、`BeanPostProcessor#postProcessBeforeInitialization`、`DisposableBeanAdapter#destroy`

## 面试常问（生命周期回调顺序）

- 常问：初始化阶段的回调顺序是什么？BPP before/after-init 与 `@PostConstruct` 谁先谁后？
  - 答题要点：constructor → aware → populate（注入）→ BPP before-init → `@PostConstruct` → `afterPropertiesSet` → initMethod → BPP after-init。
- 常见追问：为什么 prototype 默认不会走销毁回调（`@PreDestroy`）？
  - 答题要点：prototype 的生命周期末端默认不由容器托管；容器负责创建，但不负责统一回收（除非自定义 scope/显式销毁）。
