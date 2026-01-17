# springboot-data-jpa

## Purpose

学习 Spring Data JPA：实体映射、Repository、事务与查询。

## Module Overview

- **Responsibility:** 用最小示例与测试验证 JPA 行为、映射与查询方式。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-09

## Specifications

### Requirement: JPA 学习闭环
**Module:** springboot-data-jpa
覆盖实体映射、Repository CRUD 与事务边界。

#### Scenario: CRUD 行为可被测试验证
- 通过测试验证保存/查询/删除

### Requirement: 深挖对齐（对标 spring-core-beans）
**Module:** springboot-data-jpa
把“实体状态/持久化上下文/flush/脏检查/N+1/代理与 EntityGraph”落到可断言的默认 Lab 证据链。

#### Scenario: Guide 主线可作为导航图
- Guide 已补齐：实体状态 → Persistence Context → flush/可见性 → dirty checking → fetching/N+1 → slice 测试

#### Scenario: 关键分支可被稳定断言
- N+1 与 `EntityGraph` 规避可通过默认 Lab 的统计/计数断言复现
- `getReferenceById` 懒代理的“获取不等于加载”边界可通过默认 Lab 固化为断言

## Dependencies

- 与事务模块有学习路径关联（可选）

## Docs & 复现入口

- **Docs Index:** `docs/data-jpa/springboot-data-jpa/README.md`
- **Docs Guide:** `docs/data-jpa/springboot-data-jpa/part-00-guide/00-deep-dive-guide.md`
- **Lab:** `springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part01_data_jpa/BootDataJpaLabTest.java`
- **Lab (Merge/Detach):** `springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part01_data_jpa/BootDataJpaMergeAndDetachLabTest.java`
- **Lab (Debug SQL):** `springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part01_data_jpa/BootDataJpaDebugSqlLabTest.java`
- **Exercise:** `springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part00_guide/BootDataJpaExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；JPA 示例集中在 `com.learning.springboot.bootdatajpa.part01_data_jpa`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_data_jpa`（Labs）

## Change History

- [202601091802_modules_depth_align_to_beans](../../history/2026-01/202601091802_modules_depth_align_to_beans/) - ✅ 已执行：对标 spring-core-beans 深挖升级（Guide 机制主线 + 每章可断言坑点 + 默认 Lab 关键分支覆盖校验）
- [202601092110_depth_align_v2_batch01_sec_jpa_events_client](../../history/2026-01/202601092110_depth_align_v2_batch01_sec_jpa_events_client/) - ✅ 已执行：batch01 深挖对齐 v2（新增 merge/detach 默认 Lab + debug-sql/appendix 补齐坑点入口 + 自测入口补齐）
- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/<topic>/<module>/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章）
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + debug-sql 章节缺口补齐 + 补齐 min-labs=2 + 自检闸门覆盖
