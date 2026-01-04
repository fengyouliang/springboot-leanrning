# 90：常见坑清单（Async & Scheduling）

## `@Async` 不生效

- 忘了 `@EnableAsync`
- self-invocation（同类 this 调用绕过代理）
- executor 没配置导致线程/并发行为不符合预期

## 异常看不到

- void 的异常不会传回调用方：需要 AsyncUncaughtExceptionHandler

## 调度测试 flaky

- 用 `Thread.sleep` 过长/过短都不稳定
- 建议 latch + await + 上限超时

