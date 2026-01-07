# 90：常见坑清单（Security）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**90：常见坑清单（Security）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootSecurityDevProfileLabTest` / `BootSecurityLabTest`
- 建议命令：`mvn -pl springboot-security test`（或在 IDE 直接运行上面的测试类）

## F. 常见坑与边界

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

## 对应 Lab（可运行）

- `BootSecurityLabTest`
- `BootSecurityDevProfileLabTest`

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootSecurityDevProfileLabTest` / `BootSecurityLabTest`

上一章：[part-01-security/05-jwt-stateless.md](../part-01-security/05-jwt-stateless.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/99-self-check.md](99-self-check.md)

<!-- BOOKIFY:END -->
