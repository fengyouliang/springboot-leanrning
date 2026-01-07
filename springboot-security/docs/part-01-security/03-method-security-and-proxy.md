# 03：Method Security 与代理：self-invocation 陷阱

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**03：Method Security 与代理：self-invocation 陷阱**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本章解释：为什么你在方法上写了 `@PreAuthorize`，但某些调用路径却“没生效”。

对应代码：

## 你应该观察到什么

## 机制解释（Why）

Method Security 的本质仍然是 **代理**：

- 只有当调用路径经过代理对象时，`@PreAuthorize` 才会触发安全拦截器。
- 类内部的 `this.xxx()` 属于 self-invocation，会直接调用目标对象方法，绕过代理。

这也是为什么：
- AOP
- `@Transactional`
- method validation
- method security

## 建议

- 尽量避免在同一类里用 `this.xxx()` 调用带安全注解的方法。
- 或者把需要安全保护的方法拆到另一个 bean（通过依赖注入调用），确保走代理。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootSecurityLabTest`
- 建议命令：`mvn -pl springboot-security test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口

- `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
  - `methodSecurityDeniesAdminOnlyMethodForNonAdmin`
  - `methodSecurityAllowsAdminOnlyMethodForAdmin`
  - `selfInvocationBypassesMethodSecurityAsAPitfall`

## F. 常见坑与边界

- `springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/AdminOnlyService.java`
- `springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/SelfInvocationPitfallService.java`

- 非管理员调用 `AdminOnlyService#adminOnlyAction()` → 抛出 `AccessDeniedException`
- 但是非管理员调用 `SelfInvocationPitfallService#outerCallsAdminOnly()` 却可能成功：
  - 因为内部 `this.adminOnly()` 调用绕过了代理（这是经典坑）

经常共享同一类“自调用不生效”的坑。

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootSecurityLabTest`
- Test file：`springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`

上一章：[part-01-security/02-csrf.md](02-csrf.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-security/04-filter-chain-and-order.md](04-filter-chain-and-order.md)

<!-- BOOKIFY:END -->
