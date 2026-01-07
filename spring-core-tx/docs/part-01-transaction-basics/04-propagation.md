# 04. 传播行为（Propagation）：`REQUIRED` vs `REQUIRES_NEW` 到底差在哪？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**04. 传播行为（Propagation）：`REQUIRED` vs `REQUIRES_NEW` 到底差在哪？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

传播行为解决的问题是：**当一个事务方法调用另一个事务方法时，事务如何“衔接”？**

## 两个最常用的传播行为

### `REQUIRED`（默认）

- 如果当前已有事务：加入当前事务
- 如果当前没有事务：新开一个事务

直觉：**同生共死**（大多数业务场景默认就是它）

### `REQUIRES_NEW`

- 无论当前是否有事务：都新开一个事务
- 外层事务会被挂起，内层事务独立提交/回滚

直觉：**我先把内层这段“单独记账”**

- `requiresNewCanCommitEvenIfOuterTransactionRollsBack`
  - 外层最后抛异常回滚，但 `REQUIRES_NEW` 内层仍然提交
- `requiresNewRollbackDoesNotNecessarilyRollbackOuter_whenCaught`
  - 内层在新事务里失败回滚，但外层 catch 住异常后仍可提交

关键观察点：

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreTxLabTest`
- 建议命令：`mvn -pl spring-core-tx test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 在本模块如何验证

看 `SpringCoreTxLabTest` 的两个用例：

## F. 常见坑与边界

- `REQUIRES_NEW` 不是“魔法保命符”，它只是把事务边界拆开了
- 外层是否回滚，依然取决于外层的异常传播/rollback-only 标记

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreTxLabTest`

上一章：[03-rollback-rules](03-rollback-rules.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[05-transaction-template](../part-02-template-and-debugging/05-transaction-template.md)

<!-- BOOKIFY:END -->
