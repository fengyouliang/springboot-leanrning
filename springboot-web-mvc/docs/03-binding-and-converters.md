# 03：请求绑定（Binding）与 Converter/Formatter

本章聚焦“请求如何变成 Java 入参”，以及当你希望引入自定义类型（例如 `UserId`）时应该怎么做。

## 实验入口

- 绑定基础（JSON → DTO）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/BootWebMvcLabTest.java`
    - `createsUserWhenRequestIsValid`
    - `ignoresUnknownJsonFieldsByDefault`
- 练习：path variable + 自定义类型绑定：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/BootWebMvcExerciseTest.java`
    - `exercise_pathVariables`
    - `exercise_converterFormatter`

## 你应该观察到什么

- 默认情况下，JSON 多余字段不会导致失败（本模块当前实验断言“unknown 字段被忽略”）
- 当 controller 的入参不是 String/Long 等简单类型时，需要通过 Converter/Formatter 扩展绑定能力

## 机制解释（Why）

你可以把请求绑定理解为两条路径：

1) **请求体（body）**：由 message converter 完成（JSON → Java）
2) **路径/查询参数（path/query）**：由 conversion service 完成（String → Java）

Converter/Formatter 属于第二条路径：它让 Spring MVC 知道怎么把字符串转换成你的领域类型。

## Debug 建议

- 绑定失败时先确认“走的是哪条路径”（body 还是 path/query），不要在错误的地方加断点。

