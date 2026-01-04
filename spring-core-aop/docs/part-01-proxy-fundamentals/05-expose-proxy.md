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

### 1) 为什么它会“只有在 advice 链里才可用”？

你可以把它理解成：AOP 在执行 advice 链时会把“当前代理”放进一个 thread-local 里。

所以：

- 没有进入 advice 链 → thread-local 没被设置 → 取不到 currentProxy
- 换线程（例如 `@Async`） → thread-local 不会自动传播 → 也可能取不到/取错

这也是为什么它更像一个“调试/理解机制”的工具，而不是日常业务代码的默认选择。

## 在本模块的练习入口

看 `SpringCoreAopExerciseTest#exercise_makeSelfInvocationTriggerAdvice`：

- 它提示你开启 exposeProxy，并在 `outer(...)` 内通过 `AopContext.currentProxy()` 调用 `inner(...)`
- 这是一个很好的“理解机制”练习

## 代价与取舍（必须知道）

- 可读性：`AopContext` 会把代码和 AOP 强绑定，不如“抽出到另一个 bean”清晰
- 线程绑定：`currentProxy()` 基于当前线程上下文（更容易产生隐式依赖）

所以在真实项目里更推荐：

> 把需要被拦截的逻辑抽到另一个 Spring Bean，通过注入调用。

### 一个更工程化的替代方案：自注入（或 ObjectProvider）

如果你确实需要“在同一个类里触发 AOP”，更推荐的写法通常是：

- 让类依赖自己（注入自己这个 bean），必要时配合 `@Lazy` 来避免循环依赖
- 或注入 `ObjectProvider<SelfInvocationExampleService>`，在需要时再获取 proxy 并调用

它们的共同点是：

- 仍然走“通过容器拿到的 bean 引用”，因此会经过 proxy
- 不依赖 `AopContext` 的 thread-local 语义
