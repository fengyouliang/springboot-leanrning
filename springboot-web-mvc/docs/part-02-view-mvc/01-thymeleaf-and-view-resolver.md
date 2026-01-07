# 01：传统 MVC 页面渲染入门（@Controller / ViewName / Thymeleaf）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01：传统 MVC 页面渲染入门（@Controller / ViewName / Thymeleaf）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本章从“返回 HTML 页面”开始，补齐 Spring MVC 的传统用法：`@Controller` 返回视图名（view name），由 ViewResolver 解析到 Thymeleaf 模板并渲染成 HTML。

## 你应该观察到什么（What to observe）

- 访问 `/pages/ping`：
  - 返回 `Content-Type: text/html`
  - **不是** JSON（对比 `/api/ping`）
  - 响应体来自 Thymeleaf 模板渲染，而不是 Jackson 序列化

## 机制解释（Why）

把两类 Controller 的“返回值语义”分清楚：

- `@RestController`：返回值默认是 **response body**（JSON/字符串等），由 HttpMessageConverter 写入响应体。
- `@Controller`：返回值（String）默认是 **view name**，由 ViewResolver 解析到模板，再渲染为 HTML。

在本模块里可以直接对照：

- 页面 Controller：`springboot-web-mvc/src/main/java/com/learning/springboot/bootwebmvc/part02_view_mvc/MvcPingController.java`
- 页面模板：`springboot-web-mvc/src/main/resources/templates/pages/ping.html`
- 静态资源（CSS）：`springboot-web-mvc/src/main/resources/static/css/app.css`

`MvcPingController` 里同时提供两种写法：
- 返回 view name：`GET /pages/ping`
- 返回 `ModelAndView`：`GET /pages/ping-mav`

- 只写了 `@Controller`，但方法上又加了 `@ResponseBody`：会把 view name 当作字符串写回去（看起来像“模板不生效”）。
- 模板放错目录：Thymeleaf 默认从 `classpath:/templates/` 下找模板。
- 静态资源放错目录：默认从 `classpath:/static/`（以及其它约定目录）下提供静态资源。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebMvcViewLabTest` / `BootWebMvcViewSpringBootLabTest`
- 建议命令：`mvn -pl springboot-web-mvc test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口（先跑再看）

- MockMvc（切片，快速验证 view/model/HTML）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewLabTest.java`
    - `rendersPingPage`
- 端到端（真实端口拿到 HTML）：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewSpringBootLabTest.java`

## F. 常见坑与边界

## 常见坑

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcViewLabTest` / `BootWebMvcViewSpringBootLabTest`
- Test file：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewLabTest.java` / `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewSpringBootLabTest.java`

上一章：[part-01-web-mvc/04-interceptor-and-filter-ordering.md](../part-01-web-mvc/04-interceptor-and-filter-ordering.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-02-view-mvc/02-form-binding-validation-prg.md](02-form-binding-validation-prg.md)

<!-- BOOKIFY:END -->
