# Design: Advanced Spring Boot Learning Modules

## Goals
- 扩展学习主题覆盖面（Security / Web Client / Async / Cache），并保持与现有仓库一致的学习范式：
  - **可运行**（必要时）/ **可验证（tests）** / **可观察（断言 + 断点）**
  - 默认构建全绿：`mvn -q test` 不依赖启用 exercises
  - Deep Dive Track：每模块 **15+（目标 20+）实验**，至少 10 Labs + 5 Exercises
- 将“常见现象与坑”固化为可复现、可断言的实验，而不是只靠文字解释。

## Constraints
- 不引入外部基础设施（Redis/Kafka/Docker 等）。
- 尽量采用“小容器”与更快的测试切片：
  - Web/Security：优先 `@WebMvcTest` + `spring-security-test`，必要时再上 `@SpringBootTest`
  - 机制验证：优先 `ApplicationContextRunner` / 小范围 `@ContextConfiguration`
- 测试必须尽量确定性：
  - 异步/调度：避免 `Thread.sleep`；使用 latch、等待条件、或可控 executor
  - 缓存过期：使用可控 clock/ticker（例如 Caffeine 的 `Ticker`）避免“等时间”
  - HTTP Client：使用进程内 Mock Server（如 OkHttp `MockWebServer`）避免外网不稳定

## Module Types & Port Policy
- 仅当模块必须通过 HTTP 行为才能建立直觉时，才引入 Web 端口与 `spring-boot:run` 观察：
  - `springboot-security`：需要 HTTP 边界与 FilterChain 行为 → 作为 Web 模块，分配独立端口（从 `8085` 起，避免与现有 `8081–8084` 冲突）。
- 其他模块默认采用 test-driven（无端口）：
  - `springboot-web-client`：以测试驱动对比 RestClient/WebClient，使用 MockWebServer
  - `springboot-async-scheduling`：以测试驱动验证线程/代理/调度语义
  - `springboot-cache`：以测试驱动验证缓存语义与过期策略（Caffeine）

根 `README.md` 与模块 `README.md` 需要明确标注：
- 是否 Web 模块（是否占端口、端口号）
- 是否主要以 tests 驱动学习（推荐执行哪些 `*LabTest`）

## Common Content Structure (per module)
- `README.md`（中文，索引页，不写长文）
  - 学习目标
  - 运行/测试命令
  - Labs/Exercises 总索引（含难度、下一步）
  - 常见 Debug 路径
- `docs/`（中文章节短文）
  - `01-*.md`、`02-*.md` …（按学习顺序）
  - `90-common-pitfalls.md`
  - `99-self-check.md`（可选）
  - 每章必须链接至少一个对应 `*LabTest` / `*ExerciseTest`
- Tests
  - `*LabTest`：默认启用，断言固化核心机制
  - `*ExerciseTest`：默认 `@Disabled`，包含明确任务说明（最好能拆小步）

## Module-Specific Design Notes

### 1) `springboot-security`
- 目标：从“认证/授权基础”走到“JWT/Stateless 常见实践”。
- 测试策略：
  - `MockMvc` + `spring-security-test`（`@WithMockUser`、`httpBasic()`、`csrf()`）
  - 覆盖 401 vs 403、CSRF 默认行为、method security、FilterChain 顺序与自定义 filter 插入点。
- JWT：
  - 优先以“最小可理解实现”为目标（例如 HMAC 签名 + claims）并用 tests 固化行为。
  - 明确标注：示例用于学习机制，并非生产级完整方案。

### 2) `springboot-web-client`
- 目标：同一业务场景下对比 RestClient（同步）与 WebClient（响应式），并系统化讲清：
  - 序列化/反序列化
  - 错误处理（4xx/5xx → 领域异常）
  - 超时与重试（确定性可测）
  - 拦截器/Filter 注入 header（trace/correlation id）
- 测试策略：OkHttp `MockWebServer` 提供可控 HTTP 交互；WebClient 相关实验可用 `StepVerifier` 或可控的 `block()` 断言。

### 3) `springboot-async-scheduling`
- 目标：讲透 `@Async` 的“代理 + 线程池 + 异常”三件套，并补齐 `@Scheduled` 的语义。
- 测试策略：使用可注入 executor、latch、等待条件；避免睡眠导致 flaky。

### 4) `springboot-cache`
- 目标：把 Spring Cache 抽象的核心语义与坑（key/condition/evict/sync）做成可断言实验，并用 Caffeine 提供可控过期与统计。
- 测试策略：自定义 `Ticker` 或类似机制让“时间推进”可控，从而稳定断言过期行为。

## Sequencing
实现顺序与学习优先级一致：
1) Security → 2) WebClient → 3) Async/Scheduling → 4) Cache

