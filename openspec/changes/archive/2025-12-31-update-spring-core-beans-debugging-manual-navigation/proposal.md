# Change: Update `spring-core-beans` docs with a “debugging manual” block (call chain + watch list + counterexample) and expand exception navigation

## Why

`spring-core-beans/docs` 已经有了较完整的“机制章”体系，并且（`12`–`34` 章）也有统一的“源码锚点 + 断点闭环 + 排障分流”模板。
但在真实调试里，学习者仍会卡在两个缺口：

1) `03/19/35` 这条主线（DI 解析、依赖关系表、BeanDefinition 合并）目前缺少“最短可跟的调用链 + 固定观察点（变量/容器结构）+ 典型反例”的调试手册式表达。  
   结果是：即使知道要在 `doResolveDependency` / `registerDependentBean` / `getMergedLocalBeanDefinition` 下断点，也很难在 3–5 分钟内收敛到“关键分支/关键变量”。

2) `docs/11` 已经有“异常 → 断点入口”表，但覆盖面仍偏窄，并且不是每条异常都给出一个可直接跑的最小 Lab/Test 入口。  
   结果是：报错后仍需要在仓库里搜用例，无法做到“报错即导航”。

本变更的目标是把这两处缺口补齐，让学习体验更像“调试手册 + 闯关路线”：

- 看到异常/症状 → 直接跳到对应章节 → 用最小 Lab/Test 复现 → 在固定断点 + watch list 下收敛结论

## What Changes

- 对以下 3 个章节引入统一的“调试手册块（call chain + watch list + 反例）”：
  - `spring-core-beans/docs/03-dependency-injection-resolution.md`
  - `spring-core-beans/docs/19-depends-on.md`
  - `spring-core-beans/docs/35-merged-bean-definition.md`
  每章补齐：
  - **源码最短路径（call chain）**：从“入口”到“关键分支”的最小栈路径（更像调试手册）
  - **固定观察点（watch list）**：推荐在 debugger 里 watch/evaluate 的变量与容器内部结构
  - **反例（counterexample）**：一个最小复现的误区/坑，并告诉你该在 watch list 里看到什么来纠错

- 扩充 `spring-core-beans/docs/11-debugging-and-observability.md` 的“异常 → 断点入口”表：
  - 新增：`NoUniqueBeanDefinitionException` / `BeanCreationException` / `BeanDefinitionStoreException`
  - 并要求表中 **每一条异常** 都提供一个“最小可跑 Lab/Test”入口（尽量精确到测试方法）

- 为缺少最小复现入口的异常新增或补齐对应 Lab/Test：
  - `BeanDefinitionStoreException`：新增一个可控、可复现的实验（优先使用 `XmlBeanDefinitionReader` + in-memory XML/Resource，避免受 classpath 变化影响）
  - `UnsatisfiedDependencyException`：补一个最小注入失败用例，保证表格每行都有“可跑入口”

## Scope

In-scope：

- 文档：`docs/03`、`docs/19`、`docs/35` 的“调试手册块”增量补齐
- 文档：`docs/11` 异常导航表扩充与“最小可跑入口”补齐
- 测试：只为“异常导航表”补齐缺失的最小复现 Lab/Test（不做通用工具）

Out-of-scope：

- 全量重写 `docs/03/19/35` 的现有叙事结构（以增量补齐为主）
- 把异常表做成覆盖所有 Spring 异常的大而全词典
- 引入新的生产级依赖图/可视化工具（学习定位用保持 test-only + 最小能力）

## Impact

- Affected spec:
  - `spring-core-beans-module`
- Affected docs (apply stage):
  - `spring-core-beans/docs/03-dependency-injection-resolution.md`
  - `spring-core-beans/docs/19-depends-on.md`
  - `spring-core-beans/docs/35-merged-bean-definition.md`
  - `spring-core-beans/docs/11-debugging-and-observability.md`
- Affected tests (apply stage):
  - 新增或补齐少量 `*LabTest` / test method，用于异常最小复现

## Defaults / Decisions

- 章节末尾 footer（`对应 Lab/Test` + `推荐断点`）保持现状不变
- “调试手册块”采用固定小标题（便于全文检索与章节间复用）

