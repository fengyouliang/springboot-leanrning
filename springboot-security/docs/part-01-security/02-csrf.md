# 02：CSRF：为什么 GET 没事但 POST 会 403？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**02：CSRF：为什么 GET 没事但 POST 会 403？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

## 你应该观察到什么

- 对 `/api/secure/change-email` 发起 POST：
  - 即使 Basic Auth 已登录，如果没有 CSRF token → **403**（本模块返回 `csrf_failed`）
  - 在测试中显式加上 `.with(csrf())` 后 → **200**

## 机制解释（Why）

CSRF 的核心点不是“你有没有登录”，而是：

- 当请求会改变服务器状态（POST/PUT/DELETE 等），Spring Security 默认会要求一个“来自可信页面/会话”的 token。
- 这个 token 在浏览器场景通常由表单/页面自动携带；但在 API 场景/测试场景需要你显式带上。

- **有认证 ≠ 允许所有写操作**

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootSecurityLabTest`
- 建议命令：`mvn -pl springboot-security test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

本章通过一个最小 POST 接口复现 CSRF 现象，并解释：为什么你“明明已经登录了”，POST 还是会 403。

## 实验入口

- `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
  - `csrfBlocksPostEvenWhenAuthenticated`
  - `csrfTokenAllowsPostWhenAuthenticated`

本模块故意保留了 Basic Auth 链路的 CSRF 默认行为，让你亲手复现与断言：

## Debug 建议

- 优先在 tests 里复现：`MockMvc` + `csrf()` 比 curl 更可控。
- 想更进一步：把 missing/invalid CSRF 的 message 拆细（Exercise 有引导）。

## F. 常见坑与边界

### 坑点 1：为“修复 403”而全局关闭 CSRF，反而把安全边界打穿

- Symptom：你在 API 测试/本地调试里遇到 POST 403，于是直接禁用 CSRF，问题“消失”但风险扩大
- Root Cause：
  - CSRF 是针对“有状态（cookie/session）”的威胁模型；这类请求默认需要 token
  - JWT 无状态 API 通常不需要 CSRF（或按路径分流），但这不等于所有链路都该关闭
- Verification：
  - Basic 链路：缺 token 会 403：`BootSecurityLabTest#csrfBlocksPostEvenWhenAuthenticated`
  - 加 token 才通过：`BootSecurityLabTest#csrfTokenAllowsPostWhenAuthenticated`
  - JWT 链路：POST 不需要 CSRF：`BootSecurityLabTest#jwtPostDoesNotRequireCsrf`
- Fix：按链路分流（有状态链路保留 CSRF；无状态链路按需关闭），不要“一刀切”

### 坑点 2：我“禁用了 CSRF”，但 POST 还是 403（原因：请求命中了另一条 SecurityFilterChain）

- Symptom：你在配置里写了 `csrf.disable()`，但 POST 仍然返回 `csrf_failed`
- Root Cause：
  - CSRF 是否生效，不取决于“你有没有写 disable”，而取决于**请求最终命中哪条 `SecurityFilterChain`**
  - 一旦命中的是 Basic 链路（默认 CSRF 开启），就会走 `CsrfFilter`
- Verification（三段证据链闭环）：
  - Basic 链路缺 token → 403：`BootSecurityLabTest#csrfBlocksPostEvenWhenAuthenticated`
  - JWT 链路 POST 不需要 CSRF → 200：`BootSecurityLabTest#jwtPostDoesNotRequireCsrf`
  - 用过滤器列表证明“命中哪条链”：`BootSecurityMultiFilterChainOrderLabTest#jwtPathMatchesJwtChain_andApiPathMatchesBasicChain`
- Breakpoints：
  - `org.springframework.security.web.FilterChainProxy#doFilterInternal`（选择 chain）
  - `org.springframework.security.web.DefaultSecurityFilterChain#matches`（匹配判定）
  - `org.springframework.security.web.csrf.CsrfFilter#doFilterInternal`（CSRF 拦截点）
- Fix：让 matcher 覆盖范围互斥、顺序明确（@Order），并用默认 Lab 把“命中链路”固定成回归门禁

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootSecurityLabTest`
- Test file：`springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`

上一章：[part-01-security/01-basic-auth-and-authorization.md](01-basic-auth-and-authorization.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-security/03-method-security-and-proxy.md](03-method-security-and-proxy.md)

<!-- BOOKIFY:END -->
