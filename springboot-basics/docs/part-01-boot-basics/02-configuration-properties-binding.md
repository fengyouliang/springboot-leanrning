# 02：`@ConfigurationProperties` 绑定与类型转换

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**02：`@ConfigurationProperties` 绑定与类型转换**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本章聚焦 `@ConfigurationProperties`：它如何把 `application.properties` 的键值绑定到 Java 对象，以及常见失败模式。

## 你应该观察到什么（What to observe）

## 机制解释（Why）

- `@ConfigurationProperties(prefix = "app")` 负责声明绑定前缀。
- Spring Boot 在启动阶段会创建 binder，把配置键映射到对象字段：
  - `featureEnabled` ↔ `feature-enabled`（kebab-case 映射）
  - 字段类型转换（string → boolean / number / enum 等）

- 只改了 `application.properties` 但没生效：可能是 profile 覆盖/测试覆盖导致你看的不是那份配置。
- 断言依赖完整异常全文：不同版本异常文本可能略变，建议断言关键片段即可（比如“绑定失败/类型转换失败”）。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootBasicsDefaultLabTest` / `BootBasicsOverrideLabTest`
- 建议命令：`mvn -pl springboot-basics test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口

- 绑定与读取：
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDefaultLabTest.java`
- 测试级覆盖后仍能绑定：
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsOverrideLabTest.java`
- Exercises（建议做）：
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part00_guide/BootBasicsExerciseTest.java`
    - `exercise_addNewPropertyField`
    - `exercise_invalidPropertyType`

- `AppProperties` 的字段值来自 `application.properties`（默认）或 `application-dev.properties`（profile）或测试覆盖（test properties）。
- `Environment#getProperty("app.feature-enabled")` 返回的是字符串 `"true"/"false"`，但 `AppProperties#isFeatureEnabled()` 是 boolean：**类型转换发生在绑定阶段**。

## Debug 建议

- 绑定没生效：
  - 先确认是否启用了扫描（本模块使用 `@ConfigurationPropertiesScan`）
  - 再检查 prefix、字段名、kebab-case 映射是否正确
- 类型错误：
  - 先写一个“必然失败”的实验，用测试断言固定错误信息关键片段（Exercise 引导你做）

## F. 常见坑与边界

## 常见坑

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootBasicsDefaultLabTest` / `BootBasicsOverrideLabTest`
- Exercise：`BootBasicsExerciseTest`
- Test file：`springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDefaultLabTest.java` / `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsOverrideLabTest.java` / `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part00_guide/BootBasicsExerciseTest.java`

上一章：[part-01-boot-basics/01-property-sources-and-profiles.md](01-property-sources-and-profiles.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/90-common-pitfalls.md](../appendix/90-common-pitfalls.md)

<!-- BOOKIFY:END -->
