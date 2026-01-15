# 第 14 章：Validation 主线

这一章解决的问题是：**校验错误从哪里来、为什么同样是“参数不合法”会走不同分支、为什么方法级校验常常“看起来没生效”**。

---

## 主线（按时间线顺读）

1. 约束声明：`@NotNull/@Size/...`（Bean Validation）
2. 校验执行：
   - Web 场景：参数绑定后校验（BindingResult/异常分支）
   - 方法级：`@Validated` 触发代理，在方法调用边界做校验
3. 产出结果：ConstraintViolation / FieldError / ProblemDetail 等
4. 常见坑：忘了 `@Validated`、代理类型导致不生效、自调用绕过、groups 与默认组误解

---

## 深挖入口（模块 docs）

- 模块目录页：[`spring-core-validation/docs/README.md`](../spring-core-validation/docs/README.md)
- 模块主线时间线（含可跑入口）：[`spring-core-validation/docs/part-00-guide/03-mainline-timeline.md`](../spring-core-validation/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

当你把“功能正确”跑通后，下一层是“能被观察与运维”：Actuator/metrics/health 让你把系统变成可观测系统。

- 下一章：[第 15 章：Actuator/Observability 主线](15-actuator-observability-mainline.md)

