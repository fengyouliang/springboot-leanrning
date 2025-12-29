# 02：WebClient（响应式）最小闭环

本章用最小示例跑通 WebClient：发请求、解析 JSON、用 StepVerifier 断言响应。

## 实验入口

- `springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/BootWebClientWebClientLabTest.java`
  - `webClientGetsGreeting`
  - `webClientSendsExpectedPathAndHeaders`
  - `webClientCanPostJsonBody`

## 你应该观察到什么

- WebClient 返回的是 `Mono<T>`：错误与结果都在 reactive 流里
- StepVerifier 能让你在测试里把“完成/错误”写成可断言的实验

