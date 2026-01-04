# spring-core-events

## Purpose

学习 Spring 应用事件：发布/订阅、顺序、condition、同步/异步与事务边界集成。

## Module Overview

- **Responsibility:** 通过最小示例与 Labs/Exercises 展示事件系统的机制与常见坑。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Source Layout
- docs：`spring-core-events/docs/README.md`（目录页）
- docs：`spring-core-events/docs/part-00-guide/`（深挖指南）
- docs：`spring-core-events/docs/part-01-event-basics/`（事件基础）
- docs：`spring-core-events/docs/part-02-async-and-transactional/`（异步与事务事件）
- docs：`spring-core-events/docs/appendix/`（常见坑/自测题）
- src(main)：`spring-core-events/src/main/java/com/learning/springboot/springcoreevents/SpringCoreEventsApplication.java`（入口，包名保持不变）
- src(main)：`spring-core-events/src/main/java/com/learning/springboot/springcoreevents/part01_event_basics/**`
- src(test)：`spring-core-events/src/test/java/com/learning/springboot/springcoreevents/part00_guide/**`
- src(test)：`spring-core-events/src/test/java/com/learning/springboot/springcoreevents/part01_event_basics/**`

### Docs Index
- 入口：`spring-core-events/docs/README.md`

### Requirement: 事件系统学习闭环
**Module:** spring-core-events
通过测试实验覆盖同步/异步、异常传播、多监听器顺序与 condition/payload。

#### Scenario: 默认同步与异常传播
- listener 抛异常能传播回 publisher（可断言）
- `spring-boot:run` 可观察线程与异常传播（结构化前缀 `EVENTS:`）

## Change History

- [202601021322_complete_spring_core_fundamentals_remaining](../../history/2026-01/202601021322_complete_spring_core_fundamentals_remaining/) - ✅ 已执行：补齐 `EventsDemoRunner` 结构化输出（线程/异常传播）与 throwing listener（特定输入触发）
- [202601041046_spring-core-part-structure-sync](../../history/2026-01/202601041046_spring-core-part-structure-sync/) - ✅ 已执行：对齐 docs Part 目录结构与 src/main+src/test 分包结构（语义化 Part 命名），并修复 README/跨模块引用路径

## Dependencies

- 基于 `spring-core-beans` 的 IoC/Bean 基础（学习路径依赖）
