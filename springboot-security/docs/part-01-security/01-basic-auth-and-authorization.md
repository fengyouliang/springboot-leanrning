# 01：401 vs 403：Basic Auth 与授权规则

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01：401 vs 403：Basic Auth 与授权规则**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

## 你应该观察到什么

- 访问需要登录的资源（例如 `/api/secure/ping`）：
  - 未登录 → **401**（`unauthorized`）
- 访问需要更高权限的资源（例如 `/api/admin/ping`）：
  - 已登录但权限不足 → **403**（`forbidden`）

## 机制解释（Why）

可以把 Security 的判断分成两步：

1) **你是谁**（Authentication）：有没有成功登录？当前 `Authentication` 是不是匿名？
2) **你能做什么**（Authorization）：你是否具备访问该资源所需的 role/authority？

在本模块里：

- Basic Auth 用户在 `SecurityConfig#userDetailsService` 中定义（`user/password`、`admin/password`）
- `/api/admin/**` 需要 `ROLE_ADMIN`（见 `SecurityConfig#apiChain`）

- 先看响应体 `message/status/path`（本模块统一返回 JSON 错误结构），再去看 `SecurityConfig` 的规则。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootSecurityLabTest`
- 建议命令：`mvn -pl springboot-security test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

本章的目标是把“为什么有时是 401、有时是 403”讲清楚，并用可运行测试把结论固化下来。

## 实验入口

- `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
  - `secureEndpointReturns401WhenAnonymous`
  - `adminEndpointReturns403ForNonAdminUser`
  - `adminEndpointIsAccessibleForAdminUser`

## Debug 建议

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootSecurityLabTest`
- Test file：`springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`

上一章：[part-00-guide/00-deep-dive-guide.md](../part-00-guide/00-deep-dive-guide.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-security/02-csrf.md](02-csrf.md)

<!-- BOOKIFY:END -->
