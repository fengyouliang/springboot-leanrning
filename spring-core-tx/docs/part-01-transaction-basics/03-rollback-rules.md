# 03. 回滚规则：为什么 checked exception 默认不回滚？

Spring 事务默认回滚规则经常让人困惑：

- **运行时异常（RuntimeException / Error）**：默认回滚
- **受检异常（checked exception）**：默认不回滚

## 在本模块如何“看见”差异

看 `SpringCoreTxLabTest` 里的 `TxPlaygroundService`（是 test 内部类，方便做机制实验）：

- `insertThenThrowChecked()`：抛 checked exception，但默认 **不回滚**
  - 对应断言：`SpringCoreTxLabTest#checkedExceptionsDoNotRollbackByDefault`
- `insertThenThrowCheckedWithRollback()`：加了 `@Transactional(rollbackFor = ...)` 后 **会回滚**
  - 对应断言：`SpringCoreTxLabTest#rollbackForCheckedExceptionsCanBeConfigured`

## 为什么 Spring 默认这样做？

历史原因 + 语义取舍：

- checked exception 在 Java 语义里往往表示“可预期的业务分支”
- Spring 默认认为：这类异常不一定等价于“系统失败”，因此不默认回滚

学习仓库里更重要的是你得形成“可预测规则”：

> **想让 checked exception 回滚，就显式写 `rollbackFor`。**

