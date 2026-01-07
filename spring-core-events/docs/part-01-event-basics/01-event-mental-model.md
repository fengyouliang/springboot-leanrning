# 01. 事件心智模型：发布（publish）与订阅（listen）到底在解耦什么？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01. 事件心智模型：发布（publish）与订阅（listen）到底在解耦什么？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

Spring 的 Application Events 解决的是一个非常具体的问题：

> 让“发生了什么”（事件）与“需要做什么”（监听器）解耦。

你不需要一开始就把它理解成“消息队列”。在本模块里，把它当成**进程内的回调机制**更合适。

## 本模块的最小闭环

- 发布方：`UserRegistrationService`
  - 在 `register(username)` 里发布 `UserRegisteredEvent`
- 监听方：`UserRegisteredListener`
  - `@EventListener` 接收事件，并写入 `InMemoryAuditLog`

## 你需要记住的 3 件事

1) **事件默认是同步的**

- `publishEvent(...)` 会在当前线程里依次调用监听器
- 监听器执行完毕，发布方法才会返回

2) **事件类型匹配，决定谁会被调用**

- 监听方法的参数类型决定它能接收什么事件
- 你可以发布任何对象（不仅仅是 `ApplicationEvent` 子类）

3) **事件对象建议做成“不可变”**

- 学习阶段特别建议把事件建模为不可变（例如 record）
- 否则多个监听器共享同一个事件对象时，很容易出现“互相污染”的副作用

本模块的 `UserRegisteredEvent` 就是 `record`，非常适合学习。

事件不是为了“炫技”，而是为了让你的核心流程更清晰：

- 核心流程：只负责发布“发生了什么”
- 扩展动作：由监听器决定“要做什么”

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreEventsLabTest`
- 建议命令：`mvn -pl spring-core-events test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

对应测试：`SpringCoreEventsLabTest#listenerReceivesPublishedEvent`

验证入口：`SpringCoreEventsLabTest#eventsAreSynchronousByDefault`

验证入口：`SpringCoreEventsLabTest#publishingPlainObjectsAlsoWorks_asPayloadEvents`

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

## 一句话总结

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreEventsLabTest`

上一章：[00-deep-dive-guide](../part-00-guide/00-deep-dive-guide.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[02-multiple-listeners-and-order](02-multiple-listeners-and-order.md)

<!-- BOOKIFY:END -->
