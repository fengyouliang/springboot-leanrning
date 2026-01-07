# 00 - Deep Dive Guide（springboot-cache）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**00 - Deep Dive Guide（springboot-cache）**
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
- Lab：`BootCacheLabTest` / `BootCacheSpelKeyLabTest`
- 建议命令：`mvn -pl springboot-cache test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 推荐学习目标
1. 能解释“缓存命中/未命中/更新/失效”的语义差异
2. 能把 key/condition/unless 的规则写成可断言的复现
3. 能解释 `sync` 解决的是什么问题，以及它的代价与边界

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-cache test`

## 对应 Lab（可运行）

- `BootCacheLabTest`
- `BootCacheSpelKeyLabTest`
- `BootCacheExerciseTest`

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootCacheLabTest` / `BootCacheSpelKeyLabTest`
- Exercise：`BootCacheExerciseTest`

上一章：[Docs TOC](../README.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-cache/01-cacheable-basics.md](../part-01-cache/01-cacheable-basics.md)

<!-- BOOKIFY:END -->
