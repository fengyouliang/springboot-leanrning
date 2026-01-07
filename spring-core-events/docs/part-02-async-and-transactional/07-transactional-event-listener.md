# 07. `@TransactionalEventListener`：为什么 after-commit 事件能“等事务提交后再执行”？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**07. `@TransactionalEventListener`：为什么 after-commit 事件能“等事务提交后再执行”？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

很多学习者在事件与事务结合时会遇到一个困惑：

> “我事务都回滚了，为什么监听器还执行了？”

这是因为：

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

建议直接跑：

重点看测试：

- `@EventListener`：事件发生就执行（不关心事务最终命运）
- `@TransactionalEventListener(AFTER_COMMIT)`：只在事务提交后执行（避免回滚场景的副作用）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootBusinessCaseLabTest` / `SpringCoreEventsTransactionalEventLabTest`
- 建议命令：`mvn -pl spring-core-events test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

- 代码入口：`springboot-business-case/src/main/java/com/learning/springboot/bootbusinesscase/events/OrderEventListeners.java`
- 行为断言：`BootBusinessCaseLabTest` 里有两类断言
  - 成功提交：既有 `sync:` 也有 `afterCommit:` 日志
  - 回滚失败：只有 `sync:`，不会出现 `afterCommit:`

```bash
mvn -pl springboot-business-case test
```

- `BootBusinessCaseLabTest#syncListenerRunsEvenWhenTransactionRollsBack_butAfterCommitDoesNot`
- `BootBusinessCaseLabTest#afterCommitListenerRunsOnSuccess`

## 对应 Lab/Test（可运行）

- 入口测试：
  - `spring-core-events/src/test/java/com/learning/springboot/springcoreevents/part02_async_and_transactional/SpringCoreEventsTransactionalEventLabTest.java`
    - `afterCommitListenerRunsOnlyAfterCommit`
    - `afterCommitDoesNotRunOnRollback_butAfterRollbackDoes`
- 推荐运行命令：
  - `mvn -pl spring-core-events -Dtest=SpringCoreEventsTransactionalEventLabTest test`

## F. 常见坑与边界

- `@EventListener` 默认是“同步回调”，它不理解事务边界  
- 事务回滚只影响数据库提交，不会自动撤销你已经执行过的监听器逻辑

## G. 小结与下一章

## 一句话总结

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreEventsTransactionalEventLabTest`
- Test file：`spring-core-events/src/test/java/com/learning/springboot/springcoreevents/part02_async_and_transactional/SpringCoreEventsTransactionalEventLabTest.java`

上一章：[06-async-multicaster](06-async-multicaster.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[90-common-pitfalls](../appendix/90-common-pitfalls.md)

<!-- BOOKIFY:END -->
