# 03. flush：SQL 什么时候发出去？为什么 flush 后 JDBC 能查到？

新手最常见的误解是：

> “我调用了 `save()`，所以数据已经进数据库了。”

实际上，在很多情况下：

- `save()` 只是把实体交给 persistence context
- SQL 什么时候真正执行，要看 flush/commit 时机

## flush vs commit（一句话）

- **flush**：把 persistence context 的变更同步成 SQL 执行（但事务可能还没提交）
- **commit**：提交事务，让变更对其它事务可见

## 在本模块如何验证（强烈建议断点）

看 `BootDataJpaLabTest#flushMakesRowsVisibleToJdbcTemplateWithinSameTransaction`：

1. `repository.save(...)`
2. `entityManager.flush()`
3. 用 `JdbcTemplate` 直接查表行数

关键观察点：

- flush 之后，同一事务内用 JDBC 查能看到行数变化
- 这说明：SQL 已经发出并执行了（只是还没 commit）

## 你应该得到的结论

- 学习 JPA 一定要区分“上下文里有什么”与“数据库里有什么”
- flush 是你把两者对齐的手段之一（学习阶段特别好用）

