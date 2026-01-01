# Design: 把 `docs/11` + `docs/19` 做成“源码级闭环手册”（并用最小 Labs 固化关键交互）

## Context

当前 `spring-core-beans` 已有：

- `docs/11`：异常 → 断点入口 → Lab/Test 的导航表（偏“入口导航”）
- `docs/19`：dependsOn 语义、依赖关系表、销毁顺序，以及 call chain / watch list / counterexample（偏“机制解释 + 调试锚点”）
- `SpringCoreBeansDependsOnLabTest`：初始化顺序与 dependsOn 拓扑环（2 个用例）

对 B 路线读者而言，仍缺少把这些内容“工程化”的两件事：

1) 把调试问题抽象成“我应该观测哪一类对象/数据结构”  
2) 把高频误判（proxy、lazy、dependsOn 环、销毁顺序）固化成可断言的最小复现

## Goals / Non-Goals

### Goals

- `docs/11` 能做到：从症状/异常出发，**先分流，再落到具体断点与 watch list**  
  并且能解释“为什么这个观察点能回答这个问题”。
- `docs/11` 能做到：对 “为什么它是 proxy” 给出可执行闭环（判定 → 追踪替换点 → 定位 BPP）。
- `docs/19` 能做到：补齐 `dependsOn` 的两个高级交互点：
  - `dependsOn` 会强行拉起 lazy dependency（发生在创建前置阶段）
  - 销毁顺序严格按依赖边反序（可断言、可断点验证）
- 通过最小 Labs 把上述交互点固化为稳定结论（不依赖长日志，不引入新依赖）。

### Non-Goals

- 不做全量 “Spring 调试百科” 或全异常覆盖
- 不引入生产级依赖图可视化/导出工具（学习定位保持 test-only）
- 不重写 `docs/11` / `docs/19` 既有结构（以增量追加/增强为主）

## Decisions

### Decision 1: “观测对象总览”固定为 5 类对象 + 每类 1 个最小入口断点

在 `docs/11` 引入一个固定地图：把容器调试抽象成 5 类对象，并为每类给出最小断点入口与 watch list。

5 类对象（建议顺序）：

1) `BeanDefinition`（原始定义）
2) merged `RootBeanDefinition`（最终配方）
3) 实例与 proxy（最终暴露对象）
4) 依赖图（`dependentBeanMap` / `dependenciesForBeanMap`）
5) 单例缓存（三层缓存，用于循环依赖/early reference）

每类至少提供：

- “它回答的问题”
- 1 个推荐断点入口（`Class#method`）
- 3–6 个固定 watch 项（局部变量 + 容器结构）

**原因**：B 路线读者往往不是缺断点，而是缺“看什么”。

### Decision 2: “代理定位闭环”以 `initializeBean -> applyBeanPostProcessorsAfterInitialization` 为中心落点

`docs/11` 的 proxy 闭环采用三步：

1) 判定：运行时 class 与接口暴露（JDK vs CGLIB 的最小识别法）
2) 追踪：代理/包装最常见发生在 `AbstractAutowireCapableBeanFactory#initializeBean` 的 after-init 链路
3) 定位：在 `applyBeanPostProcessorsAfterInitialization` 的循环中锁定哪个 `BeanPostProcessor` 替换了对象

**原因**：对学习者来说，“谁把对象换掉了”比“代理是什么”更能直接解决问题。

### Decision 3: dependsOn × @Lazy 用 programmatic registration 做稳定复现

在 `SpringCoreBeansDependsOnLabTest` 增加用例时，采用：

- `AnnotationConfigApplicationContext`
- programmatic registration（`context.registerBean(..., bd -> ...)`）

实现策略（apply stage）：

- dependency bean：`bd.setLazyInit(true)`
- dependent bean：`bd.setDependsOn("dependency")`
- 断言：refresh 期间依然会实例化 dependency（因为创建 dependent 前会先 `getBean(dep)`）

**原因**：不用扫描/注解，场景更小、更稳定、更适合断点。

### Decision 4: 销毁顺序用 `DisposableBean` 记录，避免依赖注解基础设施

销毁顺序用例采用 `DisposableBean#destroy()` 记录事件，断言 close 时：

- 先销毁 dependent
- 再销毁 dependency

并建议在断点里观察 `DefaultSingletonBeanRegistry#dependentBeanMap`。

**原因**：`DisposableBean` 不依赖额外 BPP，比 `@PreDestroy` 更稳定、噪音更少。

### Decision 5: Boot 条件报告以 “可查询数据结构” 表达（可选 Lab）

`docs/11` 的条件报告部分不只讲 `--debug`，而强调：

- 条件评估结果是 `ConditionEvaluationReport`（可在测试中读取）
- `ApplicationContextRunner` 是最小可控入口

是否新增 Lab 取决于实现复杂度与维护成本；若新增，保持为最小断言 + 少量 `OBSERVE:`。

## Risks / Trade-offs

- 断点/内部结构名在 Spring 小版本可能变动  
  → 规避：断言只固化稳定行为，不对内部集合大小/命中次数做脆弱断言；文档锚点以主干稳定点为主（`doGetBean`、`doResolveDependency`、`registerDependentBean`）。
- `docs/11` 若增加过多内容可能变长  
  → 规避：新增内容以“地图 + 决策树 + 闭环步骤”为主，避免展开成大段解释。

## Migration Plan

Apply stage（实现阶段）按 tasks.md 顺序：

1) 先补齐 dependsOn 的 2 个新 Lab（最小可断言闭环）
2) 再补 `BeanCreationTrace` Lab（支撑 proxy 闭环）
3) 最后更新 `docs/11` 与 `docs/19` 的新增段落与互链
4) 跑 `mvn -q -pl spring-core-beans test` 与 `mvn -q test` 保证全绿

## Open Questions

- `BeanCreationTrace` Lab 是否需要强制包含 proxy 替换断言（更贴近目标，但实现略复杂）？
- Boot 条件报告 Lab 是否值得新增独立文件（更清晰），还是复用现有 auto-config lab（更少文件）？

