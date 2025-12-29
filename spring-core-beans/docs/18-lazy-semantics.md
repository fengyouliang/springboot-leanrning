# 18. Lazy：lazy-init bean vs `@Lazy` 注入点（懒代理）

懒加载经常被误用：很多人以为“加了 `@Lazy` 就不会启动慢了”，但实际效果取决于你把 lazy 放在哪里。

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansLazyLabTest.java`

## 1. lazy-init bean：refresh 阶段不创建

对应测试：

- `SpringCoreBeansLazyLabTest.lazyInitBean_isNotInstantiatedDuringRefresh_butCreatedOnFirstGetBean()`

当 bean 定义是 lazy-init：

- refresh 阶段不会创建它
- 第一次 `getBean(...)` 才会创建

## 2. 关键反直觉点：lazy-init 也挡不住“被别人依赖”

对应测试：

- `SpringCoreBeansLazyLabTest.lazyInitDoesNotHelpIfAConsumerEagerlyDependsOnTheBean()`

如果 A（非 lazy）依赖 B（lazy-init）：

- A 的创建需要 B
- 容器会为了创建 A 去创建 B

因此你会看到：

- B 仍然在 refresh 阶段被创建

这能解释很多“我明明标了 lazy，但它还是启动时创建了”的问题。

## 3. `@Lazy` 放在注入点：注入一个 proxy，而不是直接注入目标对象

对应测试：

- `SpringCoreBeansLazyLabTest.lazyInjectionPoint_canDeferCreationOfLazyBeanUntilFirstUse()`

当你把 `@Lazy` 放在依赖注入点：

- 容器会注入一个 proxy
- proxy 在第一次真正调用时，再去容器里解析目标 bean

本实验还配合把目标 bean 标成 lazy-init，从而确保：

- 没有“外部因素”提前创建目标 bean
- 你能清晰观测到：目标 bean 的构造器是在“第一次调用”时才执行

## 4. 常见坑

- **坑 1：以为 `@Lazy` 能让所有依赖都不创建**
  - 如果目标 bean 不是 lazy-init，它仍可能在 refresh 阶段被 pre-instantiate。

- **坑 2：在 proxy 上调用 `toString()` / `equals()` 触发真实创建**
  - 学习阶段尽量不要依赖日志；用断言固定“构造器是否被调用”。

## 5. 一句话自检

- 你能解释清楚：为什么“lazy-init 的 bean”仍可能在 refresh 期间被创建吗？
- 你能解释清楚：注入点 `@Lazy` 的本质是“注入 proxy”吗？
