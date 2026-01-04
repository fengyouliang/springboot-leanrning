# 06. Debug / 观察：如何排查“校验为什么没生效？”

校验没生效，常见原因通常不在约束本身，而在“校验入口”。

## 1) 程序化校验不生效？

先问自己：

- 我是不是调用了 `validator.validate(...)`？
- 我是不是在校验同一个对象实例？

本模块的 `ProgrammaticValidationService` 是最透明、最好排查的入口。

## 2) 方法参数校验不生效？

排查顺序建议是：

1. 这个对象是不是 Spring 管理的 bean？
2. 它是不是代理？（`AopUtils.isAopProxy(bean)`）
3. 我是不是“走代理调用”？（有没有自调用绕过代理）
4. 类上是否有 `@Validated`（触发 method validation 的关键标记）

对照测试：

- `SpringCoreValidationLabTest#methodValidatedServiceIsAnAopProxy`
- `SpringCoreValidationMechanicsLabTest#methodValidationDoesNotRunWhenCallingAServiceDirectly_withoutSpringProxy`

## 3) 如何把 violations 看清楚？

学习阶段建议你在断言里至少检查两项：

- `propertyPath`（定位字段）
- `message`（理解默认错误提示）

验证入口：`SpringCoreValidationMechanicsLabTest#constraintViolationIncludesMessageAndPropertyPath`

