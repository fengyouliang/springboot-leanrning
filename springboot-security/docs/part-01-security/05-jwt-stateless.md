# 05：JWT/Stateless：Bearer token + scope（最小闭环）

本章的目标是：在不依赖外部 IdP 的情况下，用最小示例理解 JWT/Stateless 的工作方式，并通过 tests 固化结论。

## 实验入口

- `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
  - `jwtSecureEndpointReturns401WhenMissingBearerToken`
  - `jwtSecureEndpointIsAccessibleWithBearerToken`
  - `jwtAdminEndpointReturns403WhenScopeMissing`
  - `jwtAdminEndpointIsAccessibleWhenAdminScopePresent`
  - `jwtPostDoesNotRequireCsrf`

对应代码：

- `springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/SecurityConfig.java`
- `springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/JwtTokenService.java`

## 你应该观察到什么

- `/api/jwt/secure/ping`：
  - 不带 token → 401
  - 带 `Authorization: Bearer <token>` → 200，且能看到 `subject`
- `/api/jwt/admin/ping`：
  - token 没有 `admin` scope → 403
  - token 有 `admin` scope → 200
- JWT 链路默认禁用 CSRF：
  - POST 在带 token 的情况下无需额外 CSRF token

## 机制解释（Why）

### 1) “Stateless”的关键点

- 不依赖 session 保存登录态
- 每次请求都携带凭证（Bearer token）

### 2) “scope → 权限”的映射

Spring Security 默认会把 JWT 的 `scope`（空格分隔）映射成 `SCOPE_xxx` 的 authority。

因此：

- token scope = `admin`
- 对应 authority = `SCOPE_admin`
- 鉴权规则可以写：`hasAuthority("SCOPE_admin")`

## 本地手动体验（可选）

默认 `spring-boot:run` 只演示 Basic Auth；如果你想手动拿 token 体验 JWT 链路：

1) 启动 dev profile（启用 token 发行端点）：

```bash
mvn -pl springboot-security spring-boot:run -Dspring-boot.run.profiles=dev
```

2) 获取 token（scope=admin）：

```bash
curl 'http://localhost:8085/api/jwt/dev/token?subject=alice&scope=admin'
```

3) 访问 admin endpoint：

```bash
curl -H "Authorization: Bearer <token>" http://localhost:8085/api/jwt/admin/ping
```

> 注意：`/api/jwt/dev/token` 仅用于学习（dev profile），不是生产做法。

