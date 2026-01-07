# 90. 常见坑清单（建议反复对照）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**90. 常见坑清单（建议反复对照）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-validation test`（或在 IDE 直接运行上面的测试类）

## F. 常见坑与边界

> 验证入口（可跑）：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`

## 坑 1：以为 `@Valid` 自动让 service 方法校验

- 事实：方法参数校验需要 Spring 代理拦截（见 [03. method-validation-proxy](../part-01-validation-core/03-method-validation-proxy.md)）

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

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreValidationLabTest` / `SpringCoreValidationMechanicsLabTest`

上一章：[06-debugging](../part-01-validation-core/06-debugging.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[99-self-check](99-self-check.md)

<!-- BOOKIFY:END -->
