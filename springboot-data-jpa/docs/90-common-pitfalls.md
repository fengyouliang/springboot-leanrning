# 90. 常见坑清单（建议反复对照）

## 坑 1：把 persistence context 当成数据库

- 现象：你改了对象字段，立刻 `findById` 看到“变了”，误以为 DB 已更新
- 解决：`entityManager.flush()` + `entityManager.clear()` 再查，避免一级缓存假象
- 对照：见 [docs/04](04-dirty-checking.md)

## 坑 2：不理解 flush 导致“JDBC 查不到/查到了但没提交”

- 现象：你用 `JdbcTemplate` 直接查表，结果和你想象不一致
- 解决：理解 flush vs commit 的差异（见 [docs/03](03-flush-and-visibility.md)）

## 坑 3：懒加载 + 循环访问触发 N+1

- 现象：查列表很快，但访问关联属性时 SQL 爆炸
- 解决：先把问题复现清楚，再讨论 fetch 策略（见 [docs/05](05-fetching-and-n-plus-one.md)）

## 坑 4：在事务外访问懒加载属性

- 现象：`LazyInitializationException`
- 原因：事务/Session 结束后再访问 lazy 属性无法触发查询

## 坑 5：测试里忘记 `@DataJpaTest` 的默认回滚

- 现象：你想“写入后在下一个测试里看到”，但看不到
- 原因：测试默认回滚
- 对照：见 [docs/06](06-datajpatest-slice.md)

