# spring-core-aop-weaving

## Purpose

学习 AspectJ weaving（织入）：LTW（`-javaagent`）与 CTW（编译期织入），以及 proxy AOP 无法覆盖的 join point 与高级 pointcut（`call/get/set/constructor/withincode/cflow` 等）。

## Module Overview

- **Responsibility:** 用可验证的 Labs/Exercises 讲清 “Proxy vs Weaving” 的能力边界与排障路径。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-07

## Specifications

### Source Layout

- docs：`spring-core-aop-weaving/docs/README.md`（目录页）
- docs：`spring-core-aop-weaving/docs/part-00-guide/`（跑通指南：LTW/CTW）
- docs：`spring-core-aop-weaving/docs/part-01-mental-model/`（Proxy vs Weaving 心智模型）
- docs：`spring-core-aop-weaving/docs/part-02-ltw/`（LTW：agent + aop.xml + include 范围）
- docs：`spring-core-aop-weaving/docs/part-03-ctw/`（CTW：编译期织入与范围控制）
- docs：`spring-core-aop-weaving/docs/part-04-join-points/`（Join Point/Pointcut Cookbook）
- docs：`spring-core-aop-weaving/docs/appendix/`（常见坑/自测题）
- src(main)：`spring-core-aop-weaving/src/main/java/com/learning/springboot/springcoreaopweaving/SpringCoreAopWeavingApplication.java`（入口）
- src(main)：`spring-core-aop-weaving/src/main/java/com/learning/springboot/springcoreaopweaving/support/**`（可断言观察点：InvocationLog/JoinPointEvent）
- src(main)：`spring-core-aop-weaving/src/main/java/com/learning/springboot/springcoreaopweaving/ctwtargets/**`（CTW 目标对象）
- src(main)：`spring-core-aop-weaving/src/main/aspect/com/learning/springboot/springcoreaopweaving/part03_ctw_fundamentals/**`（CTW aspects，AspectJ 语法）
- src(test)：`spring-core-aop-weaving/src/test/resources/META-INF/aop.xml`（LTW 配置）
- src(test)：`spring-core-aop-weaving/src/test/java/com/learning/springboot/springcoreaopweaving/ltwtargets/**`（LTW 目标对象）
- src(test)：`spring-core-aop-weaving/src/test/java/com/learning/springboot/springcoreaopweaving/part02_ltw_fundamentals/**`（LTW aspects + Labs）
- src(test)：`spring-core-aop-weaving/src/test/java/com/learning/springboot/springcoreaopweaving/part03_ctw_fundamentals/**`（CTW Labs）
- src(test)：`spring-core-aop-weaving/src/test/java/com/learning/springboot/springcoreaopweaving/part00_guide/**`（Exercises，默认 `@Disabled`）

### Docs Index

- 入口：`spring-core-aop-weaving/docs/README.md`

### Requirement: LTW/CTW 可验证闭环

**Module:** spring-core-aop-weaving  
通过两套 Labs 验证 weaving 行为：

- `*Ltw*Test`：带 `-javaagent:aspectjweaver.jar`（LTW）
- `*Ctw*Test`：不带 `-javaagent`（CTW）

并覆盖至少以下 join point / pointcut：

- `call` vs `execution`
- constructor call/execution
- field get/set
- `withincode`
- `cflow`

### Requirement: 排障分流（Proxy vs Weaving）

**Module:** spring-core-aop-weaving  
能够在真实问题中分流定位：

- Proxy 世界：是否没走 proxy（call path 问题）
- LTW：是否没带 agent / 没加载 aop.xml / include 范围错误
- CTW：是否构建未织入 / 织入范围错误 / 运行时使用未织入产物

## Dependencies

- 建议先完成 `spring-core-aop`（proxy AOP 主线）
- 构建与测试依赖 AspectJ（`aspectjrt`/`aspectjweaver`）与 Maven 插件（CTW）
- 编译目标为 Java 16（为兼容 CTW 使用的 ajc source level 上限）；运行仍要求 JDK 17+（父工程 enforcer）

## Change History

- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章），并通过 `scripts/check-docs.sh`
- [202601061556_spring_core_modules_teaching_rollout](../../history/2026-01/202601061556_spring_core_modules_teaching_rollout/) - ✅ 已执行：对齐 docs 目录页/Part 编号与章节末尾“对应 Lab/Test”入口块，清理正文 `docs/NN` 缩写引用，并通过断链检查与教学覆盖检查
- [202601061341_spring-core-aop-weaving](../../history/2026-01/202601061341_spring-core-aop-weaving/) - ✅ 已执行：创建 `spring-core-aop-weaving` 作为 weaving 深挖模块（LTW/CTW + join point cookbook + Labs/Exercises）
