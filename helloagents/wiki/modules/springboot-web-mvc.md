# springboot-web-mvc

## Purpose

学习 Spring MVC 的两条主线：

- REST API（JSON）：`@RestController`、校验、统一错误响应
- 传统 MVC（HTML）：`@Controller`、Thymeleaf 页面渲染、表单提交（绑定/校验/回显/PRG）、错误页与内容协商

## Module Overview

- **Responsibility:** 提供可运行 Web 示例与测试（MockMvc 等），帮助理解请求处理链路。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-09

## Specifications

### Requirement: Web MVC 学习闭环
**Module:** springboot-web-mvc
覆盖请求处理、参数绑定与异常处理策略，并补齐传统 MVC（HTML）渲染与错误页机制。

#### Scenario: 请求处理链路可被测试验证
- 通过 MockMvc 等方式断言响应与错误处理

### Requirement: 传统 MVC 页面渲染学习闭环
**Module:** springboot-web-mvc
覆盖 `@Controller`、Thymeleaf、表单提交（绑定/校验/回显/PRG）与错误页/Accept 内容协商，并提供可复现测试入口。

### Requirement: Advanced Deep Dive（机制内核 / 契约可控 / 真实场景 / Async / 排障）
**Module:** springboot-web-mvc
覆盖 Web MVC 的核心内部链路（DispatcherServlet/HandlerMapping/HandlerAdapter）、契约与序列化（HttpMessageConverter/Jackson/ProblemDetail）、真实 HTTP 场景（CORS/上传下载/静态资源/ETag）、Async/SSE，以及测试与排障的体系化套路，并补齐 Security 与观测（metrics）相关分支。

#### Scenario: 关键分支可被测试验证
- 通过 `@WebMvcTest` 的 Lab 固定关键行为：406/415、strict media type、CORS preflight、multipart upload/download、asyncDispatch、SSE content-type 等

## Dependencies

- 与安全/测试模块有学习路径关联（可选）

## Docs & 复现入口

- **Docs Index:** `springboot-web-mvc/docs/README.md`
- **Docs Guide:** `springboot-web-mvc/docs/part-00-guide/00-deep-dive-guide.md`
- **Labs:**
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcSpringBootLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcBindingDeepDiveLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcErrorViewLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewSpringBootLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcInternalsLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcTraceLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcMessageConverterTraceLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcExceptionResolverChainLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part04_contract/BootWebMvcContractJacksonLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part04_contract/BootWebMvcProblemDetailLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part09_advice_order/BootWebMvcAdviceOrderLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part10_advice_matching/BootWebMvcAdviceMatchingLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part05_real_world/BootWebMvcRealWorldHttpLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part06_async_sse/BootWebMvcAsyncSseLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part07_testing/BootWebMvcTestingDebuggingLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part08_security_observability/BootWebMvcSecurityLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part08_security_observability/BootWebMvcSecurityVsMvcExceptionBoundaryLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part08_security_observability/BootWebMvcObservabilityLabTest.java`
- **Exercises:** `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；示例按 Part 分组：
  - REST 主线：`com.learning.springboot.bootwebmvc.part01_web_mvc`
  - 页面主线：`com.learning.springboot.bootwebmvc.part02_view_mvc`
  - 机制内核：`com.learning.springboot.bootwebmvc.part03_internals`
  - 契约与序列化：`com.learning.springboot.bootwebmvc.part04_contract`
  - 真实 HTTP：`com.learning.springboot.bootwebmvc.part05_real_world`
  - Async/SSE：`com.learning.springboot.bootwebmvc.part06_async_sse`
  - Security/Observability：`com.learning.springboot.bootwebmvc.part08_security_observability`
  - Advice 优先级：`com.learning.springboot.bootwebmvc.part09_advice_order`
  - Advice 匹配规则：`com.learning.springboot.bootwebmvc.part10_advice_matching`
- `src/test/java`：按 `part00_guide`（Exercises）+ `part01_*`（Labs）+ `part07_testing`（排障）分包

## Change History

- [202601081505_springboot-web-mvc-deepen-v3](../../history/2026-01/202601081505_springboot-web-mvc-deepen-v3/) - ✅ 已执行：深化 v3：新增 `@ControllerAdvice` 匹配规则可复现 Labs（basePackages/annotations/assignableTypes + selector OR 语义 + @Order 叠加）、binder `suppressedFields` 证据链、HttpMessageConverter 选择可观测（selectedConverterType/selectedContentType 响应头），并新增 Part 03 章节与排障/自测升级
- [202601081308_springboot-web-mvc-deepen-even-more](../../history/2026-01/202601081308_springboot-web-mvc-deepen-even-more/) - ✅ 已执行：补齐导读/自测/坑点占位，并新增“mass assignment 防护（InitBinder allowedFields）”与“ControllerAdvice @Order 优先级”两组可复现 Labs
- [202601081108_springboot-web-mvc-deepen-more](../../history/2026-01/202601081108_springboot-web-mvc-deepen-more/) - ✅ 已执行：补齐 ExceptionResolvers 主线、Interceptor/Filter sync+async lifecycle Lab、条件请求（Last-Modified + ETag filter）与 DeferredResult（timeout/fallback），并把坑点清单与测试入口强绑定
- [202601080925_springboot-web-mvc-deep-dive-part08-security-observability](../../history/2026-01/202601080925_springboot-web-mvc-deep-dive-part08-security-observability/) - ✅ 已执行：新增知识地图、ProblemDetail 对照、ETag/304、Part 08（Security/Observability）与对应 Labs/排障升级
- [202601071635_springboot-web-mvc-advanced-deep-dive](../../history/2026-01/202601071635_springboot-web-mvc-advanced-deep-dive/) - ✅ 已执行：扩展 advanced deep dive（机制内核/契约与 Jackson/真实 HTTP/Async/SSE/排障），新增 docs Part 03–07 与对应 Labs
- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章），并通过 `scripts/check-docs.sh`
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
- [202601061309_springboot-web-mvc-thymeleaf-view-rendering](../../history/2026-01/202601061309_springboot-web-mvc-thymeleaf-view-rendering/) - ✅ 已执行：补齐传统 MVC（Thymeleaf/表单/错误页/Accept）+ docs 与 tests 闭环
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + guide/appendix 可跑入口块补齐 + 自检闸门覆盖
