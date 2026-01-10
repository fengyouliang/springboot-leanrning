# 00 - Deep Dive Guide（springboot-data-jpa）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**00 - Deep Dive Guide（springboot-data-jpa）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本模块把 JPA 最容易“看不懂”的行为收敛成一条主线：

> **实体状态机（managed/detached） + Persistence Context（一致性视图） + flush（把变化推到 DB） + fetching（决定 SQL 数量）**

如果你能用这条主线解释现象，你就不会再靠“猜 Hibernate”。

### 1) 时间线：一次 Repository.save 到底发生了什么

1. 你调用 `repository.save(entity)`（Spring Data JPA）
2. JPA 把 entity 交给 `EntityManager` 管理（进入 persistence context）
3. 在同一个事务里：
   - 修改 managed entity：不会立刻打 SQL，但会被 dirty checking 记录
4. flush 时机：
   - 显式 `entityManager.flush()`
   - 或事务提交前自动 flush（取决于 flush mode/事务边界）
5. fetching 时机：
   - 访问 lazy 关联/集合时可能触发额外 SQL（N+1 的根源）

### 2) 关键参与者

- `EntityManager`：persistence context 的核心 API（contains/flush/clear）
- Hibernate（JPA provider）：dirty checking、flush、lazy loading 的具体实现
- `@DataJpaTest`：测试 slice（默认事务、默认回滚），方便你用最小成本复现机制
- `JdbcTemplate`：用于在测试里做“SQL 层证据链”（验证 flush 可见性）

### 3) 本模块的关键分支（2–5 条，默认可回归）

1. **managed 证据：save 后 entity 处于同一 persistence context**
   - 验证：`BootDataJpaLabTest#entityIsManagedAfterSaveInSamePersistenceContext`
2. **clear 边界：clear 会 detach，后续变化不再自动同步**
   - 验证：`BootDataJpaLabTest#entityManagerClearDetachesEntities` / `BootDataJpaMergeAndDetachLabTest#detached_changesWithoutMerge_shouldNotBePersisted` / `BootDataJpaMergeAndDetachLabTest#merge_shouldPersistDetachedChangesIntoManagedCopy`
3. **dirty checking：修改 managed entity + flush → DB 变化可见**
   - 验证：`BootDataJpaLabTest#dirtyCheckingPersistsChangesOnFlush`
4. **flush 可见性：flush 后 JDBC 能在同事务里看到插入行**
   - 验证：`BootDataJpaLabTest#flushMakesRowsVisibleToJdbcTemplateWithinSameTransaction`
5. **测试默认边界：`@DataJpaTest` 默认在事务内运行（便于复现实验）**
   - 验证：`BootDataJpaLabTest#dataJpaTestRunsInsideATransaction`

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。
  
建议断点（从“现象”快速回到“机制”）：

- `EntityManager#flush`：观察何时真正发 SQL
- `EntityManager#clear`：观察 managed/detached 的边界
- `BootDataJpaDebugSqlLabTest#showSqlHelpsExplainPersistenceBehavior_whenRunningTests` 的执行路径：
  - 用 show-sql 把“我以为没 SQL”变成可见证据（避免凭感觉）

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootDataJpaDebugSqlLabTest` / `BootDataJpaLabTest` / `BootDataJpaMergeAndDetachLabTest`
- 建议命令：`mvn -pl springboot-data-jpa test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 推荐学习目标
1. 用“实体状态机 + Persistence Context”解释大多数诡异行为
2. 能用最小测试复现 flush/脏检查/N+1，并能定位到 SQL 层的证据
3. 能把 `@DataJpaTest` 的 slice 边界与真实 Boot 启动边界区分开

## 推荐阅读顺序
1. [01-entity-states](../part-01-data-jpa/01-entity-states.md)
2. [02-persistence-context](../part-01-data-jpa/02-persistence-context.md)
3. [03-flush-and-visibility](../part-01-data-jpa/03-flush-and-visibility.md)
4. [04-dirty-checking](../part-01-data-jpa/04-dirty-checking.md)
5. [05-fetching-and-n-plus-one](../part-01-data-jpa/05-fetching-and-n-plus-one.md)
6. [06-datajpatest-slice](../part-01-data-jpa/06-datajpatest-slice.md)
7. [07-debug-sql](../part-01-data-jpa/07-debug-sql.md)
8. [90-common-pitfalls](../appendix/90-common-pitfalls.md)
9. [99-self-check](../appendix/99-self-check.md)

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-data-jpa test`

## 对应 Lab（可运行）

- `BootDataJpaLabTest`
- `BootDataJpaDebugSqlLabTest`
- `BootDataJpaMergeAndDetachLabTest`
- `BootDataJpaExerciseTest`

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootDataJpaDebugSqlLabTest` / `BootDataJpaLabTest` / `BootDataJpaMergeAndDetachLabTest`
- Exercise：`BootDataJpaExerciseTest`

上一章：[Docs TOC](../README.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-data-jpa/01-entity-states.md](../part-01-data-jpa/01-entity-states.md)

<!-- BOOKIFY:END -->
