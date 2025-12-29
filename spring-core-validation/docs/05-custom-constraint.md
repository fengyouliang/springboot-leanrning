# 05. 自定义约束：如何写一个最小可用的 `@Constraint`？

当内置约束不够用时，你可以自定义约束注解：

- 声明注解（`@interface`）
- 关联一个 `ConstraintValidator`
- 在 `isValid(...)` 里实现规则

## 在本模块如何验证

看 `SpringCoreValidationMechanicsLabTest#customConstraintsCanBeDefinedWithConstraintValidator`

本模块的示例约束是：

- `@StartsWith(prefix = "user:")`

你会看到：

- `"user:bob"` 通过
- `"bob"` 失败

## 你应该得到的结论

自定义约束并不神秘，本质是：

> 把规则封装成一个可复用的“注解 + 校验器”对。

