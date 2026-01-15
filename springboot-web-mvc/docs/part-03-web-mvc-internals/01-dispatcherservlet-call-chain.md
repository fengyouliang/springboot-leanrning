# 01：DispatcherServlet 主链路（把选路/参数解析/返回值/异常串起来）

## 导读

- 本章主题：**01：DispatcherServlet 主链路（把选路/参数解析/返回值/异常串起来）**
- 目标：建立“请求在 MVC 内部如何被分派”的可观察心智模型：从 `@RequestMapping` 找到 handler，到参数解析、返回值写回、异常映射。

!!! summary "本章要点"

    - 学 MVC 内核不要背类名：**用测试用例固定一个可观察点**（例如“某个参数由自定义 ArgumentResolver 填充”），再从断点把调用链串起来。
    - `DispatcherServlet#doDispatch` 是主入口，但真正帮助你定位“为什么行为不同”的通常是：`HandlerMapping`（选路）与 `HandlerAdapter`（如何调用 handler）。

!!! example "本章配套实验（先跑再读）"

    - Lab：`BootWebMvcInternalsLabTest`

## 机制主线

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

## 参数解析/绑定/校验：把“进方法”拆成 3 段（合并自原第 02 章）

当你在工程里遇到“参数进不来/类型转换不对/校验不生效”，先把问题拆成三段再定位：

1. **解析（resolver）**：这个参数从哪里来（header/path/query/body/session…）？
2. **绑定（binder）**：这个值怎么从 String 变成目标类型（converter/formatter）？
3. **校验（validation）**：这个对象是否符合约束（`@Valid` / `@Validated`）？

### resolver vs binder：怎么快速判断“该扩展哪里”

- **这个参数从哪里来？** → 先看 resolver（或现有注解是否选错）
- **这个值怎么变成目标类型？** → 先看 binder/ConversionService（Converter/Formatter）
- **这个对象是否符合约束？** → 先看 validation（校验通常发生在绑定完成之后）

### 常见内置 ArgumentResolver（你大概率会遇到）

- `@RequestParam`：`RequestParamMethodArgumentResolver`
- `@PathVariable`：`PathVariableMethodArgumentResolver`
- `@RequestHeader`：`RequestHeaderMethodArgumentResolver`
- `@RequestBody`：`RequestResponseBodyMethodProcessor`（注意它依赖 HttpMessageConverter）
- `HttpServletRequest/HttpServletResponse`：`ServletRequestMethodArgumentResolver`

写自定义 resolver 时，核心原则是：**只解决“来源”问题，不要把“类型转换/校验”硬塞进 resolver**（否则会绕开框架的 binder/validation 机制）。

### 补充：suppressedFields（把“被禁止绑定字段”变成证据）

当你用 `@InitBinder#setAllowedFields` 或 `setDisallowedFields` 做“绑定边界”时，除了断言“值没进来”，还建议把“被阻止绑定的字段名”变成可观察证据：

- Spring 6.2+：`BindingResult#getSuppressedFields()`
- 本模块提供证据链：`POST /api/advanced/binding/mass-assignment-debug` + `BootWebMvcBindingDeepDiveLabTest`

## 源码与断点

建议断点（按优先级）：

- `org.springframework.web.servlet.DispatcherServlet#doDispatch`
- `org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping#getHandlerInternal`
- `org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter#handleInternal`
- `org.springframework.web.method.support.HandlerMethodArgumentResolverComposite#resolveArgument`
- （binder）`org.springframework.web.bind.support.WebDataBinderFactory#createBinder`
- （binder）`org.springframework.validation.DataBinder#bind`
- （binder）`org.springframework.validation.DataBinder#validate`
- （返回值）`org.springframework.web.servlet.mvc.method.annotation.AbstractMessageConverterMethodProcessor#writeWithMessageConverters`
- （异常）`org.springframework.web.servlet.mvc.method.annotation.ExceptionHandlerExceptionResolver#doResolveHandlerMethodException`

## 最小可运行实验（Lab）

- Lab：`BootWebMvcInternalsLabTest`
- Lab：`BootWebMvcLabTest`
- Lab：`BootWebMvcBindingDeepDiveLabTest`
- 建议命令：`mvn -pl springboot-web-mvc test`

## 常见坑与边界

- 看到行为不一致时，先确认你观察的是哪一层：Filter（Servlet 容器） vs Interceptor（MVC handler 链） vs ArgumentResolver（方法参数解析）。
- “我加了注解但没生效”的第一排查点：是不是落在了错误的扩展点（应该写 resolver 但写成 converter，或反过来）。

## 小结与下一章

- 下一章会把“返回值写回”（MessageConverter）与内容协商连起来，解释 406/415 在链路里发生在哪里。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcInternalsLabTest` / `BootWebMvcLabTest` / `BootWebMvcBindingDeepDiveLabTest`

上一章：[part-02-view-mvc/03-error-pages-and-content-negotiation.md](../part-02-view-mvc/03-error-pages-and-content-negotiation.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-03-web-mvc-internals/03-message-converters-and-return-values.md](03-message-converters-and-return-values.md)

<!-- BOOKIFY:END -->

