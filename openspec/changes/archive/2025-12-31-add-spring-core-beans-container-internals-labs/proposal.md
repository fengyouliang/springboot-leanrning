# Change: Add spring-core-beans container internals labs

## Why

`spring-core-beans` 是整个学习仓库的“机制底座”。目前模块已经覆盖了 DI、scope、生命周期、BFPP/BPP、`@Configuration` 增强、`FactoryBean`、循环依赖、以及部分 import/auto-configuration 的实验，但对 **容器更底层的工作方式（container internals）** 仍缺少“可运行 + 可断言”的 Labs 支撑。

本变更目标是把更多“容器机制知识点”落成：

- 小而专注的 Labs（默认启用，`mvn -q test` 全绿）
- 每个 Lab 配套一章中文 docs（从现象 → 机制 → 复现 → 断言）
- 深水区/易波动点作为 Exercises（默认 `@Disabled`）

## What Changes

- 在 `spring-core-beans` 新增一组“容器机制”Labs（默认启用），尽量使用小容器（`AnnotationConfigApplicationContext`/`GenericApplicationContext`），避免 `@SpringBootTest`。
- 为每个新增 Lab 增加一章 `spring-core-beans/docs/` 中文文档（1:1 对应）。
- 更新 `spring-core-beans/README.md`：把新增章节纳入推荐阅读顺序，并补齐“概念 → Lab/Test → 代码”的导航。
- 更新根 `README.md`：只保留 beans 模块的入口链接，不在根 README 展开列出 beans 内部新增的所有 labs。

## Impact

- Affected spec: `openspec/specs/spring-core-beans-module/spec.md`
- Affected code: `spring-core-beans/src/test/java/.../*LabTest.java`、`spring-core-beans/docs/*.md`、`spring-core-beans/README.md`、根 `README.md`

## Non-Goals

- 不新增新的 Maven 模块；所有内容聚合在 `spring-core-beans`。
- 不引入外部基础设施依赖（Kafka/Redis/Docker 等）。
- 不修改现有 Labs 的语义（除非为了统一可观测性/断言稳定性进行极小范围重构）。
