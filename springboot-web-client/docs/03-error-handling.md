# 03：错误处理：4xx/5xx → 领域异常

本章把“HTTP 状态码”变成“你的领域异常”，并对比 RestClient 与 WebClient 的写法。

## 实验入口

- RestClient：
  - `BootWebClientRestClientLabTest#restClientMaps400ToDomainException`
  - `BootWebClientRestClientLabTest#restClientMaps500ToDomainException`
- WebClient：
  - `BootWebClientWebClientLabTest#webClientMaps400ToDomainException`
  - `BootWebClientWebClientLabTest#webClientMaps500ToDomainException`

## 你应该观察到什么

- 关键不在于“抛什么异常”，而在于：
  - 你能在测试里固定“哪些状态码映射成什么异常”
  - 异常里最好包含 status（用于上层分类处理：重试/降级/告警）

