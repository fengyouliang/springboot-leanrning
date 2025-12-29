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

## 4. 一句话自检

- 你能解释清楚：为什么 `afterSingletonsInstantiated` 触发时 lazy bean 可能还没创建吗？
