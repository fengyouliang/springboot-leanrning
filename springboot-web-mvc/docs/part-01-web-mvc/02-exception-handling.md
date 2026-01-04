# 02：统一异常处理（ControllerAdvice）与“坏输入”

本章把“坏输入”分成两类，并解释它们为什么看起来都可能是 400，但根因不同：

1) JSON 解析/绑定失败（malformed JSON / 类型不匹配）
2) 校验失败（合法 JSON，但字段不满足约束）

## 实验入口

- 观察现状（malformed JSON 只断言 400）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java`
    - `returnsBadRequestWhenJsonIsMalformed`
- 练习：为 malformed JSON 补齐统一错误响应：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`
    - `exercise_handleMalformedJson`

## 你应该观察到什么

- malformed JSON 的失败发生在 **进入 controller 之前**（根本没有 DTO、也没有校验）
- 统一错误响应的关键在于：你是否在 `GlobalExceptionHandler` 中覆盖了对应异常

## 机制解释（Why）

Spring MVC 的异常可能来自不同阶段：

- **消息转换阶段**（HTTP message conversion）：例如 JSON 无法解析成对象，会抛出类似 `HttpMessageNotReadableException` 的异常
- **校验阶段**：`@Valid` 触发后，违反约束会抛出校验相关异常（最终被你映射成 `ApiError`）

所以“同样是 400”，你需要用异常处理把原因显式化，避免客户端只能靠猜。

## Debug 建议

- 先用测试把两类失败分开固化（状态码 + 错误形状/字段），避免把“绑定失败”误当成“校验失败”。

