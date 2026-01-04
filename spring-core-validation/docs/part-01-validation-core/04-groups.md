# 04. Groups：同一个对象，为什么“创建”和“更新”要用不同规则？

Validation Groups 用来解决一个常见问题：

> 同一个数据结构在不同场景下，约束规则不同。

典型场景：

- Create：字段必须填写
- Update：字段可以为空（只更新部分字段）

## 在本模块如何验证（不依赖 Spring）

看 `SpringCoreValidationMechanicsLabTest#groupsControlWhichConstraintsApply`

它演示了：

- 默认组（`Default`）校验不触发
- `Create` 组校验会触发 `@NotBlank(groups = Create.class)`

## 学习建议

- Groups 是很“工程化”的能力，但机制很清晰
- 学习阶段只需要掌握：不同 group 会选择不同的约束集合

