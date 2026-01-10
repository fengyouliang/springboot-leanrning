# 自测题（Spring Core Events）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**自测题（Spring Core Events）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

这一章用“最小实验 + 可断言证据链”复盘 4 个核心分流：

1. 同步默认值（线程模型）
2. 多监听器与顺序（@Order）
3. condition/payload（触发条件与类型匹配）
4. 异常/事务/异步（失败是否影响发布方、何时触发）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreEventsLabTest` / `SpringCoreEventsMechanicsLabTest` / `SpringCoreEventsListenerFilteringLabTest` / `SpringCoreEventsTransactionalEventLabTest` / `SpringCoreEventsAsyncMulticasterLabTest`
- 建议命令：`mvn -pl spring-core-events test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

> 验证入口（可跑）：`SpringCoreEventsLabTest` / `SpringCoreEventsMechanicsLabTest` / `SpringCoreEventsListenerFilteringLabTest` / `SpringCoreEventsTransactionalEventLabTest` / `SpringCoreEventsAsyncMulticasterLabTest`

> 用来检查你是否能“复述机制 + 解释边界 + 给出最小复现”。

1. 事件发布与监听的核心接口分别是什么？各自的职责边界是什么？
2. 多个监听器时，顺序由哪些因素决定？你如何最小化验证？
3. `@EventListener(condition = ...)` 的 condition 在哪里求值？失败时的行为是什么？
4. 同步事件里监听器抛异常会怎样影响发布方？常见的误解是什么？
5. 异步事件与事务事件组合时，最容易踩的坑是什么？你会如何设计验证用例？

## F. 常见坑与边界

### 坑点 1：把事件当“最终一致性工具”却不区分同步/异步/事务阶段

- Symptom：回滚时仍有副作用；或 afterCommit 没触发；或异常把发布方打断
- Root Cause：事件机制的行为由“线程模型 + 异常传播 + 事务阶段”共同决定
- Verification：
  - 异常默认传播：`SpringCoreEventsMechanicsLabTest#listenerExceptionsPropagateToPublisher_byDefault`
  - @Async 需要 EnableAsync：`SpringCoreEventsMechanicsLabTest#asyncAnnotationIsIgnored_withoutEnableAsync`
  - 事务阶段：`SpringCoreEventsTransactionalEventLabTest#afterCommitDoesNotRunOnRollback_butAfterRollbackDoes`
- Fix：先用测试把线程模型/异常策略/事务阶段锁住，再把“副作用”设计到合适的阶段（afterCommit/afterRollback/异步队列等）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreEventsLabTest` / `SpringCoreEventsMechanicsLabTest` / `SpringCoreEventsListenerFilteringLabTest` / `SpringCoreEventsTransactionalEventLabTest` / `SpringCoreEventsAsyncMulticasterLabTest`

上一章：[90-common-pitfalls](90-common-pitfalls.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[Docs TOC](../README.md)

<!-- BOOKIFY:END -->
