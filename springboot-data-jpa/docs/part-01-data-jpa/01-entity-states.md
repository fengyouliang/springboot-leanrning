# 01. Entity 状态机：transient / managed / detached / removed

学 JPA 最容易“学成玄学”的原因是：你只看到了 `repository.save()`，没看清楚背后有一套明确的状态机。

这一章只讲一个问题：

> **一个 Entity 在生命周期里会经历哪些状态？这些状态有什么可观察的后果？**

## 四种经典状态（务必记住）

1. **transient（瞬时/新建）**
   - 你 `new Book(...)` 出来的对象
   - 没有持久化身份（通常 `id == null`）

2. **managed（受管/持久化上下文内）**
   - Entity 被当前 persistence context 管理
   - 你对它的字段修改会被“脏检查”捕获（见 [docs/04](04-dirty-checking.md)）

3. **detached（游离/脱管）**
   - Entity 曾经是 managed，但被 detach/clear 后不再受当前 context 管理
   - 修改它不会自动同步到数据库（除非你 merge 回去）

4. **removed（已标记删除）**
   - 删除操作在 flush/commit 时真正反映到数据库

## 在本模块如何验证

看 `BootDataJpaLabTest`：

- `entityIsManagedAfterSaveInSamePersistenceContext`
  - `repository.save(...)` 后，`entityManager.contains(saved)` 为 true（managed）
- `entityManagerClearDetachesEntities`
  - `entityManager.clear()` 后，`contains(saved)` 变成 false（detached）

## 你应该得到的结论

- JPA 不是“直接对数据库写”，而是“先写进 persistence context，再在 flush/commit 时同步”
- 所以你后面学 flush / dirty checking / N+1 时，逻辑都会回到这套状态机上

