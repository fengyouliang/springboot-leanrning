# 01：WebMvc 测试与排障（resolvedException / handler / 断点清单）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01：WebMvc 测试与排障（resolvedException / handler / 断点清单）**
- 目标：把“怎么调 Web MVC”写成可执行套路：先靠测试拿到现象，再用 `resolvedException`/`handler` 定位分支，最后用断点看调用链。

## B. 核心结论

- 看到 406/415，不要盯 controller：先看 `Accept`/`Content-Type`/`produces`/`consumes`，再看 converter 选择。
- 用 MockMvc 的 `MvcResult#getResolvedException()` 能快速把“猜”变成“证据”：异常类型就是分支位置。
- 看到 401/403，优先怀疑 Filter/Security，而不是 MVC handler：**很多安全分支发生在 DispatcherServlet 之前**。
- 当你需要“确认到底选了哪个 HttpMessageConverter”：可以用 `ResponseBodyAdvice#beforeBodyWrite` 把 `selectedConverterType/selectedContentType` 写进响应头，再用测试固化它（证据链优先）。

## C. 机制主线

- 本章用 `BootWebMvcTestingDebuggingLabTest` 固定两条排障证据链：
  - 415 → `HttpMediaTypeNotSupportedException`
  - 406 → `HttpMediaTypeNotAcceptableException`

## D. 源码与断点

常用断点清单（按场景）：
- 400（解析失败/校验失败）：`RequestResponseBodyMethodProcessor#resolveArgument`、`DataBinder#validate`、`ExceptionHandlerExceptionResolver`
- 406/415：`AbstractMessageConverterMethodProcessor#writeWithMessageConverters`、`AbstractMessageConverterMethodArgumentResolver#readWithMessageConverters`
- 404/选路问题：`RequestMappingHandlerMapping#getHandlerInternal`
- 401/403（Security/CSRF）：`DelegatingFilterProxy#doFilter`、`FilterChainProxy#doFilterInternal`、`CsrfFilter#doFilterInternal`、`ExceptionTranslationFilter`

## E. 最小可运行实验（Lab）

- Lab：`BootWebMvcTestingDebuggingLabTest`
- Lab：`BootWebMvcMessageConverterTraceLabTest`（converter 选择证据：响应头）

## F. 常见坑与边界

- `@WebMvcTest` 不会加载完整上下文：当问题涉及 filter chain、真实端口、静态资源链路差异时，需要用 `@SpringBootTest(webEnvironment=RANDOM_PORT)` 再补一条端到端断言。
- 引入 `spring-boot-starter-security` 后，POST 变 403：常见原因是 CSRF。教学场景可以保留一个端点演示分支；真实 API 通常会对无状态接口关闭 CSRF。
- 当你需要“确认到底是 401 还是 403”：用 `status()` 固化现象后，再看响应头/异常入口（filter 链断点），避免盲改 controller。

## G. 小结与下一章

- 本章完成后建议回看 Part 03/04：用断点验证你对 resolver/converter 的理解是否正确。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcTestingDebuggingLabTest`
- Lab：`BootWebMvcMessageConverterTraceLabTest`

上一章：[part-06-async-sse/03-deferredresult-and-timeout.md](../part-06-async-sse/03-deferredresult-and-timeout.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-08-security-observability/01-security-filterchain-and-mvc.md](../part-08-security-observability/01-security-filterchain-and-mvc.md)

<!-- BOOKIFY:END -->
