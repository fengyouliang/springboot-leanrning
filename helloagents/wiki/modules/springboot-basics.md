# springboot-basics

## Purpose

Spring Boot 基础：工程结构、配置、启动流程与最常用开发习惯。

## Module Overview

- **Responsibility:** 帮助学习者能跑通项目、理解配置与基础概念，为后续模块打底。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-07

## Specifications

### Requirement: 基础学习闭环
**Module:** springboot-basics
覆盖启动、配置、依赖管理与常用开发命令。

#### Scenario: 能跑通并理解最小应用
- 通过命令行与测试验证模块可运行

## Dependencies

- 与其他模块弱耦合

## Docs & 复现入口

- **Docs Index:** `springboot-basics/docs/README.md`
- **Docs Guide:** `springboot-basics/docs/part-00-guide/00-deep-dive-guide.md`
- **Labs:**
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDefaultLabTest.java`
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDevLabTest.java`
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsOverrideLabTest.java`
- **Exercises:** `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part00_guide/BootBasicsExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；示例代码集中在 `com.learning.springboot.bootbasics.part01_boot_basics`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_boot_basics`（Labs）

## Change History

- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章），并通过 `scripts/check-docs.sh`
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + guide/appendix 可跑入口块补齐 + 自检闸门覆盖
