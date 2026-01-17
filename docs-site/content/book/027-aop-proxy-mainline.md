# 第 27 章：AOP/代理主线
<!-- CHAPTER-CARD:START -->
!!! summary "章节学习卡片（五问闭环）"

    - 知识点：AOP/代理主线
    - 怎么使用：通过切点表达式与通知声明横切意图；在 Spring 中多数能力（Tx/Cache/Validation/Method Security）都以代理方式织入。
    - 原理：目标 Bean → `AbstractAutoProxyCreator` 判断 → 生成代理（JDK/CGLIB）→ advisor/interceptor 链 → `proceed()` 形成嵌套调用。
    - 源码入口：`org.springframework.aop.framework.autoproxy.AbstractAutoProxyCreator#postProcessAfterInitialization` / `org.springframework.aop.framework.ProxyFactory` / `org.springframework.aop.framework.ReflectiveMethodInvocation#proceed`
    - 推荐 Lab：`SpringCoreAopLabTest`
<!-- CHAPTER-CARD:END -->

<!-- GLOBAL-BOOK-NAV:START -->
上一章：[第 26 章：99. 自测题：你是否真的理解了？](../spring-core-beans/docs/appendix/026-99-self-check.md) ｜ 全书目录：[Book TOC](/book/) ｜ 下一章：[第 28 章：主线时间线：Spring Core AOP](../spring-core-aop/docs/part-00-guide/028-03-mainline-timeline.md)
<!-- GLOBAL-BOOK-NAV:END -->

这一章解决的问题是：**为什么你没写任何“拦截器代码”，却能获得事务/缓存/安全/审计**？答案通常不是魔法，而是代理：在“方法调用边界”插入一段可观察、可调试、可组合的增强逻辑。

---

## 小结与下一章

<!-- BOOKLIKE-V2:SUMMARY:START -->
- 一句话总结：AOP/代理主线 —— 通过切点表达式与通知声明横切意图；在 Spring 中多数能力（Tx/Cache/Validation/Method Security）都以代理方式织入。
- 回到主线：目标 Bean → `AbstractAutoProxyCreator` 判断 → 生成代理（JDK/CGLIB）→ advisor/interceptor 链 → `proceed()` 形成嵌套调用。
- 下一章：建议按模块目录/全书目录继续顺读。
<!-- BOOKLIKE-V2:SUMMARY:END -->

## 导读

<!-- BOOKLIKE-V2:INTRO:START -->
这一章围绕「AOP/代理主线」展开：先把边界说清楚，再沿主线推进到关键分支，最后用可运行入口把结论验证出来。

阅读建议：
- 先看章首的“章节学习卡片/本章要点”，建立预期；
- 推荐先跑一遍本章 Lab，再带着问题回到正文。
<!-- BOOKLIKE-V2:INTRO:END -->

## 主线（按时间线顺读）

1. 你声明切面意图：切点（pointcut）+ 通知（advice）
2. 容器在创建 Bean 时识别“需要增强”的目标（典型是 AutoProxyCreator）
3. 选择代理策略：JDK 动态代理 or CGLIB（final/接口/可见性等边界）
4. 调用发生：进入代理 → 组装拦截链（advisors）→ `proceed()` 形成嵌套
5. 常见坑：自调用绕过代理、多个代理叠加顺序、`@Order` 与优先级

---

## 深挖入口（模块 docs）

- 模块目录页：[`spring-core-aop/docs/README.md`](../spring-core-aop/docs/README.md)
- 模块主线时间线（含可跑入口）：[`spring-core-aop/docs/part-00-guide/03-mainline-timeline.md`](../spring-core-aop/docs/part-00-guide/028-03-mainline-timeline.md)

建议先跑的最小闭环：

- `SpringCoreAopLabTest`（最小 advice 闭环 + 自调用陷阱）

---

## 本章可跑入口（最小闭环）

- Lab：`mvn -q -pl spring-core-aop -Dtest=SpringCoreAopLabTest test`（`spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part01_proxy_fundamentals/SpringCoreAopLabTest.java`）
- Exercise（动手练习，默认 `@Disabled`）：`spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part00_guide/SpringCoreAopExerciseTest.java`

---

## 下一章怎么接

当“代理”解决不了你的需求（例如拦截 constructor/field access），你需要织入（weaving）这条线。

- 下一章：[第 42 章：织入主线（LTW/CTW）](042-aop-weaving-mainline.md)

## 证据链（如何验证你真的理解了）

<!-- BOOKLIKE-V2:EVIDENCE:START -->
- 观察点 1：运行本章推荐入口后，聚焦「AOP/代理主线」的生效时机/顺序/边界；断点/入口：`org.springframework.aop.framework.autoproxy.AbstractAutoProxyCreator#postProcessAfterInitialization`；断言：你能解释“为什么此处生效/为什么此处不生效”。
- 观察点 2：运行本章推荐入口后，聚焦「AOP/代理主线」的生效时机/顺序/边界；断点/入口：`org.springframework.aop.framework.ProxyFactory`；断言：你能解释“为什么此处生效/为什么此处不生效”。
- 观察点 3：运行本章推荐入口后，聚焦「AOP/代理主线」的生效时机/顺序/边界；断点/入口：`org.springframework.aop.framework.ReflectiveMethodInvocation#proceed`；断言：你能解释“为什么此处生效/为什么此处不生效”。
- 建议：跑完 ``SpringCoreAopLabTest`` 后，把上述观察点逐条对照，写出你自己的 1–2 句结论（可复述）。
<!-- BOOKLIKE-V2:EVIDENCE:END -->
