# springboot-security

## Purpose

学习 Spring Security：认证、授权、过滤器链与常见安全配置。

## Module Overview

- **Responsibility:** 用可运行示例与测试验证安全规则生效、端点访问控制。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-09

## Specifications

### Requirement: 安全学习闭环
**Module:** springboot-security
覆盖基本认证/授权、常见安全坑与测试方式。

#### Scenario: 不同角色访问控制可验证
- 通过测试断言 200/401/403

### Requirement: 深挖对齐（对标 spring-core-beans）
**Module:** springboot-security
把“FilterChain → Authentication → Authorization”主线、CSRF 威胁模型与常见误区落到可断言的默认 Lab 证据链。

#### Scenario: Guide 主线可作为导航图
- Guide 已补齐：FilterChain→Authentication→Authorization；CSRF；JWT 无状态边界；method security 代理

#### Scenario: 章节坑点可回归
- 每章至少 1 个可断言坑点，并绑定默认 `*LabTest#method` 作为证据链

## Dependencies

- 与 Web MVC 模块有学习路径关联

## Docs & 复现入口

- **Docs Index:** `docs/security/springboot-security/README.md`
- **Docs Guide:** `docs/security/springboot-security/part-00-guide/00-deep-dive-guide.md`
- **Lab:** `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
- **Lab (Multi FilterChain):** `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityMultiFilterChainOrderLabTest.java`
- **Lab (Dev Profile):** `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityDevProfileLabTest.java`
- **Exercise:** `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part00_guide/BootSecurityExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；Security 示例集中在 `com.learning.springboot.bootsecurity.part01_security`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_security`（Labs）

## Change History

- [202601091802_modules_depth_align_to_beans](../../history/2026-01/202601091802_modules_depth_align_to_beans/) - ✅ 已执行：对标 spring-core-beans 深挖升级（Guide 机制主线 + 每章可断言坑点 + 默认 Lab 关键分支覆盖校验）
- [202601092110_depth_align_v2_batch01_sec_jpa_events_client](../../history/2026-01/202601092110_depth_align_v2_batch01_sec_jpa_events_client/) - ✅ 已执行：batch01 深挖对齐 v2（补齐多 FilterChain 可断言 Lab + 章节坑点可回归 + 自测入口补齐）
- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/<topic>/<module>/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章）
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + guide/appendix 可跑入口块补齐 + 补齐 min-labs=2 + 自检闸门覆盖
