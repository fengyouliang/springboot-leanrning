# 07. `@Configuration` 增强与 `@Bean` 语义（proxyBeanMethods）

这一章解释一个经常让人“以为 Spring 坏了”的现象：

> 为什么在 `@Configuration` 里调用另一个 `@Bean` 方法，有时会得到同一个实例，有时会 new 出一个新实例？

答案就在 `proxyBeanMethods`。

## 1. 两种配置方式的核心差异

`@Configuration(proxyBeanMethods = true)`（默认 true 的经典行为）：

- Spring 会对配置类做增强（通常是 CGLIB 子类）
- 当你调用 `@Bean` 方法时，会被拦截并重定向到容器
- 因此即便你在 `@Bean` 方法里直接调用另一个 `@Bean` 方法，也能维持“单例语义”

`@Configuration(proxyBeanMethods = false)`（Lite 模式 / 更偏性能）：

- Spring 不会为“方法调用语义”提供额外保障
- 你在方法体里直接调用另一个 `@Bean` 方法，就是一次普通 Java 方法调用
- 这可能会产生额外实例（绕过容器缓存）

## 2. 本模块的实验：一对比就明白

对应测试：

- `SpringCoreBeansContainerLabTest.configurationProxyBeanMethodsTruePreservesSingletonSemanticsForBeanMethodCalls()`
- `SpringCoreBeansContainerLabTest.configurationProxyBeanMethodsFalseAllowsDirectMethodCallToCreateExtraInstance()`

你会看到：

- proxy=true：`configB()` 内调用 `configA()`，拿到的是容器里的同一个 `ConfigA`
- proxy=false：方法体直接调用导致 new 出另一个 `ConfigA`

## 3. 最推荐的写法：用“方法参数”声明依赖

如果你写：

```java
@Bean
ConfigB configB(ConfigA a) {
  return new ConfigB(a);
}
```

那么：

- 依赖解析由容器完成
- 不需要在方法体里调用另一个 `@Bean` 方法
- `proxyBeanMethods=false` 也能保持语义正确

这也是 Spring Boot / 自动配置里非常常见的写法：性能更好、语义更清晰。

## 4. 你应该能回答的 2 个问题

1) `proxyBeanMethods` 影响的到底是什么？（提示：不是“这个 bean 是否是单例”，而是“配置类里方法调用会不会走容器”）
2) 为什么在大规模应用里，经常把 `proxyBeanMethods` 设为 false？

下一章我们讲另一个“名字相同但拿到的东西不同”的概念：`FactoryBean`。
