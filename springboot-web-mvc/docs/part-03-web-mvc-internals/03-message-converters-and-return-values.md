# 03：HttpMessageConverter 与返回值处理（序列化发生在哪里）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**03：HttpMessageConverter 与返回值处理（序列化发生在哪里）**
- 目标：讲清 `@ResponseBody`/`@RequestBody` 与 `HttpMessageConverter` 的关系，以及 406/415 属于链路的哪一段失败。

## B. 核心结论

- `HttpMessageConverter` 是“HTTP body ↔ Java 对象”的关键桥梁；它同时影响入站（read）与出站（write）。
- 406/415 通常不是你的业务逻辑问题，而是 **媒体类型与 converter 匹配失败**：`Accept`/`Content-Type`/`produces`/`consumes` 不一致。

## C. 机制主线

- 把证据链连接到 Part 04：用 `BootWebMvcContractJacksonLabTest` 固定 406/415 的可复现用例，再回到断点看 converter 选择分支。
- 本模块还提供了一个“排障视角”的 Lab：`BootWebMvcTestingDebuggingLabTest`（用 `resolvedException` 固定分支入口）。
- 本章新增一条“可观测证据链”：用 `ResponseBodyAdvice` 把 `selectedConverterType/selectedContentType` 写入响应头，直接回答“到底选了哪个 converter”。

## D. 源码与断点

建议断点：
- `AbstractMessageConverterMethodProcessor#writeWithMessageConverters`
- `RequestResponseBodyMethodProcessor#resolveArgument`
- `org.springframework.web.accept.ContentNegotiationManager#resolveMediaTypes`
- `org.springframework.web.method.support.HandlerMethodReturnValueHandlerComposite#handleReturnValue`（返回值处理链入口）
- `org.springframework.web.servlet.mvc.method.annotation.AbstractMessageConverterMethodProcessor#beforeBodyWrite`（ResponseBodyAdvice 链入口）

## 关键分支：read 与 write 的差异

当你看到“406/415”，先判断它属于 read 还是 write：

- **read（入站）**：`@RequestBody` 读取请求体 → 依赖 `AbstractMessageConverterMethodArgumentResolver#readWithMessageConverters`
  - 典型失败：415（找不到能读该 `Content-Type` 的 converter）
- **write（出站）**：`@ResponseBody` 写回响应体 → 依赖 `AbstractMessageConverterMethodProcessor#writeWithMessageConverters`
  - 典型失败：406（找不到能写出 `Accept` 的 converter）

这也是为什么你排障时应该优先检查 header 与 method mapping 约束，而不是先改业务逻辑。

## 你真正要理解的“两个链”

### 1) ReturnValueHandlers（返回值处理链）

在 `@ResponseBody` 场景下，最常见的 handler 是：
- `RequestResponseBodyMethodProcessor`：负责把返回值交给 HttpMessageConverter 写回 body

它通常发生在：
- `HandlerMethodReturnValueHandlerComposite#handleReturnValue`（链入口）
- `AbstractMessageConverterMethodProcessor#writeWithMessageConverters`（真正写回）

### 2) ContentNegotiation（内容协商）

内容协商不是“只看 Accept”：
- `Accept`：客户端希望的响应格式（write）
- `Content-Type`：请求体实际格式（read）
- `produces/consumes`：你在 mapping 上写的约束（会直接影响匹配与异常类型）

排障建议：当 406/415 出现时，优先把下面三件事写进证据链：
1. 请求头（Accept/Content-Type）
2. handler mapping 约束（produces/consumes）
3. resolvedException（异常类型就是分支位置）

## E. 最小可运行实验（Lab）

- Lab：`BootWebMvcContractJacksonLabTest`
- Lab：`BootWebMvcTestingDebuggingLabTest`
- Lab：`BootWebMvcMessageConverterTraceLabTest`（converter 选择可观测：响应头证据链）

## 补充：如何把 “selectedConverterType/selectedContentType” 变成证据

断点能解释“为什么”，但排障往往还需要一条可复现证据链来回答“选的结果是什么”。

Spring MVC 在 `ResponseBodyAdvice#beforeBodyWrite(...)` 提供了两个非常关键的入参：
- `selectedConverterType`：最终选中的 `HttpMessageConverter` 类型
- `selectedContentType`：最终协商出的响应 `Content-Type`

本模块把它落成了可运行实验：
- `MessageConverterTraceAdvice`：仅对 `/api/advanced/message-converters/**` 写入响应头
- endpoints：String/JSON/bytes/strict media type 四种返回值对照
- Lab：`BootWebMvcMessageConverterTraceLabTest` 固定断言（不用猜、可回归）

## F. 常见坑与边界

- 你“只想对某个自定义 media type 严格校验”，不要全局改默认 ObjectMapper；更安全的做法是 **新增一个只支持该 media type 的 converter**。

## G. 小结与下一章

- 下一章进入 Part 04：专门用 406/415 与 Jackson 严格模式，把“契约可控”做成工程闭环。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcContractJacksonLabTest`
- Lab：`BootWebMvcTestingDebuggingLabTest`
- Lab：`BootWebMvcMessageConverterTraceLabTest`

上一章：[part-03-web-mvc-internals/02-argument-resolver-and-binder.md](02-argument-resolver-and-binder.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-03-web-mvc-internals/04-exception-resolvers-and-error-flow.md](04-exception-resolvers-and-error-flow.md)

<!-- BOOKIFY:END -->
