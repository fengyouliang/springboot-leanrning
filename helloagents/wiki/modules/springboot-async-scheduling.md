# springboot-async-scheduling

## Purpose

学习异步与调度：`@Async`、线程池、`@Scheduled` 与可测试策略。

## Module Overview

- **Responsibility:** 用最小示例与测试验证异步/调度行为与常见误区。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Requirement: 异步与调度学习闭环
**Module:** springboot-async-scheduling
覆盖线程切换、异常处理与调度触发。

#### Scenario: 异步执行发生在线程池
- 通过测试断言线程名/执行时机

## Dependencies

- 基于 `spring-core-events`/`spring-core-beans` 的基础概念（可选）

## Docs & 复现入口

- **Docs Index:** `springboot-async-scheduling/docs/README.md`
- **Docs Guide:** `springboot-async-scheduling/docs/part-00-guide/00-deep-dive-guide.md`
- **Lab:** `springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part01_async_scheduling/BootAsyncSchedulingLabTest.java`
- **Exercise:** `springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part00_guide/BootAsyncSchedulingExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；async/scheduling 示例集中在 `com.learning.springboot.bootasyncscheduling.part01_async_scheduling`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_async_scheduling`（Labs）

## Change History

- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
