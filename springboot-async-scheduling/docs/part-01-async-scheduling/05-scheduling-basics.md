# 05：`@Scheduled` 基础与可测试性

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**05：`@Scheduled` 基础与可测试性**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本章关注两点：

## 你应该观察到什么

- 没有 `@EnableScheduling`：调度不会启动
- 有 `@EnableScheduling`：任务会被注册并按 fixedDelay 执行（本模块用 latch 抓住第一次触发）

## 建议的测试写法

- 用 `CountDownLatch` 固定“至少触发一次”的结论
- 避免长 `Thread.sleep`：用短 delay + 有上限的 await 更稳定

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootAsyncSchedulingLabTest`
- 建议命令：`mvn -pl springboot-async-scheduling test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

1) `@Scheduled` 需要什么才能生效？
2) 如何在 tests 里做出不 flaky 的调度断言？

## 实验入口

- `BootAsyncSchedulingLabTest#schedulingRequiresEnableScheduling`
- `BootAsyncSchedulingLabTest#schedulingTriggersTaskWhenEnableSchedulingPresent`

## F. 常见坑与边界

### 坑点 1：用 `Thread.sleep` 写调度测试，导致 flaky（偶现失败/偶现通过）

- Symptom：本地能跑，CI 偶发失败；或者为了“等它触发”把 sleep 写得很长导致测试很慢
- Root Cause：调度本身是时间相关行为，如果没有上限与同步点，很难稳定断言
- Verification：
  - 没有开关不会触发：`BootAsyncSchedulingLabTest#schedulingRequiresEnableScheduling`
  - 开启后至少触发一次：`BootAsyncSchedulingLabTest#schedulingTriggersTaskWhenEnableSchedulingPresent`
- Fix：用 `CountDownLatch` + 有上限的 await 固定“至少触发一次”的事实，不要靠长 sleep 试运气

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootAsyncSchedulingLabTest`

上一章：[part-01-async-scheduling/04-self-invocation.md](04-self-invocation.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/90-common-pitfalls.md](../appendix/90-common-pitfalls.md)

<!-- BOOKIFY:END -->
