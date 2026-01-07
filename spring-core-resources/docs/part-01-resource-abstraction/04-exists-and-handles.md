# 04. `getResource(...)` 的返回值：为什么它会“返回一个不存在的资源句柄”？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**04. `getResource(...)` 的返回值：为什么它会“返回一个不存在的资源句柄”？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

很多人第一次看到下面的现象会困惑：

> `resolver.getResource("classpath:data/missing.txt")` 也会返回一个 Resource 对象。

这并不是 bug，这是设计。

- `getResource(...)` 返回一个 handle（句柄）
- 你需要用 `resource.exists()` 判断它是否真实存在

## 为什么要这样设计？

因为 Resource 的目标是统一抽象：

## 学习建议

当你需要更友好的错误处理时：

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreResourcesMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-resources test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 在本模块如何验证

看 `SpringCoreResourcesMechanicsLabTest#getResourceReturnsAHandle_evenIfTheResourceDoesNotExist`

- “如何定位资源” 与 “资源是否存在” 是两件事
- 句柄可以携带描述信息，方便 debug（见 [05. reading-and-encoding](05-reading-and-encoding.md)）

- 先显式 `exists()` 判断
- 再决定抛出什么异常/提示（Exercise 里会让你练）

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreResourcesMechanicsLabTest`

上一章：[03-classpath-star-and-pattern](03-classpath-star-and-pattern.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[05-reading-and-encoding](05-reading-and-encoding.md)

<!-- BOOKIFY:END -->
