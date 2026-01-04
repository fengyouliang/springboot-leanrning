# 02：`@ConfigurationProperties` 绑定与类型转换

本章聚焦 `@ConfigurationProperties`：它如何把 `application.properties` 的键值绑定到 Java 对象，以及常见失败模式。

## 实验入口

- 绑定与读取：
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDefaultLabTest.java`
- 测试级覆盖后仍能绑定：
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsOverrideLabTest.java`
- Exercises（建议做）：
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part00_guide/BootBasicsExerciseTest.java`
    - `exercise_addNewPropertyField`
    - `exercise_invalidPropertyType`

## 你应该观察到什么（What to observe）

- `AppProperties` 的字段值来自 `application.properties`（默认）或 `application-dev.properties`（profile）或测试覆盖（test properties）。
- `Environment#getProperty("app.feature-enabled")` 返回的是字符串 `"true"/"false"`，但 `AppProperties#isFeatureEnabled()` 是 boolean：**类型转换发生在绑定阶段**。

## 机制解释（Why）

- `@ConfigurationProperties(prefix = "app")` 负责声明绑定前缀。
- Spring Boot 在启动阶段会创建 binder，把配置键映射到对象字段：
  - `featureEnabled` ↔ `feature-enabled`（kebab-case 映射）
  - 字段类型转换（string → boolean / number / enum 等）

## Debug 建议

- 绑定没生效：
  - 先确认是否启用了扫描（本模块使用 `@ConfigurationPropertiesScan`）
  - 再检查 prefix、字段名、kebab-case 映射是否正确
- 类型错误：
  - 先写一个“必然失败”的实验，用测试断言固定错误信息关键片段（Exercise 引导你做）

## 常见坑

- 只改了 `application.properties` 但没生效：可能是 profile 覆盖/测试覆盖导致你看的不是那份配置。
- 断言依赖完整异常全文：不同版本异常文本可能略变，建议断言关键片段即可（比如“绑定失败/类型转换失败”）。

