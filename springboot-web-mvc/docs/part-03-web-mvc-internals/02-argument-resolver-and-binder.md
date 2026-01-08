# 02：ArgumentResolver 与 Binder（参数解析/绑定/校验的边界）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**02：ArgumentResolver 与 Binder（参数解析/绑定/校验的边界）**
- 目标：把“参数怎么进到 controller 方法里”的问题拆成三段：解析（resolver）→ 绑定（binder）→ 校验（validation）。

## B. 核心结论

- `HandlerMethodArgumentResolver` 解决的是“**这个参数从哪里来**”（header/path/query/session 等）。
- `WebDataBinder`/`ConversionService` 解决的是“**字符串如何变成目标类型**”（converter/formatter）。
- `@Valid` 解决的是“**这个对象是否符合约束**”；它通常发生在绑定完成之后。

## C. 机制主线

- 本章以两个证据链对照：
  - `BootWebMvcInternalsLabTest`：证明 resolver 在 handler 调用前被执行
  - `BootWebMvcLabTest`：证明 binding/validation 失败后会进入统一错误映射

## resolver vs binder：怎么快速判断“该扩展哪里”

当你在工程里遇到“参数进不来/类型转换不对/校验不生效”，先做这个判断：

- **这个参数从哪里来？**（header/path/query/body/session…）
  - 结论：优先看 resolver（或现有注解是否选错）
- **这个值怎么从 String 变成目标类型？**
  - 结论：优先看 binder/ConversionService（Converter/Formatter）
- **这个对象是否符合约束？**
  - 结论：优先看 validation（`@Valid` / `@Validated`）

## 常见内置 ArgumentResolver（你大概率会遇到）

- `@RequestParam`：`RequestParamMethodArgumentResolver`
- `@PathVariable`：`PathVariableMethodArgumentResolver`
- `@RequestHeader`：`RequestHeaderMethodArgumentResolver`
- `@RequestBody`：`RequestResponseBodyMethodProcessor`（注意它依赖 HttpMessageConverter）
- `HttpServletRequest/HttpServletResponse`：`ServletRequestMethodArgumentResolver`

当你写自定义 resolver 时，核心原则是：**只解决“来源”问题，不要把“类型转换/校验”硬塞进 resolver**（否则会绕开框架的 binder/validation 机制）。

## D. 源码与断点

建议断点：
- `HandlerMethodArgumentResolverComposite#resolveArgument`
- `org.springframework.web.bind.support.WebDataBinderFactory#createBinder`
- `org.springframework.validation.DataBinder#bind`
- `org.springframework.validation.DataBinder#validate`

## E. 最小可运行实验（Lab）

- Lab：`BootWebMvcInternalsLabTest` / `BootWebMvcLabTest`

## F. 常见坑与边界

- “我加了注解但没生效”的第一排查点：是不是落在了错误的扩展点（应该写 resolver 但写成 converter，或反过来）。

## 补充：suppressedFields（把“被禁止绑定字段”变成证据）

当你用 `@InitBinder#setAllowedFields` 或 `setDisallowedFields` 做“绑定边界”时，除了断言“值没进来”，你还需要能回答：

- 请求里到底传了哪些“被禁止绑定”的字段？
- 这是否能作为排障信号（例如怀疑前端/客户端多传参数、或怀疑 mass assignment 风险）？

Spring 6.2+ 提供 `BindingResult#getSuppressedFields()`，可返回“被 binder 阻止绑定的字段名”。

本模块提供了可复现证据链：
- endpoint：`POST /api/advanced/binding/mass-assignment-debug`
- Lab：`BootWebMvcBindingDeepDiveLabTest`（断言 `suppressedFields` 包含 `admin`）

## G. 小结与下一章

- 下一章会把返回值写回（MessageConverter）与内容协商连起来，解释 406/415 在链路里发生在哪里。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcInternalsLabTest` / `BootWebMvcLabTest`
- Lab：`BootWebMvcBindingDeepDiveLabTest`

上一章：[part-03-web-mvc-internals/01-dispatcherservlet-call-chain.md](01-dispatcherservlet-call-chain.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-03-web-mvc-internals/03-message-converters-and-return-values.md](03-message-converters-and-return-values.md)

<!-- BOOKIFY:END -->
