# 04：FilterChain：多链路 + 顺序 + 自定义 Filter

本章关注两个问题：

1) 为什么一个应用里可以有多个 `SecurityFilterChain`？
2) 自定义 Filter 应该插在哪、如何用测试证明它真的执行了？

## 实验入口

- TraceId Filter（无论 200/401 都会写 header）：
  - `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
    - `traceIdHeaderIsAddedEvenOnUnauthorizedResponses`
- 配置入口：
  - `springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/SecurityConfig.java`
  - `springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/TraceIdFilter.java`

## 你应该观察到什么

- 即使请求被拒绝（401/403），响应依然带有 `X-Trace-Id`。
- `/api/jwt/**` 与 `/api/**` 走的是不同的 filter chain（本模块用路径分流 + `@Order` 固定优先级）。

## 机制解释（Why）

- Spring Security 支持多个 `SecurityFilterChain`：
  - 每个 chain 有自己的 matcher（例如 `securityMatcher("/api/jwt/**")`）
  - 通过 `@Order`（或内部排序）决定优先级：先匹配/先应用
- 自定义 Filter 的位置通常通过：
  - `addFilterBefore(filter, SomeFilter.class)`
  - `addFilterAfter(filter, SomeFilter.class)`
固定下来。

## Debug 建议

- 用断点观察：请求进来时到底命中了哪个 chain（尤其是多个 matcher 的场景）。

