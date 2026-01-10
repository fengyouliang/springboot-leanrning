# 深挖指南（Spring Core Validation）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**深挖指南（Spring Core Validation）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

Validation 的“深挖主线”不是记注解，而是把三件事分清：

1. **Constraint 是什么**：声明式约束如何变成 `ConstraintViolation`
2. **谁来触发校验**：programmatic（你主动调用 Validator） vs method validation（代理触发）
3. **校验结果怎么被消费**：exception（`ConstraintViolationException`）或 violations 集合（可用于自定义错误结构）

### 1) 时间线：一次校验从输入到 violations

1. 你拥有一个“待校验对象”（字段/入参）
2. Validator 扫描约束（如 `@NotBlank`/`@Email`/自定义 constraint）
3. 逐条执行 `ConstraintValidator#isValid`
4. 收集 violations（propertyPath/message 等是排障的第一现场）

### 2) 时间线：method validation 为什么需要代理

1. 你在 service 方法上声明“需要校验”（通常是 `@Validated` + 约束注解）
2. Spring 创建代理并在方法调用前触发校验
3. 校验失败：抛 `ConstraintViolationException`（调用方可统一处理）

如果你绕开 Spring 直接 new 一个 service 并调用方法：**没有代理就不会触发 method validation**（这是最常见的误解点）。

### 3) 关键参与者

- `jakarta.validation.Validator`：校验入口（programmatic validation）
- `ConstraintViolation`：失败证据（propertyPath/message/rootBeanClass）
- `ConstraintViolationException`：method validation 常见失败载体
- groups：决定“哪些约束参与本次校验”（避免把所有约束都绑死在 Default）
- 自定义 constraint：`@Constraint(validatedBy = ...)` + `ConstraintValidator`

### 4) 本模块的关键分支（2–5 条，默认可回归）

1. **programmatic 校验：返回 violations（可用于自定义错误结构）**
   - 验证：`SpringCoreValidationLabTest#programmaticValidationFindsViolations`
2. **method validation：无效入参会抛 ConstraintViolationException（代理触发）**
   - 验证：`SpringCoreValidationLabTest#methodValidationThrowsForInvalidInput`
3. **代理边界：不经 Spring 代理调用时，method validation 不会触发（坑点）**
   - 验证：`SpringCoreValidationMechanicsLabTest#methodValidationDoesNotRunWhenCallingAServiceDirectly_withoutSpringProxy`
4. **groups 控制生效范围：同一个对象在不同 group 下 violations 不同**
   - 验证：`SpringCoreValidationMechanicsLabTest#groupsControlWhichConstraintsApply`
5. **自定义 constraint：你可以定义并验证自己的约束语义**
   - 验证：`SpringCoreValidationMechanicsLabTest#customConstraintsCanBeDefinedWithConstraintValidator`

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。
  
建议断点（把“为什么没校验”快速分流）：

- method validation 是否真的走代理：
  - 先在 `SpringCoreValidationLabTest#methodValidatedServiceIsAnAopProxy` 的断言处确认代理存在性
- violations 的“证据字段”用于排障：
  - 对照 `SpringCoreValidationMechanicsLabTest#constraintViolationIncludesMessageAndPropertyPath`，优先看 propertyPath/message

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-validation test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

> 验证入口（可跑）：
> - `SpringCoreValidationLabTest`
> - `SpringCoreValidationMechanicsLabTest`

配套验证入口：
- Labs/Exercises：见 `src/test/java/com/learning/springboot/springcorevalidation/**`

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`

上一章：[Docs TOC](../README.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[01-constraint-mental-model](../part-01-validation-core/01-constraint-mental-model.md)

<!-- BOOKIFY:END -->
