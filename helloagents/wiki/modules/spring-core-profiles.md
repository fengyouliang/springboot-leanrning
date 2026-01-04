# spring-core-profiles

## Purpose

学习 Profiles/Environment：条件装配、环境切换与配置优先级。

## Module Overview

- **Responsibility:** 通过最小示例与测试实验理解 profile 选择与条件生效边界。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Source Layout
- docs：`spring-core-profiles/docs/README.md`（目录页）
- docs：`spring-core-profiles/docs/part-00-guide/`（深挖指南）
- docs：`spring-core-profiles/docs/part-01-profiles/`（profiles 激活与选择）
- docs：`spring-core-profiles/docs/appendix/`（常见坑/自测题）
- src(main)：`spring-core-profiles/src/main/java/com/learning/springboot/springcoreprofiles/SpringCoreProfilesApplication.java`（入口，包名保持不变）
- src(main)：`spring-core-profiles/src/main/java/com/learning/springboot/springcoreprofiles/part01_profiles/**`
- src(test)：`spring-core-profiles/src/test/java/com/learning/springboot/springcoreprofiles/part00_guide/**`
- src(test)：`spring-core-profiles/src/test/java/com/learning/springboot/springcoreprofiles/part01_profiles/**`

### Docs Index
- 入口：`spring-core-profiles/docs/README.md`

### Requirement: Profiles 学习闭环
**Module:** spring-core-profiles
用可断言实验覆盖 profile 生效、覆盖与回退行为。

#### Scenario: profile 切换导致不同 Bean 生效
- 通过测试稳定验证不同 profile 下的 Bean 图差异

## Change History

- [202601041046_spring-core-part-structure-sync](../../history/2026-01/202601041046_spring-core-part-structure-sync/) - ✅ 已执行：补齐 docs 书本骨架（含目录页/深挖指南/附录），并对齐 src/main+src/test 分包结构（语义化 Part 命名）

## Dependencies

- 基于 `spring-core-beans` 的容器基础概念（学习路径依赖）
