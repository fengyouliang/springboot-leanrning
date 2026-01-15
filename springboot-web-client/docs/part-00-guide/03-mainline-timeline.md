# 主线时间线：Spring Boot Web Client

!!! summary
    - 这一模块关注：RestClient/WebClient 的调用主线、错误处理与超时重试，以及如何用测试把外部依赖固定下来。
    - 读完你应该能复述：**构建请求 → 发出调用 → 处理状态码/异常 → 超时/重试 → 测试验证** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → Part 01 顺读 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`BootWebClientWebClientLabTest`

## 在 Spring 主线中的位置

- Web Client 是“对外出口”：它把外部 HTTP 依赖纳入你的系统边界，错误处理与超时策略决定系统韧性。
- 真实项目里，调用链排障需要“可观察证据”：日志、指标、以及 mock server 测试。

## 主线时间线（建议顺读）

1. RestClient 基础：同步调用的主线与最小闭环
   - 阅读：[01. RestClient](../part-01-web-client/01-restclient-basics.md)
2. WebClient 基础：响应式调用的主线与背压意识
   - 阅读：[02. WebClient](../part-01-web-client/02-webclient-basics.md)
3. 错误处理：状态码与异常的统一策略
   - 阅读：[03. 错误处理](../part-01-web-client/03-error-handling.md)
4. 超时与重试：避免“卡死/雪崩”的关键边界
   - 阅读：[04. 超时与重试](../part-01-web-client/04-timeout-and-retry.md)
5. 测试：用 MockWebServer 把外部依赖变成可重复实验
   - 阅读：[05. MockWebServer 测试](../part-01-web-client/05-testing-with-mockwebserver.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
