# 05：过期与可测性：用 Ticker 控制时间

## 实验入口

- `BootCacheLabTest#expiryCanBeTestedDeterministicallyWithManualTicker`

## 你应该观察到什么

- 通过 `ManualTicker` 快进时间，不需要 `Thread.sleep` 也能断言 TTL 过期行为

## 机制解释（Why）

基于真实时间的 TTL tests 很容易 flaky：

- 机器负载高 → sleep 不够
- sleep 太长 → tests 变慢

Ticker 的核心价值是：让“时间推进”变成可控输入，从而写出稳定断言。

