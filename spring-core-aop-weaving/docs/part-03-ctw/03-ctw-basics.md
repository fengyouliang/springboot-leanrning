# 03. CTW：Compile-Time Weaving（编译期织入）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**03. CTW：Compile-Time Weaving（编译期织入）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

CTW 的一句话定义：

---

因此本模块提供一个关键断言：

它用于证明：CTW 的结论不是“因为 agent 在”，而是“因为字节码已经变了”。

---

## 2. 为什么 CTW 仍然需要谨慎

CTW 的代价主要在于：

- 构建过程更复杂（插件配置、织入范围、与 IDE 的一致性）
- 织入范围不当会让“全局行为”变得难以预期

因此本模块默认把 CTW 的织入范围控制在：

- `com.learning.springboot.springcoreaopweaving.ctwtargets..*`

---

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`AspectjCtwLabTest`
- 建议命令：`mvn -pl spring-core-aop-weaving test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

> 在 **构建期** 把横切逻辑织入字节码，运行时不需要 `-javaagent`。

## 1. CTW 的“验证点”与 LTW 不同

LTW 的验证点是“JVM 启动参数 + aop.xml + include 范围”。  
CTW 的验证点是“构建产物是否已被织入”。

- `AspectjCtwLabTest#ctw_testJvmIsNotStartedWithAspectjJavaAgent`

> ⚠️ 版本提示：本模块为了兼容 `aspectj-maven-plugin` 内置的 ajc，把编译目标设置为 `--release 16`（运行仍需 JDK 17+）。  
> 这不影响 weaving 关键结论，但会影响你在本模块里使用 Java 17+ 语法特性。

并用 Labs 验证“只织入应该织入的类”。

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

下一章：[`04-join-point-cookbook`](../part-04-join-points/04-join-point-cookbook.md)

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`AspectjCtwLabTest`

上一章：[02-ltw-basics](../part-02-ltw/02-ltw-basics.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[04-join-point-cookbook](../part-04-join-points/04-join-point-cookbook.md)

<!-- BOOKIFY:END -->
