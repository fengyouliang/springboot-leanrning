# 01：校验（Validation）与错误响应形状（Error Shape）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01：校验（Validation）与错误响应形状（Error Shape）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

## 你应该观察到什么（What to observe）

- 当请求体字段不满足约束（`@NotBlank`、`@Email` 等）时：
  - HTTP 状态码为 `400 Bad Request`
  - 响应体是统一形状（`ApiError`），包含：
    - `message = "validation_failed"`
    - `fieldErrors` 中包含对应字段（`name`、`email`）

## 机制解释（Why）

可以把 Web MVC 的请求处理分成三段：

在本模块里，错误形状由：
- `springboot-web-mvc/src/main/java/com/learning/springboot/bootwebmvc/part01_web_mvc/GlobalExceptionHandler.java`
控制。

- 看到 400：先看响应体的 `fieldErrors`，定位是哪一个字段失败，再回到 DTO 的注解。
- 校验没触发：确认 controller 入参是否带 `@Valid`；如果只写了约束注解但没写 `@Valid`，通常不会触发。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebMvcLabTest` / `BootWebMvcSpringBootLabTest`
- 建议命令：`mvn -pl springboot-web-mvc test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口（先跑再看）

- `@WebMvcTest` 切片（更快、更聚焦）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java`
    - `returnsValidationErrorWhenRequestIsInvalid`
    - `rejectsInvalidEmail`
    - `rejectsBlankName`
- 端到端（完整上下文）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcSpringBootLabTest.java`

## Debug 建议

## F. 常见坑与边界

本章聚焦 Web MVC 的“边界校验”：请求从 HTTP/JSON 进入 Controller 时，校验在哪里触发、失败后如何形成可控的错误响应。

1) **数据绑定（binding）**：JSON → DTO（例如 `CreateUserRequest`）
2) **边界校验（validation）**：`@Valid` 触发 Bean Validation，对 DTO 执行约束检查
3) **错误映射（error mapping）**：异常被 `@RestControllerAdvice` 捕获，转换成你的 `ApiError` 形状

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcLabTest` / `BootWebMvcSpringBootLabTest`
- Test file：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java` / `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcSpringBootLabTest.java`

上一章：[part-00-guide/00-deep-dive-guide.md](../part-00-guide/00-deep-dive-guide.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-web-mvc/02-exception-handling.md](02-exception-handling.md)

<!-- BOOKIFY:END -->
