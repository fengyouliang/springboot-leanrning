# 05. 程序化事务：为什么 `TransactionTemplate` 在学习阶段很有价值？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**05. 程序化事务：为什么 `TransactionTemplate` 在学习阶段很有价值？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

声明式事务（`@Transactional`）的优点是“用起来很爽”，但学习阶段往往会隐藏机制。

`TransactionTemplate` 的优点是把 commit/rollback 的控制权暴露出来：

它演示了两次执行：

1. 正常执行：插入成功 → 提交 → 能查到数据
2. `status.setRollbackOnly()`：显式标记回滚 → 最终查不到数据

## 学习建议

- 学完 `@Transactional` 后，用 `TransactionTemplate` 复写一遍同样的场景  
  你会更清楚“事务管理器到底在干什么”。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreTxLabTest`
- 建议命令：`mvn -pl spring-core-tx test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 在本模块如何验证

看测试：`SpringCoreTxLabTest#transactionTemplateAllowsProgrammaticCommitOrRollback`

## F. 常见坑与边界

- 你能清楚看到：什么时候提交、什么时候标记回滚
- 你能把“事务边界”写成显式代码（帮助建立直觉）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreTxLabTest`

上一章：[04-propagation](../part-01-transaction-basics/04-propagation.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[06-debugging](06-debugging.md)

<!-- BOOKIFY:END -->
