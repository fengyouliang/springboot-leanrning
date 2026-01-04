# 00 - Deep Dive Guide（springboot-security）

## 推荐学习目标
1. 能按“Filter Chain → Authentication → Authorization”讲清主线
2. 能解释 CSRF 的威胁模型与默认行为
3. 能解释方法级安全为何依赖代理，以及常见的自调用绕过陷阱
4. 能解释 JWT 无状态方案的边界：认证与授权分别在哪里发生

## 推荐阅读顺序
1. `docs/part-01-security/01-basic-auth-and-authorization.md`
2. `docs/part-01-security/02-csrf.md`
3. `docs/part-01-security/04-filter-chain-and-order.md`
4. `docs/part-01-security/03-method-security-and-proxy.md`
5. `docs/part-01-security/05-jwt-stateless.md`
6. `docs/appendix/90-common-pitfalls.md`
7. `docs/appendix/99-self-check.md`

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-security test`

