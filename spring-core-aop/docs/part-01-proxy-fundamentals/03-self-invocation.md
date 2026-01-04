# 03. 自调用（self-invocation）：为什么 `this.inner()` 不会被拦截？

这是 Spring AOP 的经典“入门必踩坑”，而且它不止影响 AOP：事务（`@Transactional`）也会踩同一个坑。

## 现象（在本模块如何复现）

看 `SelfInvocationExampleService`：

- `outer(...)` 和 `inner(...)` 都标了 `@Traced`
- `outer(...)` 内部调用 `inner(...)`

在测试 `SpringCoreAopLabTest#selfInvocationDoesNotTriggerAdviceForInnerMethod` 里：

- 调用 `selfInvocationExampleService.outer("Bob")`
- 你会看到 `InvocationLog` 只记录了一次（只拦截了 `outer`）

如果你想把“怎么修复”也做成可验证的闭环，直接看练习：

- `SpringCoreAopExerciseTest#exercise_makeSelfInvocationTriggerAdvice`

## 原因（一句话版本）

> **内部调用没有经过代理对象**，因此不会进入 advice 链。

更精确地说：

- 外部调用：`proxy.outer(...)` → advice → `target.outer(...)`（此时生效）
- `target.outer(...)` 内部：`this.inner(...)` → 直接调用目标对象方法（绕过 proxy）

## 常见解决思路（按“学习成本”排序）

1) **把 `inner(...)` 抽到另一个 Spring Bean**
   - 外部通过注入另一个 bean 调用，调用链自然会走代理
   - 最推荐（最符合“依赖注入”的风格）

2) **通过“注入自己的代理”来调用自己（中级，工程里常见）**
   - 思路：不要用 `this.inner()`，而是注入一个“指向自己 bean 的引用”，并通过它调用 `inner()`
   - 常见实现：
     - 自己依赖自己（自注入），必要时配合 `@Lazy` 避免循环依赖
     - 用 `ObjectProvider<SelfInvocationExampleService>` 延迟拿到 proxy 再调用
   - 优点：不需要依赖 `AopContext` 的 thread-local 语义，可读性也通常更好

3) **通过代理对象调用自己（进阶，理解机制用）**
   - `exposeProxy` + `AopContext.currentProxy()`（见 [docs/05](05-expose-proxy.md)）
   - 代价：更“技巧化”，容易滥用；但非常适合用来理解“call path 必须走 proxy”

4) **AspectJ 编译期/加载期织入**
   - 不是代理模型，能拦截“类内部调用”
   - 代价：配置更重，不适合作为学习仓库的默认路径

## 你应该得到的结论

当你遇到 “AOP 不生效” 的问题时，排查顺序建议是：

1. bean 是否被代理（`AopUtils.isAopProxy`）
2. 调用入口是否走代理（是否发生自调用）
3. 代理类型/限制（JDK/CGLIB、`final` 等）

## 源码锚点：怎么在断点里证明“inner 根本没进代理”？

最直接的方法是把断点打在“代理接管调用”的入口：

- JDK proxy：`JdkDynamicAopProxy#invoke`
- CGLIB proxy：`CglibAopProxy.DynamicAdvisedInterceptor#intercept`

然后跑：

- `SpringCoreAopLabTest#selfInvocationDoesNotTriggerAdviceForInnerMethod`

你会看到：

- 外部调用 `outer(...)` 会命中代理入口
- `outer(...)` 内部的 `this.inner(...)` 根本不会命中代理入口（因为它是目标对象内部的普通方法调用）
