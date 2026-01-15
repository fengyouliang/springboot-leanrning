# 主线时间线：Spring Boot Web MVC

!!! summary
    - 这一模块关注：一次 HTTP 请求如何在 Spring MVC 中被“选路、绑定、执行、返回、异常处理”，以及你如何在关键分支上定位问题。
    - 读完你应该能复述：**DispatcherServlet → HandlerMapping → HandlerAdapter → 参数解析/消息转换 → 返回/异常** 这一条主线。
    - 推荐顺序：先读《知识地图/断点图》→ 本章 → 先把 Web MVC Internals 的主线跑通 → 再按场景扩展（REST、文件、异步、测试、安全）。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`BootWebMvcInternalsLabTest`

## 在 Spring 主线中的位置

- Web MVC 处在“应用对外入口”：它把 Servlet 容器的请求事件，翻译成 Controller 方法调用与响应输出。
- 你调试 404/400/415/500、参数绑定失败、返回值序列化异常时，本质都在主线的某个分支上。

## 主线时间线（推荐顺读：先把请求跑通）

1. 先拿到全图：知道“问题可能出现在主线的哪一段”
   - 知识地图：[01-knowledge-map.md](01-knowledge-map.md)
   - 断点图：[02-breakpoint-map.md](02-breakpoint-map.md)
2. 把“入口调用链”跑通：DispatcherServlet#doDispatch 到底做了什么
   - 阅读：[01. DispatcherServlet 主链路](../part-03-web-mvc-internals/01-dispatcherservlet-call-chain.md)
3. 把“返回值如何出方法”跑通：MessageConverter / ReturnValueHandler
   - 阅读：[03. MessageConverter 与返回值](../part-03-web-mvc-internals/03-message-converters-and-return-values.md)
4. 把“异常如何被收敛”跑通：ExceptionResolver / Error Flow / @ControllerAdvice
   - 阅读：[04. ExceptionResolver 与错误流](../part-03-web-mvc-internals/04-exception-resolvers-and-error-flow.md)
   - 阅读：[05. @ControllerAdvice 顺序](../part-03-web-mvc-internals/05-controlleradvice-matching-and-ordering.md)
5. 再回到应用层：把验证、异常、绑定、拦截器这些最常见需求接回主线
   - 阅读：[校验与错误塑形](../part-01-web-mvc/01-validation-and-error-shaping.md)
   - 阅读：[异常处理](../part-01-web-mvc/02-exception-handling.md)
   - 阅读：[绑定与 Converter](../part-01-web-mvc/03-binding-and-converters.md)
   - 阅读：[拦截器与过滤器顺序](../part-01-web-mvc/04-interceptor-and-filter-ordering.md)
6. 进入真实世界场景：REST 合同、CORS、文件上传下载、异步与测试
   - REST 合同：从 [01](../part-04-rest-contract/01-content-negotiation-406-415.md) 开始按目录推进
   - HTTP 场景：从 [01](../part-05-real-world-http/01-cors-preflight.md) 开始按目录推进
   - 异步/SSE：从 [01](../part-06-async-sse/01-servlet-async-and-testing.md) 开始按目录推进
   - 测试排障：[01](../part-07-testing-debugging/01-webmvc-testing-and-troubleshooting.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
