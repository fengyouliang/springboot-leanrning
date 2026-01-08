# 90：常见坑清单（Web MVC）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**90：常见坑清单（Web MVC）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

把“现象（状态码/响应体）”映射回 MVC 主线，是排障的最快路径。本章建议你按下面顺序收敛：

1. **先判断发生在 Filter 还是 DispatcherServlet 内**
   - 典型现象：401/403 往往发生在 FilterChain（Security）里，而不是 controller。

2. **再判断是 mapping 失败还是 handler 执行失败**
   - mapping：404/405（路由/方法不支持）
   - handler 链路：参数解析/绑定/校验/消息体读写/业务异常

3. **把 400 拆成三类（不要混成“校验失败”）**
   - JSON 解析失败（body read）：`HttpMessageNotReadableException`
   - 类型不匹配（binder/param）：`MethodArgumentTypeMismatchException`
   - 约束失败（validation）：`MethodArgumentNotValidException` / `BindException`

4. **把 406/415 拆成 read vs write**
   - 415：read（Content-Type / consumes / converter 不匹配）
   - 406：write（Accept / produces / converter 不匹配）

5. **最后再看错误体“是谁翻译的”**
   - `@ControllerAdvice`（自定义 ApiError/ProblemDetail）
   - MVC 默认 resolver（405/406/415/…）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebMvcLabTest` / `BootWebMvcSpringBootLabTest`
- Lab：`BootWebMvcBindingDeepDiveLabTest` / `BootWebMvcTestingDebuggingLabTest`
- Lab：`BootWebMvcRealWorldHttpLabTest` / `BootWebMvcSecurityLabTest` / `BootWebMvcObservabilityLabTest`
- Lab：`BootWebMvcAsyncSseLabTest`（含 DeferredResult）
- Lab：`BootWebMvcTraceLabTest`（Filter/Interceptor 顺序 + async lifecycle）
- 建议命令：`mvn -pl springboot-web-mvc test`（或在 IDE 直接运行上面的测试类）

## F. 常见坑与边界

## 400/校验相关

- DTO 上写了约束注解，但 controller 入参没加 `@Valid`：校验不会触发。
- 400 不等于校验失败：建议先把“坏输入”分成三类（对应不同异常/断点）：
  - JSON 解析失败：`HttpMessageNotReadableException`（body 路径）
  - 绑定/类型不匹配：`MethodArgumentTypeMismatchException`（binder 路径）
  - 校验失败：`MethodArgumentNotValidException`（@RequestBody）或 `BindException`（@ModelAttribute）
  - 对照证据：`BootWebMvcLabTest` / `BootWebMvcBindingDeepDiveLabTest`
- binder 边界不止要“阻止绑定”，还要能“留下证据”：
  - `@InitBinder#setAllowedFields` 阻止危险字段（mass assignment）
  - `BindingResult#getSuppressedFields()` 输出“被阻止绑定字段”用于排障
  - 对照证据：`BootWebMvcBindingDeepDiveLabTest`

## 401/403（Security/CSRF）相关

- 引入 `spring-boot-starter-security` 后，很多 401/403 发生在 MVC 之前：优先从 FilterChainProxy 入手，不要先改 controller。
- 403 很多时候不是“没权限”，而是 **CSRF 缺失**（尤其是 POST/PUT/DELETE）。
  - 对照证据：`BootWebMvcSecurityLabTest`（401/403/CSRF）

## 406/415（内容协商）相关

- 415：`Content-Type` 与 `consumes`/converter 不匹配（read 失败）
- 406：`Accept` 与 `produces`/converter 不匹配（write 失败）
  - 对照证据：`BootWebMvcContractJacksonLabTest` / `BootWebMvcTestingDebuggingLabTest`
- 当你需要确认“到底选了哪个 converter / 协商出的 content-type 是什么”：
  - 用 `ResponseBodyAdvice#beforeBodyWrite` 的 `selectedConverterType/selectedContentType` 写入响应头
  - 对照证据：`BootWebMvcMessageConverterTraceLabTest`

## ControllerAdvice 匹配/优先级相关

