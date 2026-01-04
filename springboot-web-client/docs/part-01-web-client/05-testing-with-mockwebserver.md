# 05：测试策略：为什么用 MockWebServer？

## 目的

学习 HTTP client 的最大坑之一是：你不知道“请求到底发了什么”，以及你的 client 行为是否稳定（比如是否重试、header 是否注入、body 是否正确）。

MockWebServer 的优势：

- 在进程内启动一个可控的 HTTP server（不依赖外部网络）
- 能断言请求的：
  - method/path
  - headers
  - body
- 能精确控制响应：
  - status code
  - body
  - 延迟（用于 timeout）
  - 多次响应（用于 retry）

## 对应实验入口

- `BootWebClientRestClientLabTest#restClientSendsExpectedPathAndHeaders`
- `BootWebClientWebClientLabTest#webClientSendsExpectedPathAndHeaders`

