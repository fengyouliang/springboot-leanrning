# springboot-testing

## Purpose

学习 Spring Boot 测试：测试分层、Test Slice、Mock 策略与可维护断言。

## Module Overview

- **Responsibility:** 提供多种测试策略的示例，让学习者能写出稳定、快速、可读的测试。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-09

## Specifications

### Requirement: 测试策略学习闭环
**Module:** springboot-testing
覆盖单元测试/集成测试/Test Slice 与常见误区。

#### Scenario: 能选择合适的测试切片并写出稳定断言
- 给出推荐路径与对比示例

### Requirement: 深挖对齐（对标 spring-core-beans）
**Module:** springboot-testing
把“测试切片边界/Mock 替换语义/排障分流”写成可执行主线，并用默认 Lab 固化关键分支。

#### Scenario: Guide 主线可作为导航图
- Guide 已补齐：slice vs full、@MockBean 替换边界、排障分流（失败分层定位）

#### Scenario: 章节坑点可回归
- 每章至少 1 个可断言坑点，并绑定默认 `*LabTest#method` 作为证据链

## Dependencies

- 与其他模块弱耦合（为它们提供测试方法论）

## Docs & 复现入口

- **Docs Index:** `docs/testing/springboot-testing/README.md`
- **Docs Guide:** `docs/testing/springboot-testing/part-00-guide/00-deep-dive-guide.md`
- **Labs:**
  - `springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/GreetingControllerWebMvcLabTest.java`
  - `springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/GreetingControllerSpringBootLabTest.java`
  - `springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/BootTestingMockBeanLabTest.java`
- **Exercise:** `springboot-testing/src/test/java/com/learning/springboot/boottesting/part00_guide/BootTestingExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；示例代码集中在 `com.learning.springboot.boottesting.part01_testing`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_testing`（Labs）

## Change History

- [202601091802_modules_depth_align_to_beans](../../history/2026-01/202601091802_modules_depth_align_to_beans/) - ✅ 已执行：对标 spring-core-beans 深挖升级（Guide 机制主线 + 每章可断言坑点 + 默认 Lab 关键分支覆盖校验）
- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/<topic>/<module>/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章）
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + guide/appendix 可跑入口块补齐 + 自检闸门覆盖
