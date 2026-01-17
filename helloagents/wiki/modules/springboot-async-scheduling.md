# springboot-async-scheduling

## Purpose

学习异步与调度：`@Async`、线程池、`@Scheduled` 与可测试策略。

## Module Overview

- **Responsibility:** 用最小示例与测试验证异步/调度行为与常见误区。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-09

## Specifications

### Requirement: 异步与调度学习闭环
**Module:** springboot-async-scheduling
覆盖线程切换、异常处理与调度触发。

#### Scenario: 异步执行发生在线程池
- 通过测试断言线程名/执行时机

### Requirement: 深挖对齐（对标 spring-core-beans）
**Module:** springboot-async-scheduling
把“@Async 代理语义/线程池选择/异常传播/调度触发与并发边界”落到可断言的默认 Lab 与断点入口。

#### Scenario: Guide 主线可作为导航图
- Guide 已补齐：@Async proxy 心智模型、Executor/Threading、异常处理、Scheduling 基础与排障入口

#### Scenario: 章节坑点可回归
- 每章至少 1 个可断言坑点，并绑定默认 `*LabTest#method` 作为证据链

## Dependencies

- 基于 `spring-core-events`/`spring-core-beans` 的基础概念（可选）

## Docs & 复现入口

- **Docs Index:** `docs/async-scheduling/springboot-async-scheduling/README.md`
- **Docs Guide:** `docs/async-scheduling/springboot-async-scheduling/part-00-guide/00-deep-dive-guide.md`
- **Lab:** `springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part01_async_scheduling/BootAsyncSchedulingLabTest.java`
- **Lab (Scheduling):** `springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part01_async_scheduling/BootAsyncSchedulingSchedulingLabTest.java`
- **Exercise:** `springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part00_guide/BootAsyncSchedulingExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；async/scheduling 示例集中在 `com.learning.springboot.bootasyncscheduling.part01_async_scheduling`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_async_scheduling`（Labs）

## Change History

- [202601091802_modules_depth_align_to_beans](../../history/2026-01/202601091802_modules_depth_align_to_beans/) - ✅ 已执行：对标 spring-core-beans 深挖升级（Guide 机制主线 + 每章可断言坑点 + 默认 Lab 关键分支覆盖校验）
- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/<topic>/<module>/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章）
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + guide/appendix 可跑入口块补齐 + 补齐 min-labs=2 + 自检闸门覆盖
