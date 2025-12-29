# 01. 约束（Constraint）心智模型：你在校验什么？校验结果是什么？

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

## 在本模块如何验证

看 `SpringCoreValidationLabTest#programmaticValidationFindsViolations`：

- 传入非法 `CreateUserCommand`
- 得到 violations，并断言包含 `username/email/age`

## 一句话总结

Bean Validation 的价值在于：

> 你得到的不是 boolean，而是一组“可定位、可解释、可断言”的错误信息。

