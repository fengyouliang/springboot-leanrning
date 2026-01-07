# 03. `classpath*:` 与 pattern：为什么它能“扫到多个资源”？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**03. `classpath*:` 与 pattern：为什么它能“扫到多个资源”？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

当你想一次性加载多个资源时，会用到两件事：

- `ResourcePatternResolver`
- `classpath*:` + 通配符（pattern）

- pattern：`classpath*:data/*.txt`
- 断言能找到 `hello.txt` 与 `info.txt`

- `ResourceReadingService#listResourceLocations(...)` 会返回 `Resource#getDescription()`
- 并排序，保证断言稳定

## 学习建议：避免“顺序不稳定”误判机制

pattern 扫描返回的资源数组顺序不一定稳定（与 classpath 顺序、jar 顺序有关）。

本模块的做法值得复用：

- 把结果映射成可读的 description
- 排序后再断言

`classpath*:` 的价值在于：

> 它面向的是“classpath 上的所有匹配资源”，而不是某一个具体位置。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreResourcesLabTest` / `SpringCoreResourcesMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-resources test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 在本模块如何验证

看 `SpringCoreResourcesMechanicsLabTest#classpathStarPatternLoadsResourcesFromClasspath`

看 `SpringCoreResourcesLabTest#patternResultsContainExpectedFilenames`：

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

## 一句话总结

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreResourcesLabTest` / `SpringCoreResourcesMechanicsLabTest`

上一章：[02-classpath-locations](02-classpath-locations.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[04-exists-and-handles](04-exists-and-handles.md)

<!-- BOOKIFY:END -->
