# springboot-async-scheduling

## Purpose

学习异步与调度：`@Async`、线程池、`@Scheduled` 与可测试策略。

## Module Overview

- **Responsibility:** 用最小示例与测试验证异步/调度行为与常见误区。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-07

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
- **Lab (Scheduling):** `springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part01_async_scheduling/BootAsyncSchedulingSchedulingLabTest.java`
- **Exercise:** `springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part00_guide/BootAsyncSchedulingExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；async/scheduling 示例集中在 `com.learning.springboot.bootasyncscheduling.part01_async_scheduling`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_async_scheduling`（Labs）

## Change History

- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章），并通过 `scripts/check-docs.sh`
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + guide/appendix 可跑入口块补齐 + 补齐 min-labs=2 + 自检闸门覆盖
