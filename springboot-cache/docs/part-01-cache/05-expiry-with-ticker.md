# 05：过期与可测性：用 Ticker 控制时间

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**05：过期与可测性：用 Ticker 控制时间**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

## 你应该观察到什么

- 通过 `ManualTicker` 快进时间，不需要 `Thread.sleep` 也能断言 TTL 过期行为

## 机制解释（Why）

Ticker 的核心价值是：让“时间推进”变成可控输入，从而写出稳定断言。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootCacheLabTest`
- 建议命令：`mvn -pl springboot-cache test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口

- `BootCacheLabTest#expiryCanBeTestedDeterministicallyWithManualTicker`

基于真实时间的 TTL tests 很容易 flaky：

- 机器负载高 → sleep 不够
- sleep 太长 → tests 变慢

## F. 常见坑与边界

### 坑点 1：用真实时间 + sleep 测 TTL，导致 flaky 与慢测试

- Symptom：缓存过期测试偶发失败（机器负载/调度抖动），或为避免失败把 sleep 写很长导致测试很慢
- Root Cause：真实时间不可控，sleep 不是确定性输入
- Verification：`BootCacheLabTest#expiryCanBeTestedDeterministicallyWithManualTicker`
- Fix：用 `Ticker`（如 `ManualTicker`）把时间推进变成可控输入，把“过期”变成可断言事实

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootCacheLabTest`

上一章：[part-01-cache/04-sync-stampede.md](04-sync-stampede.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/90-common-pitfalls.md](../appendix/90-common-pitfalls.md)

<!-- BOOKIFY:END -->
