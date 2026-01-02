# spring-core-tx

## Purpose

学习 Spring 事务：传播行为、回滚规则与代理边界。

## Module Overview

- **Responsibility:** 用最小业务场景与测试实验理解事务传播/回滚，并能定位常见坑。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-02

## Specifications

### Requirement: 事务学习闭环
**Module:** spring-core-tx
通过 Labs/Exercises 覆盖传播、只读、回滚规则与自调用陷阱。

#### Scenario: 不同传播行为差异可被断言
- REQUIRED/REQUIRES_NEW 等差异在测试中可稳定验证
- 自调用绕过 `@Transactional` 的陷阱可最小复现并对比修复（Lab）
- `spring-boot:run` 可观察事务活跃状态与回滚/提交差异（结构化前缀 `TX:`）

## Change History

- [202601021322_complete_spring_core_fundamentals_remaining](../../history/2026-01/202601021322_complete_spring_core_fundamentals_remaining/) - ✅ 已执行：新增 Tx 自调用陷阱 Lab，并补齐 `TxDemoRunner` 结构化输出与进度清单入口

## Dependencies

- 依赖 `spring-core-aop`/`spring-core-beans` 的代理与容器基础（学习路径依赖）
