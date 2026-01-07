# 深挖指南（Spring Core Tx）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**深挖指南（Spring Core Tx）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreTxLabTest` / `SpringCoreTxSelfInvocationPitfallLabTest`
- 建议命令：`mvn -pl spring-core-tx test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

> 验证入口（可跑）：
> - `SpringCoreTxLabTest`
> - `SpringCoreTxSelfInvocationPitfallLabTest`

配套验证入口：
- Labs/Exercises：见 `src/test/java/com/learning/springboot/springcoretx/**`

## F. 常见坑与边界

建议阅读顺序：
1. 先把“事务边界”想清楚：哪里开、哪里关（Part 01）
2. 再把“代理机制”想清楚：为什么 self-invocation 会绕过事务（Part 01 + Appendix）
3. 最后进入回滚规则、传播与编程式事务（Part 01 + Part 02）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreTxLabTest` / `SpringCoreTxSelfInvocationPitfallLabTest`

上一章：[Docs TOC](../README.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[01-transaction-boundary](../part-01-transaction-basics/01-transaction-boundary.md)

<!-- BOOKIFY:END -->
