# 03. 方法参数校验：为什么它必须依赖 Spring 代理？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**03. 方法参数校验：为什么它必须依赖 Spring 代理？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

很多人第一次接触方法参数校验时会困惑：

> “我只是给方法参数加了 `@Valid`，为什么还要代理？”

## 本模块的最小闭环

`MethodValidatedUserService`：

- 类上有 `@Validated`
- 方法参数是 `@Valid CreateUserCommand`

对应测试：

## 关键结论：没有 Spring 代理，就没有 method validation 拦截器

- 直接 `new MethodValidatedUserService()`
- 调用 `register(invalid)`
- 不会抛异常（因为没有代理，没有拦截器）

## 你应该得到的结论

方法校验（以及 AOP/Tx）都共享同一个底层规律：

> 只有“走代理的调用”才会被拦截增强。

因此它也会受到同类自调用等问题影响（见 AOP 模块的自调用章节）。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-validation test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

原因是：方法校验不是编译器能力，它需要在运行时拦截方法调用。

- `SpringCoreValidationLabTest#methodValidationThrowsForInvalidInput`
- `SpringCoreValidationLabTest#methodValidatedServiceIsAnAopProxy`

看 `SpringCoreValidationMechanicsLabTest#methodValidationDoesNotRunWhenCallingAServiceDirectly_withoutSpringProxy`：

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`

上一章：[02-programmatic-validator](02-programmatic-validator.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[04-groups](04-groups.md)

<!-- BOOKIFY:END -->
