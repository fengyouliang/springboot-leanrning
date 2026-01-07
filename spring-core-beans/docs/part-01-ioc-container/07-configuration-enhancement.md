# 07. `@Configuration` 增强与 `@Bean` 语义（proxyBeanMethods）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**07. `@Configuration` 增强与 `@Bean` 语义（proxyBeanMethods）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

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

建议先把“现象”做成可断言的闭环（别靠日志猜）：

### 2.1 你到底在对比什么？

两种模式都能把 `@Bean` 注册进容器；差异在于：**配置类自身是否会被增强（enhance）**，从而拦截 `@Bean` 方法调用。

- `@Configuration(proxyBeanMethods=true)`（默认）
  - 配置类会被 CGLIB 增强（你常会在类名里看到 `$$SpringCGLIB$$`）。
  - 在同一个配置类里，`@Bean` 方法互相调用时，会被拦截并改成 **从容器取 bean**。
  - 结果：你在 `@Bean` 方法里调用另一个 `@Bean` 方法，仍能保持 singleton 语义（同一个实例）。
- `@Configuration(proxyBeanMethods=false)`
  - 配置类不会拦截 `@Bean` 方法调用。
  - 在配置类内部互相调用 `@Bean` 方法，本质就是 **普通 Java 方法调用**。
  - 结果：你可能 new 出“额外对象”，即使容器里的对应 bean 依然是 singleton。

> 关键点：`proxyBeanMethods=false` 不是“Bean 变多例”，而是“你在配置类里手写的互调绕过了容器语义”。

对应测试：

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

- 配置类解析与增强入口：
  - `ConfigurationClassPostProcessor#postProcessBeanFactory`
  - `ConfigurationClassEnhancer#enhance`
- `@Bean` 方法拦截入口（proxyBeanMethods=true 才会走到）：
  - `ConfigurationClassEnhancer.BeanMethodInterceptor#intercept`（内部类名可能随版本略有变化）

### 4.1 推荐观察点（watch list）

## 5. 你应该能回答的 2 个问题

1) `proxyBeanMethods` 影响的到底是什么？（提示：不是“这个 bean 是否是单例”，而是“配置类里方法调用会不会走容器”）
2) 为什么在大规模应用里，经常把 `proxyBeanMethods` 设为 false？

## 面试常问（`@Configuration(proxyBeanMethods=...)` 的语义）

- 常问：`proxyBeanMethods=true/false` 有什么差异？为什么 `false` 可能出现“额外实例”？
  - 答题要点：`true` 时配置类被增强，`@Bean` 方法互调会被拦截并走容器缓存，保持单例语义；`false` 时互调是普通 Java 调用，可能 new 出额外对象。
- 常见追问：在工程里如何避免误用？
  - 答题要点：避免在 `@Bean` 方法体内直接调用另一个 `@Bean` 方法；优先使用方法参数注入或构造注入，让依赖解析回到容器。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreBeansContainerLabTest`
- 建议命令：`mvn -pl spring-core-beans test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 0. 复现入口（可运行）

- 入口测试（推荐先跑通再下断点）：
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansContainerLabTest.java`
- 推荐运行命令：
  - `mvn -pl spring-core-beans -Dtest=SpringCoreBeansContainerLabTest test`

## 2. 本模块的实验：一对比就明白

- 对比入口（直接从测试方法开始打断点）：
  - `SpringCoreBeansContainerLabTest#configurationProxyBeanMethodsTruePreservesSingletonSemanticsForBeanMethodCalls`
  - `SpringCoreBeansContainerLabTest#configurationProxyBeanMethodsFalseAllowsDirectMethodCallToCreateExtraInstance`
- 你要观察的不是“能不能注入”，而是 **配置类内部 `@Bean` 方法互相调用时：返回的是容器 singleton，还是一个新的 Java 对象**。

- `SpringCoreBeansContainerLabTest.configurationProxyBeanMethodsTruePreservesSingletonSemanticsForBeanMethodCalls()`
- `SpringCoreBeansContainerLabTest.configurationProxyBeanMethodsFalseAllowsDirectMethodCallToCreateExtraInstance()`

## 4. 源码锚点（建议从这里下断点）

如果你想把 `proxyBeanMethods` 的本质打穿（读者 C 目标），建议至少走一遍下面的断点闭环：

- 配置类 bean 的运行时 class：是否出现 `$$SpringCGLIB$$`
- `@Bean` 方法互调时的调用栈：是否进入 `BeanMethodInterceptor`

下一章我们讲另一个“名字相同但拿到的东西不同”的概念：`FactoryBean`。
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansContainerLabTest.java`
推荐断点：`ConfigurationClassPostProcessor#postProcessBeanFactory`、`ConfigurationClassEnhancer#enhance`

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreBeansContainerLabTest`
- Test file：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansContainerLabTest.java`

上一章：[06. 容器扩展点：BFPP vs BPP（以及它们能/不能做什么）](06-post-processors.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[08. FactoryBean：product vs factory（& 前缀）](08-factorybean.md)

<!-- BOOKIFY:END -->
