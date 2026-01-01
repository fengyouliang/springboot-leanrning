# Change: Deepen `spring-core-beans` docs/11 + docs/19 into a “source-level closure” playbook (and add dependsOn closure Labs)

## Why

`spring-core-beans` 的文档与 Labs 已经基本满足“能跑、能断言、能用断点跟”的学习体验，尤其 `docs/11`（异常导航）与 `docs/19`（dependsOn + 依赖关系表）已经很接近“调试手册”的表达。

但对 **B 路线（有经验、补内功）** 的读者来说，仍然存在几个高频卡点：

1) **缺少统一的“观测对象地图”**  
   读者知道要打 `doResolveDependency` / `registerDependentBean` 等断点，但不知道“这一类问题到底应该看哪一种对象/哪一种容器内部结构”，导致调试靠猜、靠日志、靠碰运气。

2) **“为什么它是代理？”缺少闭环打法**  
   目前 `docs/11` 提到了 proxy 现象，但还缺少一套稳定的“判定 → 追踪代理产生点 → 定位具体 BPP”的闭环步骤，无法把代理问题从玄学变成可复现、可验证的流程。

3) **`dependsOn` 的两个高级交互点缺少“可断言的闭环”**  
   - `dependsOn` vs `@Lazy`：很多人仍会误以为 lazy-init 一定不会在 refresh 时实例化  
   - 销毁顺序：知道“初始化顺序和销毁顺序相反”，但缺少最小可跑实验固化

本变更把 `docs/11` 与 `docs/19` 进一步“工程化”：把它们从“讲得对”升级为“**按步骤做就能用源码/断点解释并复现**”。

## What Changes

- 更新 `spring-core-beans/docs/11-debugging-and-observability.md`：
  - 增加一个“观测对象总览”小节：把容器调试抽象成 5 类对象（`BeanDefinition` / merged BD / 实例与代理 / 依赖图 / 单例缓存），并为每类给出最小断点入口 + watch list。
  - 补齐“代理定位闭环”：从“怎么判定是 proxy”到“在哪个阶段被替换”再到“哪个 BPP 做的”。
  - 将现有线性自检流程升级为“排障决策树”，让读者能先分流再下断点。
  - 扩充异常导航表：新增对 `Circular depends-on relationship`（dependsOn 拓扑环）的专门行，并关联最小可跑用例。
  - 增补 Boot 条件报告的“数据化”用法（不只停留在 `--debug` 日志技巧）：给出在 `ApplicationContextRunner` 场景下读取 `ConditionEvaluationReport` 的建议路径。
  - 增加一组“高收益条件断点模板”（降噪策略固化成可复制片段）。

- 更新 `spring-core-beans/docs/19-depends-on.md`：
  - 增加 `dependsOn` vs `@Lazy` 的交互小节：写死结论 + 给出最小复现入口。
  - 补一段“为什么 dependsOn 不影响 DI 选择”的机制解释（发生阶段不同：`doGetBean` vs `doResolveDependency`）。
  - 增加“写入时机对照”：`@Component`/扫描 vs `@Bean`/配置解析 vs 编程式注册，分别在何时写入 `BeanDefinition`。
  - 将“销毁顺序”从概念升级为可断言闭环（引用新增 Lab/Test），并强化与 `docs/11` 的互链。

- 新增/补齐最小闭环 Labs（默认启用，`mvn -q -pl spring-core-beans test` 全绿）：
  - 在 `SpringCoreBeansDependsOnLabTest` 增加 2 个可断言用例：
    - `dependsOn_triggersLazyDependencyInstantiation()`
    - `dependsOn_affectsDestroyOrder_viaDependentBeanMap()`
  - 新增一个“创建链路相位追踪”Lab（命名建议：`SpringCoreBeansBeanCreationTraceLabTest`）：用 test-only BPP/InstantiationAwareBPP 记录实例化/注入/初始化/代理替换的关键阶段，为 `docs/11` 的“代理定位闭环”提供可跑入口。
  - （如需要）在 Boot 场景补一个最小 Lab：演示如何在测试中读取 `ConditionEvaluationReport` 并输出少量 `OBSERVE:` 行（不对日志做断言）。

## Scope

In-scope:

- 仅聚焦 `spring-core-beans` 模块
- 文档改动限定在：
  - `spring-core-beans/docs/11-debugging-and-observability.md`
  - `spring-core-beans/docs/19-depends-on.md`
- 新增/修改的代码仅限 test 侧（`src/test/java/.../*LabTest.java`），且默认启用必须全绿

Out-of-scope:

- 重写 `docs/11` / `docs/19` 的整体叙事结构（以增量追加为主）
- 引入生产级依赖图可视化/导出工具（保持 learning + test-only）
- 扩展为覆盖所有 Spring 异常的大而全词典
- 修改业务/生产代码（只做学习实验与文档）

## Impact

- Affected spec:
  - `spring-core-beans-module`
- Affected docs (apply stage):
  - `spring-core-beans/docs/11-debugging-and-observability.md`
  - `spring-core-beans/docs/19-depends-on.md`
- Affected tests (apply stage):
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansDependsOnLabTest.java`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansBeanCreationTraceLabTest.java` (new)
  - (Optional) Boot condition report lab test (new or extend existing lab)

## Defaults / Decisions

- 文档遵循本仓库既有原则：短文 + 可跑入口 + 断点闭环；避免大段贴源码
- Labs 以 “小容器优先” 为默认：
  - Spring Core 机制：优先 `AnnotationConfigApplicationContext` / `GenericApplicationContext`
  - Boot 条件装配：优先 `ApplicationContextRunner`
- 测试以断言固化行为为主，`OBSERVE:` 输出只做辅助观察，不把日志当断言

## Open Questions

1) `SpringCoreBeansBeanCreationTraceLabTest` 是否需要覆盖“代理替换（after initialization）”的可断言结果？  
   - A（默认）：覆盖（更贴近 `docs/11` 的“代理定位闭环”）  
   - B：只做“阶段时间线”记录，不做 proxy 替换（更小，但闭环弱）

2) Boot 条件报告的最小 Lab 是否独立成一个 `*LabTest`，还是扩展现有 `SpringCoreBeansAutoConfigurationLabTest`？  
   - A：独立（更聚焦，便于索引）  
   - B：扩展现有（更少文件，但主题混杂）

