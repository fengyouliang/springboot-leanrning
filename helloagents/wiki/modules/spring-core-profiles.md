# spring-core-profiles

## Purpose

学习 Profiles/Environment：条件装配、环境切换与配置优先级。

## Module Overview

- **Responsibility:** 通过最小示例与测试实验理解 profile 选择与条件生效边界。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-09

## Specifications

### Source Layout
- docs：`docs/profiles/spring-core-profiles/README.md`（目录页）
- docs：`docs/profiles/spring-core-profiles/part-00-guide/`（深挖指南）
- docs：`docs/profiles/spring-core-profiles/part-01-profiles/`（profiles 激活与选择）
- docs：`docs/profiles/spring-core-profiles/appendix/`（常见坑/自测题）
- src(main)：`spring-core-profiles/src/main/java/com/learning/springboot/springcoreprofiles/SpringCoreProfilesApplication.java`（入口，包名保持不变）
- src(main)：`spring-core-profiles/src/main/java/com/learning/springboot/springcoreprofiles/part01_profiles/**`
- src(test)：`spring-core-profiles/src/test/java/com/learning/springboot/springcoreprofiles/part00_guide/**`
- src(test)：`spring-core-profiles/src/test/java/com/learning/springboot/springcoreprofiles/part01_profiles/**`

### Docs Index
- 入口：`docs/profiles/spring-core-profiles/README.md`

### Requirement: Profiles 学习闭环
**Module:** spring-core-profiles
用可断言实验覆盖 profile 生效、覆盖与回退行为。

#### Scenario: profile 切换导致不同 Bean 生效
- 通过测试稳定验证不同 profile 下的 Bean 图差异

### Requirement: 深挖对齐（对标 spring-core-beans）
**Module:** spring-core-profiles
把“激活来源/默认 vs active/negation/优先级与排障入口”写成可断言主线，并补齐章节坑点证据链。

## Change History

- [202601091802_modules_depth_align_to_beans](../../history/2026-01/202601091802_modules_depth_align_to_beans/) - ✅ 已执行：对标 spring-core-beans 深挖升级（Guide 机制主线 + 每章可断言坑点 + 排障入口统一）
- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/<topic>/<module>/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章）
- [202601061556_spring_core_modules_teaching_rollout](../../history/2026-01/202601061556_spring_core_modules_teaching_rollout/) - ✅ 已执行：对齐 docs 目录页/Part 编号与章节末尾“对应 Lab/Test”入口块，清理正文 `docs/NN` 缩写引用，并通过断链检查与教学覆盖检查
- [202601041046_spring-core-part-structure-sync](../../history/2026-01/202601041046_spring-core-part-structure-sync/) - ✅ 已执行：补齐 docs 书本骨架（含目录页/深挖指南/附录），并对齐 src/main+src/test 分包结构（语义化 Part 命名）

## Dependencies

- 基于 `spring-core-beans` 的容器基础概念（学习路径依赖）
