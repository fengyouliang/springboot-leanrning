# Change: Add “debugging manual” blocks to `spring-core-beans` docs/13 (BDRPP) and docs/25 (programmatic BPP)

## Why

当前 `spring-core-beans/docs` 已经通过“源码锚点 + 断点闭环 + 排障分流”把机制章做成了可运行的学习路径，但在真实断点调试里，学习者仍会在两类场景上反复卡住：

1) **注册阶段的“动态加定义”到底发生在 refresh 的哪一段？**  
   很多人能记住 BDRPP（`BeanDefinitionRegistryPostProcessor`）“更早、更强”，但遇到“我明明注册了/修改了定义，为什么实例阶段结果不符合预期”时，很难用 3–5 分钟从调用栈收敛到关键分支、关键变量。

2) **手工 `addBeanPostProcessor(...)` 为什么会绕过 `Ordered`/排序体系？**  
   docs/25 已解释现象与结论，但还缺少一段“调试手册式”的最短调用链与固定观察点，帮助读者用 debugger 直接看到：
   - 程序化注册发生在 refresh 前
   - 自动发现/排序发生在 `registerBeanPostProcessors`
   - 最终执行顺序来自 `beanFactory.getBeanPostProcessors()`

本变更把 docs/13 与 docs/25 进一步升级为“闯关路线”的同款表达：  
**源码最短路径（call chain）+ 固定观察点（watch list）+ 反例（counterexample）**，让读者从现象到定位机制更快闭环。

## What Changes

- 更新 `spring-core-beans/docs/13-bdrpp-definition-registration.md`：
  - 追加 3 段固定结构：
    - `## 源码最短路径（call chain）`
    - `## 固定观察点（watch list）`
    - `## 反例（counterexample）`
  - 重点把 BDRPP 在 refresh 时间线的精确位置写成“最短可跟栈”：
    - `AbstractApplicationContext#refresh`
    - `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`
    - `BeanDefinitionRegistryPostProcessor#postProcessBeanDefinitionRegistry`
    - `DefaultListableBeanFactory#registerBeanDefinition`
  - watch list 侧重：
    - registry 里“新增/修改”的定义是否真的进入 `beanDefinitionMap` / `beanDefinitionNames`
    - `invokeBeanFactoryPostProcessors` 的分组/排序与 `processedBeans` 的去重语义
  - 反例默认选择（可调整）：**在 BDRPP/BFPP 阶段调用 `getBean()` 触发过早实例化，导致后续 BPP 来不及介入**（见 Open Questions）。

- 更新 `spring-core-beans/docs/25-programmatic-bpp-registration.md`：
  - 同样追加 3 段固定结构（call chain / watch list / counterexample）
  - 把“程序化注册 vs 自动发现+排序”明确拆成两条链路，并给出固定观察点：
    - `ConfigurableListableBeanFactory#addBeanPostProcessor`
    - `PostProcessorRegistrationDelegate#registerBeanPostProcessors`
    - `beanFactory.getBeanPostProcessors()`（最终顺序即执行顺序）
  - 反例复用现有必现用例：程序化注册的多个 BPP **只按注册顺序执行，不按 `Ordered`**。

## Scope

In-scope：

- 仅补齐 docs/13 与 docs/25 的“调试手册块”（call chain / watch list / counterexample）
- 反例必须提供“最小可跑 Lab/Test 入口”
  - docs/25 复用现有 Lab/Test
  - docs/13 如需要新增一个最小复现实验，限制为 **新增一个 test method**（不引入外部依赖，不改生产代码）

Out-of-scope：

- 大规模重写 docs/13 与 docs/25 的既有叙事结构（以增量追加为主）
- 扩展 docs/11 的异常导航表（本变更聚焦章节本身的调试闭环）
- 引入通用化的“定义/依赖图导出工具”（保持学习定位为主，避免膨胀）

## Impact

- Affected spec:
  - `spring-core-beans-module`（补充 docs/13、docs/25 的调试手册要求）
- Affected docs (apply stage):
  - `spring-core-beans/docs/13-bdrpp-definition-registration.md`
  - `spring-core-beans/docs/25-programmatic-bpp-registration.md`
- Affected tests (apply stage):
  - 可能新增：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansRegistryPostProcessorLabTest.java`（仅 1 个最小反例方法；若采用复用型反例则不改）

## Defaults / Decisions

- 保留 docs/13、docs/25 现有结构与既有“三段模板标题”（源码锚点/断点闭环/排障分流）
- 每章末尾 footer（`对应 Lab/Test` + `推荐断点`）保持现状不变
- “调试手册块”的小标题与既有章节保持一致，便于全文检索与跨章复用

## Open Questions

1) docs/13 的反例你更偏好哪一种？
   - A（默认建议）：**在 BDRPP/BFPP 阶段 `getBean()` 触发过早实例化，导致后续 BPP 不生效/顺序反直觉**  
     - 优点：与“注册阶段”强相关，且能把 `docs/14`、`docs/25` 的“时机/顺序”串起来
     - 代价：可能需要新增 1 个 test method 做稳定复现
   - B：**动态注册 beanName 冲突/覆盖策略**（反例入口可复用 [24](../../spring-core-beans/docs/24-bean-definition-overriding.md) 的 Lab）  
     - 优点：无需新增测试
     - 代价：与 BDRPP 的独特机制关联稍弱（更像“注册通用坑”）

