# 06. `@DataJpaTest`：为什么它适合学 JPA（切片测试）

`@DataJpaTest` 是学习 JPA 的绝佳工具，因为它提供了：

- 更小、更快的 Spring Boot 测试上下文（只加载 JPA 相关）
- 默认事务包裹（测试结束自动回滚，减少污染）
- EntityManager / Repository 等关键对象开箱即用

## 在本模块如何验证

看 `BootDataJpaLabTest#dataJpaTestRunsInsideATransaction`：

- `TransactionSynchronizationManager.isActualTransactionActive()` 为 true

这意味着：

- 你的实体通常是 managed 的
- flush/dirty checking 的行为更容易复现与验证

## 练习入口：回滚行为

看 `BootDataJpaExerciseTest#exercise_rollbackBehavior`：

- 目标：演示 `@DataJpaTest` 默认回滚
- 并通过 `@Commit` 或 `@Rollback(false)` 改变行为，再观察差异

## 学习建议

- 学机制优先用 `@DataJpaTest`
- 需要跨层（Web + Service + JPA + Tx）再用 `@SpringBootTest` 或去 capstone 模块练

