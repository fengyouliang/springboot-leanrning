# spring-core-resources

## Purpose

学习 Spring Resource 抽象：classpath/file/url 资源定位与读取。

## Module Overview

- **Responsibility:** 用最小示例与测试实验覆盖 Resource 加载、路径语义与常见坑。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-07

## Specifications

### Source Layout
- docs：`spring-core-resources/docs/README.md`（目录页）
- docs：`spring-core-resources/docs/part-00-guide/`（深挖指南）
- docs：`spring-core-resources/docs/part-01-resource-abstraction/`（Resource 抽象与定位规则）
- docs：`spring-core-resources/docs/appendix/`（常见坑/自测题）
- src(main)：`spring-core-resources/src/main/java/com/learning/springboot/springcoreresources/SpringCoreResourcesApplication.java`（入口，包名保持不变）
- src(main)：`spring-core-resources/src/main/java/com/learning/springboot/springcoreresources/part01_resource_abstraction/**`
- src(test)：`spring-core-resources/src/test/java/com/learning/springboot/springcoreresources/part00_guide/**`
- src(test)：`spring-core-resources/src/test/java/com/learning/springboot/springcoreresources/part01_resource_abstraction/**`

### Docs Index
- 入口：`spring-core-resources/docs/README.md`

### Requirement: Resource 学习闭环
**Module:** spring-core-resources
通过实验让用户理解不同前缀与相对路径的实际含义。

#### Scenario: 多种 Resource 前缀可验证
- classpath/file/url 的行为差异可通过测试稳定断言

## Change History

- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 升级 A–G 章节契约（每章 A–G + 对应 Lab/Test + 至少 1 个 LabTest），并更新根 README 跨模块入口
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章），并通过 `scripts/check-docs.sh`
- [202601061556_spring_core_modules_teaching_rollout](../../history/2026-01/202601061556_spring_core_modules_teaching_rollout/) - ✅ 已执行：对齐 docs 目录页/Part 编号与章节末尾“对应 Lab/Test”入口块，清理正文 `docs/NN` 缩写引用，并通过断链检查与教学覆盖检查
- [202601041046_spring-core-part-structure-sync](../../history/2026-01/202601041046_spring-core-part-structure-sync/) - ✅ 已执行：对齐 docs Part 目录结构与 src/main+src/test 分包结构（语义化 Part 命名），并修复 README/跨模块引用路径

## Dependencies

- 基础容器概念（可选）
