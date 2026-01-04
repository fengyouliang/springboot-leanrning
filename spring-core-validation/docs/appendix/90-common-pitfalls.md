# 90. 常见坑清单（建议反复对照）

## 坑 1：以为 `@Valid` 自动让 service 方法校验

- 事实：方法参数校验需要 Spring 代理拦截（见 [docs/03](03-method-validation-proxy.md)）

## 坑 2：忘了加 `@Validated`

- 现象：`@Valid` 写在方法参数上，但不抛 `ConstraintViolationException`
- 建议：对照 `MethodValidatedUserService` 的类级别 `@Validated`

## 坑 3：自调用导致 method validation 不触发

- 规律：同 AOP/Tx，自调用绕过代理
- 建议：学习阶段先用 tests 复现，再讨论设计规避方式

## 坑 4：Group 没指定导致你以为规则“失效”

- 现象：你写了 `@NotBlank(groups=Create.class)`，但 validate(Default.class) 没有 violations
- 解释：group 决定“启用哪组规则”

## 坑 5：把 violations 当成字符串拼接错误

- 建议：学会看 `propertyPath` 与 `message`，它们是结构化信息，不是“日志文本”

