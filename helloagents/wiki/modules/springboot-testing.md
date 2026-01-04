# springboot-testing

## Purpose

学习 Spring Boot 测试：测试分层、Test Slice、Mock 策略与可维护断言。

## Module Overview

- **Responsibility:** 提供多种测试策略的示例，让学习者能写出稳定、快速、可读的测试。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Requirement: 测试策略学习闭环
**Module:** springboot-testing
覆盖单元测试/集成测试/Test Slice 与常见误区。

#### Scenario: 能选择合适的测试切片并写出稳定断言
- 给出推荐路径与对比示例

## Dependencies

- 与其他模块弱耦合（为它们提供测试方法论）

## Docs & 复现入口

- **Docs Index:** `springboot-testing/docs/README.md`
- **Docs Guide:** `springboot-testing/docs/part-00-guide/00-deep-dive-guide.md`
- **Labs:**
  - `springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/GreetingControllerWebMvcLabTest.java`
  - `springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/GreetingControllerSpringBootLabTest.java`
  - `springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/BootTestingMockBeanLabTest.java`
- **Exercise:** `springboot-testing/src/test/java/com/learning/springboot/boottesting/part00_guide/BootTestingExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；示例代码集中在 `com.learning.springboot.boottesting.part01_testing`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_testing`（Labs）

## Change History

- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
