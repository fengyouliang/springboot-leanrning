# springboot-web-mvc 文档

本模块聚焦 Spring Web MVC 的“请求进入 → 绑定与校验 → 异常处理 → 响应塑形”的主线，并补齐过滤器/拦截器顺序与常见坑点。

## Start Here
- 导读：[part-00-guide/00-deep-dive-guide.md](part-00-guide/00-deep-dive-guide.md)
- 知识地图：[part-00-guide/01-knowledge-map.md](part-00-guide/01-knowledge-map.md)

## Part 01 - Web MVC（主线机制）
- 01 校验与错误塑形：[part-01-web-mvc/01-validation-and-error-shaping.md](part-01-web-mvc/01-validation-and-error-shaping.md)
- 02 异常处理：[part-01-web-mvc/02-exception-handling.md](part-01-web-mvc/02-exception-handling.md)
- 03 绑定与 Converter：[part-01-web-mvc/03-binding-and-converters.md](part-01-web-mvc/03-binding-and-converters.md)
- 04 Filter/Interceptor 顺序：[part-01-web-mvc/04-interceptor-and-filter-ordering.md](part-01-web-mvc/04-interceptor-and-filter-ordering.md)
- 05 Interceptor 生命周期（sync vs async）：[part-01-web-mvc/05-interceptor-async-lifecycle.md](part-01-web-mvc/05-interceptor-async-lifecycle.md)

## Part 02 - View MVC（页面渲染主线）
- 01 传统 MVC 页面渲染入门：[part-02-view-mvc/01-thymeleaf-and-view-resolver.md](part-02-view-mvc/01-thymeleaf-and-view-resolver.md)
- 02 表单提交闭环：[part-02-view-mvc/02-form-binding-validation-prg.md](part-02-view-mvc/02-form-binding-validation-prg.md)
- 03 错误页与内容协商：[part-02-view-mvc/03-error-pages-and-content-negotiation.md](part-02-view-mvc/03-error-pages-and-content-negotiation.md)

## Part 03 - Web MVC Internals（机制内核）
- 01 DispatcherServlet 主链路：[part-03-web-mvc-internals/01-dispatcherservlet-call-chain.md](part-03-web-mvc-internals/01-dispatcherservlet-call-chain.md)
- 02 ArgumentResolver/Binder：[part-03-web-mvc-internals/02-argument-resolver-and-binder.md](part-03-web-mvc-internals/02-argument-resolver-and-binder.md)
- 03 MessageConverter/ReturnValue：[part-03-web-mvc-internals/03-message-converters-and-return-values.md](part-03-web-mvc-internals/03-message-converters-and-return-values.md)
- 04 ExceptionResolvers（状态码从哪来）：[part-03-web-mvc-internals/04-exception-resolvers-and-error-flow.md](part-03-web-mvc-internals/04-exception-resolvers-and-error-flow.md)
- 05 ControllerAdvice 匹配与优先级：[part-03-web-mvc-internals/05-controlleradvice-matching-and-ordering.md](part-03-web-mvc-internals/05-controlleradvice-matching-and-ordering.md)

## Part 04 - REST Contract & Jackson（契约与序列化）
- 01 Content Negotiation（406/415）：[part-04-rest-contract/01-content-negotiation-406-415.md](part-04-rest-contract/01-content-negotiation-406-415.md)
- 02 Jackson 可控（ObjectMapper）：[part-04-rest-contract/02-jackson-objectmapper-controls.md](part-04-rest-contract/02-jackson-objectmapper-controls.md)
- 03 错误契约加固：[part-04-rest-contract/03-error-contract-hardening.md](part-04-rest-contract/03-error-contract-hardening.md)
- 04 ProblemDetail vs ApiError：[part-04-rest-contract/04-problemdetail-vs-custom-error.md](part-04-rest-contract/04-problemdetail-vs-custom-error.md)

