# 01：校验（Validation）与错误响应形状（Error Shape）

本章聚焦 Web MVC 的“边界校验”：请求从 HTTP/JSON 进入 Controller 时，校验在哪里触发、失败后如何形成可控的错误响应。

## 实验入口（先跑再看）

- `@WebMvcTest` 切片（更快、更聚焦）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java`
    - `returnsValidationErrorWhenRequestIsInvalid`
    - `rejectsInvalidEmail`
    - `rejectsBlankName`
- 端到端（完整上下文）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcSpringBootLabTest.java`

## 你应该观察到什么（What to observe）

- 当请求体字段不满足约束（`@NotBlank`、`@Email` 等）时：
  - HTTP 状态码为 `400 Bad Request`
  - 响应体是统一形状（`ApiError`），包含：
    - `message = "validation_failed"`
    - `fieldErrors` 中包含对应字段（`name`、`email`）

## 机制解释（Why）

可以把 Web MVC 的请求处理分成三段：

1) **数据绑定（binding）**：JSON → DTO（例如 `CreateUserRequest`）
2) **边界校验（validation）**：`@Valid` 触发 Bean Validation，对 DTO 执行约束检查
3) **错误映射（error mapping）**：异常被 `@RestControllerAdvice` 捕获，转换成你的 `ApiError` 形状

在本模块里，错误形状由：
- `springboot-web-mvc/src/main/java/com/learning/springboot/bootwebmvc/part01_web_mvc/GlobalExceptionHandler.java`
控制。

## Debug 建议

- 看到 400：先看响应体的 `fieldErrors`，定位是哪一个字段失败，再回到 DTO 的注解。
- 校验没触发：确认 controller 入参是否带 `@Valid`；如果只写了约束注解但没写 `@Valid`，通常不会触发。

