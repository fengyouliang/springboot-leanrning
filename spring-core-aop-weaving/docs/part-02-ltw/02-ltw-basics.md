# 02. LTW：Load-Time Weaving（-javaagent）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**02. LTW：Load-Time Weaving（-javaagent）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

LTW 的一句话定义：

> 在 **类加载** 时织入（不改源码），通过 `-javaagent:aspectjweaver.jar` 启动 JVM。

---

## 1. LTW 的三个“生效前提”

### 1.1 JVM 必须带 `-javaagent`

- `-javaagent:${project.build.directory}/aspectjweaver.jar`

### 1.2 classpath 必须有 `META-INF/aop.xml`

本模块的 `aop.xml` 放在：

### 1.3 织入范围必须覆盖到目标类

`aop.xml` 里的 `<weaver><include within="..."/></weaver>` 决定了 weaving 的范围。  
范围太大：风险与噪声大；范围太小：你会误判“没生效”。

---

## 2. LTW 的学习闭环（本模块提供）

- 非 Spring Bean（`new`）也可拦截：`ltw_canWeaveExecutionForNonSpringObjects`
- 自调用不绕过：`ltw_selfInvocationDoesNotBypassWeaving`
- `call vs execution`：`ltw_callVsExecution_areDifferentJoinPointKinds`
- constructor / field get/set：`ltw_constructorCallAndExecution_canBeIntercepted`、`ltw_fieldGetAndSet_canBeIntercepted`
- 高级表达式：`withincode` / `cflow`

---

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`AspectjLtwLabTest`
- 建议命令：`mvn -pl spring-core-aop-weaving test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

本模块通过 surefire 执行 `*Ltw*Test` 时自动附带：

对应的 Lab 断言：

- `AspectjLtwLabTest#ltw_testJvmIsStartedWithJavaAgent`

- `src/test/resources/META-INF/aop.xml`

因此它只影响测试运行（学习用），不会影响你 `spring-boot:run` 的默认启动。

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

下一章：[`03-ctw-basics`](../part-03-ctw/03-ctw-basics.md)

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`AspectjLtwLabTest`

上一章：[01-proxy-vs-weaving](../part-01-mental-model/01-proxy-vs-weaving.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[03-ctw-basics](../part-03-ctw/03-ctw-basics.md)

<!-- BOOKIFY:END -->
