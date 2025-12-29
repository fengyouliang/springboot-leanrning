# 05. exposeProxy：用 `AopContext.currentProxy()` 绕过自调用（进阶）

这一章的目标不是鼓励你在项目里大量使用 `AopContext`，而是让你把“代理 = 调用入口”这个概念吃透。

## 解决的是什么问题？

自调用绕过代理（见 [docs/03](03-self-invocation.md)）：

- `outer()` 内部调用 `inner()` → 不走 proxy → `inner()` 不被拦截

如果你能在 `outer()` 内部拿到“当前代理对象”，就可以改成：

- `((SelfInvocationExampleService) AopContext.currentProxy()).inner(...)`

这样 `inner(...)` 就会再次走代理链。

## 关键点：`AopContext.currentProxy()` 不是随时可用

它只有在满足两个条件时才工作：

1. **必须开启 exposeProxy**
   - Spring：`@EnableAspectJAutoProxy(exposeProxy = true)`
   - Spring Boot：`application.properties` 里设置 `spring.aop.expose-proxy=true`

2. **必须在 AOP 调用链上下文中调用**
   - 也就是：你需要先进入一个被 AOP 拦截的方法（在 advice 链里），此时 `currentProxy()` 才有意义

## 在本模块的练习入口

看 `SpringCoreAopExerciseTest#exercise_makeSelfInvocationTriggerAdvice`：

- 它提示你开启 exposeProxy，并在 `outer(...)` 内通过 `AopContext.currentProxy()` 调用 `inner(...)`
- 这是一个很好的“理解机制”练习

## 代价与取舍（必须知道）

- 可读性：`AopContext` 会把代码和 AOP 强绑定，不如“抽出到另一个 bean”清晰
- 线程绑定：`currentProxy()` 基于当前线程上下文（更容易产生隐式依赖）

所以在真实项目里更推荐：

> 把需要被拦截的逻辑抽到另一个 Spring Bean，通过注入调用。

