# 03：Method Security 与代理：self-invocation 陷阱

本章解释：为什么你在方法上写了 `@PreAuthorize`，但某些调用路径却“没生效”。

## 实验入口

- `springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java`
  - `methodSecurityDeniesAdminOnlyMethodForNonAdmin`
  - `methodSecurityAllowsAdminOnlyMethodForAdmin`
  - `selfInvocationBypassesMethodSecurityAsAPitfall`

对应代码：

- `springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/AdminOnlyService.java`
- `springboot-security/src/main/java/com/learning/springboot/bootsecurity/part01_security/SelfInvocationPitfallService.java`

## 你应该观察到什么

- 非管理员调用 `AdminOnlyService#adminOnlyAction()` → 抛出 `AccessDeniedException`
- 但是非管理员调用 `SelfInvocationPitfallService#outerCallsAdminOnly()` 却可能成功：
  - 因为内部 `this.adminOnly()` 调用绕过了代理（这是经典坑）

## 机制解释（Why）

Method Security 的本质仍然是 **代理**：

- 只有当调用路径经过代理对象时，`@PreAuthorize` 才会触发安全拦截器。
- 类内部的 `this.xxx()` 属于 self-invocation，会直接调用目标对象方法，绕过代理。

这也是为什么：
- AOP
- `@Transactional`
- method validation
- method security

经常共享同一类“自调用不生效”的坑。

## 建议

- 尽量避免在同一类里用 `this.xxx()` 调用带安全注解的方法。
- 或者把需要安全保护的方法拆到另一个 bean（通过依赖注入调用），确保走代理。

