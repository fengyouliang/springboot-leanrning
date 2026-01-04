# spring-core-tx

## Purpose

学习 Spring 事务：传播行为、回滚规则与代理边界。

## Module Overview

- **Responsibility:** 用最小业务场景与测试实验理解事务传播/回滚，并能定位常见坑。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Source Layout
- docs：`spring-core-tx/docs/README.md`（目录页）
- docs：`spring-core-tx/docs/part-00-guide/`（深挖指南）
- docs：`spring-core-tx/docs/part-01-transaction-basics/`（边界/代理/回滚/传播）
- docs：`spring-core-tx/docs/part-02-template-and-debugging/`（TransactionTemplate/调试）
- docs：`spring-core-tx/docs/appendix/`（常见坑/自测题）
- src(main)：`spring-core-tx/src/main/java/com/learning/springboot/springcoretx/SpringCoreTxApplication.java`（入口，包名保持不变）
- src(main)：`spring-core-tx/src/main/java/com/learning/springboot/springcoretx/part01_transaction_basics/**`
- src(main)：`spring-core-tx/src/main/java/com/learning/springboot/springcoretx/part02_template_and_debugging/**`
- src(test)：`spring-core-tx/src/test/java/com/learning/springboot/springcoretx/part00_guide/**`
- src(test)：`spring-core-tx/src/test/java/com/learning/springboot/springcoretx/part01_transaction_basics/**`
- src(test)：`spring-core-tx/src/test/java/com/learning/springboot/springcoretx/appendix/**`

### Docs Index
- 入口：`spring-core-tx/docs/README.md`

### Requirement: 事务学习闭环
**Module:** spring-core-tx
通过 Labs/Exercises 覆盖传播、只读、回滚规则与自调用陷阱。

#### Scenario: 不同传播行为差异可被断言
- REQUIRED/REQUIRES_NEW 等差异在测试中可稳定验证
- 自调用绕过 `@Transactional` 的陷阱可最小复现并对比修复（Lab）
- `spring-boot:run` 可观察事务活跃状态与回滚/提交差异（结构化前缀 `TX:`）

## Change History

- [202601021322_complete_spring_core_fundamentals_remaining](../../history/2026-01/202601021322_complete_spring_core_fundamentals_remaining/) - ✅ 已执行：新增 Tx 自调用陷阱 Lab，并补齐 `TxDemoRunner` 结构化输出与进度清单入口
- [202601041046_spring-core-part-structure-sync](../../history/2026-01/202601041046_spring-core-part-structure-sync/) - ✅ 已执行：对齐 docs Part 目录结构与 src/main+src/test 分包结构（语义化 Part 命名），并修复 README/跨模块引用路径

## Dependencies

- 依赖 `spring-core-aop`/`spring-core-beans` 的代理与容器基础（学习路径依赖）
