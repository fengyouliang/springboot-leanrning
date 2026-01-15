# 主线时间线：Spring Core AOP

!!! summary
    - 这一模块关注：AOP 在 Spring 中如何以“代理”的方式织入横切逻辑，以及 AutoProxy 这条主线如何工作。
    - 读完你应该能复述：**目标 Bean → AutoProxyCreator 判断 → 生成代理 → 代理链执行** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → Part 01（代理基础）→ Part 02（自动代理与切点）→ Part 03（多层代理叠加）。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`SpringCoreAopLabTest`

## 在 Spring 主线中的位置

- AOP 基于 Beans 的创建过程：**BeanPostProcessor 在创建阶段“包一层代理”** 是主线。
- 事务（@Transactional）、异步（@Async）、方法校验等很多能力，本质都依赖这条“代理主线”。

## 主线时间线（建议顺读）

1. 先把“代理 = AOP”的心智模型建立起来
   - 阅读：[01. 代理心智模型](../part-01-proxy-fundamentals/01-aop-proxy-mental-model.md)
2. 选择代理技术：JDK vs CGLIB（以及它们决定的边界）
   - 阅读：[02. JDK vs CGLIB](../part-01-proxy-fundamentals/02-jdk-vs-cglib.md)
3. 把最常见的坑先打掉：self-invocation（自调用）为什么不生效
   - 阅读：[03. self-invocation](../part-01-proxy-fundamentals/03-self-invocation.md)
4. 理解“哪些情况不能被代理”（final 等限制）与临时兜底方案（exposeProxy）
   - 阅读：[04. final 与代理限制](../part-01-proxy-fundamentals/04-final-and-proxy-limits.md)
   - 阅读：[05. exposeProxy](../part-01-proxy-fundamentals/05-expose-proxy.md)
5. 学会调试代理：先能把代理链看清楚
   - 阅读：[06. 调试代理](../part-01-proxy-fundamentals/06-debugging.md)
6. 进入主线：AutoProxyCreator 是怎么决定“要不要代理”的
   - 阅读：[07. AutoProxyCreator 主线](../part-02-autoproxy-and-pointcuts/07-autoproxy-creator-mainline.md)
7. 再进入“选择切点”的系统：表达式与匹配规则
   - 阅读：[08. 切点表达式系统](../part-02-autoproxy-and-pointcuts/08-pointcut-expression-system.md)
8. 最后处理真实世界：多个代理/多个增强如何叠加与排查
   - 阅读：[09. 多层代理叠加](../part-03-proxy-stacking/09-multi-proxy-stacking.md)
   - 阅读：[10. 叠加排障手册](../part-03-proxy-stacking/10-real-world-stacking-playbook.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
