# 自测题（Spring Core Tx）

## 导读

- 本章主题：**自测题（Spring Core Tx）**
- 阅读方式建议：先看“本章要点”，再沿主线阅读；需要时穿插源码/断点，最后跑通实验闭环。

!!! summary "本章要点"

    - 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
    - 如果只看一眼：请先跑一次本章的最小实验，再回到主线对照阅读。


!!! example "本章配套实验（先跑再读）"

    - Lab：`SpringCoreTxLabTest` / `SpringCoreTxPropagationMatrixLabTest` / `SpringCoreTxRollbackRulesLabTest` / `SpringCoreTxSelfInvocationPitfallLabTest`

## 机制主线

这一章用“最小实验 + 数据证据”复盘 4 条主线：

1. 事务边界：代理是否参与、方法内是否真的有事务
2. 回滚规则：runtime vs checked + rollbackFor/noRollbackFor
3. 传播行为：外层/内层的提交与回滚如何交互
4. 排障方法：以“数据是否落库”为最终证据，而不是只看异常/日志

## 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreTxLabTest` / `SpringCoreTxPropagationMatrixLabTest` / `SpringCoreTxRollbackRulesLabTest` / `SpringCoreTxSelfInvocationPitfallLabTest`
- 建议命令：`mvn -pl spring-core-tx test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

> 验证入口（可跑）：`SpringCoreTxLabTest` / `SpringCoreTxPropagationMatrixLabTest` / `SpringCoreTxRollbackRulesLabTest` / `SpringCoreTxSelfInvocationPitfallLabTest`

1. `@Transactional` 的“边界”是如何确定的？为什么不等于“方法开始到方法结束”？
2. 为什么自调用（self-invocation）会绕过事务？如何最小复现？
3. 默认回滚规则是什么？`checked exception` 与 `runtime exception` 的差异在哪里？
4. 传播行为（propagation）解决的核心问题是什么？最常见误用是什么？
5. 什么时候应该用 `TransactionTemplate`？如何验证它与注解事务的差异？
6. `MANDATORY` 的设计目的是什么？当你在“无事务”调用它时会发生什么？对应哪条可复现测试？
7. `NEVER` 的设计目的是什么？当你在“有事务”调用它时会发生什么？对应哪条可复现测试？
8. `NESTED` 与 `REQUIRES_NEW` 的核心区别是什么？你如何用最小对照用例证明它们的差异？
9. 为什么“内层抛异常但外层 catch 住”可能导致最终提交？你如何判断 outer 是否被标记为 rollback-only？
10. 为什么排查事务问题时，建议以“数据是否落库/行数变化”作为最终证据，而不是只看异常或日志？

## 常见坑与边界

### 坑点 1：只看异常不看数据，导致对 commit/rollback 的判断经常反过来

- Symptom：你以为回滚了，但表里数据还在；或你以为提交了，但数据没落库
- Root Cause：异常只是触发条件之一；最终结果由事务边界、回滚规则、传播行为共同决定
- Verification：
  - runtime 回滚：`SpringCoreTxLabTest#rollsBackOnRuntimeException`
  - checked 默认不回滚：`SpringCoreTxLabTest#checkedExceptionsDoNotRollbackByDefault`
  - REQUIRES_NEW 独立提交：`SpringCoreTxLabTest#requiresNewCanCommitEvenIfOuterTransactionRollsBack`
- Fix：把“行数变化/标签写入”作为最终证据链（本模块 tests 已提供），先锁住事实再讨论机制

## 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreTxLabTest` / `SpringCoreTxPropagationMatrixLabTest` / `SpringCoreTxRollbackRulesLabTest` / `SpringCoreTxSelfInvocationPitfallLabTest`

上一章：[90-common-pitfalls](90-common-pitfalls.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[Docs TOC](../README.md)

<!-- BOOKIFY:END -->
