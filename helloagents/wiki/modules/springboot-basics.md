# springboot-basics

## Purpose

Spring Boot 基础：工程结构、配置、启动流程与最常用开发习惯。

## Module Overview

- **Responsibility:** 帮助学习者能跑通项目、理解配置与基础概念，为后续模块打底。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

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

- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
