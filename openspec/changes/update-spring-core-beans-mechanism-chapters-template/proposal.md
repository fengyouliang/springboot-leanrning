# Change: Update Spring Core Beans mechanism deep-dive chapters with a heavy “source anchors + breakpoint loop” template

## Why

`spring-core-beans/docs` 已经覆盖了大量 IoC/Bean 的关键机制，并且每章都有对应的 Lab/Test 作为“可运行、可断言”的闭环入口。

但当学习者进入“机制深挖”阶段（开始需要对齐源码、用断点建立阶段感）时，目前文档存在一个一致性缺口：

- 只有少数章节提供了明确的“断点路线/阶段感”指导（例如 `docs/30`），而多数机制章仍然主要停留在“现象 + 解释”的文字层面
- 章节间缺乏统一的**源码锚点**与**排障分流（定义层 vs 实例层）**结构，导致学习者遇到问题时难以快速定位“该去哪一层、在哪些类/方法下断点”

本变更的目标是把机制章统一升级到同一种“可追踪的学习体验”：每章都能提供稳定的源码锚点与可执行的断点闭环步骤。

## What Changes

仅针对“机制深潜章”（不触碰基础概念章）引入**重度模板**，在每章补齐 3 类固定内容：

1) **源码锚点（Key classes/methods）**
   - 每章提供至少 3–5 个“可跳转/可下断点”的 Spring 关键类/方法锚点
   - 以方法级别为主（例如 `AbstractApplicationContext#refresh`、`AbstractAutowireCapableBeanFactory#doCreateBean`）

2) **断点闭环（Breakpoint loop with Lab/Test）**
   - 每章至少指向 1 个本仓库现有的 `*LabTest`（或更聚焦的单测方法）作为可运行入口
   - 给出推荐断点清单与观察点，使学习者能在 30 分钟内闭环验证本章结论

3) **排障分流：定义层 vs 实例层**
   - 每章用一个小的分流提示，回答“出现某类症状时应优先检查定义层还是实例层”
   - 引导读者回到对应的章节/测试入口，而不是只靠猜和日志碰运气

为减少侵入性与保持现有写作风格，本变更采取“增量补齐”的方式：

- 保留每章现有的“现象/机制/常见坑/自检”结构
- 在章末（或常见坑之前）追加统一的模板段落（章节标题与术语保持一致，方便全文检索）

## Scope

仅覆盖 `spring-core-beans/docs` 中的“机制深潜章”，定义为：

- `12` 到 `34` 号章节（`spring-core-beans/docs/12-*.md` … `spring-core-beans/docs/34-*.md`）
- 不包含基础概念章（`01-11`）
- 不包含清单/自测类章节（`90-*`、`99-*`）

## Impact

- Affected spec:
  - `spring-core-beans-module`（补充机制章文档模板化要求）
- Affected docs (apply stage):
  - `spring-core-beans/docs/12-*.md` … `spring-core-beans/docs/34-*.md`
- No code changes:
  - 不新增/修改 Lab 代码与示例代码（本次只做文档结构与导航增强）

## Out of Scope

- 将基础概念章（`01-11`）整体重写或模板化
- 新增/调整 `*LabTest`（本变更不引入新的机制实验）
- 引入 Spring 源码引用的大段贴码（只提供“锚点与断点建议”，避免文档膨胀）

