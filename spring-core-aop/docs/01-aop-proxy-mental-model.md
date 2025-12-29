# 01. AOP 心智模型：代理（Proxy）+ 入口（Call Path）

Spring AOP 学习最关键的不是“会写一个 `@Aspect`”，而是建立一个稳定的心智模型：

> **AOP 默认基于代理实现**：只有“通过代理对象发起的调用”才会被 advice 包起来。

## 你需要记住的 3 件事

1. **代理对象 ≠ 目标对象**
   - 你注入的 bean 很可能是一个“包装对象”（proxy），而不是你的实现类本身。
   - 这会影响：类型判断（`instanceof`）、`getClass()`、调试时看到的调用栈。

2. **advice 生效的前提：调用必须“经过代理”**
   - 外部（其它 bean / Controller / Test）调用 bean 方法：通常会经过代理 → advice 生效。
   - 同一个类内部 `this.xxx()` 调用：不会经过代理 → advice **不生效**（见 [docs/03](03-self-invocation.md)）。

3. **AOP 的本质是“在调用链上插一段逻辑”**
   - `@Around` 最直观：`joinPoint.proceed()` 前后都能做事（计时、鉴权、日志、事务等）。

## 在本模块如何验证（建议先跑这个）

运行测试：

```bash
mvn -pl spring-core-aop test
```

重点看这些断言：

- `SpringCoreAopLabTest#tracedBusinessServiceIsAnAopProxy`：证明注入的 bean 是代理
- `SpringCoreAopLabTest#adviceIsAppliedToTracedMethod`：证明 `@Traced` 方法被 `TracingAspect` 拦截

## 对照代码（最小闭环）

- `spring-core-aop/src/main/java/.../Traced.java`：标记注解
- `spring-core-aop/src/main/java/.../TracingAspect.java`：`@Around("@annotation(...@Traced)")`
- `spring-core-aop/src/main/java/.../TracedBusinessService.java`：被拦截的目标方法
- `spring-core-aop/src/main/java/.../InvocationLog.java`：用来做“可断言的观察点”（比日志更稳定）

## 一句话总结

当你觉得 AOP “没生效”时，先不要怀疑注解/表达式，第一时间问自己：

> **这次调用有没有走代理？**

