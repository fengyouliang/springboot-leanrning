# 01. `Resource` 抽象：为什么 Spring 不让你直接用 `File`？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01. `Resource` 抽象：为什么 Spring 不让你直接用 `File`？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

> 同样一段读取逻辑，既可能读 classpath 文件，也可能读本地文件，也可能读 URL。

如果你只用 `File`：

## 本模块的最小闭环

`ResourceReadingService` 做了两件事：

- `readClasspathText(location)`：读取单个资源内容
- `listResourceLocations(pattern)`：用 pattern 扫描多个资源并返回 description 列表

`Resource` 的学习价值在于：

> 你写的是“读取资源”的逻辑，而不是“读取某种存储形态”的逻辑。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreResourcesLabTest`
- 建议命令：`mvn -pl spring-core-resources test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

对应 tests：

- `SpringCoreResourcesLabTest#readsClasspathResourceContent`
- `SpringCoreResourcesLabTest#loadsMultipleResourcesWithPattern`

## F. 常见坑与边界

Spring 的 `Resource` 抽象解决的是一个常见问题：

- classpath 资源在 jar 包里时根本不是“文件路径”
- 你会在开发环境 OK、打包后崩溃（典型学习陷阱）

## G. 小结与下一章

## 一句话总结

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreResourcesLabTest`

上一章：[00-deep-dive-guide](../part-00-guide/00-deep-dive-guide.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[02-classpath-locations](02-classpath-locations.md)

<!-- BOOKIFY:END -->
