# 04. 传播行为（Propagation）：`REQUIRED` vs `REQUIRES_NEW` 到底差在哪？

传播行为解决的问题是：**当一个事务方法调用另一个事务方法时，事务如何“衔接”？**

## 两个最常用的传播行为

### `REQUIRED`（默认）

- 如果当前已有事务：加入当前事务
- 如果当前没有事务：新开一个事务

直觉：**同生共死**（大多数业务场景默认就是它）

### `REQUIRES_NEW`

- 无论当前是否有事务：都新开一个事务
- 外层事务会被挂起，内层事务独立提交/回滚

直觉：**我先把内层这段“单独记账”**

## 在本模块如何验证

看 `SpringCoreTxLabTest` 的两个用例：

- `requiresNewCanCommitEvenIfOuterTransactionRollsBack`
  - 外层最后抛异常回滚，但 `REQUIRES_NEW` 内层仍然提交
- `requiresNewRollbackDoesNotNecessarilyRollbackOuter_whenCaught`
  - 内层在新事务里失败回滚，但外层 catch 住异常后仍可提交

关键观察点：

- `REQUIRES_NEW` 不是“魔法保命符”，它只是把事务边界拆开了
- 外层是否回滚，依然取决于外层的异常传播/rollback-only 标记

