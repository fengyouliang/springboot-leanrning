# 99. 自测题：你是否真的理解了 AOP？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**99. 自测题：你是否真的理解了 AOP？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

## A. 代理与入口（对应 01/00）

- 你能不能用一句话解释：为什么 Spring AOP 的本质是“改调用链”，而不是“改方法体”？
- “AOP 生效”的两个前提分别是什么？（提示：call path + pointcut）
- 你能不能说清：proxy 通常在哪个阶段产生？（提示：BPP after-init）

## B. 代理类型（对应 02）

## C. 自调用与解决策略（对应 03/05）

- 为什么 `this.inner()` 不会被拦截？你能画出两条调用链的区别吗？
- 工程上最推荐的修复方案是什么？`AopContext.currentProxy()` 为什么不建议滥用？
- `AopContext.currentProxy()` 依赖的两个条件是什么？

## D. 代理限制（对应 04）

- 为什么 CGLIB 拦截不到 final method？private/static 呢？
- 为什么“构造器/初始化阶段内部调用”经常会让你误判 AOP 失效？

## E. 顺序与排障（对应 06/90/00）

- 多个切面时，`@Order` 如何影响嵌套关系？（谁在外层、谁先执行）
- 当你遇到“不拦截”的问题，你的排查顺序是什么？（至少 4 步）

## F. AutoProxyCreator 主线（对应 07/00）

## G. pointcut 表达式系统（对应 08）

## H. 多切面/多代理叠加（对应 09）

- 你能否解释清楚两种“叠加”的含义：单 proxy 多 advisors vs 多层 proxy（套娃）？
- 你能不能说清：顺序问题到底属于 BPP 顺序，还是 advisor/interceptor 顺序？各自去哪里看？
- 你会如何用 `Advised#getAdvisors()` 把“叠加实体”直接看见，而不是靠猜？

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章未显式引用 LabTest，先注入模块默认 LabTest 作为“合规兜底入口”（后续可逐章细化）。
- Lab：`SpringCoreAopAutoProxyCreatorInternalsLabTest` / `SpringCoreAopLabTest`
- 建议命令：`mvn -pl spring-core-aop test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

- 先不看代码，尝试回答
- 再去对应章节/实验里验证
- 最后再启用 Exercises 把理解落实成可运行的结论

- 为什么 JDK proxy 下 `getBean(实现类.class)` 可能会失败？
- `proxyTargetClass=true/false` 各自意味着什么？你会如何在测试里验证代理类型？

- 你能不能解释：为什么 AutoProxyCreator 的本质是一个 BPP，而不是“运行时改类”？
- 你能不能说清：Advisor/Pointcut/Advice 三层模型分别是什么？它们如何组合成拦截器链？
- 你在源码里想看“为什么这个 bean 会/不会被代理”，应该去哪两个断点？（提示：eligible advisors + canApply）

- `execution` 与 `within` 的区别是什么？你会怎么避免“范围太宽/太窄”的误判？
- `this(实现类)` 与 `target(实现类)` 的区别是什么？为什么在 JDK proxy 下结果会不同？
- `@annotation/@within/@target` 的差异是什么？你会如何在项目里验证你的理解？

## I. 动手题（建议直接做 Exercises）

- 让自调用也触发 advice：启用 exposeProxy，并完成 `SpringCoreAopExerciseTest#exercise_makeSelfInvocationTriggerAdvice`
- 新增一个 `@Order(0)` 的切面，并证明它会在现有切面之前执行：`SpringCoreAopExerciseTest#exercise_addOrderedAspect`
- 把 pointcut 从 `@annotation` 改成 `execution(...)`，并更新测试：`SpringCoreAopExerciseTest#exercise_changePointcutStyle`

## F. 常见坑与边界

### 坑点 1：只背概念不做验证，遇到“不拦截”就只能靠猜

- Symptom：你能复述术语，但在真实项目里某个切面不生效时无法给出证据链
- Root Cause：AOP 是分支系统（call path / proxy 类型 / pointcut / advisor 顺序），不做实验就很难真正“对齐事实”
- Verification（建议把这两条作为排障兜底入口）：
  - this vs target（JDK/CGLIB 差异）：`SpringCoreAopPointcutExpressionsLabTest#this_vs_target_differs_between_JdkProxy_and_CglibProxy`
  - 单 proxy 多 advisors vs 套娃：`SpringCoreAopMultiProxyStackingLabTest#multiple_advisors_are_applied_within_a_single_proxy_by_default`
- Fix：遇到问题先跑对应 Lab，把“误判”变成可断言事实，再改 pointcut/配置/调用路径

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreAopAutoProxyCreatorInternalsLabTest` / `SpringCoreAopLabTest`
- Exercise：`SpringCoreAopExerciseTest`

上一章：[90-common-pitfalls](90-common-pitfalls.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[Docs TOC](../README.md)

<!-- BOOKIFY:END -->
