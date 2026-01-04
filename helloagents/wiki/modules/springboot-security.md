# springboot-security

## Purpose

学习 Spring Security：认证、授权、过滤器链与常见安全配置。

## Module Overview

- **Responsibility:** 用可运行示例与测试验证安全规则生效、端点访问控制。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Requirement: 安全学习闭环
**Module:** springboot-security
覆盖基本认证/授权、常见安全坑与测试方式。

#### Scenario: 不同角色访问控制可验证
- 通过测试断言 200/401/403

## Dependencies

- 与 Web MVC 模块有学习路径关联

## Docs & 复现入口

- **Docs Index:** `springboot-security/docs/README.md`
- **Docs Guide:** `springboot-security/docs/part-00-guide/00-deep-dive-guide.md`
- **Lab:** `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
- **Exercise:** `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part00_guide/BootSecurityExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；Security 示例集中在 `com.learning.springboot.bootsecurity.part01_security`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_security`（Labs）

## Change History

- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
