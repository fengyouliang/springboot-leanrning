# 04. Dirty Checking（脏检查）：为什么改字段不用 save 也能落库？

这是 JPA 最“神奇”但也最容易被误用的机制：脏检查。

## 现象

- 你拿到一个 managed entity
- 修改它的字段
- 没有再调用 `save()`
- flush/commit 之后，数据库值变了

## 在本模块如何验证

看 `BootDataJpaLabTest#dirtyCheckingPersistsChangesOnFlush`：

1. `Book saved = repository.save(...)`
2. `saved.changeAuthor("B")`（只改字段）
3. `entityManager.flush()`（触发同步）
4. `entityManager.clear()`（清掉上下文，避免“一级缓存假象”）
5. 重新 `findById` 并断言 author 已经变成 B

## 你应该得到的结论

1. dirty checking 的前提是：实体必须是 managed（受 persistence context 管理）
2. flush/commit 是“把变化写进 DB”的时机
3. 清理 context（`clear()`）能避免你误把“一级缓存”当成“数据库状态”

