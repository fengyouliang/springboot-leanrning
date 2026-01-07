# springboot-web-mvc 文档

本模块聚焦 Spring Web MVC 的“请求进入 → 绑定与校验 → 异常处理 → 响应塑形”的主线，并补齐过滤器/拦截器顺序与常见坑点。

## Start Here
- 导读：[part-00-guide/00-deep-dive-guide.md](part-00-guide/00-deep-dive-guide.md)

## Part 01 - Web MVC（主线机制）
- 01 校验与错误塑形：[part-01-web-mvc/01-validation-and-error-shaping.md](part-01-web-mvc/01-validation-and-error-shaping.md)
- 02 异常处理：[part-01-web-mvc/02-exception-handling.md](part-01-web-mvc/02-exception-handling.md)
- 03 绑定与 Converter：[part-01-web-mvc/03-binding-and-converters.md](part-01-web-mvc/03-binding-and-converters.md)
- 04 Filter/Interceptor 顺序：[part-01-web-mvc/04-interceptor-and-filter-ordering.md](part-01-web-mvc/04-interceptor-and-filter-ordering.md)

## Part 02 - View MVC（页面渲染主线）
- 01 传统 MVC 页面渲染入门：[part-02-view-mvc/01-thymeleaf-and-view-resolver.md](part-02-view-mvc/01-thymeleaf-and-view-resolver.md)
- 02 表单提交闭环：[part-02-view-mvc/02-form-binding-validation-prg.md](part-02-view-mvc/02-form-binding-validation-prg.md)
- 03 错误页与内容协商：[part-02-view-mvc/03-error-pages-and-content-negotiation.md](part-02-view-mvc/03-error-pages-and-content-negotiation.md)

## Appendix
- 常见坑：[appendix/90-common-pitfalls.md](appendix/90-common-pitfalls.md)
- 自测题：[appendix/99-self-check.md](appendix/99-self-check.md)

## Labs & Exercises（最小可复现入口）
- Labs（端到端主线）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java`
- Labs（更贴近真实 Boot 配置）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcSpringBootLabTest.java`
- Exercises：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`

## 核心源码入口（用于对照 docs）
- `@ControllerAdvice`：`springboot-web-mvc/src/main/java/com/learning/springboot/bootwebmvc/part01_web_mvc/GlobalExceptionHandler.java`
