# 90：常见坑清单（Security）

## 401 vs 403 判断错

- 401：没认证（anonymous / 登录失败）
- 403：已认证但没权限（或 CSRF 拦截）

建议先看本模块统一错误响应的 `message`：
- `unauthorized`
- `forbidden`
- `csrf_failed`

## CSRF 误区

- Basic Auth 并不天然绕过 CSRF：你只要是“写操作”，就可能需要 CSRF token（取决于你的链路配置）。
- 对 API 场景常见做法是禁用 CSRF，但要明确安全边界（本模块用 `/api/jwt/**` 做了演示）。

## Method Security 没生效

- 最常见根因：self-invocation 没走代理。
- 排查时先问自己：调用是从另一个 bean 进来的吗？还是同类 `this.xxx()`？

## JWT 授权不匹配

- scope claim 长什么样？（`scope` vs `scp`）
- 你的规则写的是 `hasRole` 还是 `hasAuthority("SCOPE_xxx")`？

## 多个 FilterChain 规则冲突

- matcher 覆盖范围是否互斥？
- `@Order` 是否符合你的预期？

