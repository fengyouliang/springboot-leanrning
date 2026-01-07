# 03：请求绑定（Binding）与 Converter/Formatter

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**03：请求绑定（Binding）与 Converter/Formatter**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本章聚焦“请求如何变成 Java 入参”，以及当你希望引入自定义类型（例如 `UserId`）时应该怎么做。

## 你应该观察到什么

## 机制解释（Why）

你可以把请求绑定理解为两条路径：

1) **请求体（body）**：由 message converter 完成（JSON → Java）
2) **路径/查询参数（path/query）**：由 conversion service 完成（String → Java）

Converter/Formatter 属于第二条路径：它让 Spring MVC 知道怎么把字符串转换成你的领域类型。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebMvcLabTest`
- 建议命令：`mvn -pl springboot-web-mvc test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口

- 绑定基础（JSON → DTO）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java`
    - `createsUserWhenRequestIsValid`
    - `ignoresUnknownJsonFieldsByDefault`
- 练习：path variable + 自定义类型绑定：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`
    - `exercise_pathVariables`
    - `exercise_converterFormatter`

- 默认情况下，JSON 多余字段不会导致失败（本模块当前实验断言“unknown 字段被忽略”）
- 当 controller 的入参不是 String/Long 等简单类型时，需要通过 Converter/Formatter 扩展绑定能力

## Debug 建议

- 绑定失败时先确认“走的是哪条路径”（body 还是 path/query），不要在错误的地方加断点。

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcLabTest`
- Exercise：`BootWebMvcExerciseTest`
- Test file：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java` / `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`

上一章：[part-01-web-mvc/02-exception-handling.md](02-exception-handling.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-web-mvc/04-interceptor-and-filter-ordering.md](04-interceptor-and-filter-ordering.md)

<!-- BOOKIFY:END -->
