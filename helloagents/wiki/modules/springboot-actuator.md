# springboot-actuator

## Purpose

学习 Spring Boot Actuator：健康检查、指标、日志与端点暴露策略。

## Module Overview

- **Responsibility:** 提供 Actuator 的可运行示例与验证用例，理解端点与安全边界。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Requirement: Actuator 学习闭环
**Module:** springboot-actuator
覆盖常用端点、配置项与可观测性基础。

#### Scenario: 端点暴露与访问控制
- 通过配置与测试验证端点是否可访问

## Dependencies

- 与其他模块弱耦合

## Docs & 复现入口

- **Docs Index:** `springboot-actuator/docs/README.md`
- **Docs Guide:** `springboot-actuator/docs/part-00-guide/00-deep-dive-guide.md`
- **Labs:**
  - `springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part01_actuator/BootActuatorLabTest.java`
  - `springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part01_actuator/BootActuatorExposureOverrideLabTest.java`
- **Exercise:** `springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part00_guide/BootActuatorExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；Actuator 示例集中在 `com.learning.springboot.bootactuator.part01_actuator`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_actuator`（Labs）

## Change History

- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
