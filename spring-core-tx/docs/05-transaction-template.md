# 05. 程序化事务：为什么 `TransactionTemplate` 在学习阶段很有价值？

声明式事务（`@Transactional`）的优点是“用起来很爽”，但学习阶段往往会隐藏机制。

`TransactionTemplate` 的优点是把 commit/rollback 的控制权暴露出来：

- 你能清楚看到：什么时候提交、什么时候标记回滚
- 你能把“事务边界”写成显式代码（帮助建立直觉）

## 在本模块如何验证

看测试：`SpringCoreTxLabTest#transactionTemplateAllowsProgrammaticCommitOrRollback`

它演示了两次执行：

1. 正常执行：插入成功 → 提交 → 能查到数据
2. `status.setRollbackOnly()`：显式标记回滚 → 最终查不到数据

## 学习建议

- 学完 `@Transactional` 后，用 `TransactionTemplate` 复写一遍同样的场景  
  你会更清楚“事务管理器到底在干什么”。

