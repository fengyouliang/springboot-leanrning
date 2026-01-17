# springboot-actuator

## Purpose

学习 Spring Boot Actuator：健康检查、指标、日志与端点暴露策略。

## Module Overview

- **Responsibility:** 提供 Actuator 的可运行示例与验证用例，理解端点与安全边界。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-09

## Specifications

### Requirement: Actuator 学习闭环
**Module:** springboot-actuator
覆盖常用端点、配置项与可观测性基础。

#### Scenario: 端点暴露与访问控制
- 通过配置与测试验证端点是否可访问

### Requirement: 深挖对齐（对标 spring-core-beans）
**Module:** springboot-actuator
把“端点注册/暴露策略/安全边界/排障入口”落到可断言的默认 Lab 证据链与断点入口。

#### Scenario: Guide 主线可作为导航图
- Guide 已补齐：端点注册 → 暴露策略 → 安全边界 → 排障入口
- 关键分支与断点在 Guide 中可一跳定位

#### Scenario: 章节坑点可回归
- 每章至少 1 个可断言坑点，并绑定默认 `*LabTest#method` 作为证据链

## Dependencies

- 与其他模块弱耦合

## Docs & 复现入口

- **Docs Index:** `docs/actuator/springboot-actuator/README.md`
- **Docs Guide:** `docs/actuator/springboot-actuator/part-00-guide/00-deep-dive-guide.md`
- **Labs:**
  - `springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part01_actuator/BootActuatorLabTest.java`
  - `springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part01_actuator/BootActuatorExposureOverrideLabTest.java`
- **Exercise:** `springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part00_guide/BootActuatorExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；Actuator 示例集中在 `com.learning.springboot.bootactuator.part01_actuator`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_actuator`（Labs）

## Change History

- [202601091802_modules_depth_align_to_beans](../../history/2026-01/202601091802_modules_depth_align_to_beans/) - ✅ 已执行：对标 spring-core-beans 深挖升级（Guide 机制主线 + 每章可断言坑点 + 默认 Lab 关键分支覆盖校验）
- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/<topic>/<module>/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章）
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + guide/appendix 可跑入口块补齐 + 自检闸门覆盖
