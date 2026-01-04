# 06. Debug / 观察：如何“看见”代理与切点

学习 AOP 时，最怕的不是概念难，而是“感觉它在工作，但我看不见”。这一章给出一套可复用的观察方法。

## 1) 先判断 bean 是否为代理

在测试/代码里直接断言：

- `AopUtils.isAopProxy(bean)`：是不是代理
- `AopUtils.isJdkDynamicProxy(bean)`：是不是 JDK 代理
- `AopUtils.isCglibProxy(bean)`：是不是 CGLIB 代理

本模块的 `SpringCoreAopLabTest` 已经给了现成例子。

### 1.1 进一步：怎么看“真实目标类型”？

当你在调试器里看到 `com.sun.proxy.$ProxyXX` 或 `$$SpringCGLIB$$`，不要直接用 `getClass()` 下结论。

更稳定的做法是：

- `AopUtils.getTargetClass(bean)`：获取目标类型（对 proxy 友好）
- `AopProxyUtils.ultimateTargetClass(bean)`：追到最终目标类型（对多层代理更友好）

## 2) 不要只靠日志：用“可断言的观察点”

`TracingAspect` 里除了 `System.out.println(...)`，更关键的是：

- 它把方法签名写入了 `InvocationLog`
- 测试通过断言 `InvocationLog` 来判断“是否拦截、拦截了谁”

这比“看控制台输出顺序”更稳定，也更适合学习。

### 2.1 想看得更细：把 advisor/拦截链也“可视化”

如果你想更深入（读者 C 目标），可以用 `Advised` 接口观察 proxy 的内部结构：

- `bean instanceof Advised` 为 true（大多数 Spring AOP proxy 都是）
- `((Advised) bean).getAdvisors()`：查看这个 bean 上挂了哪些 advisor

这对于排查“为什么这个 bean 没被增强”特别有用：你能直观看到 advisor 列表是空还是非空。

### 2.2 再往前一步：区分“单 proxy 多 advisor”还是“多层 proxy（套娃）”

真实项目里你经常会把“叠加”理解成“很多层 proxy”，但 Spring 的主流形态其实是：

- **一个 proxy 上挂多个 advisors**（事务/缓存/安全/自定义切面本质都在 advisors 列表里）

只有在下面场景才更容易出现套娃：

- 你显式用 `ProxyFactory` 再包一层
- 存在多个会返回替身对象的 BPP，且顺序导致互相包裹（scoped proxy 等基础设施也可能参与）

快速判断方法：

1. 先看 `bean instanceof Advised`
2. 再看 `((Advised) bean).getTargetSource().getTarget()` 返回的 target 是否还是 AOP proxy

配套章节：见 [docs/09](09-multi-proxy-stacking.md)。

## 3) 验证切点是否命中（从最小切点开始）

建议学习路径：

1. 先用最小切点（例如 `@annotation(Traced)`）确保你“能拦截”
2. 再尝试把切点换成更通用表达式（例如 `execution(...)`），对照命中范围变化

练习入口：`SpringCoreAopExerciseTest#exercise_changePointcutStyle`

如果你经常误判（尤其是 this vs target），建议直接做这个 Lab：

- `SpringCoreAopPointcutExpressionsLabTest`（JDK/CGLIB 下命中差异可断言）

配套章节：见 [docs/08](08-pointcut-expression-system.md)。

## 4) 遇到“不拦截”的排查顺序（经验）

1. 调用入口是否走代理（是否自调用）
2. 目标方法是否能被拦截（`final/private` 等限制）
3. proxy 上是否挂了你期望的 advisor（`Advised#getAdvisors()`）
4. 切点表达式是否覆盖到目标方法（必要时从最小切点回退验证）
5. 代理类型是否与你的注入/获取方式匹配（JDK vs CGLIB）
6. 是否存在多层 proxy（你拿到的是 outer 还是 inner？）

## 5) 源码断点建议（够用版）

当你要把问题定位到源码层面，建议从两条主线各打一组断点：

### 5.1 “proxy 是怎么来的”（容器阶段）

- `PostProcessorRegistrationDelegate#registerBeanPostProcessors`（确认 AutoProxyCreator 作为 BPP 被注册）
- `AbstractAutoProxyCreator#postProcessAfterInitialization`
- `AbstractAutoProxyCreator#wrapIfNecessary`
- `DefaultAopProxyFactory#createAopProxy`

如果你要进一步看清“advisor 是怎么筛出来的”，加这两个断点（命中频繁，建议加条件）：

- `AbstractAdvisorAutoProxyCreator#findEligibleAdvisors`
- `AopUtils#canApply`

### 5.2 “advice 链是怎么跑的”（调用阶段）

- `JdkDynamicAopProxy#invoke` / `CglibAopProxy.DynamicAdvisedInterceptor#intercept`
- `DefaultAdvisorChainFactory#getInterceptorsAndDynamicInterceptionAdvice`
- `ReflectiveMethodInvocation#proceed`

> 读者 C/D 目标（看懂嵌套关系）：建议配合 `SpringCoreAopProceedNestingLabTest` 或 `SpringCoreAopMultiProxyStackingLabTest`，在 `proceed()` 里观察：
>
> - `interceptorsAndDynamicMethodMatchers`（链条顺序）
> - `currentInterceptorIndex`（执行到哪一层）

对应章节：

- 如果你想系统跑一遍断点闭环：见 [00 深挖指南](00-deep-dive-guide.md)
