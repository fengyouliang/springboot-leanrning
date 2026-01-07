# 04：FilterChain：多链路 + 顺序 + 自定义 Filter

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**04：FilterChain：多链路 + 顺序 + 自定义 Filter**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本章关注两个问题：

1) 为什么一个应用里可以有多个 `SecurityFilterChain`？
2) 自定义 Filter 应该插在哪、如何用测试证明它真的执行了？

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

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootSecurityLabTest`
- 建议命令：`mvn -pl springboot-security test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口

- TraceId Filter（无论 200/401 都会写 header）：
  - `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
    - `traceIdHeaderIsAddedEvenOnUnauthorizedResponses`
- 配置入口：
  - `springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/SecurityConfig.java`
  - `springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/TraceIdFilter.java`

## Debug 建议

- 用断点观察：请求进来时到底命中了哪个 chain（尤其是多个 matcher 的场景）。

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootSecurityLabTest`
- Test file：`springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`

上一章：[part-01-security/03-method-security-and-proxy.md](03-method-security-and-proxy.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-security/05-jwt-stateless.md](05-jwt-stateless.md)

<!-- BOOKIFY:END -->
