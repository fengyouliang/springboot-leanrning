# Project Context

## Purpose
本仓库是一个面向初学者的 **Spring / Spring Boot 学习工作区**：

- 目标不是“做一个业务项目”，而是通过 **可运行 + 可验证（tests）+ 可观察（logs/断点）** 的方式建立正确心智模型
- 采用 **多模块** 组织方式：`一个模块 = 一个主题`，避免“大杂烩工程”带来的认知噪音
- 默认保持 `mvn -q test` 全绿：学习者不需要先“修工程”，就能开始学习

## Tech Stack
- JDK：17
- 构建：Maven 多模块（不使用 Maven Wrapper，直接系统 `mvn`）
- Spring Boot：3.x（父 POM 统一管理）
- 测试：JUnit 5 + Spring Boot Test（按主题选择切片或全量上下文）

## Project Conventions

### Code Style
- Java：保持示例代码短小、可读，优先表达“机制”而非工程完备性
- 命名：类名/方法名尽量体现机制（例如 `SelfInvocationExampleService`、`*LabTest`）
- **README 语言规则**：本仓库所有 `README.md` 必须使用中文撰写

### Architecture Patterns
- 多模块：每个模块独立运行、独立测试、独立 README
- 示例偏好：能用更小的 Spring 容器就不用更大的
  - Spring Core 机制：优先 `AnnotationConfigApplicationContext`
  - Spring Boot 条件装配：优先 `ApplicationContextRunner`
  - 只有当主题需要完整链路时才使用 `@SpringBootTest`

### Testing Strategy
默认采用 “Deep Dive Track”（深潜学习轨道）：

- **Labs**：`src/test/java/.../*LabTest.java`
  - 默认启用，必须全绿
  - 目标是“可运行的机制实验”：有断言、有观察点、可用断点跟进
- **Exercises**：`src/test/java/.../*ExerciseTest.java`
  - 默认 `@Disabled`，学习者手动开启
  - 目标是“带提示的练习题”：通过失败的断言/提示引导学习者动手

推荐实践：

- 一个测试只讲一个点（一个机制/一个坑/一个结论）
- 优先写“行为断言”，日志只做辅助观察

### Documentation Pattern
文档目标不是“写长文”，而是让学习者能形成 **从现象 → 机制 → 复现 → 断言** 的闭环。

- `README.md` 是模块索引页（导航 + 怎么跑 + 怎么验证），不承担长篇解释
- 需要深入机制的模块使用 `docs/*.md` 做章节化讲解（短文即可）
  - 建议命名：`01-*.md`、`02-*.md` …（按学习顺序）
  - 常见坑：`90-common-pitfalls.md`（建议每次踩坑就回填）
  - 自测题（可选）：`99-self-check.md`
- 模块 `README.md` 推荐固定版式（顺序尽量一致）：  
  学习目标 → 运行 → 测试 → 推荐阅读顺序（docs） → 概念映射（概念→测试/代码） → Labs → Exercises → Debug/观察建议 → 常见坑 → 延伸阅读

### Git Workflow
- 对学习仓库而言，最重要的工作流约束是：主分支默认可运行、默认全绿
- 如需扩展新主题，建议按模块追加，避免把多个主题揉在同一个模块里

## Domain Context
这是一个“学习型仓库”，因此设计决策的优先级通常是：

1. 初学者是否容易跑起来（快速反馈）
2. 是否能建立正确机制心智模型（从现象到原因）
3. 是否容易用 tests 复现与验证（避免只靠口述/玄学）
4. 工程完备性（在不影响 1-3 的前提下再考虑）

## Important Constraints
- 默认构建必须全绿：`mvn -q test` 不依赖开启 exercises
- 文档优先：`README.md` 做索引导航，复杂主题推荐使用 `docs/*.md` 章节化讲解
- 不强制引入外部基础设施（Kafka/Redis/Docker 等），避免把环境搭建变成学习门槛

## External Dependencies
- 默认使用内嵌数据库（H2）或内存结构模拟外部依赖，以降低学习成本