## Part 05 - Real World HTTP（真实场景）
- 01 CORS 预检：[part-05-real-world-http/01-cors-preflight.md](part-05-real-world-http/01-cors-preflight.md)
- 02 Multipart 上传：[part-05-real-world-http/02-multipart-upload.md](part-05-real-world-http/02-multipart-upload.md)
- 03 下载与 Header：[part-05-real-world-http/03-download-and-streaming.md](part-05-real-world-http/03-download-and-streaming.md)
- 04 静态资源与缓存：[part-05-real-world-http/04-static-resources-and-cache.md](part-05-real-world-http/04-static-resources-and-cache.md)
- 05 条件请求（Last-Modified/ETag）：[part-05-real-world-http/05-conditional-requests-last-modified-etag-filter.md](part-05-real-world-http/05-conditional-requests-last-modified-etag-filter.md)

## Part 06 - Async & SSE（异步与长连接）
- 01 Servlet Async + 测试：[part-06-async-sse/01-servlet-async-and-testing.md](part-06-async-sse/01-servlet-async-and-testing.md)
- 02 SSE（SseEmitter）：[part-06-async-sse/02-sse-emitter.md](part-06-async-sse/02-sse-emitter.md)
- 03 DeferredResult 与 timeout：[part-06-async-sse/03-deferredresult-and-timeout.md](part-06-async-sse/03-deferredresult-and-timeout.md)

## Part 07 - Testing & Debugging（测试与排障）
- 01 排障工具箱：[part-07-testing-debugging/01-webmvc-testing-and-troubleshooting.md](part-07-testing-debugging/01-webmvc-testing-and-troubleshooting.md)

## Part 08 - Security & Observability（安全与观测）
- 01 Security FilterChain 与 MVC：[part-08-security-observability/01-security-filterchain-and-mvc.md](part-08-security-observability/01-security-filterchain-and-mvc.md)
- 02 Observability 与指标：[part-08-security-observability/02-observability-and-metrics.md](part-08-security-observability/02-observability-and-metrics.md)

## Appendix
- 常见坑：[appendix/90-common-pitfalls.md](appendix/90-common-pitfalls.md)
- 自测题：[appendix/99-self-check.md](appendix/99-self-check.md)

## Labs & Exercises（最小可复现入口）
- Labs（端到端主线）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java`
- Labs（更贴近真实 Boot 配置）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcSpringBootLabTest.java`
- Labs（绑定/校验深入）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcBindingDeepDiveLabTest.java`
- Labs（机制内核）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcInternalsLabTest.java`
- Labs（MessageConverter 选择可观测）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcMessageConverterTraceLabTest.java`
- Labs（Filter/Interceptor + async lifecycle）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcTraceLabTest.java`
- Labs（契约与 Jackson）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part04_contract/BootWebMvcContractJacksonLabTest.java`
- Labs（ProblemDetail 对照）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part04_contract/BootWebMvcProblemDetailLabTest.java`
- Labs（ControllerAdvice 优先级）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part09_advice_order/BootWebMvcAdviceOrderLabTest.java`
- Labs（ControllerAdvice 匹配规则）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part10_advice_matching/BootWebMvcAdviceMatchingLabTest.java`
- Labs（真实 HTTP）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part05_real_world/BootWebMvcRealWorldHttpLabTest.java`
- Labs（Async/SSE）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part06_async_sse/BootWebMvcAsyncSseLabTest.java`
- Labs（排障技巧）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part07_testing/BootWebMvcTestingDebuggingLabTest.java`
- Labs（Security）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part08_security_observability/BootWebMvcSecurityLabTest.java`
- Labs（Security vs MVC 边界证据链）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part08_security_observability/BootWebMvcSecurityVsMvcExceptionBoundaryLabTest.java`
- Labs（Observability）：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part08_security_observability/BootWebMvcObservabilityLabTest.java`
- Exercises：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`

## 核心源码入口（用于对照 docs）
- `@ControllerAdvice`：`springboot-web-mvc/src/main/java/com/learning/springboot/bootwebmvc/part01_web_mvc/GlobalExceptionHandler.java`
