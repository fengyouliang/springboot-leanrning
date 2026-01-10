# 01. 约束（Constraint）心智模型：你在校验什么？校验结果是什么？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01. 约束（Constraint）心智模型：你在校验什么？校验结果是什么？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

Bean Validation（Jakarta Validation）解决的是一个核心问题：

> 把“规则”声明在数据结构上，并得到结构化的校验结果（violations）。

## 你需要记住的 3 个对象

1) **Constraint（约束）**

例如：

- `@NotBlank`
- `@Email`
- `@Min(0)`

本模块的 `CreateUserCommand` 是最小示例。

2) **Validator**

`Validator` 是执行校验的入口：

- 你可以在代码里直接调用它（程序化校验）
- Spring Boot 会把它作为 bean 放进容器

3) **ConstraintViolation**

一次校验可能产生多个 violations，它们携带关键信息：

- 违反了哪个字段（property path）
- 错误消息（message）
- 具体的无效值、约束描述等（学习阶段先看前两个就够）

- 传入非法 `CreateUserCommand`
- 得到 violations，并断言包含 `username/email/age`

Bean Validation 的价值在于：

> 你得到的不是 boolean，而是一组“可定位、可解释、可断言”的错误信息。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreValidationLabTest`
- 建议命令：`mvn -pl spring-core-validation test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 在本模块如何验证

看 `SpringCoreValidationLabTest#programmaticValidationFindsViolations`：

## F. 常见坑与边界

### 坑点 1：只看“校验失败/成功”，忽略 violations 的证据字段，导致排障效率很低

- Symptom：你知道失败了，但不知道“失败在哪个字段、因为什么规则”，只能靠日志/猜测
- Root Cause：Bean Validation 的输出不是 boolean，而是 `ConstraintViolation` 集合（propertyPath/message 是第一现场）
- Verification：
  - violations 含字段路径：`SpringCoreValidationLabTest#programmaticValidationFindsViolations`
  - violations 含 message/propertyPath：`SpringCoreValidationMechanicsLabTest#constraintViolationIncludesMessageAndPropertyPath`
- Fix：排障先看 propertyPath/message，再决定是改数据、改规则，还是改 groups/触发方式

## G. 小结与下一章

## 一句话总结

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreValidationLabTest`

上一章：[00-deep-dive-guide](../part-00-guide/00-deep-dive-guide.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[02-programmatic-validator](02-programmatic-validator.md)

<!-- BOOKIFY:END -->
