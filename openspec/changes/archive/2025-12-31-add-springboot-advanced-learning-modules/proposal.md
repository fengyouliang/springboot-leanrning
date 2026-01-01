# Change: Add Advanced Spring Boot Learning Modules (Security / WebClient / Async / Cache)

## Why
当前学习工作区已经覆盖了 Spring Boot 的基础模块（启动配置、Web MVC、JPA、Actuator、Testing）以及 Spring Core 的机制模块（Beans/AOP/Tx/Events/Validation/Resources/Profiles）。

为了让学习路径更贴近真实工程，同时保持“可运行 + 可验证（tests）+ 可观察（断点/断言）”的学习闭环，需要补齐以下高频主题的可复现实验集：

- **Security**：认证/授权、CSRF、方法级安全、Filter Chain、以及 **JWT/Stateless**（从入门到常见实践）。
- **Web Client**：对比 **RestClient vs WebClient**，涵盖错误处理、超时、重试、拦截/Filter、以及可测试性。
- **Async & Scheduling**：`@Async` 线程池、异常传播、代理陷阱、自调用；以及 `@Scheduled` 的语义与可测试性。
- **Cache**：Spring Cache 抽象（`@Cacheable/@CachePut/@CacheEvict`）、key/condition、缓存一致性常见坑，以及基于 Caffeine 的可控/可断言实验（含过期）。

本变更将新增 4 个 Spring Boot 学习模块，并以 Deep Dive Track 的标准提供 **15+（目标 20+）实验**，优先以 tests 驱动学习；仅在主题确需“启动观察”时才引入端口与可运行 HTTP 行为。

## What Changes
- 新增 4 个模块（按实现顺序）：
  1) `springboot-security`
  2) `springboot-web-client`
  3) `springboot-async-scheduling`
  4) `springboot-cache`
- 每个模块均提供：
  - 至少 15 个实验（目标 20+）：**10+ Labs（默认启用） + 5+ Exercises（默认 `@Disabled`）**
  - 模块级 `README.md`（中文）：运行/测试命令、Labs/Exercises 索引、Debug 路径
  - `docs/`（中文，章节化）：从“现象 → 机制 → 复现 → 断言”的短文讲解，并链接到对应测试
- 更新工作区入口：
  - 根 `pom.xml` 引入新模块
  - 根 `README.md` Catalog 增补新模块（并标注是否 Web/端口或 test-driven）

## Impact
- Affected specs:
  - `learning-module-template`（补充 test-driven 模块与端口策略约束）
  - `learning-module-catalog`（新增模块目录条目）
  - `learning-workspace`（默认构建覆盖新增模块）
  - `boot-security-module`
  - `boot-web-client-module`
  - `boot-async-scheduling-module`
  - `boot-cache-module`
- Affected code (apply stage):
  - Root: `pom.xml`, `README.md`
  - New modules: `springboot-security/`, `springboot-web-client/`, `springboot-async-scheduling/`, `springboot-cache/`

## Out of Scope
- 引入外部基础设施（Redis、Kafka、Docker 依赖等）
- 生产级安全方案全景（OAuth2/OIDC、SSO、第三方 IdP 集成等）
- 引入重型弹性治理栈（完整的熔断/限流/服务发现平台等）

