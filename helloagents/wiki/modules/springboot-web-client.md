# springboot-web-client

## Purpose

学习 HTTP Client：WebClient、重试、超时、错误处理与可测试性。

## Module Overview

- **Responsibility:** 用最小示例与测试覆盖 HTTP 调用的关键问题与最佳实践。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Requirement: WebClient 学习闭环
**Module:** springboot-web-client
覆盖请求构建、响应处理、错误与超时策略。

#### Scenario: 错误处理与超时策略可验证
- 通过测试稳定复现并断言行为

## Dependencies

- 与 Web MVC/基础模块弱耦合

## Docs & 复现入口

- **Docs Index:** `springboot-web-client/docs/README.md`
- **Docs Guide:** `springboot-web-client/docs/part-00-guide/00-deep-dive-guide.md`
- **Labs:**
  - `springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientRestClientLabTest.java`
  - `springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientWebClientLabTest.java`
- **Exercise:** `springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part00_guide/BootWebClientExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；client/model/support 集中在 `com.learning.springboot.bootwebclient.part01_web_client`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_web_client`（Labs）

## Change History

- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
