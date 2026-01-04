# 深挖指南（Spring Core Tx）

建议阅读顺序：
1. 先把“事务边界”想清楚：哪里开、哪里关（Part 01）
2. 再把“代理机制”想清楚：为什么 self-invocation 会绕过事务（Part 01 + Appendix）
3. 最后进入回滚规则、传播与编程式事务（Part 01 + Part 02）

配套验证入口：
- Labs/Exercises：见 `src/test/java/com/learning/springboot/springcoretx/**`

