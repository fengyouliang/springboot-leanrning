# 01：DispatcherServlet 主链路（从测试反推调用链）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01：DispatcherServlet 主链路（从测试反推调用链）**
- 目标：建立“请求在 MVC 内部如何被分派”的可观察心智模型：从 `@RequestMapping` 找到 handler，到参数解析、返回值写回、异常映射。

## B. 核心结论

- 学 MVC 内核不要背类名：**用测试用例固定一个可观察点**（例如“某个参数由自定义 ArgumentResolver 填充”），再从断点把调用链串起来。
- `DispatcherServlet#doDispatch` 是主入口，但真正帮助你定位“为什么行为不同”的通常是：`HandlerMapping`（选路）与 `HandlerAdapter`（如何调用 handler）。

## C. 机制主线

（本章以 `BootWebMvcInternalsLabTest` 为证据链：用 `@ClientIp` + 自定义 `HandlerMethodArgumentResolver` 让“参数解析阶段”可被稳定断言。）

## 主线伪代码（你要能“顺着念出来”）

你不需要背源码细节，但要能把主链路用伪代码复述出来（这样你才知道断点该打在哪里）：

1. `DispatcherServlet#doDispatch`
   - `getHandler(request)` → **HandlerMapping**（选路）
   - `getHandlerAdapter(handler)` → **HandlerAdapter**（决定怎么调用）
   - `adapter.handle(...)` → 进入 handler 调用（ArgumentResolver/HandlerMethod）
   - `processDispatchResult(...)` → 写回响应（ReturnValue/MessageConverter）或处理异常（ExceptionResolvers）

2. handler 调用（以 `@RequestMapping` 方法为例）
   - `HandlerMethodArgumentResolverComposite`：解析每个方法参数
   - `WebDataBinder`：对 `@RequestParam/@ModelAttribute` 做绑定与校验
   - `HttpMessageConverter`：对 `@RequestBody/@ResponseBody` 做读写

3. 异常处理
   - 任一阶段抛异常 → 进入 `processHandlerException` → 交给 `HandlerExceptionResolver` 链翻译成状态码/响应体

## 关键对象：你在调试时“手里拿着什么”

- `HandlerExecutionChain`：handler + interceptors（能解释“为什么 preHandle 没执行/执行了两次”）
- `HandlerMethod`：你的 controller 方法的封装（参数、注解、返回值信息都在这里）
- `RequestMappingHandlerAdapter`：最常见的 adapter（负责把 `HandlerMethod` 变成“可调用”）

## D. 源码与断点

建议断点（按优先级）：
- `org.springframework.web.servlet.DispatcherServlet#doDispatch`
- `org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping#getHandlerInternal`
- `org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter#handleInternal`
- `org.springframework.web.method.support.HandlerMethodArgumentResolverComposite#resolveArgument`
- （返回值）`org.springframework.web.servlet.mvc.method.annotation.AbstractMessageConverterMethodProcessor#writeWithMessageConverters`
- （异常）`org.springframework.web.servlet.mvc.method.annotation.ExceptionHandlerExceptionResolver#doResolveHandlerMethodException`

## E. 最小可运行实验（Lab）

- Lab：`BootWebMvcInternalsLabTest`
- 建议命令：`mvn -pl springboot-web-mvc test`

## F. 常见坑与边界

- 看到行为不一致时，先确认你观察的是哪一层：Filter（Servlet 容器） vs Interceptor（MVC handler 链） vs ArgumentResolver（方法参数解析）。

## G. 小结与下一章

- 下一章会把“参数解析/绑定/校验”拆开，讲清 ArgumentResolver 与 Binder 的边界。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcInternalsLabTest`

上一章：[part-02-view-mvc/03-error-pages-and-content-negotiation.md](../part-02-view-mvc/03-error-pages-and-content-negotiation.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-03-web-mvc-internals/02-argument-resolver-and-binder.md](02-argument-resolver-and-binder.md)

<!-- BOOKIFY:END -->
