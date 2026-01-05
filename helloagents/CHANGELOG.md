# Changelog

本文件记录本仓库的重要变更，格式参考 Keep a Changelog，版本号遵循语义化版本（SemVer）。

## [Unreleased]

### Changed
- `spring-core-beans`：将源码分组目录命名语义化（`part00/part01/...` → `part00_guide/part01_ioc_container/...`），提升与 docs Part（具名章节域）的对齐程度。
- `spring-core-beans`：源码与测试按 docs Part 结构分组：将 `src/main/java` 与 `src/test/java` 从平铺改为 `part00_guide/part01_ioc_container/part02_boot_autoconfig/part03_container_internals/part04_wiring_and_boundaries/appendix` 分包，并新增跨 Part 复用的 `testsupport`；同时全量修复 docs/README/知识库中的源码路径引用；保留 `com.learning.springboot.springcorebeans.SpringCoreBeansApplication` 包名不变。
- `spring-core-beans`：docs 书本化（Bookify）：引入 `docs/README.md` 目录页与 Part 结构，对 docs 章节进行移动/重命名/重新分组；统一每章 A–G 章节契约（定位/结论/主线/源码/实验/坑点/小结预告）并补齐“上一章｜目录｜下一章”导航；同时全局修复 docs 内链与模块 README 的入口链接。
- `spring-core-beans`：补齐模块 README 学习路线（Start Here/入门→进阶→深挖/refresh 主线一页纸/运行态观察点），新增“注入歧义最小复现”Lab + 对应 Exercise，并增强 `BeansDemoRunner` 的 `BEANS:` 结构化输出；同时同步根 README 与 progress 打卡入口。
- `spring-core-beans`：把“新增面试点”按主题嵌入到 docs/01、03、05、16、31、33 的正文对应小节，并补齐可断言复现入口（新增 BeanFactory vs ApplicationContext / Aware 基础设施 / 泛型匹配坑 Labs；扩展 proxy 章节增加 CGLIB vs JDK 对照与 BPP 定位闭环）。
- `spring-core-beans`：在 docs/01、02、03、05、09 增补 Spring 源码解析（refresh 主线/ConfigurationClassPostProcessor 注册入口/`doResolveDependency` 候选收敛/`doCreateBean` 生命周期/三级缓存循环依赖），并补充最小仓库 src 代码片段辅助理解。
- `spring-core-beans`：继续深化 docs/06 与 docs/12（PostProcessors/容器启动基础设施）：补齐 `PostProcessorRegistrationDelegate` 两段算法的源码级解释，并新增“static @Bean BFPP”最小可运行 Lab 用于解释早实例化与顺序陷阱。
- `spring-core-beans`：把 docs/14（Ordering）与 docs/25（programmatic BPP 注册）补成“算法级 + 可复现”版本：补齐分段执行/排序器规则/internal BPP 重新注册，以及 `addBeanPostProcessor` 的 list 语义与“BPP 不会 retroactive”的时机陷阱；同时增强 ordering Lab 覆盖 order 数值与 @Order 反例。
- `spring-core-beans`：移除误添加的 `docs/00-first-pass-learning-loop.md` 并清理引用；同时把可执行的“First Pass（10 个最小实验入口）”融入 `docs/00-deep-dive-guide.md` 与 `docs/99-self-check.md`，避免额外文件带来的重复编号与噪声。
- `spring-core-beans`：深化 Boot 自动装配章节（docs/10）：补齐 `matchIfMissing` 三态语义与自动配置顺序依赖（after/before）最小复现 Lab，并在 docs/11 与 README 的索引表同步入口。
- `spring-core-beans`：深化 Boot 自动装配 Exercises：新增 matchIfMissing 三态与 `@ConditionalOnBean` 顺序/时机差异的练习题，并提供“条件报告可查询”的 helper 练习，确保所有面试点落位到 docs/10 对应正文小节。
- `spring-core-beans`：补齐 auto-config back-off/覆盖排障闭环：新增 early/late registrar 对照 Lab，解释“为什么写了覆盖 Bean 但没退让”的真实原因，并把入口落位到 docs/10 的“覆盖”正文小节。
- `spring-core-beans`：补齐 Boot 自动装配主线与排障“可观察性”：新增 import/排序主线 Lab、BeanDefinition 来源追踪 Dumper，以及覆盖/back-off 场景矩阵 Lab；同步 docs/10 与模块 README 入口。
- `spring-core-beans`：提升 docs/01-03 连贯性：为连续教程主线补齐“本章定位/主线 vs 深挖/下一章预告”桥接段，统一阅读契约但不删减知识点。
- 深化 `spring-core-beans` 核心章节：扩写 docs/03、05、06、07、08、09、16、17、23、29、31，并扩展 docs/90（常见坑）与 docs/99（自测题），补齐源码级决策树/断点闭环/排障速查与 Lab 映射。
- `spring-core-beans`：新增 docs/36（类型转换链路：BeanWrapper/ConversionService）与 docs/37（泛型匹配注入坑：ResolvableType/代理/实例注册），新增 appendix/91（术语表）与 appendix/92（知识点跳读地图），并新增 component-scan/profile/optional injection/type conversion Labs 形成文档→实验闭环；同时修复 docs/README.md 排版并补齐快速定位与章节↔Lab 对照表。
- `spring-core-beans`：统一 docs 全章“上一章｜目录｜下一章”导航与“复现入口（可运行）”块，新增 JSR-330 `@Inject`/`Provider<T>` 对照 Lab（补齐 `jakarta.inject-api` 测试依赖），并增强 testsupport dumper 输出（候选集合/依赖边/来源定位）以提升排障可观察性。
- `spring-core-beans`：补齐 3 类易翻车边界机制：编程式注册差异（定义层 vs 实例层）、raw injection despite wrapping（`allowRawInjectionDespiteWrapping` 一致性保护）、prototype 销毁语义（默认不销毁 + `destroyBean` 手动销毁）；并在 docs/04、docs/05、docs/16、docs/25 增补复现入口与断点锚点。
- `spring-core-beans`：新增 Part 05（AOT/RuntimeHints/XML/容器外对象/SpEL/自定义 Qualifier）与对应 Labs，并新增 Appendix（面试复述模板 / 生产排障清单），同步更新 docs/README、模块 README、知识点地图与术语表索引。
- `scripts`：新增 Markdown 相对链接存在性检查脚本（用于文档 0 断链自检）。
- 深化 `spring-core-aop` 核心章节：新增 docs/00（深挖指南）与 docs/99（自测题），扩写 docs/01-06、docs/90（常见坑），补齐源码断点入口/观察点与排障闭环。
- 二次深化 `spring-core-aop`：新增 docs/07-09（AutoProxyCreator 主线 / pointcut 表达式系统 / 多代理叠加与顺序），并新增 4 组 Labs 覆盖 BPP 主线、proceed 嵌套、this vs target、以及多 advisor vs 套娃 proxy 的可断言闭环；同时在 `spring-core-beans` 的 BPP/代理/顺序章节补齐 AutoProxyCreator 承接与跨模块链接。
- 三次深化 `spring-core-aop`：新增 docs/10（真实叠加 Debug Playbook）与集成 Lab（Tx/Cache/Method Security），把“多代理叠加”落到真实基础设施断点与可断言语义，并更新 README/深挖指南/多代理章节导航。
- `spring-core-aop`/`spring-core-events`/`spring-core-tx`：补齐 DemoRunner 结构化输出（`AOP:`/`EVENTS:`/`TX:` 前缀），在 events 增加可控的异常传播演示（特定输入触发 throwing listener）；`spring-core-tx` 新增“自调用绕过事务”Lab，并同步 README/根 README/progress 的入口索引。
- `spring-core-aop`/`spring-core-events`/`spring-core-profiles`/`spring-core-resources`/`spring-core-tx`/`spring-core-validation`：对齐 docs Part 目录结构与 src/main+src/test 分包结构（语义化 Part 命名），并同步修复 README/文档中的源码路径与跨模块引用；保持各模块 `*Application` 入口包名不变。
- `springboot-*`：将 Part 结构（docs + src/test + src/main 最小分组）推广到全部 `springboot-*` 模块：新增 `docs/README.md` 与 `part-00-guide/`、迁移 docs 章节到 `part-01-*/` 与 `appendix/`；tests 按 `part00_guide`（Exercises）/ `part01_*`（Labs）分包；在不修改各模块 `*Application` 入口包名的前提下，将示例代码迁移到 `part01_*`（`springboot-business-case` 例外：为保留领域分层，仅对 tests 与 docs 对齐）；同时修复各模块 README 与 docs 内的源码路径引用。
