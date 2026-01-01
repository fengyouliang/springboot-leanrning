## Context

本变更为 `spring-core-beans` 增加更多“容器机制”可运行实验。目标是让学习者能用测试复现结论，而不是靠口述/玄学。

## Goals / Non-Goals

- Goals
  - 每个机制点都可通过断言稳定复现
  - 优先使用小容器（`AnnotationConfigApplicationContext`/`GenericApplicationContext`），提高反馈速度
  - 每个 Lab 1:1 对应一章 docs（中文）

- Non-Goals
  - 不追求覆盖 Spring 内部所有细节（避免版本波动导致不稳定）
  - 不把复杂业务逻辑引入 beans 模块

## Decisions

- 测试容器选择
  - Spring Core 容器机制：优先 `AnnotationConfigApplicationContext`（需要时使用 `GenericApplicationContext`）
  - Boot 条件装配：继续使用 `ApplicationContextRunner`（已有模式）
  - 避免 `@SpringBootTest`（除非主题必须）

- 稳定性策略
  - 不断言 Spring 内置处理器的“完整顺序/完整列表”；只断言“我们自己注册的处理器”的相对顺序
  - 不断言异常 message 全文；断言异常类型 + 关键片段
  - 所有“观察点”优先用内存记录器（list/queue）固定，再用少量 `OBSERVE:` 打印辅助

- 结构与命名
  - 新增 Labs：独立 `*LabTest` 类，每个测试方法只讲一个结论
  - 文档编号从 `12-` 开始连续递增；每章开头给出对应 LabTest 入口

## Risks / Trade-offs

- 风险：容器 internals 与 Spring 版本强相关
  - 缓解：避免依赖内部实现细节（只断言对外可观察行为 + 适度的 SPI 行为）

- 风险：知识点“越多越好”可能导致测试变慢
  - 缓解：核心点做 Labs（启用），深水区做 Exercises（默认禁用）
