# 90. 常见坑清单（建议反复对照）

## 导读

- 本章主题：**90. 常见坑清单（建议反复对照）**
- 阅读方式建议：先看“本章要点”，再沿主线阅读；需要时穿插源码/断点，最后跑通实验闭环。

!!! summary "本章要点"

    - 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
    - 如果只看一眼：请先跑一次本章的最小实验，再回到主线对照阅读。


!!! example "本章配套实验（先跑再读）"

    - Lab：`BootDataJpaDebugSqlLabTest` / `BootDataJpaLabTest`

## 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootDataJpaDebugSqlLabTest` / `BootDataJpaLabTest`
- 建议命令：`mvn -pl springboot-data-jpa test`（或在 IDE 直接运行上面的测试类）

## 常见坑与边界

## 坑 1：把 persistence context 当成数据库

- 现象：你改了对象字段，立刻 `findById` 看到“变了”，误以为 DB 已更新
- 解决：`entityManager.flush()` + `entityManager.clear()` 再查，避免一级缓存假象
- 对照：见 [docs/04](../part-01-data-jpa/04-dirty-checking.md)

## 坑 2：不理解 flush 导致“JDBC 查不到/查到了但没提交”

- 现象：你用 `JdbcTemplate` 直接查表，结果和你想象不一致
- 解决：理解 flush vs commit 的差异（见 [docs/03](../part-01-data-jpa/03-flush-and-visibility.md)）

## 坑 3：懒加载 + 循环访问触发 N+1

- 现象：查列表很快，但访问关联属性时 SQL 爆炸
- 解决：先把问题复现清楚，再讨论 fetch 策略（见 [docs/05](../part-01-data-jpa/05-fetching-and-n-plus-one.md)）

## 坑 4：在事务外访问懒加载属性

- 现象：`LazyInitializationException`
- 原因：事务/Session 结束后再访问 lazy 属性无法触发查询

## 坑 5：测试里忘记 `@DataJpaTest` 的默认回滚

## 坑 6：以为 `merge()` 会“把原对象重新托管”，结果改了半天没生效

- Symptom：你在 `detach()/clear()` 之后继续改对象，觉得“脏检查会帮我 UPDATE”，但数据库里啥都没变；或者你调用了 `merge()`，但后续仍然在 **原对象** 上继续改，结果再次不生效。
- Root Cause：JPA 的 `merge()` 语义是 **复制状态到一个新的 managed 实例**，并返回这个 managed 实例；传入的那个对象本身仍然是 detached，后续修改不会被脏检查追踪。
- Verification：`BootDataJpaMergeAndDetachLabTest#detached_changesWithoutMerge_shouldNotBePersisted`、`BootDataJpaMergeAndDetachLabTest#merge_shouldPersistDetachedChangesIntoManagedCopy`
- Breakpoints：`org.hibernate.internal.SessionImpl#merge`、`org.hibernate.event.internal.DefaultMergeEventListener#onMerge`
- Fix：后续操作一律使用 `merge()` 的返回值，或重新 `find()` 获取 managed；把“对象状态（managed/detached）→ 预期 SQL”用 Lab/Test 固化。

- 现象：你想“写入后在下一个测试里看到”，但看不到
- 原因：测试默认回滚
- 对照：见 [docs/06](../part-01-data-jpa/06-datajpatest-slice.md)

## 对应 Lab（可运行）

- `BootDataJpaLabTest`
- `BootDataJpaDebugSqlLabTest`

## 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootDataJpaDebugSqlLabTest` / `BootDataJpaLabTest`

上一章：[part-01-data-jpa/07-debug-sql.md](../part-01-data-jpa/07-debug-sql.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/99-self-check.md](99-self-check.md)

<!-- BOOKIFY:END -->
