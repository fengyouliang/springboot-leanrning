# springboot-business-case

## Purpose

用一个端到端业务案例串联：Web → 数据 → 事务 → 安全 → 可观测性。

## Module Overview

- **Responsibility:** 用可运行案例让学习者把多个知识点串成完整链路。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Requirement: 业务案例串联
**Module:** springboot-business-case
覆盖一个可运行业务流程与关键非功能点（日志、事务、安全）。

#### Scenario: 端到端流程可被测试验证
- 核心流程有集成测试兜底

## Dependencies

- 依赖多个基础模块（学习路径依赖）

## Docs & 复现入口

- **Docs Index:** `springboot-business-case/docs/README.md`
- **Docs Guide:** `springboot-business-case/docs/part-00-guide/00-deep-dive-guide.md`
- **Lab:** `springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/part01_business_case/BootBusinessCaseLabTest.java`
- **Exercise:** `springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/part00_guide/BootBusinessCaseExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：为保留领域分层（`api/app/domain/events/tracing`），仅对 tests 与 docs 做 Part 对齐
- `src/test/java`：`part00_guide`（Exercises）/ `part01_business_case`（Labs）

## Change History

- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 tests 分包（保留领域分层），并修复 README/docs 引用
