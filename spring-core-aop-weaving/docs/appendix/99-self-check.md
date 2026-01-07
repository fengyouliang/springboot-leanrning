# 99. 自测题：你是否真的理解了 weaving？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**99. 自测题：你是否真的理解了 weaving？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

## A. 心智模型

- 你能用一句话解释：proxy AOP 与 weaving 的根本差异是什么？
- 你能说清：为什么 weaving 不依赖“走代理的 call path”？

## B. LTW

## C. CTW

- 为什么 CTW 不需要 `-javaagent`？
- CTW 的主要代价是什么？你会如何控制织入范围？

## D. join point / pointcut

## E. 排障

- 当你遇到“拦截没发生”时，你的分流排查顺序是什么？（至少 4 步）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`AspectjCtwLabTest` / `AspectjLtwLabTest`
- 建议命令：`mvn -pl spring-core-aop-weaving test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

> 验证入口（可跑）：`AspectjLtwLabTest` / `AspectjCtwLabTest`

- LTW 生效的三个前提是什么？
- 为什么把 `aop.xml` 放在 `src/test/resources` 是一个“学习友好”的选择？它的代价是什么？

- `call` 与 `execution` 的差异是什么？你会如何在测试里验证它们触发的 kind？
- `withincode` 与 `cflow` 各自解决什么问题？为什么说它们“很强但也更难维护”？

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`AspectjCtwLabTest` / `AspectjLtwLabTest`

上一章：[90-common-pitfalls](90-common-pitfalls.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[Docs TOC](../README.md)

<!-- BOOKIFY:END -->
