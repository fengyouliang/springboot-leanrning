# 06. Debug / 观察：如何判断“当前是否真的有事务”？

## 导读

- 本章主题：**06. Debug / 观察：如何判断“当前是否真的有事务”？**
- 阅读方式建议：先看“本章要点”，再沿主线阅读；需要时穿插源码/断点，最后跑通实验闭环。

!!! summary "本章要点"

    - 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
    - 如果只看一眼：请先跑一次本章的最小实验，再回到主线对照阅读。


!!! example "本章配套实验（先跑再读）"

    - Lab：`SpringCoreTxLabTest`

## 机制主线

事务相关的学习痛点通常是：你以为有事务，但其实没有；或者你以为回滚了，但其实提交了。

这一章给出几个“可落地的观察手段”。

## 1) 直接问 Spring：当前是否有事务？

最简单的判断方式是：

- `TransactionSynchronizationManager.isActualTransactionActive()`

## 2) 看 SQL/数据，而不是只看异常

事务最终影响的是“数据是否落库”：

- 一次插入 + 抛异常，最后查表行数（是否回滚）
- 这是最直观、最不容易误判的方式

## 3) 观察传播行为：用“不同 owner 写入”做标签

本模块的做法值得复用：

- outer 写 `outer`，inner 写 `inner`
- 你能直接从表里看到哪段提交了、哪段回滚了

## 4)（可选）打开事务日志

如果你需要更细粒度观察，可以在模块的 `application.properties` 中设置日志级别（学习用即可）：

## 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreTxLabTest`
- 建议命令：`mvn -pl spring-core-tx test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

本模块在 `SpringCoreTxLabTest#transactionsAreActiveInsideTransactionalMethods` 已经验证了这一点。

- `logging.level.org.springframework.transaction=DEBUG`
- `logging.level.org.springframework.jdbc.datasource=DEBUG`

## 常见坑与边界

### 坑点 1：看到 `@Transactional` 就以为“肯定有事务”，忽略代理边界与 self-invocation

- Symptom：你以为当前方法在事务里，但 `isActualTransactionActive()` 为 false，或异常后数据仍落库
- Root Cause：`@Transactional` 依赖代理；自调用/绕开 Spring 管理的 bean 会让拦截器不生效
- Verification：
  - 事务在方法内确实活跃：`SpringCoreTxLabTest#transactionsAreActiveInsideTransactionalMethods`
  - self-invocation 绕过事务（坑点）：`SpringCoreTxSelfInvocationPitfallLabTest#selfInvocationBypassesTransactional_onInnerMethod`
- Fix：排障先锁住两条证据链：是否走代理（AopProxy）+ 方法内事务是否活跃（TransactionSynchronizationManager），再讨论传播/回滚细节

## 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreTxLabTest`

上一章：[05-transaction-template](05-transaction-template.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[90-common-pitfalls](../appendix/90-common-pitfalls.md)

<!-- BOOKIFY:END -->
