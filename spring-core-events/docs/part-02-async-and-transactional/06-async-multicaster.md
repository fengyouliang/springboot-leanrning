# 06. 异步广播：让事件“默认异步”而不是靠 `@Async`

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**06. 异步广播：让事件“默认异步”而不是靠 `@Async`**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

上一章（`@Async`）的做法是：**让监听器方法异步执行**。

还有另一种思路是：让事件分发器（multicaster）本身就异步。

> 这会让“所有事件监听器”默认异步执行（除非你显式选择同步）。

## 为什么这是一个好练习？

它能帮你理解：事件机制不是黑盒，Spring 通过一个 `ApplicationEventMulticaster` 把事件分发到监听器。

## 在本模块的练习入口

- 目标：把事件改为“默认异步分发”
- 然后更新/补充断言，证明它确实不再是同步线程

## 实现思路（提示，不直接给最终代码）

你需要在 Spring 容器里提供一个自定义的 multicaster，并为它设置 `TaskExecutor`。

学习建议：

- 先让 thread name 可控（线程池 prefix），再写断言
- 再回头对照 `@Async` 方案：它们解决的“异步点”其实不同

- `@Async`：让“某个监听器方法”异步
- multicaster async：让“事件分发过程”默认异步

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章未显式引用 LabTest，先注入模块默认 LabTest 作为“合规兜底入口”（后续可逐章细化）。
- Lab：`SpringCoreEventsLabTest` / `SpringCoreEventsMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-events test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

看 `SpringCoreEventsExerciseTest#exercise_asyncMulticaster`：

## F. 常见坑与边界

### 坑点 1：只加了 `@Async` 却没想清“异步点在哪里”，导致线程模型与异常策略混乱

- Symptom：你以为“事件已经异步”，但实际只有某个 listener 异步；或者你以为发布方不会被影响，结果仍被同步 listener 拖慢/异常打断
- Root Cause：
  - `@Async`：异步点在“监听器方法”
  - async multicaster：异步点在“分发过程”（默认让所有 listener 异步）
- Verification（用线程名把异步点固定成证据）：
  - async multicaster：`SpringCoreEventsAsyncMulticasterLabTest#asyncMulticasterDispatchesListenersOnExecutorThread`
  - @Async listener：`SpringCoreEventsMechanicsLabTest#asyncListenerRunsOnDifferentThread_whenEnableAsyncIsOn`
- Fix：先选清楚你要异步的是“某个 listener”还是“整个分发过程”，再用可断言的线程名/执行时机把行为锁住

## G. 小结与下一章

## 一句话总结

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreEventsLabTest` / `SpringCoreEventsMechanicsLabTest`
- Exercise：`SpringCoreEventsExerciseTest`

上一章：[05-async-listener](05-async-listener.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[07-transactional-event-listener](07-transactional-event-listener.md)

<!-- BOOKIFY:END -->
