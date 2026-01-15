# 第 3 章：AOP/代理主线

这一章解决的问题是：**为什么你没写任何“拦截器代码”，却能获得事务/缓存/安全/审计**？答案通常不是魔法，而是代理：在“方法调用边界”插入一段可观察、可调试、可组合的增强逻辑。

---

## 主线（按时间线顺读）

1. 你声明切面意图：切点（pointcut）+ 通知（advice）
2. 容器在创建 Bean 时识别“需要增强”的目标（典型是 AutoProxyCreator）
3. 选择代理策略：JDK 动态代理 or CGLIB（final/接口/可见性等边界）
4. 调用发生：进入代理 → 组装拦截链（advisors）→ `proceed()` 形成嵌套
5. 常见坑：自调用绕过代理、多个代理叠加顺序、`@Order` 与优先级

---

## 深挖入口（模块 docs）

- 模块目录页：[`spring-core-aop/docs/README.md`](../spring-core-aop/docs/README.md)
- 模块主线时间线（含可跑入口）：[`spring-core-aop/docs/part-00-guide/03-mainline-timeline.md`](../spring-core-aop/docs/part-00-guide/03-mainline-timeline.md)

建议先跑的最小闭环：

- `SpringCoreAopLabTest`（最小 advice 闭环 + 自调用陷阱）

---

## 下一章怎么接

当“代理”解决不了你的需求（例如拦截 constructor/field access），你需要织入（weaving）这条线。

- 下一章：[第 4 章：织入主线（LTW/CTW）](04-aop-weaving-mainline.md)