- advice “不生效” 常见原因不是 handler 写错，而是 selector 没命中：
  - `basePackages` 不包含 controller（包名变更/分包调整）
  - `annotations` selector：注解必须是 RUNTIME，且要标在 controller 类型上
  - `assignableTypes` selector：controller 必须满足可赋值关系（接口/父类）
  - 多个 selector 的组合是“并集（OR）”：不要把 basePackages 当成“再过滤一次”
  - 对照证据：`BootWebMvcAdviceMatchingLabTest`
- 当多个 advice 同时可处理同一异常时，`@Order` 决定最终生效（数值越小优先级越高）
  - 对照证据：`BootWebMvcAdviceOrderLabTest`

## 304/缓存（ETag）相关

- 304 是“条件请求命中”的正常分支：客户端带 `If-None-Match`，服务端用 ETag 判断没变化就不返回 body。
  - 对照证据：`BootWebMvcRealWorldHttpLabTest`
- 静态资源也可能命中 304：`Last-Modified` + `If-Modified-Since`。
  - 对照证据：`BootWebMvcRealWorldHttpLabTest`（静态资源条件请求）
- 通过 `ShallowEtagHeaderFilter` 也能触发 ETag/304（框架级计算 ETag）。
  - 对照证据：`BootWebMvcRealWorldHttpLabTest`（filter-etag）

## Async 相关（Callable/DeferredResult/SSE）

- 测试只断言 `asyncStarted` 不算闭环：必须 `asyncDispatch` 才能断言最终响应。
  - 对照证据：`BootWebMvcAsyncSseLabTest`
- async 下 Interceptor 回调“少一截”是正常现象：第一次 dispatch 会触发 `afterConcurrentHandlingStarted`，第二次 dispatch 才会走 `postHandle/afterCompletion`。
  - 对照证据：`BootWebMvcTraceLabTest`

## `@WebMvcTest` 相关

- `@WebMvcTest` 只加载 Web 层：如果 controller 依赖 service/repository，通常需要 `@MockBean` 或显式 `@Import`。
- `@WebMvcTest` 的“更快”来自加载范围更小：如果你把太多东西 `@Import` 进来，它就不再快了。

## 404/路由相关

- 路由拼错：确认类级 `@RequestMapping` 与方法级 `@GetMapping/@PostMapping` 的组合。
- path variable 名称不匹配：`@PathVariable("id") Long id`

## 500/异常相关

- 先确认异常来自哪个阶段：resolver/binder/converter/controller，不要一上来就 try/catch。
- 建议先用 `resolvedException` 或日志把异常类型固定，再决定是加 `@ExceptionHandler` 还是修输入约束。

## 建议的排查顺序

1. 先用测试把“现象”固化（状态码 + 响应形状）
2. 再回到 controller / handler / advice 看“为什么”
3. 需要更接近真实链路时，再用 `@SpringBootTest(webEnvironment=RANDOM_PORT)`

## 对应 Lab（可运行）

- `BootWebMvcLabTest`
- `BootWebMvcSpringBootLabTest`
- `BootWebMvcTestingDebuggingLabTest`
- `BootWebMvcSecurityLabTest`
- `BootWebMvcObservabilityLabTest`

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcLabTest` / `BootWebMvcSpringBootLabTest`
- Lab：`BootWebMvcBindingDeepDiveLabTest`
- Lab：`BootWebMvcTestingDebuggingLabTest`
- Lab：`BootWebMvcRealWorldHttpLabTest`
- Lab：`BootWebMvcAsyncSseLabTest`
- Lab：`BootWebMvcTraceLabTest`
- Lab：`BootWebMvcMessageConverterTraceLabTest`
- Lab：`BootWebMvcAdviceOrderLabTest`
- Lab：`BootWebMvcAdviceMatchingLabTest`
- Lab：`BootWebMvcSecurityLabTest`
- Lab：`BootWebMvcObservabilityLabTest`

上一章：[part-08-security-observability/02-observability-and-metrics.md](../part-08-security-observability/02-observability-and-metrics.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/99-self-check.md](99-self-check.md)

<!-- BOOKIFY:END -->
