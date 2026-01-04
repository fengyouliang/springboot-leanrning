# 02：Executor 与线程命名/并发边界

本章建议你把“线程名”当成最稳定的观察点之一：当你不知道代码到底跑在哪个线程时，线程名比日志更直接。

## 实验入口

- `BootAsyncSchedulingLabTest#executorThreadNamePrefixIsAStableObservationPoint`

## 你应该观察到什么

- 通过 `ThreadPoolTaskExecutor#setThreadNamePrefix("async-")`，你可以用断言稳定证明：
  - 调用确实发生在你提供的 executor 上

