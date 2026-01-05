# spring-core-beans

## Purpose

讲透 Spring Framework IoC 容器与 Bean：从定义注册 → 注入解析 → 生命周期 → 扩展点 → 代理/循环依赖边界，做到“能解释、能断点、能定位问题”。

## Module Overview

- **Responsibility:** 提供 Bean 机制的系统文档与可运行 Labs/Exercises，用于建立源码级心智模型与排障能力。
- **Docs Reading:** 推荐从 `spring-core-beans/docs/README.md` 开始（书本目录 + Part 划分）；主线可按 Part 顺读，每章顶部提供“上一章｜目录｜下一章”导航，降低章节切换成本。
- **Highlights:** 在补齐类型转换/泛型匹配章节与 Labs 闭环的基础上，进一步统一 docs 的“上一章｜目录｜下一章”导航与“复现入口（可运行）”块；新增 JSR-330 `@Inject`/`Provider<T>` 对照 Lab，并增强 testsupport dumper 让排障输出更结构化；补齐 3 类易翻车边界机制 Labs（编程式注册差异 / allowRawInjectionDespiteWrapping / prototype 销毁语义），并将入口落位到 docs/04、docs/05、docs/16、docs/25。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-05

## Source Layout（与 docs Part 对齐）

为保证“像书本一样”的可发现性与可复现性，`spring-core-beans` 的源码与测试代码按 docs 的 Part 结构分组：

- `spring-core-beans/docs/part-01-ioc-container/**` ⇔ `src/main/java/.../part01_ioc_container/**` + `src/test/java/.../part01_ioc_container/**`
- `spring-core-beans/docs/part-02-boot-autoconfig/**` ⇔ `src/test/java/.../part02_boot_autoconfig/**`
- `spring-core-beans/docs/part-03-container-internals/**` ⇔ `src/test/java/.../part03_container_internals/**`
- `spring-core-beans/docs/part-04-wiring-and-boundaries/**` ⇔ `src/test/java/.../part04_wiring_and_boundaries/**`
- `spring-core-beans/docs/appendix/**` ⇔ `src/test/java/.../appendix/**`
- 跨 Part 的测试支撑：`src/test/java/.../testsupport/**`

约束（必须遵守）：

- 必须保留 `com.learning.springboot.springcorebeans.SpringCoreBeansApplication` 的包名不变（便于 Spring Boot 测试向上包查找 `@SpringBootConfiguration`）。

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

#### Scenario: 能把 post-processor 的“顺序与时机”讲成源码算法（Ordering + programmatic 注册）
- 能用 `PostProcessorRegistrationDelegate` 的两段算法解释：为什么 BFPP/BDRPP 更早、为什么 BPP 注册发生在 refresh 中前段、以及顺序如何由“三段分组 + comparator”决定
- 能解释 `addBeanPostProcessor` 的 list 语义：为什么它绕过容器排序、为什么执行顺序 = 注册顺序、以及“BPP 不会 retroactive”的时机陷阱
- 对应可复现闭环入口：
  - `spring-core-beans/docs/part-03-container-internals/14-post-processor-ordering.md`
  - `spring-core-beans/docs/part-04-wiring-and-boundaries/25-programmatic-bpp-registration.md`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansPostProcessorOrderingLabTest.java`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansProgrammaticBeanPostProcessorLabTest.java`

## Dependencies

- 无跨模块硬依赖（该模块是 Spring Core 学习底座）

## Change History

