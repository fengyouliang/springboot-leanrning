# 03. 方法参数校验：为什么它必须依赖 Spring 代理？

很多人第一次接触方法参数校验时会困惑：

> “我只是给方法参数加了 `@Valid`，为什么还要代理？”

原因是：方法校验不是编译器能力，它需要在运行时拦截方法调用。

## 本模块的最小闭环

`MethodValidatedUserService`：

- 类上有 `@Validated`
- 方法参数是 `@Valid CreateUserCommand`

对应测试：

- `SpringCoreValidationLabTest#methodValidationThrowsForInvalidInput`
- `SpringCoreValidationLabTest#methodValidatedServiceIsAnAopProxy`

## 关键结论：没有 Spring 代理，就没有 method validation 拦截器

看 `SpringCoreValidationMechanicsLabTest#methodValidationDoesNotRunWhenCallingAServiceDirectly_withoutSpringProxy`：

- 直接 `new MethodValidatedUserService()`
- 调用 `register(invalid)`
- 不会抛异常（因为没有代理，没有拦截器）

## 你应该得到的结论

方法校验（以及 AOP/Tx）都共享同一个底层规律：

> 只有“走代理的调用”才会被拦截增强。

因此它也会受到同类自调用等问题影响（见 AOP 模块的自调用章节）。

