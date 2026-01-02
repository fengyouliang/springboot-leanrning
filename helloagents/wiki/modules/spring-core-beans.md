# spring-core-beans

## Purpose

讲透 Spring Framework IoC 容器与 Bean：从定义注册 → 注入解析 → 生命周期 → 扩展点 → 代理/循环依赖边界，做到“能解释、能断点、能定位问题”。

## Module Overview

- **Responsibility:** 提供 Bean 机制的系统文档与可运行 Labs/Exercises，用于建立源码级心智模型与排障能力。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-02

## Specifications

### Requirement: 深化 spring-core-beans 文档与 Labs（源码级）
**Module:** spring-core-beans
将 `spring-core-beans` 文档从“概念解释”升级为“源码级可验证”：每个关键主题都能通过可运行的测试实验复现，并在文档中给出断点入口与观察点。

#### Scenario: 能复述容器启动主线（refresh 时间线）
- 给出 `refresh()` 的关键阶段与“你应该在哪一段看见什么”的映射
- 提供最小 Lab，使用户能在本地打断点观察 BFPP/BPP/单例实例化发生的顺序

#### Scenario: 能从注入报错反推候选选择过程
- 文档明确候选收集与缩小过程（@Primary/@Qualifier/名称匹配/集合注入排序）
- 提供 Lab 覆盖：多实现歧义、@Primary、@Qualifier、集合注入排序与可选依赖

#### Scenario: 能讲清循环依赖“能救/不能救”的边界（含代理介入）
- 文档解释三层缓存与 early reference 的真实语义
- 提供 Lab 覆盖：构造器循环失败、setter 循环可能成功、代理介入导致 early reference 行为变化

#### Scenario: 能把 Bean 三层模型映射到关键类与扩展点
- 文档明确：BeanDefinition/实例/生命周期 三层与关键参与者的关系
- 提供 Lab 使用户能在断点里看到这些对象在何时出现与被修改

#### Scenario: 能把 AOP/事务等“代理能力”放回容器时间线解释（BPP 视角）
- 能解释 AutoProxyCreator 作为典型 BPP 如何在 pre/early/after-init 介入，导致最终暴露对象可能是 proxy
- 能分清“BPP 包裹顺序（容器阶段）”与“advisor/interceptor 顺序（调用阶段）”，并能给出跨模块的断点闭环路径

## Dependencies

- 无跨模块硬依赖（该模块是 Spring Core 学习底座）

## Change History

- [202601010649_spring-core-beans-deep-dive](../../history/2026-01/202601010649_spring-core-beans-deep-dive/) - ✅ 已执行：深化 DI/生命周期/PostProcessor/循环依赖/@Configuration/FactoryBean，并补齐坑点与自测题的闭环指引
- [202601010845_beans-aop-deep-dive-v2](../../history/2026-01/202601010845_beans-aop-deep-dive-v2/) - ✅ 已执行：在 BPP/代理/顺序章节补齐 AutoProxyCreator 承接，并补齐与 AOP 模块的多代理叠加闭环链接
- [202601020725_enhance_spring_core_fundamentals](../../history/2026-01/202601020725_enhance_spring_core_fundamentals/) - ✅ 已执行：把“新增面试点”嵌入正文对应小节，并补齐可断言复现入口（BeanFactory vs ApplicationContext/Aware/泛型匹配坑/CGLIB 对照）
- [202601020934_spring_core_beans_learning_route](../../history/2026-01/202601020934_spring_core_beans_learning_route/) - ✅ 已执行：补齐 README 学习路线与 Start Here（含 refresh 主线一页纸/运行态观察点），并新增注入歧义 Lab + 对应 Exercise
- [202601021002_spring_core_beans_auto_config_ordering](../../history/2026-01/202601021002_spring_core_beans_auto_config_ordering/) - ✅ 已执行：补齐 matchIfMissing（三态）与自动配置顺序依赖（after/before）Lab，并把面试点落到 docs/10 与 docs/11 的正文入口
