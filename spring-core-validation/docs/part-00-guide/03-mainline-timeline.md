# 主线时间线：Spring Validation

!!! summary
    - 这一模块关注：Bean Validation（JSR-380）在 Spring 中如何落地，包括约束模型、方法级校验与代理边界。
    - 读完你应该能复述：**定义约束 → 触发校验（对象/方法）→ 生成约束违规 → 映射为错误输出** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → Part 01 顺读 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`SpringCoreValidationLabTest`

## 在 Spring 主线中的位置

- 校验贯穿“入口层”（Web 参数/DTO）与“领域层”（方法级约束）：很多问题会同时触及 WebMVC 与 AOP 代理边界。
- 如果你遇到“方法校验不生效/自调用不生效”，通常要回到“代理主线”一起看（AOP 模块）。

## 主线时间线（建议顺读）

1. 先建立约束心智模型：Constraint/Validator/Violation 的关系
   - 阅读：[01. 约束心智模型](../part-01-validation-core/01-constraint-mental-model.md)
2. 显式校验：Programmatic Validator 如何工作（以及什么时候用它）
   - 阅读：[02. Programmatic Validator](../part-01-validation-core/02-programmatic-validator.md)
3. 方法级校验：为什么它需要代理、边界在哪里
   - 阅读：[03. 方法校验与代理](../part-01-validation-core/03-method-validation-proxy.md)
4. Groups：一套 DTO 多场景校验怎么组织
   - 阅读：[04. Groups](../part-01-validation-core/04-groups.md)
5. 自定义约束：从注解到 Validator 的闭环
   - 阅读：[05. 自定义约束](../part-01-validation-core/05-custom-constraint.md)
6. 学会调试：先能把“触发点/执行链/失败原因”看见
   - 阅读：[06. 调试](../part-01-validation-core/06-debugging.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
