# Change: Add Spring Core Beans merged-BeanDefinition deep-dive and debugging navigation

## Why

`spring-core-beans` 已经通过 Labs + 中文 docs 把“Bean 三层模型”（定义层/实例层/缓存与循环依赖）讲得比较完整，也覆盖了注入阶段（`postProcessProperties`）、代理阶段（BPP wrapping）等关键机制。

但在更深一层的源码阅读/断点调试里，很多学习者会卡在一个“桥接点”：

- **BeanDefinition 的“合并”（merged）到底是什么？为什么我们在 IDE 里经常看到的是 `RootBeanDefinition`？**
- `getMergedLocalBeanDefinition(...)` / `MergedBeanDefinitionPostProcessor` 这条链路在容器时间线上出现在哪里？
- 为什么 `@Autowired` / `@PostConstruct` / init-method 这些“元数据”看起来像是在“定义层”就已经准备好了？它们是在哪个阶段被解析/缓存的？

当前模块缺少一个专门的、可断言可观察的实验，把“定义层（BeanDefinition）→ 合并后的 RootBeanDefinition → 注入/生命周期元数据准备”这条线打通。

另外，从实战定位角度，学习者在遇到异常时（DI 找不到 bean、循环依赖、启动阶段批量创建失败），需要一个“**异常 → 最有效断点入口**”的快速导航，以缩短从报错到定位机制的路径。

## What Changes

- 新增 1 个默认启用的 Lab（`*LabTest`），专门讲 BeanDefinition 合并与 merged metadata 处理：
  - 展示 parent/child `BeanDefinition` 合并后的 `RootBeanDefinition`（属性值、init/destroy 等元数据）
  - 在最关键的入口点提供断点抓手：`getMergedLocalBeanDefinition(...)`、`applyMergedBeanDefinitionPostProcessors(...)`、`MergedBeanDefinitionPostProcessor#postProcessMergedBeanDefinition(...)`
  - 用一个最小的 `MergedBeanDefinitionPostProcessor`（自定义 probe）把“调用时机”和“合并后的定义长什么样”变得可观察、可断言
- 新增 1 章中文 deep-dive 文档（`spring-core-beans/docs/`）与该 Lab 1:1 对应：
  - 解释 merged 的语义、为什么需要 merged、它与注入/生命周期元数据准备的关系
  - 给出推荐断点与观察点清单（和 `docs/00` 的深挖路线一致）
- 在 `docs/11`（调试与自检）补充一个“异常 → 断点入口”对照表：
  - `UnsatisfiedDependencyException` / `NoSuchBeanDefinitionException` / `BeanCurrentlyInCreationException`（至少覆盖这三个）
  - 每个异常映射到 1–3 个最有效的断点入口（例如 `doResolveDependency` / `getSingleton` / `preInstantiateSingletons`）
  - 关联到对应章节与 Lab，做到“从报错能秒跳到实验”
- 统一 `spring-core-beans/docs/*.md` 每章末尾增加 1–2 行固定 footer：
  - `对应 Lab/Test：...`
  - `推荐断点：...`
  让文档从“文章集合”变成“闯关路线”，复习时可以快速回到可运行实验
- 增加一个“bean graph 调试小工具/小测试”（优先以 test-only helper + Lab 的形式落地）：
  - 打印候选集合、最终注入谁、以及一条可读的依赖链（足够用于学习/定位）
  - 与 `docs/11` 的自检流程对齐（不追求通用/完整依赖图工具）

## Impact

- Affected spec:
  - `spring-core-beans-module`（新增 merged BeanDefinition + debugging navigation 的学习要求）
- Affected code/docs (apply stage):
  - `spring-core-beans/src/test/java/.../*LabTest.java`（新增 2 个 Labs：merged BD + bean graph debugging）
  - `spring-core-beans/src/test/java/...`（新增 1 个 test-only helper，用于打印/格式化 bean graph 关键信息）
  - `spring-core-beans/docs/*.md`（新增 merged BD 章节、更新 docs/11、为所有章节追加 footer）
  - `spring-core-beans/README.md`（更新阅读顺序、Labs 索引与概念地图）

## Out of Scope

- 引入新的外部依赖或基础设施（保持 `mvn -q test` 低门槛）
- 把调试工具做成通用、可配置的生产级“依赖图导出器”（只做学习/定位所需的最小能力）
- 大规模重写现有文档结构（本次以增量补齐 + 导航增强为主）

## Open Questions

- 新增 merged BD 章节的编号与插入位置：优先采用 `35-*` 并保持 `90/99` 不变；是否接受？
- “每章 footer”是否包含 `docs/00`、`docs/90`、`docs/99`？（默认：全部覆盖）
- bean graph 输出更偏“文本树”（易读）还是“表格”（易扫描）？（默认：文本树 + 关键集合用逗号列表）
