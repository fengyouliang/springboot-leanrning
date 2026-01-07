# springboot-security 文档

本模块聚焦 Spring Security 的认证授权、CSRF、Filter Chain 顺序、方法级安全（AOP/proxy）以及 JWT 无状态方案。

## Start Here
- 导读：[part-00-guide/00-deep-dive-guide.md](part-00-guide/00-deep-dive-guide.md)

## Part 01 - Security（主线机制）
- 01 Basic Auth 与授权：[part-01-security/01-basic-auth-and-authorization.md](part-01-security/01-basic-auth-and-authorization.md)
- 02 CSRF：[part-01-security/02-csrf.md](part-01-security/02-csrf.md)
- 03 方法级安全与代理：[part-01-security/03-method-security-and-proxy.md](part-01-security/03-method-security-and-proxy.md)
- 04 Filter Chain 与顺序：[part-01-security/04-filter-chain-and-order.md](part-01-security/04-filter-chain-and-order.md)
- 05 JWT Stateless：[part-01-security/05-jwt-stateless.md](part-01-security/05-jwt-stateless.md)

## Appendix
- 常见坑：[appendix/90-common-pitfalls.md](appendix/90-common-pitfalls.md)
- 自测题：[appendix/99-self-check.md](appendix/99-self-check.md)

## Labs & Exercises（最小可复现入口）
- Labs：`springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
- Exercises：`springboot-security/src/test/java/com/learning/springboot/bootsecurity/part00_guide/BootSecurityExerciseTest.java`

## 核心源码入口（用于对照 docs）
- 安全配置：`springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/SecurityConfig.java`
- Filter：`springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/TraceIdFilter.java`
- 方法级安全示例：`springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/AdminOnlyService.java`
- 自调用陷阱示例：`springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/SelfInvocationPitfallService.java`
- JWT：`springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/JwtTokenService.java`
