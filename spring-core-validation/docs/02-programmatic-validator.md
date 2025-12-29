# 02. 程序化校验：为什么直接用 `Validator` 仍然很重要？

即使你最终会在 Web 层用 `@Valid`，学习阶段仍然建议掌握程序化校验：

- 它最直接、最可控
- 不依赖 Spring MVC / Controller
- 更适合做机制实验与精确断言

## 本模块的最小示例

`ProgrammaticValidationService` 只是做了一件事：

- `validator.validate(command)`

对应测试：

- `SpringCoreValidationLabTest#programmaticValidationFindsViolations`
- `SpringCoreValidationLabTest#programmaticValidationReturnsNoViolationsForValidInput`

## Debug / 观察建议

学习阶段建议你重点观察两项：

- `violation.getPropertyPath()`：究竟是哪一个字段违反了规则
- `violation.getMessage()`：默认消息是什么（后续你会学到如何自定义）

机制实验入口：`SpringCoreValidationMechanicsLabTest#constraintViolationIncludesMessageAndPropertyPath`

