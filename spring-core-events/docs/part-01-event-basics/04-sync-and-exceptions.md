# 04. 同步与异常传播：为什么监听器抛异常会“炸到发布方”？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**04. 同步与异常传播：为什么监听器抛异常会“炸到发布方”？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

事件默认是同步的，所以异常传播也很直观：

> 监听器在发布方的调用栈里执行，因此监听器抛异常会直接传播回发布方。

- 监听器直接 `throw new IllegalStateException("listener boom")`
- `context.publishEvent(...)` 会抛出同样的异常

## 你应该得到的结论

1) **同步事件不是“吞异常”的机制**

- 如果你希望“监听器失败不影响主流程”，你需要显式设计（比如异步、隔离、重试等）
- 学习仓库里建议先理解默认行为，再谈工程化处理

2) **事件不是“保证交付”的消息系统**

进程内同步事件更像“回调链”：

- 快
- 简单
- 但耦合在同一个线程与同一段调用链上

## 学习建议：如何避免“学歪”

当你想用事件做解耦时，先问自己：

- 这个动作如果失败，是否应该让主流程失败？
  - 应该：同步事件 + 异常传播是合理的
  - 不应该：考虑异步/隔离（见 [05. async-listener](../part-02-async-and-transactional/05-async-listener.md) 与 [06. async-multicaster](../part-02-async-and-transactional/06-async-multicaster.md)）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreEventsMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-events test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 在本模块如何验证

看 `SpringCoreEventsMechanicsLabTest#listenerExceptionsPropagateToPublisher_byDefault`

## F. 常见坑与边界

### 坑点 1：以为“监听器失败不会影响主流程”，结果异常直接炸回发布方

- Symptom：某个监听器抛异常后，发布事件的主流程也失败，导致你误判“业务逻辑本身坏了”
- Root Cause：同步事件的监听器在发布方调用栈里执行，异常默认向发布方传播
- Verification：`SpringCoreEventsMechanicsLabTest#listenerExceptionsPropagateToPublisher_byDefault`
- Fix：需要“监听器失败不影响主流程”时，选择异步/隔离策略（并明确异常处理与补偿），不要把同步事件当消息队列

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreEventsMechanicsLabTest`

上一章：[03-condition-and-payload](03-condition-and-payload.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[05-async-listener](../part-02-async-and-transactional/05-async-listener.md)

<!-- BOOKIFY:END -->
