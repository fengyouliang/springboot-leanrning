# 04：超时与重试（确定性实验）

本章重点是：把 timeout/retry 做成 **可测** 的实验，避免“线上偶现、测试不稳定”。

## 实验入口

- RestClient 超时：
  - `BootWebClientRestClientLabTest#restClientReadTimeoutFailsFast`
- WebClient 超时：
  - `BootWebClientWebClientLabTest#webClientResponseTimeoutFailsFast`
- 重试：
  - `BootWebClientRestClientLabTest#restClientRetriesOn5xxAndEventuallySucceeds`
  - `BootWebClientWebClientLabTest#webClientRetriesOn5xxAndEventuallySucceeds`

## 你应该观察到什么

- MockWebServer 通过延迟响应复现 timeout（比连不可达地址更稳定）
- 重试需要明确边界：
  - 对哪些错误重试（通常是 5xx 或网络错误）
  - 最大次数
  - 是否有 backoff

