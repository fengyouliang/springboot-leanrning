# 02：统一异常处理（ControllerAdvice）与“坏输入”

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**02：统一异常处理（ControllerAdvice）与“坏输入”**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本章把“坏输入”分成两类，并解释它们为什么看起来都可能是 400，但根因不同：

1) JSON 解析/绑定失败（malformed JSON / 类型不匹配）
2) 校验失败（合法 JSON，但字段不满足约束）

## 你应该观察到什么

- malformed JSON 的失败发生在 **进入 controller 之前**（根本没有 DTO、也没有校验）
- 统一错误响应的关键在于：你是否在 `GlobalExceptionHandler` 中覆盖了对应异常

## 机制解释（Why）

Spring MVC 的异常可能来自不同阶段：

- **消息转换阶段**（HTTP message conversion）：例如 JSON 无法解析成对象，会抛出类似 `HttpMessageNotReadableException` 的异常
- **校验阶段**：`@Valid` 触发后，违反约束会抛出校验相关异常（最终被你映射成 `ApiError`）

所以“同样是 400”，你需要用异常处理把原因显式化，避免客户端只能靠猜。

- 先用测试把两类失败分开固化（状态码 + 错误形状/字段），避免把“绑定失败”误当成“校验失败”。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebMvcLabTest`
- 建议命令：`mvn -pl springboot-web-mvc test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口

- 观察现状（malformed JSON 只断言 400）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java`
    - `returnsBadRequestWhenJsonIsMalformed`
- 练习：为 malformed JSON 补齐统一错误响应：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`
    - `exercise_handleMalformedJson`

## Debug 建议

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

上一章：[part-01-web-mvc/01-validation-and-error-shaping.md](01-validation-and-error-shaping.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-web-mvc/03-binding-and-converters.md](03-binding-and-converters.md)

<!-- BOOKIFY:END -->
