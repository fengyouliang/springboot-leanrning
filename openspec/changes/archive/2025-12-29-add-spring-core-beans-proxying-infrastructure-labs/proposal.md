# Change: Add `spring-core-beans` proxying & infrastructure (injection) deep-dive labs

## Why
当前仓库已经有较完整的 `spring-core-beans` 深潜内容（BFPP/BPP、early reference、生命周期、FactoryBean、覆盖策略等），但学习者在进入 `spring-core-aop` / `spring-core-tx` 后依然很容易“被折磨”，典型表现是：

- 看到现象（AOP/事务不生效、注入为 null、`@PostConstruct` 不执行）却无法定位到“容器哪个阶段/哪个扩展点导致的”
- 只知道“事务也是代理”，但不知道 **这个代理是怎么被容器创建并替换进 bean graph 的**
- 对 `@Autowired` 的生效时机没有清晰心智模型（它不是语言魔法，而是注解处理器 + instantiation-aware BPP 在特定阶段完成注入）

因此本变更聚焦补齐两类“桥梁知识点”，并把它们落实为可运行、可断言、可调试的 Labs + 对应中文 docs：

1) **注入阶段（Injection Phase）**：`@Autowired`/属性填充发生在生命周期的哪一步？为什么它依赖 `AutowiredAnnotationBeanPostProcessor`？
2) **代理/替换阶段（Proxying Phase）**：AOP/Tx 这种“看见的是代理、调用链才生效”的现象，如何用一个最小的 `BeanPostProcessor` 实验解释清楚？

## What Changes
- 在 `spring-core-beans` 增加一组新增 Labs（默认启用）：
  - Injection Phase Lab：对照 **field injection** 与 **constructor injection**，演示注入发生在生命周期的哪个阶段、由哪些扩展点参与（包含 `InstantiationAwareBeanPostProcessor#postProcessProperties` 等），并对照解释 `AutowiredAnnotationBeanPostProcessor` 的角色
  - Proxying Phase Lab：演示一个最小的“auto-proxying”模式（`postProcessAfterInitialization` 返回代理/包装对象），并用断言复现：
    - 容器最终暴露的 bean 可能不是“原始对象”
    - 为什么类型暴露（interface vs class）会影响注入/获取
    - 为什么 self-invocation 会绕过代理（与 AOP/Tx 同源）
- 为每个新增 Lab 增加一章中文 `spring-core-beans/docs/`（1:1 对应），并在文档中显式把现象映射到：
  - `spring-core-aop`（自调用/代理类型）
  - `spring-core-tx`（事务也是拦截器链/代理入口）
- 更新 `spring-core-beans/README.md`：补齐新增章节的阅读顺序 + “概念 → Lab/Test → 代码”导航

## Impact
- Affected spec:
  - `openspec/specs/spring-core-beans-module/spec.md`（新增/扩展对 injection/proxying 的学习要求）
- Affected code/docs (apply stage):
  - `spring-core-beans/src/test/java/.../*LabTest.java`（新增）
  - `spring-core-beans/docs/*.md`（新增章节）
  - `spring-core-beans/README.md`（索引更新）

## Out of Scope
- 不新增 Maven 模块（内容聚合在 `spring-core-beans`）
- 不引入外部基础设施依赖（Kafka/Redis/Docker 等）
- 不修改现有 `spring-core-aop` / `spring-core-tx` 的核心实验，只做必要的 cross-link（如需新增 AOP/Tx 的“基础设施 bean 可视化”实验，作为后续独立变更）
