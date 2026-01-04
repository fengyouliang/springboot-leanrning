# 自测题（Spring Core Tx）

1. `@Transactional` 的“边界”是如何确定的？为什么不等于“方法开始到方法结束”？
2. 为什么自调用（self-invocation）会绕过事务？如何最小复现？
3. 默认回滚规则是什么？`checked exception` 与 `runtime exception` 的差异在哪里？
4. 传播行为（propagation）解决的核心问题是什么？最常见误用是什么？
5. 什么时候应该用 `TransactionTemplate`？如何验证它与注解事务的差异？

