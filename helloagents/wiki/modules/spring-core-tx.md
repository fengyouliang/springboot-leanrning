# spring-core-tx

## Purpose

学习 Spring 事务：传播行为、回滚规则与代理边界。

## Module Overview

- **Responsibility:** 用最小业务场景与测试实验理解事务传播/回滚，并能定位常见坑。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-01

## Specifications

### Requirement: 事务学习闭环
**Module:** spring-core-tx
通过 Labs/Exercises 覆盖传播、只读、回滚规则与自调用陷阱。

#### Scenario: 不同传播行为差异可被断言
- REQUIRED/REQUIRES_NEW 等差异在测试中可稳定验证

## Dependencies

- 依赖 `spring-core-aop`/`spring-core-beans` 的代理与容器基础（学习路径依赖）

