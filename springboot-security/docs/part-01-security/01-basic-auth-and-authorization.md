# 01：401 vs 403：Basic Auth 与授权规则

本章的目标是把“为什么有时是 401、有时是 403”讲清楚，并用可运行测试把结论固化下来。

## 实验入口

- `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
  - `secureEndpointReturns401WhenAnonymous`
  - `adminEndpointReturns403ForNonAdminUser`
  - `adminEndpointIsAccessibleForAdminUser`

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

## Debug 建议

- 先看响应体 `message/status/path`（本模块统一返回 JSON 错误结构），再去看 `SecurityConfig` 的规则。

