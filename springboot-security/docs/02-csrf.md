# 02：CSRF：为什么 GET 没事但 POST 会 403？

本章通过一个最小 POST 接口复现 CSRF 现象，并解释：为什么你“明明已经登录了”，POST 还是会 403。

## 实验入口

- `springboot-security/src/test/java/com/learning/springboot/bootsecurity/BootSecurityLabTest.java`
  - `csrfBlocksPostEvenWhenAuthenticated`
  - `csrfTokenAllowsPostWhenAuthenticated`

## 你应该观察到什么

- 对 `/api/secure/change-email` 发起 POST：
  - 即使 Basic Auth 已登录，如果没有 CSRF token → **403**（本模块返回 `csrf_failed`）
  - 在测试中显式加上 `.with(csrf())` 后 → **200**

## 机制解释（Why）

CSRF 的核心点不是“你有没有登录”，而是：

- 当请求会改变服务器状态（POST/PUT/DELETE 等），Spring Security 默认会要求一个“来自可信页面/会话”的 token。
- 这个 token 在浏览器场景通常由表单/页面自动携带；但在 API 场景/测试场景需要你显式带上。

本模块故意保留了 Basic Auth 链路的 CSRF 默认行为，让你亲手复现与断言：

- **有认证 ≠ 允许所有写操作**

## Debug 建议

- 优先在 tests 里复现：`MockMvc` + `csrf()` 比 curl 更可控。
- 想更进一步：把 missing/invalid CSRF 的 message 拆细（Exercise 有引导）。

