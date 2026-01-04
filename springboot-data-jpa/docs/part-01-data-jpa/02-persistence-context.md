# 02. Persistence Context：JPA 的“一级缓存”与事务绑定

Persistence Context（持久化上下文）是 JPA/Hibernate 的核心：

- 它管理实体的 **生命周期与状态**
- 它保证同一个事务/上下文内的 **对象标识一致性**
- 它承载 **脏检查**、**延迟加载** 等机制的基础

## 在本模块如何验证

看 `BootDataJpaLabTest` 里的这些实验：

- `entityIsManagedAfterSaveInSamePersistenceContext`
- `entityManagerClearDetachesEntities`
- `dataJpaTestRunsInsideATransaction`

尤其是 `dataJpaTestRunsInsideATransaction`：

- `@DataJpaTest` 默认会在一个事务里运行测试
- 这意味着 persistence context 通常也跟着事务生命周期走

## 关键心智模型（建议背下来）

> 在同一个事务（更准确：同一个 persistence context）里：
>
> - 实体对象不是“普通 POJO”，而是被管理的状态机
> - 修改对象字段 ≈ 修改待同步的持久化状态（最终在 flush/commit 写入 DB）

## Debug/观察建议

学习阶段推荐做两件事：

1. 经常用 `entityManager.contains(entity)` 问自己：它现在是 managed 还是 detached？
2. 经常用 `entityManager.flush()` 强制把“上下文里的变化”同步到数据库，验证你对机制的理解

