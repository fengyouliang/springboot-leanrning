# 01. AOP 心智模型：代理（Proxy）+ 入口（Call Path）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01. AOP 心智模型：代理（Proxy）+ 入口（Call Path）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

Spring AOP 学习最关键的不是“会写一个 `@Aspect`”，而是建立一个稳定的心智模型：

> **AOP 默认基于代理实现**：只有“通过代理对象发起的调用”才会被 advice 包起来。

## 你需要记住的 3 件事

3. **AOP 的本质是“在调用链上插一段逻辑”**
   - `@Around` 最直观：`joinPoint.proceed()` 前后都能做事（计时、鉴权、日志、事务等）。

## 2. 容器视角：AOP 不是“改类”，而是 BPP 把 Bean 换成 Proxy

当你把 AOP 放回到 IoC 容器里看，会更清晰：

- Bean 的创建过程里会执行很多 `BeanPostProcessor`
- AOP 的关键基础设施（AutoProxyCreator）就是一个 **BeanPostProcessor**
- 它会在初始化后阶段判断：这个 bean 是否需要被增强？如果需要，就 **返回一个 proxy** 作为“最终暴露的 bean”

这也是为什么：

> 深挖入口：如果你想在源码里“看见”这一段，建议先读 [00. 深挖指南](../part-00-guide/00-deep-dive-guide.md)。

重点看这些断言：

- proxy 产生（容器阶段）：
  - `AbstractAutoProxyCreator#postProcessAfterInitialization`
  - `AbstractAutoProxyCreator#wrapIfNecessary`
- advice 链执行（调用阶段）：
  - `JdkDynamicAopProxy#invoke` / `CglibAopProxy.DynamicAdvisedInterceptor#intercept`
  - `ReflectiveMethodInvocation#proceed`

### 推荐观察点（watch list）

- `beanName`：你在看哪个 bean 的代理决策
- `AopUtils.isAopProxy(bean)` / `AopUtils.isJdkDynamicProxy(bean)` / `AopUtils.isCglibProxy(bean)`：最终形态
- `interceptorsAndDynamicMethodMatchers`：这次调用的拦截器链条（顺序非常关键）

建议你按这个顺序跑（每个都能快速闭环）：

## 对照代码（最小闭环）

- `spring-core-aop/src/main/java/.../Traced.java`：标记注解
- `spring-core-aop/src/main/java/.../TracingAspect.java`：`@Around("@annotation(...@Traced)")`
- `spring-core-aop/src/main/java/.../TracedBusinessService.java`：被拦截的目标方法
- `spring-core-aop/src/main/java/.../InvocationLog.java`：用来做“可断言的观察点”（比日志更稳定）

当你觉得 AOP “没生效”时，先不要怀疑注解/表达式，第一时间问自己：

> **这次调用有没有走代理？**

## 排障分流：这是调用路径问题，还是匹配/限制问题？

当你遇到 “AOP 没生效” 的问题，建议先用分流思路避免走弯路：

把问题落到这三类里，你就会发现排障会稳定很多。

## 下一步（把理解推进到“源码级可复述”）

- 想看清 AOP 作为容器扩展点的主线：AutoProxyCreator/Advisor/Advice/Pointcut → 见 [07. autoproxy-creator-mainline](../part-02-autoproxy-and-pointcuts/07-autoproxy-creator-mainline.md)
- 想系统掌握 pointcut 表达式并避免误判（execution/within/this/target/...）→ 见 [08. pointcut-expression-system](../part-02-autoproxy-and-pointcuts/08-pointcut-expression-system.md)
- 想看懂“多切面/多代理叠加与顺序”（AOP/Tx/Cache/Security）→ 见 [09. multi-proxy-stacking](../part-03-proxy-stacking/09-multi-proxy-stacking.md)

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreAopLabTest`
- 建议命令：`mvn -pl spring-core-aop test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

1. **代理对象 ≠ 目标对象**
   - 你注入的 bean 很可能是一个“包装对象”（proxy），而不是你的实现类本身。
   - 这会影响：类型判断（`instanceof`）、`getClass()`、调试时看到的调用栈。

2. **advice 生效的前提：调用必须“经过代理”**
   - 外部（其它 bean / Controller / Test）调用 bean 方法：通常会经过代理 → advice 生效。
   - 同一个类内部 `this.xxx()` 调用：不会经过代理 → advice **不生效**（见 [03. self-invocation](03-self-invocation.md)）。

- 你注入到业务里的对象可能不是你写的实现类
- `getClass()`/类型匹配/调试栈会出现你没写过的 proxy 类
- 同一套 proxy 限制会同时影响 AOP、事务（`@Transactional`）、缓存（`@Cacheable`）等（它们底层都离不开 proxy）

## 在本模块如何验证（建议先跑这个）

运行测试：

```bash
mvn -pl spring-core-aop test
```

- `SpringCoreAopLabTest#tracedBusinessServiceIsAnAopProxy`：证明注入的 bean 是代理
- `SpringCoreAopLabTest#adviceIsAppliedToTracedMethod`：证明 `@Traced` 方法被 `TracingAspect` 拦截

## 源码锚点（建议从这里下断点）

如果你只想抓主线，不想在 AOP 源码里迷路，这几个断点足够覆盖 80% 的理解与排障：

## 断点闭环（用本仓库 Lab/Test 跑一遍）

1. `SpringCoreAopLabTest#tracedBusinessServiceIsAnAopProxy`：先确认“你拿到的是 proxy”
2. `SpringCoreAopLabTest#adviceIsAppliedToTracedMethod`：再确认“advice 确实包住了方法调用”
3. `SpringCoreAopLabTest#selfInvocationDoesNotTriggerAdviceForInnerMethod`：最后确认“call path 决定是否拦截”

## F. 常见坑与边界

1. **调用路径（call path）**
   - 是否自调用？是否绕过 Spring 容器（`new` 出来/静态方法）？
2. **匹配（pointcut）**
   - 切点是否命中？是否命中到了你以为的方法？
3. **代理限制（proxy limits）**
   - final/private/static/构造期调用 等边界是否踩中？

## G. 小结与下一章

## 一句话总结

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreAopLabTest`

上一章：[00-deep-dive-guide](../part-00-guide/00-deep-dive-guide.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[02-jdk-vs-cglib](02-jdk-vs-cglib.md)

<!-- BOOKIFY:END -->
