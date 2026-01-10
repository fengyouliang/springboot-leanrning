# 02. 程序化校验：为什么直接用 `Validator` 仍然很重要？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**02. 程序化校验：为什么直接用 `Validator` 仍然很重要？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

即使你最终会在 Web 层用 `@Valid`，学习阶段仍然建议掌握程序化校验：

## 本模块的最小示例

`ProgrammaticValidationService` 只是做了一件事：

- `validator.validate(command)`

对应测试：

学习阶段建议你重点观察两项：

- `violation.getPropertyPath()`：究竟是哪一个字段违反了规则
- `violation.getMessage()`：默认消息是什么（后续你会学到如何自定义）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-validation test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

- 它最直接、最可控
- 不依赖 Spring MVC / Controller
- 更适合做机制实验与精确断言

- `SpringCoreValidationLabTest#programmaticValidationFindsViolations`
- `SpringCoreValidationLabTest#programmaticValidationReturnsNoViolationsForValidInput`

## Debug / 观察建议

机制实验入口：`SpringCoreValidationMechanicsLabTest#constraintViolationIncludesMessageAndPropertyPath`

## F. 常见坑与边界

### 坑点 1：以为“声明了注解就会自动校验”，忽略 programmatic 需要显式调用

- Symptom：你在对象字段上加了约束，但某条业务路径没有任何校验行为
- Root Cause：programmatic validation 的触发点是 `Validator#validate(...)`（不调用就不会发生）
- Verification：
  - 显式调用得到 violations：`SpringCoreValidationLabTest#programmaticValidationFindsViolations`
  - 有效输入返回空 violations：`SpringCoreValidationLabTest#programmaticValidationReturnsNoViolationsForValidInput`
- Fix：把“触发点”写进代码与测试：要么在边界层显式 validate，要么使用 method validation/框架集成触发

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`

上一章：[01-constraint-mental-model](01-constraint-mental-model.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[03-method-validation-proxy](03-method-validation-proxy.md)

<!-- BOOKIFY:END -->
