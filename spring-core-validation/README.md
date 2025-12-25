# spring-core-validation

本模块用于学习 **Bean Validation**（Jakarta Validation），以及它在 Spring 应用中的常见用法。

包含内容：

- 在请求/命令对象上声明约束（`@NotBlank`、`@Email`、`@Min` 等）
- 使用 `jakarta.validation.Validator` 进行程序化校验
- 通过 `@Validated` 启用方法参数校验（Spring 集成）

## 学习目标

- 理解约束（constraint）的含义，以及 `ConstraintViolation` 里有什么信息
- 能进行程序化校验并查看 violation 列表
- 能触发 Spring Bean 的方法参数校验并观察异常类型

## 运行

```bash
mvn -pl spring-core-validation spring-boot:run
```

运行后观察控制台输出：

- 程序化校验得到的 violations
- 方法参数校验在输入非法时抛出的异常

## 测试

```bash
mvn -pl spring-core-validation test
```

## Deep Dive（Labs / Exercises）

- Labs（默认启用）：
  - `SpringCoreValidationLabTest`：程序化校验 + 方法参数校验（Spring 集成）
  - `SpringCoreValidationMechanicsLabTest`：无代理时不会触发 method validation、groups、自定义 constraint
- Exercises（默认禁用）：`SpringCoreValidationExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl spring-core-validation test`。

## 小练习

- 给 `CreateUserCommand` 新增一个约束（例如 `@Size`），并更新测试
- 给方法增加返回值校验，并用测试验证会触发
- （进阶）增加分组（`Default`、`Create`），并用指定分组进行校验

## 参考

- Jakarta Bean Validation（Jakarta Validation）规范
- Spring Framework Reference：Validation, Data Binding, and Type Conversion
