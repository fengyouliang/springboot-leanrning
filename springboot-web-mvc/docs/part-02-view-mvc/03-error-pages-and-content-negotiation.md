# 03：错误页（error/*.html）与内容协商（Accept：HTML vs JSON）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**03：错误页（error/*.html）与内容协商（Accept：HTML vs JSON）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本章把“错误响应”的学习从 JSON API 扩展到页面场景：同一类错误，在浏览器访问与 API 调用时，往往需要不同的呈现方式。

## 你应该观察到什么（What to observe）

1) 当 Accept 偏向 `text/html`（浏览器）
- 404/4xx/5xx 会返回 HTML 错误页（可读、可导航）

2) 当 Accept 偏向 `application/json`（接口调用/脚本）
- 错误会返回 JSON（便于程序处理与断言）

## 机制解释（Why）

### 1) Spring Boot 的错误页约定

当进入错误处理链路时，Boot 会尝试渲染错误页模板：

- `templates/error/404.html`（最具体）
- `templates/error/4xx.html`（兜底 4xx）
- `templates/error/5xx.html`（兜底 5xx）

因此你只要提供这些模板，就能在“无 handler 的 404”等场景看到自定义页面。

### 2) 内容协商：Accept 决定“渲染 HTML 还是返回 JSON”

同一条错误链路，通常会根据请求的 Accept 选择：
- 返回视图（HTML）
- 或返回 JSON（错误体/ProblemDetail/自定义结构）

在本模块里，我们用一个最小示例演示这种差异：

- `/pages/error-demo` 主动抛出异常
- `MvcExceptionHandler` 基于 Accept 做兜底：HTML → 错误页，JSON → ApiError

## 在本模块里去哪里看

- 错误页模板：
  - `springboot-web-mvc/src/main/resources/templates/error/404.html`
  - `springboot-web-mvc/src/main/resources/templates/error/4xx.html`
  - `springboot-web-mvc/src/main/resources/templates/error/5xx.html`
- 示例 Controller / 异常处理：
  - `springboot-web-mvc/src/main/java/com/learning/springboot/bootwebmvc/part02_view_mvc/MvcErrorDemoController.java`
  - `springboot-web-mvc/src/main/java/com/learning/springboot/bootwebmvc/part02_view_mvc/MvcExceptionHandler.java`

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebMvcErrorViewLabTest` / `BootWebMvcViewSpringBootLabTest`
- 建议命令：`mvn -pl springboot-web-mvc test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口（先跑再看）

- MockMvc（固定行为，最直观）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcErrorViewLabTest.java`
    - `returnsCustom404HtmlPageForUnknownRoute`
    - `renders5xxHtmlPageWhenControllerThrows`
    - `returnsJsonWhenAcceptIsJson`
- 端到端（真实端口验证错误页模板生效）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewSpringBootLabTest.java`

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcErrorViewLabTest` / `BootWebMvcViewSpringBootLabTest`
- Test file：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcErrorViewLabTest.java` / `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewSpringBootLabTest.java`

上一章：[part-02-view-mvc/02-form-binding-validation-prg.md](02-form-binding-validation-prg.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/90-common-pitfalls.md](../appendix/90-common-pitfalls.md)

<!-- BOOKIFY:END -->
