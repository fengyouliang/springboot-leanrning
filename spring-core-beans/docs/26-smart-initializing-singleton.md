# 26. SmartInitializingSingleton：所有单例都创建完之后再做事

有时候你需要一个“容器已经把主要单例都创建完”的时机点，比如：

- 想扫描容器里所有某类 bean，并建立索引
- 想做一次性校验（例如检查某些 bean 组合是否合法）

Spring 提供了一个非常明确的回调：

- `SmartInitializingSingleton#afterSingletonsInstantiated`

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansSmartInitializingSingletonLabTest.java`

## 1. 现象：回调发生在“非 lazy 单例创建完成之后”

对应测试：

- `SpringCoreBeansSmartInitializingSingletonLabTest.afterSingletonsInstantiated_runsAfterNonLazySingletons_andBeforeLazyBeans()`

实验里：

- `eager` 是普通单例（refresh 时创建）
- `lazy` 是 lazy-init（refresh 时不创建）
- `callback` 实现 `SmartInitializingSingleton`

观察点：

- `afterSingletonsInstantiated` 触发时，`lazy` 还不在 singleton cache（还没创建）
- 之后你第一次 `getBean(lazy)` 才会创建它

## 2. 机制：它是 preInstantiateSingletons 的“收尾回调”

把它理解成：

- 容器在创建完所有非 lazy 单例后，给你一个“做一次性事情”的机会

它比你自己写 `ApplicationRunner` 更贴近容器内部生命周期。

## 3. 常见坑

- **坑 1：误以为它能看到 lazy bean 实例**
  - 它看到的是“已创建的单例”。lazy bean 可能还没创建。

- **坑 2：在回调里触发大量 `getBean`**
  - 会把 lazy bean 全部提前创建，可能导致启动变慢。

## 源码锚点（建议从这里下断点）

- `AbstractApplicationContext#finishBeanFactoryInitialization`：refresh 中“创建单例”阶段的入口（会调用 preInstantiateSingletons）
- `DefaultListableBeanFactory#preInstantiateSingletons`：批量创建非 lazy 单例，并在末尾触发 SmartInitializingSingleton 回调
- `SmartInitializingSingleton#afterSingletonsInstantiated`：你能拿到的“单例都创建完了”的明确时机点
- `DefaultSingletonBeanRegistry#getSingleton`：观察某个 bean 是否已经进入 singleton cache（解释 lazy bean 尚未创建）
- `AbstractBeanFactory#doGetBean`：后续第一次 `getBean(lazy)` 才会触发真正创建

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansSmartInitializingSingletonLabTest.java`
  - `afterSingletonsInstantiated_runsAfterNonLazySingletons_andBeforeLazyBeans()`

建议断点：

1) `DefaultListableBeanFactory#preInstantiateSingletons`：观察非 lazy 单例创建结束后的“收尾回调”位置
2) `SmartInitializingSingleton#afterSingletonsInstantiated`（你在 Lab 里的实现）：观察回调触发时机与可见的单例集合
3) `DefaultSingletonBeanRegistry#getSingleton`：在回调里或断言点查看 lazy bean 是否已在缓存中
4) `AbstractBeanFactory#doGetBean`：在测试后半段第一次 `getBean(lazy)` 时观察真正创建发生在哪里

## 排障分流：这是定义层问题还是实例层问题？

- “回调没触发” → **实例层（生命周期时机）**：该 bean 是否是 singleton？context 是否真的 refresh？
- “回调里拿不到 lazy bean 实例” → **实例层语义**：这是预期；lazy-init 在 refresh 阶段不会创建（对照 [18](18-lazy-semantics.md)）
- “回调里 `getBean` 导致启动变慢” → **实例层行为**：你把 lazy bean 全部提前创建了（本章第 3 节）
- “我以为它等价于 ApplicationRunner” → **生命周期粒度差异**：它更贴近 BeanFactory 的创建阶段（本章第 2 节 + `preInstantiateSingletons`）

## 4. 一句话自检

- 你能解释清楚：为什么 `afterSingletonsInstantiated` 触发时 lazy bean 可能还没创建吗？
