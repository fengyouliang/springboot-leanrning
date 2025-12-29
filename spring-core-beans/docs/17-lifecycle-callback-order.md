# 17. 生命周期回调顺序：Aware / BPP / init / destroy（以及 prototype 为什么不销毁）

很多“容器行为”只有把生命周期顺序看清楚才能解释。

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansLifecycleCallbackOrderLabTest.java`

## 1. 一个可断言的顺序（比看日志更可靠）

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

## 4. 一句话自检

- 你能解释清楚：为什么 `postProcessAfterInitialization` 一定发生在 init callbacks 之后吗？
- 你能解释清楚：为什么 prototype 默认不会触发 `@PreDestroy` 吗？
