# 90：常见坑清单（Async & Scheduling）

## 导读

- 本章主题：**90：常见坑清单（Async & Scheduling）**
- 阅读方式建议：先看“本章要点”，再沿主线阅读；需要时穿插源码/断点，最后跑通实验闭环。

!!! summary "本章要点"

    - 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
    - 如果只看一眼：请先跑一次本章的最小实验，再回到主线对照阅读。


!!! example "本章配套实验（先跑再读）"

    - Lab：`BootAsyncSchedulingLabTest` / `BootAsyncSchedulingSchedulingLabTest`

## 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootAsyncSchedulingLabTest` / `BootAsyncSchedulingSchedulingLabTest`
- 建议命令：`mvn -pl springboot-async-scheduling test`（或在 IDE 直接运行上面的测试类）

## 常见坑与边界

## `@Async` 不生效

- 忘了 `@EnableAsync`
- self-invocation（同类 this 调用绕过代理）
- executor 没配置导致线程/并发行为不符合预期

## 异常看不到

- void 的异常不会传回调用方：需要 AsyncUncaughtExceptionHandler

## 调度测试 flaky

- 用 `Thread.sleep` 过长/过短都不稳定
- 建议 latch + await + 上限超时

## 对应 Lab（可运行）

- `BootAsyncSchedulingLabTest`
- `BootAsyncSchedulingSchedulingLabTest`

## 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootAsyncSchedulingLabTest` / `BootAsyncSchedulingSchedulingLabTest`

上一章：[part-01-async-scheduling/05-scheduling-basics.md](../part-01-async-scheduling/05-scheduling-basics.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/99-self-check.md](99-self-check.md)

<!-- BOOKIFY:END -->
