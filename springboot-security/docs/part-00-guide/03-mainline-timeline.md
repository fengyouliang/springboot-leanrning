# 主线时间线：Spring Boot Security

!!! summary
    - 这一模块关注：安全在 Spring 中如何以 FilterChain 形式接入请求链路，以及认证/授权/CSRF/JWT 的关键分支。
    - 读完你应该能复述：**请求进入 → Security FilterChain → 认证 → 授权 → 继续到 MVC/返回** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → Part 01 顺读 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`BootSecurityLabTest`

## 在 Spring 主线中的位置

- Security 在 Web 入口之前：先过 FilterChain，再进入 MVC（DispatcherServlet）。
- 很多“401/403/登录态不对”的问题，本质是过滤器顺序、匹配范围、鉴权表达式或 Session/JWT 的边界。

## 主线时间线（建议顺读）

1. 基础认证与授权：先把 401/403 的含义与分支跑通
   - 阅读：[01. 基础认证与授权](../part-01-security/01-basic-auth-and-authorization.md)
2. CSRF：什么时候需要、为什么会报 403、怎么验证
   - 阅读：[02. CSRF](../part-01-security/02-csrf.md)
3. 方法级安全：为什么它依赖代理（以及常见边界）
   - 阅读：[03. 方法安全与代理](../part-01-security/03-method-security-and-proxy.md)
4. FilterChain 与顺序：很多“看起来怪”的行为都在这里
   - 阅读：[04. FilterChain 与顺序](../part-01-security/04-filter-chain-and-order.md)
5. JWT 无状态：如何把认证态从 Session 迁移到 Token
   - 阅读：[05. JWT 无状态](../part-01-security/05-jwt-stateless.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