- [202601010649_spring-core-beans-deep-dive](../../history/2026-01/202601010649_spring-core-beans-deep-dive/) - ✅ 已执行：深化 DI/生命周期/PostProcessor/循环依赖/@Configuration/FactoryBean，并补齐坑点与自测题的闭环指引
- [202601010845_beans-aop-deep-dive-v2](../../history/2026-01/202601010845_beans-aop-deep-dive-v2/) - ✅ 已执行：在 BPP/代理/顺序章节补齐 AutoProxyCreator 承接，并补齐与 AOP 模块的多代理叠加闭环链接
- [202601020725_enhance_spring_core_fundamentals](../../history/2026-01/202601020725_enhance_spring_core_fundamentals/) - ✅ 已执行：把“新增面试点”嵌入正文对应小节，并补齐可断言复现入口（BeanFactory vs ApplicationContext/Aware/泛型匹配坑/CGLIB 对照）
- [202601020934_spring_core_beans_learning_route](../../history/2026-01/202601020934_spring_core_beans_learning_route/) - ✅ 已执行：补齐 README 学习路线与 Start Here（含 refresh 主线一页纸/运行态观察点），并新增注入歧义 Lab + 对应 Exercise
- [202601021002_spring_core_beans_auto_config_ordering](../../history/2026-01/202601021002_spring_core_beans_auto_config_ordering/) - ✅ 已执行：补齐 matchIfMissing（三态）与自动配置顺序依赖（after/before）Lab，并把面试点落到 docs/10 与 docs/11 的正文入口
- [202601021023_spring_core_beans_auto_config_exercises](../../history/2026-01/202601021023_spring_core_beans_auto_config_exercises/) - ✅ 已执行：深化 Boot 自动装配 Exercises（matchIfMissing 三态 / 顺序确定化 / 条件报告 helper），并在 docs/10 条件正文补齐 `@ConditionalOnBean` 顺序/时机差异小节
- [202601021041_spring_core_beans_auto_config_backoff_debug](../../history/2026-01/202601021041_spring_core_beans_auto_config_backoff_debug/) - ✅ 已执行：补齐 auto-config back-off/覆盖“为何没生效”的时机差异 Lab（early/late registrar 对照），并在 docs/10 的“覆盖”章节补齐排障闭环入口
- [202601021144_spring_core_beans_auto_config_mainline_debug](../../history/2026-01/202601021144_spring_core_beans_auto_config_mainline_debug/) - ✅ 已执行：补齐 Boot 自动装配主线（import/排序/条件可断言）与排障可观察性（BeanDefinition 来源追踪 Dumper + 覆盖/back-off 场景矩阵 Lab），并同步 docs/10 与模块 README 入口
- [202601030641_spring-core-beans-first-pass](../../history/2026-01/202601030641_spring-core-beans-first-pass/) - 🚫 已撤回：原计划新增的 First Pass 闭环文档已按反馈删除，仅保留方案包作为学习清单归档
- [202601031327_first-pass-content-merge-into-existing-docs](../../history/2026-01/202601031327_first-pass-content-merge-into-existing-docs/) - ✅ 已执行：把 First Pass 的“10 个最小实验入口”融入 docs/00 与 docs/99（不新增独立文件）
- [202601030652_spring-core-beans-source-deep-dive](../../history/2026-01/202601030652_spring-core-beans-source-deep-dive/) - ✅ 已执行：在 docs/01、02、03、05、09 补齐 Spring 源码解析（refresh 主线/注册入口/依赖解析/生命周期/循环依赖），并用仓库 src 最小片段辅助理解
- [202601030731_spring-core-beans-post-processors-bootstrap-source-deepening](../../history/2026-01/202601030731_spring-core-beans-post-processors-bootstrap-source-deepening/) - ✅ 已执行：深化 docs/06 与 docs/12 的源码解析（PostProcessorRegistrationDelegate 算法/annotation processors bootstrap），并新增 “static @Bean BFPP” 最小可运行 Lab
- [202601030752_spring-core-beans-ordering-programmatic-bpp-deepening](../../history/2026-01/202601030752_spring-core-beans-ordering-programmatic-bpp-deepening/) - ✅ 已执行：把 docs/14 与 docs/25 补成“算法级 + 可复现”版本（排序器规则/分段执行/手工 addBeanPostProcessor 的 list 语义与时机陷阱），并增强 ordering Lab 覆盖 order 数值与 @Order 反例
- [202601031508_spring-core-beans-docs-coherence](../../history/2026-01/202601031508_spring-core-beans-docs-coherence/) - ✅ 已执行：优化 docs/01-03 连贯性（本章定位/主线 vs 深挖/下一章预告），让 01→02→03 主线阅读更顺畅且不丢知识点
- [202601032012_spring-core-beans-bookify-docs](../../history/2026-01/202601032012_spring-core-beans-bookify-docs/) - ✅ 已执行：docs 书本化（目录页 + Part 结构 + 全章 A–G 契约 + 上下章导航），并全局修复 docs 内链与模块 README 入口
- [202601032124_spring-core-beans-src-part-grouping](../../history/2026-01/202601032124_spring-core-beans-src-part-grouping/) - ✅ 已执行：src/main 与 src/test 按 docs Part 分组（分包 + testsupport），并同步修复 docs/README/知识库中的源码路径引用
- [202601041013_spring-core-beans-src-part-naming](../../history/2026-01/202601041013_spring-core-beans-src-part-naming/) - ✅ 已执行：将 src 分组目录命名语义化（partXX → partXX_<topic>），进一步对齐 docs Part 的具名章节域
- [202601051050_spring_core_beans_deepen](../../history/2026-01/202601051050_spring_core_beans_deepen/) - ✅ 已执行：补齐 docs 目录页索引与跳读地图，新增类型转换/泛型匹配章节，并新增 component-scan/profile/optional injection/type conversion Labs 形成可复现实验闭环
- [202601051252_spring_core_beans_finish_all_tasks](../../history/2026-01/202601051252_spring_core_beans_finish_all_tasks/) - ✅ 已执行：统一 docs 全章导航与复现入口块，补齐 JSR-330 注入对照 Lab，并增强 testsupport dump 工具提升可观察性
- [202601051339_spring_core_beans_edge_case_labs](../../history/2026-01/202601051339_spring_core_beans_edge_case_labs/) - ✅ 已执行：补齐编程式注册差异 / raw injection despite wrapping / prototype 销毁语义三类边界机制，并同步 docs 入口与断点锚点
