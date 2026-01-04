# springboot-web-mvc

## Purpose

学习 Spring MVC：Controller、参数绑定、异常处理、拦截器与测试。

## Module Overview

- **Responsibility:** 提供可运行 Web 示例与测试（MockMvc 等），帮助理解请求处理链路。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Requirement: Web MVC 学习闭环
**Module:** springboot-web-mvc
覆盖请求处理、参数绑定与异常处理策略。

#### Scenario: 请求处理链路可被测试验证
- 通过 MockMvc 等方式断言响应与错误处理

## Dependencies

- 与安全/测试模块有学习路径关联（可选）

## Docs & 复现入口

- **Docs Index:** `springboot-web-mvc/docs/README.md`
- **Docs Guide:** `springboot-web-mvc/docs/part-00-guide/00-deep-dive-guide.md`
- **Labs:**
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcSpringBootLabTest.java`
- **Exercises:** `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；Web 层示例集中在 `com.learning.springboot.bootwebmvc.part01_web_mvc`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_web_mvc`（Labs）

## Change History

- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
