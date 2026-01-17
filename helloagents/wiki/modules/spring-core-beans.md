# spring-core-beans

## Purpose

讲透 Spring Framework IoC 容器与 Bean：从定义注册 → 注入解析 → 生命周期 → 扩展点 → 代理/循环依赖边界，做到“能解释、能断点、能定位问题”。

## Module Overview

- **Responsibility:** 提供 Bean 机制的系统文档与可运行 Labs/Exercises，用于建立源码级心智模型与排障能力。
- **Docs Reading:** 推荐从 `docs/beans/spring-core-beans/README.md` 开始（书本目录 + Part 划分）；主线可按 Part 顺读，每章顶部提供“上一章｜目录｜下一章”导航，降低章节切换成本。
- **Start Here（30 分钟快启）:** 先跑 3 个最小实验建立容器主线直觉，再进入深潜：`docs/beans/spring-core-beans/part-00-guide/01-quickstart-30min.md`。
- **断点地图（可复用清单）:** `docs/beans/spring-core-beans/part-00-guide/02-breakpoint-map.md`
- **Learning Path（路线图）:** `helloagents/wiki/learning-path.md`（主线：Beans → AOP → Tx → Web MVC）
- **第一个可运行入口（3 分钟开跑）:**
  - `mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansLabTest#usesQualifierToResolveMultipleBeans test`
  - 对应测试类：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part00_guide/SpringCoreBeansLabTest.java`
- **Highlights:** 在补齐类型转换/泛型匹配章节与 Labs 闭环的基础上，进一步统一 docs 的“上一章｜目录｜下一章”导航与“复现入口（可运行）”块；新增 JSR-330 `@Inject`/`Provider<T>` 对照 Lab，并增强 testsupport dumper 让排障输出更结构化；补齐 3 类易翻车边界机制 Labs（编程式注册差异 / allowRawInjectionDespiteWrapping / prototype 销毁语义），并将入口落位到 docs/04、docs/05、docs/16、docs/25；新增 Part 05（AOT/RuntimeHints/XML/容器外对象/SpEL/自定义 Qualifier）与对应 Labs，并新增面试复述模板与生产排障清单用于体系化复盘；同时为 Exercises 补齐对应 Solution（默认参与回归），并在 docs/README 收敛“章节↔Lab↔Exercise↔Solution”对照表与运行建议，补强 ImportSelector 等新手高频卡点的“源码主线/断点/观察点”；进一步补齐 Spring Framework `spring-beans` 体系的 5 组“真实世界常见但容易缺失”的机制闭环（docs 46–50：XML namespace 扩展 / Properties+Groovy Reader / replaced-method 方法注入 / 内置 FactoryBean / PropertyEditor+值解析），并新增对应 Labs（默认参与回归）；补齐 Spring Framework `BeanFactory API` 与 `Environment Abstraction` 两类常用但容易“只会用不会解释”的主题：新增 docs/38–39 与对应可断言 Labs（默认参与回归）；新增 spring-beans Public API 索引（docs Appendix 95/96）用于“按类型检索/可审计”，并补齐 aot.factories/AotServices 与 ServiceLoader*FactoryBean 的闭环，新增 Explore/Debug 用例（docs Appendix 97，显式开关启用，不影响默认回归）；并补齐 `org.springframework.beans.support`（ArgumentConvertingMethodInvoker/ResourceEditorRegistrar/PropertyComparator/PagedListHolder/SortDefinition）闭环，新增可运行 Lab，并将 Appendix 96 Gap 归零。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-14

## Source Layout（与 docs Part 对齐）

为保证“像书本一样”的可发现性与可复现性，`spring-core-beans` 的源码与测试代码按 docs 的 Part 结构分组：

- `docs/beans/spring-core-beans/part-01-ioc-container/**` ⇔ `src/main/java/.../part01_ioc_container/**` + `src/test/java/.../part01_ioc_container/**`
- `docs/beans/spring-core-beans/part-02-boot-autoconfig/**` ⇔ `src/test/java/.../part02_boot_autoconfig/**`
- `docs/beans/spring-core-beans/part-03-container-internals/**` ⇔ `src/test/java/.../part03_container_internals/**`
- `docs/beans/spring-core-beans/part-04-wiring-and-boundaries/**` ⇔ `src/test/java/.../part04_wiring_and_boundaries/**`
- `docs/beans/spring-core-beans/part-05-aot-and-real-world/**` ⇔ `src/test/java/.../part05_aot_and_real_world/**`
- `docs/beans/spring-core-beans/appendix/**` ⇔ `src/test/java/.../appendix/**`
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
- 文档明确候选收集与缩小过程（@Qualifier/@Primary/by-name fallback（依赖名匹配 beanName）/@Priority/名称匹配/集合注入排序）
- 提供 Lab 覆盖：多实现歧义、@Primary、@Qualifier、by-name fallback、泛型收敛、集合注入排序、以及 `ObjectProvider#getIfUnique()` 的可选/多候选语义

#### Scenario: 能把 Environment/PropertySource 放回容器主线解释（含覆盖优先级与时机）
- 能解释 PropertySources 的优先级与“占位符解析”如何接入 BeanFactory 的值解析链路
- 能解释：refresh 前/后修改 Environment 对 Bean 的影响边界（不会 retroactive 影响已创建 bean）
- 对应可复现闭环入口：
  - `docs/beans/spring-core-beans/part-04-wiring-and-boundaries/38-environment-and-propertysource.md`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansEnvironmentPropertySourceLabTest.java`

#### Scenario: 能把 BeanFactory API 当作“最小容器”理解（并解释与 ApplicationContext 的边界）
- 能解释：为什么 plain BeanFactory 不会自动启用注解注入/生命周期（需要显式 BPP），以及 BPP 安装顺序/时机的影响
- 能给出最小可运行路径：`DefaultListableBeanFactory` + 手动注册 annotation processors + `addBeanPostProcessor` 的可断言对照
- 对应可复现闭环入口：
  - `docs/beans/spring-core-beans/part-04-wiring-and-boundaries/39-beanfactory-api-deep-dive.md`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansBeanFactoryApiLabTest.java`

#### Scenario: 能讲清循环依赖“能救/不能救”的边界（含代理介入）
- 文档解释三层缓存与 early reference 的真实语义
- 提供 Lab 覆盖：构造器循环失败、setter 循环可能成功、代理介入导致 early reference 行为变化
- 对应可复现闭环入口：
  - `docs/beans/spring-core-beans/part-01-ioc-container/09-circular-dependencies.md`
  - `docs/beans/spring-core-beans/part-03-container-internals/16-early-reference-and-circular.md`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansCircularDependencyBoundaryLabTest.java`

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
  - `docs/beans/spring-core-beans/part-03-container-internals/14-post-processor-ordering.md`
  - `docs/beans/spring-core-beans/part-04-wiring-and-boundaries/25-programmatic-bpp-registration.md`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansPostProcessorOrderingLabTest.java`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansProgrammaticBeanPostProcessorLabTest.java`

#### Scenario: 能解释 AOT/Native 约束，并把 RuntimeHints 变成可断言结论
- 能说清：AOT/Native 的关键是“构建期契约”，RuntimeHints 用于声明反射/代理/资源需求
- 能用 JVM 单测验证 hints 的存在性（不必构建 native image）
- 对应可复现闭环入口：
  - `docs/beans/spring-core-beans/part-05-aot-and-real-world/40-aot-and-native-overview.md`
  - `docs/beans/spring-core-beans/part-05-aot-and-real-world/41-runtimehints-basics.md`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansAotRuntimeHintsLabTest.java`

#### Scenario: 能补齐“真实世界高频但易忽略”的机制（XML/容器外对象/SpEL/自定义 Qualifier）
- 能把 XML 输入归一为 BeanDefinition（定义层分型），并给出断点入口
- 能解释容器外对象的注入/初始化/销毁三段能力与边界（AutowireCapableBeanFactory）
- 能解释 `@Value("#{...}")` 的 SpEL 链路（与 `${...}` 占位符的职责边界）
- 能用自定义 Qualifier（meta-annotation）把候选收敛规则提升为业务语义
- 对应可复现闭环入口：
  - `docs/beans/spring-core-beans/part-05-aot-and-real-world/42-xml-bean-definition-reader.md`
  - `docs/beans/spring-core-beans/part-05-aot-and-real-world/43-autowirecapablebeanfactory-external-objects.md`
  - `docs/beans/spring-core-beans/part-05-aot-and-real-world/44-spel-and-value-expression.md`
  - `docs/beans/spring-core-beans/part-05-aot-and-real-world/45-custom-qualifier-meta-annotation.md`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/*LabTest.java`

## Dependencies

- 无跨模块硬依赖（该模块是 Spring Core 学习底座）

## Change History

- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/<topic>/<module>/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章）
- [202601061556_spring_core_modules_teaching_rollout](../../history/2026-01/202601061556_spring_core_modules_teaching_rollout/) - ✅ 已执行：清理 docs 正文残留的 `docs/NN` 缩写引用，统一替换为“章节名 + 真实相对路径”的 Markdown 链接，并通过断链检查与教学覆盖检查
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
- [202601032012_spring-core-beans-bookify-docs](../../history/2026-01/202601032012_spring-core-beans-bookify-docs/) - ✅ 已执行：docs 书本化（目录页 + Part 结构 + 全章结构统一（A–G） + 上下章导航），并全局修复 docs 内链与模块 README 入口
- [202601032124_spring-core-beans-src-part-grouping](../../history/2026-01/202601032124_spring-core-beans-src-part-grouping/) - ✅ 已执行：src/main 与 src/test 按 docs Part 分组（分包 + testsupport），并同步修复 docs/README/知识库中的源码路径引用
- [202601041013_spring-core-beans-src-part-naming](../../history/2026-01/202601041013_spring-core-beans-src-part-naming/) - ✅ 已执行：将 src 分组目录命名语义化（partXX → partXX_<topic>），进一步对齐 docs Part 的具名章节域
- [202601051050_spring_core_beans_deepen](../../history/2026-01/202601051050_spring_core_beans_deepen/) - ✅ 已执行：补齐 docs 目录页索引与跳读地图，新增类型转换/泛型匹配章节，并新增 component-scan/profile/optional injection/type conversion Labs 形成可复现实验闭环
- [202601051252_spring_core_beans_finish_all_tasks](../../history/2026-01/202601051252_spring_core_beans_finish_all_tasks/) - ✅ 已执行：统一 docs 全章导航与复现入口块，补齐 JSR-330 注入对照 Lab，并增强 testsupport dump 工具提升可观察性
- [202601051339_spring_core_beans_edge_case_labs](../../history/2026-01/202601051339_spring_core_beans_edge_case_labs/) - ✅ 已执行：补齐编程式注册差异 / raw injection despite wrapping / prototype 销毁语义三类边界机制，并同步 docs 入口与断点锚点
- [202601051507_spring_core_beans_aot_playbook](../../history/2026-01/202601051507_spring_core_beans_aot_playbook/) - ✅ 已执行：新增 Part 05（AOT/RuntimeHints/XML/容器外对象/SpEL/自定义 Qualifier）与对应 Labs，并新增面试复述模板/生产排障清单用于体系化复盘
- [202601052057_spring_core_beans_teaching_upgrade](../../history/2026-01/202601052057_spring_core_beans_teaching_upgrade/) - ✅ 已执行：为 Exercises 补齐对应 Solution（默认参与回归）并在 docs/README 收敛“章节↔Lab↔Exercise↔Solution”对照表；补强 ImportSelector 新手闭环与 Part05（42–45）的“源码/断点建议”与观察点
- [202601052200_spring_core_beans_beans_package_full_coverage](../../history/2026-01/202601052200_spring_core_beans_beans_package_full_coverage/) - ✅ 已执行：补齐 Spring Framework `spring-beans` 包 5 组机制闭环（XML namespace 扩展 / Properties+Groovy Reader / `replaced-method` 方法注入 / 内置 FactoryBean / PropertyEditor+值解析），新增 docs 46–50 与对应 Labs（默认参与回归）
- [202601060957_spring_core_beans_environment_beanfactory_deepening](../../history/2026-01/202601060957_spring_core_beans_environment_beanfactory_deepening/) - ✅ 已执行：补齐 Spring Framework `BeanFactory API` 与 `Environment Abstraction` 深挖闭环（docs 38–39 + Labs）
- [202601061038_spring_core_beans_spring_beans_api_full_coverage](../../history/2026-01/202601061038_spring_core_beans_spring_beans_api_full_coverage/) - ✅ 已执行：新增 spring-beans Public API 索引（95/96）+ AOT/ServiceLoader* 补齐 + Explore/Debug 用例（97）
- [202601061359_spring_core_beans_beans_support_utils](../../history/2026-01/202601061359_spring_core_beans_beans_support_utils/) - ✅ 已执行：补齐 `org.springframework.beans.support` support 工具类闭环（ArgumentConvertingMethodInvoker/ResourceEditorRegistrar/PropertyComparator/PagedListHolder/SortDefinition）并新增可运行 Lab，Appendix 96 Gap 归零
- [20260106_docs-crossref-fix](../../../docs/beans/spring-core-beans/part-00-guide/011-00-deep-dive-guide.md) - ✅ 已执行：将 `docs/01`、`docs/06/12/14/31/16/15` 这类缩写引用替换为真实章节链接，避免误解为路径
- [202601131039_teaching-experience-webmvc-beans](../../history/2026-01/202601131039_teaching-experience-webmvc-beans/) - ✅ 已执行：spring-core-beans：新增 30 分钟快启 + docs 知识点补齐（Start Here/断点观察点/自检/索引坑点）
