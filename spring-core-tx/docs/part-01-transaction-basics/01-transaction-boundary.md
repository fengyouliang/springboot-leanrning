# 01. 事务边界（Transaction Boundary）：你到底在“保护”哪一段代码？

## 导读

- 本章主题：**01. 事务边界（Transaction Boundary）：你到底在“保护”哪一段代码？**
- 阅读方式建议：先看“本章要点”，再沿主线阅读；需要时穿插源码/断点，最后跑通实验闭环。

!!! summary "本章要点"

    - 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
    - 如果只看一眼：请先跑一次本章的最小实验，再回到主线对照阅读。


!!! example "本章配套实验（先跑再读）"

    - Lab：`SpringCoreTxLabTest`

## 机制主线

## 在本模块的最小闭环

看 `AccountService`：

对应测试：

## 你需要记住的 3 件事

## 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreTxLabTest`
- 建议命令：`mvn -pl spring-core-tx test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

- `createTwoAccounts()`：成功 → commit → 表里有两行
- `createTwoAccountsThenFail()`：抛运行时异常 → rollback → 表里没有行

- `SpringCoreTxLabTest#commitsOnSuccess`
- `SpringCoreTxLabTest#rollsBackOnRuntimeException`

2. **回滚与否取决于异常是否“逃逸出边界”**
   - 抛出运行时异常并向外传播：默认回滚
   - 异常被你 catch 住了：默认会提交（除非你显式标记 rollback-only，见 [90. common-pitfalls](../appendix/90-common-pitfalls.md)）

## 常见坑与边界

事务学习最重要的是先把概念落地：**事务边界** 是你定义的“原子单元”。

> 事务边界 = “从哪里开始”到“哪里结束”这一段逻辑，要么全部成功提交，要么全部失败回滚。

1. **事务边界通常是“方法级别”的**
   - 声明式事务（`@Transactional`）默认就是围绕方法的 begin/commit/rollback

3. **事务边界不是“语法糖”，它依赖代理机制**
   - `@Transactional` 的生效条件见 [02. transactional-proxy](02-transactional-proxy.md)

## 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreTxLabTest`

上一章：[00-deep-dive-guide](../part-00-guide/00-deep-dive-guide.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[02-transactional-proxy](02-transactional-proxy.md)

<!-- BOOKIFY:END -->
