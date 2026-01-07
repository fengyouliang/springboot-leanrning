# spring-core-aop

## Purpose

学习 Spring AOP 与代理：Advice/Aspect、代理类型、自调用陷阱与可验证实验。

## Module Overview

- **Responsibility:** 提供 AOP 的最小可运行示例与测试实验，帮助理解代理行为与切面生效边界。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-07

## Specifications

### Source Layout
- docs：`spring-core-aop/docs/README.md`（目录页）
- docs：`spring-core-aop/docs/part-00-guide/`（深挖指南）
- docs：`spring-core-aop/docs/part-01-proxy-fundamentals/`（代理基础/自调用/限制/调试）
- docs：`spring-core-aop/docs/part-02-autoproxy-and-pointcuts/`（AutoProxyCreator 主线/pointcut 系统）
- docs：`spring-core-aop/docs/part-03-proxy-stacking/`（多代理叠加/真实项目 playbook）
- docs：`spring-core-aop/docs/appendix/`（常见坑/自测题）
- src(main)：`spring-core-aop/src/main/java/com/learning/springboot/springcoreaop/SpringCoreAopApplication.java`（入口，包名保持不变）
- src(main)：`spring-core-aop/src/main/java/com/learning/springboot/springcoreaop/part01_proxy_fundamentals/**`
- src(main)：`spring-core-aop/src/main/java/com/learning/springboot/springcoreaop/part02_autoproxy_and_pointcuts/**`
- src(test)：`spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part00_guide/**`
- src(test)：`spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part01_proxy_fundamentals/**`
- src(test)：`spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part02_autoproxy_and_pointcuts/**`
- src(test)：`spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part03_proxy_stacking/**`

### Docs Index
- 入口：`spring-core-aop/docs/README.md`

### Requirement: AOP 学习闭环
**Module:** spring-core-aop
通过 Labs/Exercises 让用户能验证 advice 是否生效、代理类型与自调用行为。

#### Scenario: advice 生效与自调用差异
- 直接调用与内部自调用的行为差异可被稳定断言
- `spring-boot:run` 可观察代理类型与自调用现象（结构化前缀 `AOP:`）

### Requirement: AOP 源码级深化（能解释 + 能断点 + 能定位问题）
**Module:** spring-core-aop
在已有 Labs/Exercises 的基础上，补齐“结论 → 实验 → 断点入口 → 观察点”的闭环指引，使读者能在真实项目中定位：
不拦截、代理类型不对、advice 顺序不对、pointcut 误命中/漏命中等问题。

#### Scenario: 能解释代理产生时机（BPP after-init）
- 能说清 proxy 通常在 `postProcessAfterInitialization` 阶段产生
- 能用断点看到目标对象被 AutoProxyCreator 包装为 proxy

#### Scenario: 能复述 AutoProxyCreator/Advisor/Advice/Pointcut 主线（源码级）
- 能解释 AutoProxyCreator 是典型 `BeanPostProcessor`，并能定位其注册与介入点（pre/early/after-init）
- 能解释 Advisor=Pointcut+Advice，并能在断点里看见 eligible advisors 的筛选与 proxy 生成

#### Scenario: 能解释并验证 JDK vs CGLIB 的类型差异
- 能解释为什么 JDK proxy 下按实现类查找会失败
- 能用测试断言代理类型（JDK/CGLIB）与可注入类型边界

#### Scenario: 能解释 self-invocation 与 exposeProxy 的取舍
- 能解释 why：call path 必须走 proxy
- 能说明常见工程解法（拆分 bean / 自注入 / exposeProxy）与风险

#### Scenario: 能解释并验证 advice 链顺序
- 能解释多个切面嵌套关系与 `@Order` 的影响
- 能在断点里观察拦截器链顺序

#### Scenario: 能解释并验证 pointcut 表达式系统（避免误判）
- 能解释 `execution/within/this/target/args/@annotation/...` 的语义差异与常见误判来源
- 能用 Lab 固化 this vs target 在 JDK/CGLIB 下的命中差异

#### Scenario: 能解释并验证多切面/多代理叠加（AOP/Tx/Cache/Security 视角）
- 能区分“单 proxy 多 advisors”与“多层 proxy（套娃）”，并能用 `Advised#getAdvisors()` 直接观察
- 能分清顺序问题的归属：BPP 顺序 vs advisor/interceptor 顺序

#### Scenario: 能在真实基础设施下验证叠加语义（Tx/Cache/Security）
- 能用最小可复现 Lab 验证：鉴权阻断、缓存短路、事务激活三类真实语义
- 能把这三类语义落到断点：链条组装 → proceed 嵌套 → 具体拦截器的短路/抛错点

## Dependencies

- 依赖 `spring-core-beans` 的 Bean/容器基础概念（学习路径依赖）
- 测试范围引入 `spring-tx` 与 `spring-security-config`，用于“真实叠加”集成 Lab（不依赖外部 DB/Web）
- 进阶扩展：`spring-core-aop-weaving`（AspectJ weaving：LTW/CTW、更多 join point/高级表达式，用于理解 proxy AOP 的能力边界）

## Change History

- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 升级 A–G 章节契约（每章 A–G + 对应 Lab/Test + 至少 1 个 LabTest），并更新根 README 跨模块入口
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章），并通过 `scripts/check-docs.sh`
- [202601061556_spring_core_modules_teaching_rollout](../../history/2026-01/202601061556_spring_core_modules_teaching_rollout/) - ✅ 已执行：对齐 docs 目录页/Part 编号与章节末尾“对应 Lab/Test”入口块，清理正文 `docs/NN` 缩写引用，并通过断链检查与教学覆盖检查
- [202601010804_spring-core-aop-deep-dive](../../history/2026-01/202601010804_spring-core-aop-deep-dive/) - ✅ 已执行：新增深挖指南/自测题，扩写 01-06/90，补齐源码级断点与排障闭环
- [202601010845_beans-aop-deep-dive-v2](../../history/2026-01/202601010845_beans-aop-deep-dive-v2/) - ✅ 已执行：新增 07-09（AutoProxyCreator 主线/pointcut/多代理叠加），并新增 Labs 覆盖 proceed 嵌套、this vs target、多 advisor vs 套娃 proxy
- [202601011121_aop-real-stacking-labs](../../history/2026-01/202601011121_aop-real-stacking-labs/) - ✅ 已执行：新增 10（真实叠加 Debug Playbook）与集成 Lab（Tx/Cache/Method Security），补齐“真实叠加”断点与排障闭环
- [202601021322_complete_spring_core_fundamentals_remaining](../../history/2026-01/202601021322_complete_spring_core_fundamentals_remaining/) - ✅ 已执行：补齐 `AopDemoRunner` 结构化输出（proxyType/targetClass/自调用现象）并同步进度清单入口
- [202601041046_spring-core-part-structure-sync](../../history/2026-01/202601041046_spring-core-part-structure-sync/) - ✅ 已执行：对齐 docs Part 目录结构与 src/main+src/test 分包结构（语义化 Part 命名），并修复 README/跨模块引用路径
