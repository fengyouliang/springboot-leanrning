# Change: Add Spring Core Beans injection-annotations labs

## Why

`spring-core-beans` 已经覆盖了大量 IoC/Bean 的核心机制（DI 解析、scope、生命周期、BFPP/BPP、循环依赖、early reference、proxying、Boot auto-configuration 等），并且有较完整的中文 deep-dive 文档与默认启用的 Labs。

但从“初学者/进阶学习者最常踩坑”的角度看，目前仍缺少几个非常高频、且能显著提升心智模型完整度的点：

- `@Resource` 注入的 **默认按名称（name）优先** 的语义，以及它与 `CommonAnnotationBeanPostProcessor` 的关系（为什么“没注册处理器就不生效”）
- 单依赖注入（single injection）里，候选冲突时的 **选择规则**：`@Primary`、`@Priority` 与 beanName 默认候选之间的关系；并澄清 `@Order` 主要影响的是 **集合注入顺序**，而不是“单 bean 选择”
- `@Value("${...}")` 的占位符解析：默认容器的 embedded value resolver 的行为（非严格），以及通过显式注册 `PropertySourcesPlaceholderConfigurer` 如何把语义变成“严格/缺失即失败”

这些点如果只有文字解释，学习者很难建立“从现象 → 机制 → 可复现 → 可断言”的闭环；因此需要补充 **默认启用的 `*LabTest`** 与 **对应的中文章节文档**，并在 `README.md` 上增加更“可跟”的概念导航。

## What Changes

- 新增 3 个默认启用的 Labs（`*LabTest`），每个 Lab 聚焦一个机制点，全部可运行、可断言、可观察（少量 `OBSERVE:` 输出，但不依赖长日志做断言）：
  - `@Resource` name-based injection
  - autowire candidate selection：`@Primary` vs `@Priority` vs `@Order`
  - `@Value` placeholder resolution：默认 resolver vs `PropertySourcesPlaceholderConfigurer`
- 为每个新增 Lab 增加一章中文 `spring-core-beans/docs/*.md`（1:1 对应），包含：实验入口、预期现象、机制解释、调试建议、常见坑、与其他模块的交叉链接。
- 更新 `spring-core-beans/README.md`：
  - 把新章节纳入推荐阅读顺序
  - 在 Labs 索引表加入新 Lab
  - 增补一个“按容器阶段/注入机制划分的概念地图”（让学习路线更可跟）

## Impact

- Affected spec:
  - `spring-core-beans-module`（新增注入注解/占位符解析相关要求）
- Affected code (apply stage):
  - `spring-core-beans/src/test/java/.../*LabTest.java`
  - `spring-core-beans/docs/*.md`
  - `spring-core-beans/README.md`

## Out of Scope

- 新增 Maven 模块或引入外部基础设施依赖
- 把实验升级为 `@SpringBootTest` 大上下文（除非某个机制点无法用小容器表达；默认仍优先 `GenericApplicationContext`/`AnnotationConfigApplicationContext`）
- 重写现有章节结构（本次只做增量补齐与导航增强）

