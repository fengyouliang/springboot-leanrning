# 00 - Deep Dive Guide（springboot-basics）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**00 - Deep Dive Guide（springboot-basics）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

## 你将学到什么
1. 配置从哪里来：`Environment` 里的 `PropertySources` 如何组合
2. Profiles 如何影响 Bean 与属性：`spring.profiles.active` 的作用域与优先级
3. `@ConfigurationProperties` 如何绑定：从 `Binder` 到目标对象的映射规则

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootBasicsDefaultLabTest` / `BootBasicsDevLabTest` / `BootBasicsOverrideLabTest`
- 建议命令：`mvn -pl springboot-basics test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 如何跑实验（建议）
- 运行本模块全部测试：`mvn -pl springboot-basics test`

## Labs & Exercises 快速入口
- Labs（观察点 + 断言）：见 `docs/README.md` 的 “Labs & Exercises”

## 对应 Lab（可运行）

- `BootBasicsDefaultLabTest`
- `BootBasicsDevLabTest`
- `BootBasicsOverrideLabTest`
- `BootBasicsExerciseTest`

## F. 常见坑与边界

## 推荐阅读顺序
1. [01-property-sources-and-profiles](../part-01-boot-basics/01-property-sources-and-profiles.md)
2. [02-configuration-properties-binding](../part-01-boot-basics/02-configuration-properties-binding.md)
3. [90-common-pitfalls](../appendix/90-common-pitfalls.md)
4. [99-self-check](../appendix/99-self-check.md)

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootBasicsDefaultLabTest` / `BootBasicsDevLabTest` / `BootBasicsOverrideLabTest`
- Exercise：`BootBasicsExerciseTest`

上一章：[Docs TOC](../README.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-boot-basics/01-property-sources-and-profiles.md](../part-01-boot-basics/01-property-sources-and-profiles.md)

<!-- BOOKIFY:END -->
