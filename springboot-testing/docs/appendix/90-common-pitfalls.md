# 90 - Common Pitfalls（springboot-testing）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**90 - Common Pitfalls（springboot-testing）**
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
- Lab：`BootTestingMockBeanLabTest` / `GreetingControllerSpringBootLabTest` / `GreetingControllerWebMvcLabTest`
- 建议命令：`mvn -pl springboot-testing test`（或在 IDE 直接运行上面的测试类）

## F. 常见坑与边界

## 常见坑
1. 误把 slice 当成全量上下文：缺失的 bean/auto-config 导致误判
2. `@MockBean` 过度使用：测试变成“模拟驱动”，与真实行为脱节
3. 测试不稳定：依赖随机端口/时间/并发时机但没有隔离策略

## 对应 Lab（可运行）

- `GreetingControllerWebMvcLabTest`
- `GreetingControllerSpringBootLabTest`
- `BootTestingMockBeanLabTest`

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootTestingMockBeanLabTest` / `GreetingControllerSpringBootLabTest` / `GreetingControllerWebMvcLabTest`

上一章：[part-01-testing/01-slice-and-mocking.md](../part-01-testing/01-slice-and-mocking.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/99-self-check.md](99-self-check.md)

<!-- BOOKIFY:END -->
