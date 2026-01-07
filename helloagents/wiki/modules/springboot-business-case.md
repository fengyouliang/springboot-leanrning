# springboot-business-case

## Purpose

用一个端到端业务案例串联：Web → 数据 → 事务 → 安全 → 可观测性。

## Module Overview

- **Responsibility:** 用可运行案例让学习者把多个知识点串成完整链路。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-07

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
- **Lab (Service):** `springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/part01_business_case/BootBusinessCaseServiceLabTest.java`
- **Exercise:** `springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/part00_guide/BootBusinessCaseExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：为保留领域分层（`api/app/domain/events/tracing`），仅对 tests 与 docs 做 Part 对齐
- `src/test/java`：`part00_guide`（Exercises）/ `part01_business_case`（Labs）

## Change History

- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章），并通过 `scripts/check-docs.sh`
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 tests 分包（保留领域分层），并修复 README/docs 引用
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + guide/appendix 可跑入口块补齐 + 补齐 min-labs=2 + 自检闸门覆盖
