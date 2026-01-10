# 自测题（Spring Core Validation）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**自测题（Spring Core Validation）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

这一章用“最小实验 + 可断言证据链”复盘三条主线：

1. programmatic validation：你显式触发，拿到 violations
2. method validation：代理触发，失败时抛 `ConstraintViolationException`
3. groups/custom constraint：决定哪些约束生效、如何扩展约束语义

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-validation test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

> 验证入口（可跑）：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`

1. `Validator` 的职责是什么？它和 `Constraint` 的关系是什么？
2. method validation 为什么需要代理？它和 `@Transactional` 这类注解一样吗？
3. group 解决的核心问题是什么？你会如何设计一个最小用例验证 group 生效？
4. 自定义约束的关键点有哪些？（注解、校验器、message、payload）

## F. 常见坑与边界

### 坑点 1：把校验当成“注解装饰”，忽略触发边界与代理边界

- Symptom：你写了很多注解，但在某些路径上没任何效果（或效果与预期不同）
- Root Cause：校验是机制系统：触发点（programmatic/method）+ 代理边界（是否走 Spring）+ groups（生效范围）
- Verification：
  - programmatic：`SpringCoreValidationLabTest#programmaticValidationFindsViolations`
  - method proxy 边界：`SpringCoreValidationMechanicsLabTest#methodValidationDoesNotRunWhenCallingAServiceDirectly_withoutSpringProxy`
  - groups：`SpringCoreValidationMechanicsLabTest#groupsControlWhichConstraintsApply`
- Fix：先把“触发边界”写成测试断言，再谈“规则设计/错误结构/工程化集成”

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`

上一章：[90-common-pitfalls](90-common-pitfalls.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[Docs TOC](../README.md)

<!-- BOOKIFY:END -->
