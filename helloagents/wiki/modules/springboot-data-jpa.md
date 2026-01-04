# springboot-data-jpa

## Purpose

学习 Spring Data JPA：实体映射、Repository、事务与查询。

## Module Overview

- **Responsibility:** 用最小示例与测试验证 JPA 行为、映射与查询方式。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Requirement: JPA 学习闭环
**Module:** springboot-data-jpa
覆盖实体映射、Repository CRUD 与事务边界。

#### Scenario: CRUD 行为可被测试验证
- 通过测试验证保存/查询/删除

## Dependencies

- 与事务模块有学习路径关联（可选）

## Docs & 复现入口

- **Docs Index:** `springboot-data-jpa/docs/README.md`
- **Docs Guide:** `springboot-data-jpa/docs/part-00-guide/00-deep-dive-guide.md`
- **Lab:** `springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part01_data_jpa/BootDataJpaLabTest.java`
- **Exercise:** `springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part00_guide/BootDataJpaExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；JPA 示例集中在 `com.learning.springboot.bootdatajpa.part01_data_jpa`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_data_jpa`（Labs）

## Change History

- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
