# 90. 常见坑清单（建议反复对照）

## 坑 1：同类自调用导致 `@Transactional` 不生效

- 现象：你给 `inner()` 加了 `@Transactional`，但从 `outer()` 调 `inner()` 时事务没生效
- 原因：和 AOP 一样，自调用绕过代理
- 对照：`SpringCoreTxExerciseTest#exercise_selfInvocation`

## 坑 2：异常被 catch 住，结果没有回滚

- 现象：你以为“抛过异常”就会回滚，但实际提交了
- 原因：事务是否回滚取决于异常是否逃逸出事务边界，或是否显式标记 rollback-only
- 建议：学习阶段优先用“查表行数”做验证，不要只看异常

## 坑 3：checked exception 默认不回滚

- 对照：见 [docs/03](03-rollback-rules.md)
- 解决：显式写 `rollbackFor`

## 坑 4：`REQUIRES_NEW` 不是“神奇回滚开关”

- 它只是把事务边界拆成两段：内层提交/回滚不直接决定外层
- 对照：见 [docs/04](04-propagation.md)

## 坑 5：事务=代理，因此也会受到代理限制

- `final` 方法拦截不到（CGLIB 情况）
- private 方法通常也不会被拦截
- 对照：AOP 模块的 [spring-core-aop/docs/04](../../spring-core-aop/docs/04-final-and-proxy-limits.md)

