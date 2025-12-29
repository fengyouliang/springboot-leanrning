# 04：self-invocation：为什么异步有时不生效

## 实验入口

- `BootAsyncSchedulingLabTest#selfInvocationBypassesAsyncAsAPitfall`
- `BootAsyncSchedulingLabTest#callingAsyncThroughAnotherBeanGoesThroughProxy`

## 你应该观察到什么

- 同类内部 `this.asyncMethod()` 调用会绕过代理 → 不切线程
- 通过另一个 bean 调用（走代理） → 能切线程

## 机制解释（Why）

这是 Spring 代理体系的通用坑：
- AOP
- `@Transactional`
- method validation
- method security
- `@Async`

都要求“调用路径必须经过代理”。

