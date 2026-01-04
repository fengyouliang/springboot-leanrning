# 05：`@Scheduled` 基础与可测试性

本章关注两点：

1) `@Scheduled` 需要什么才能生效？
2) 如何在 tests 里做出不 flaky 的调度断言？

## 实验入口

- `BootAsyncSchedulingLabTest#schedulingRequiresEnableScheduling`
- `BootAsyncSchedulingLabTest#schedulingTriggersTaskWhenEnableSchedulingPresent`

## 你应该观察到什么

- 没有 `@EnableScheduling`：调度不会启动
- 有 `@EnableScheduling`：任务会被注册并按 fixedDelay 执行（本模块用 latch 抓住第一次触发）

## 建议的测试写法

- 用 `CountDownLatch` 固定“至少触发一次”的结论
- 避免长 `Thread.sleep`：用短 delay + 有上限的 await 更稳定

