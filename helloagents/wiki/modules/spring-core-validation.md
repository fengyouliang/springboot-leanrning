# spring-core-validation

## Purpose

学习 Bean Validation（Jakarta Validation）与 Spring 的集成：校验触发时机、异常表现与消息国际化。

## Module Overview

- **Responsibility:** 用最小示例与测试实验覆盖 `@Valid`、约束注解与校验器配置。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Source Layout
- docs：`spring-core-validation/docs/README.md`（目录页）
- docs：`spring-core-validation/docs/part-00-guide/`（深挖指南）
- docs：`spring-core-validation/docs/part-01-validation-core/`（Validation 核心机制）
- docs：`spring-core-validation/docs/appendix/`（常见坑/自测题）
- src(main)：`spring-core-validation/src/main/java/com/learning/springboot/springcorevalidation/SpringCoreValidationApplication.java`（入口，包名保持不变）
- src(main)：`spring-core-validation/src/main/java/com/learning/springboot/springcorevalidation/part01_validation_core/**`
- src(test)：`spring-core-validation/src/test/java/com/learning/springboot/springcorevalidation/part00_guide/**`
- src(test)：`spring-core-validation/src/test/java/com/learning/springboot/springcorevalidation/part01_validation_core/**`

### Docs Index
- 入口：`spring-core-validation/docs/README.md`

### Requirement: Validation 学习闭环
**Module:** spring-core-validation
通过测试实验覆盖常见约束、嵌套校验与消息输出。

#### Scenario: 校验失败表现可被稳定断言
- 校验异常类型与消息内容可验证

## Change History

- [202601041046_spring-core-part-structure-sync](../../history/2026-01/202601041046_spring-core-part-structure-sync/) - ✅ 已执行：对齐 docs Part 目录结构与 src/main+src/test 分包结构（语义化 Part 命名），并修复 README/跨模块引用路径

## Dependencies

- 基础容器概念（可选）
