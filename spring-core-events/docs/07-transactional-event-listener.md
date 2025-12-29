# 07. `@TransactionalEventListener`：为什么 after-commit 事件能“等事务提交后再执行”？

很多学习者在事件与事务结合时会遇到一个困惑：

> “我事务都回滚了，为什么监听器还执行了？”

这是因为：

- `@EventListener` 默认是“同步回调”，它不理解事务边界  
- 事务回滚只影响数据库提交，不会自动撤销你已经执行过的监听器逻辑

为了解决这个问题，Spring 提供了 `@TransactionalEventListener`：

> 把监听器的触发时机绑定到事务生命周期（例如 AFTER_COMMIT）。

## 你需要记住的 2 种监听器

1) `@EventListener`（默认同步）

- 事件发布后立刻执行（在同一调用链里）
- 即使外层事务最终回滚，监听器也已经执行过了

2) `@TransactionalEventListener(phase = AFTER_COMMIT)`

- 事件先“挂起”，等事务提交后再触发
- 如果事务回滚，AFTER_COMMIT 监听器不会执行

## 在本仓库如何“看见”差异（推荐用 capstone 模块）

这个机制在 `springboot-business-case` 里已经集成好了（更接近真实业务）：

- 代码入口：`springboot-business-case/src/main/java/com/learning/springboot/bootbusinesscase/events/OrderEventListeners.java`
- 行为断言：`BootBusinessCaseLabTest` 里有两类断言
  - 成功提交：既有 `sync:` 也有 `afterCommit:` 日志
  - 回滚失败：只有 `sync:`，不会出现 `afterCommit:`

建议直接跑：

```bash
mvn -pl springboot-business-case test
```

重点看测试：

- `BootBusinessCaseLabTest#syncListenerRunsEvenWhenTransactionRollsBack_butAfterCommitDoesNot`
- `BootBusinessCaseLabTest#afterCommitListenerRunsOnSuccess`

## 一句话总结

- `@EventListener`：事件发生就执行（不关心事务最终命运）
- `@TransactionalEventListener(AFTER_COMMIT)`：只在事务提交后执行（避免回滚场景的副作用）

