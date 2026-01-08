# 01：Security FilterChain 与 Web MVC（401/403/CSRF 在哪发生）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01：Security FilterChain 与 Web MVC（401/403/CSRF 在哪发生）**
- 目标：把“加了 Spring Security 之后怎么就 401/403 了”变成可解释、可复现、可排障的调用链问题。

## B. 核心结论

- Spring Security 的主要入口是 **Servlet Filter 链**（FilterChainProxy），它发生在 **DispatcherServlet 之前**。
- 401/403 往往不是 controller 的问题：
  - **401**：未认证（Authentication 不存在/失败）
  - **403**：已认证但不允许（权限不足）或 **CSRF 缺失**（常见于 POST/PUT/DELETE）
- 工程落地建议：把“教学安全端点”与“既有教学主线端点”隔离，避免影响现有 Labs（本模块采用只保护 `/api/advanced/secure/**` 的策略）。

## C. 机制主线（请求从哪进、在哪拦）

请求进入顺序（从外到内）：

1. **Servlet 容器 Filter 链**
   - Spring Security：`DelegatingFilterProxy` → `FilterChainProxy`
2. **DispatcherServlet**
   - HandlerMapping/HandlerAdapter/ArgumentResolver/Binder/Converter
3. **Controller**
4. **异常解析与响应写回**

因此：当你看到 401/403，第一反应应该是“我有没有走到 DispatcherServlet”，而不是“controller 写错了”。

## D. 源码与断点

推荐断点（按常见问题）：

- 是否进入了 Security FilterChain：
  - `org.springframework.web.filter.DelegatingFilterProxy#doFilter`
  - `org.springframework.security.web.FilterChainProxy#doFilterInternal`
- 401（未认证）：
  - `org.springframework.security.web.authentication.www.BasicAuthenticationFilter#doFilterInternal`
  - `org.springframework.security.web.authentication.AuthenticationEntryPointFailureHandler`
- 403（权限不足）：
  - `org.springframework.security.authorization.AuthorizationManager`（实现/调用点）
  - `org.springframework.security.web.access.ExceptionTranslationFilter`
- 403（CSRF）：
  - `org.springframework.security.web.csrf.CsrfFilter#doFilterInternal`

## E. 最小可运行实验（Lab）

- Lab：`BootWebMvcSecurityLabTest`
  - 401：未认证访问 `/api/advanced/secure/ping`
  - 403：普通用户访问 `/api/advanced/secure/admin/ping`
  - 403（CSRF）：认证后 POST `/api/advanced/secure/update` 不带 token

对应源码：
- `SecurityConfig`：`springboot-web-mvc/src/main/java/com/learning/springboot/bootwebmvc/part08_security_observability/SecurityConfig.java`
- `SecureDemoController`：`springboot-web-mvc/src/main/java/com/learning/springboot/bootwebmvc/part08_security_observability/SecureDemoController.java`

## F. 常见坑与边界

- **引入 security 依赖后，slice 测试（@WebMvcTest）默认也会受到安全过滤器影响**：要么显式导入你的 `SecurityFilterChain`（本模块示例），要么在特定测试里关闭 filters（不推荐默认关闭）。
- **CSRF 的“误伤”**：如果你没有刻意控制 CSRF，原本正常的 POST 会突然 403。真实工程里通常对纯 API 关闭 CSRF，但教学场景可以保留一小段端点用于演示分支。

## G. 小结与下一章

- 下一章进入 Observability：用 Interceptor 与 Actuator 指标把“请求耗时/请求量”变成可观察事实。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcSecurityLabTest`

上一章：[part-07-testing-debugging/01-webmvc-testing-and-troubleshooting.md](../part-07-testing-debugging/01-webmvc-testing-and-troubleshooting.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-08-security-observability/02-observability-and-metrics.md](02-observability-and-metrics.md)

<!-- BOOKIFY:END -->

