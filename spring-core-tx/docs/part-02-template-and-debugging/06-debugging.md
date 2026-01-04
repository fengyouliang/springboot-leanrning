# 06. Debug / 观察：如何判断“当前是否真的有事务”？

事务相关的学习痛点通常是：你以为有事务，但其实没有；或者你以为回滚了，但其实提交了。

这一章给出几个“可落地的观察手段”。

## 1) 直接问 Spring：当前是否有事务？

最简单的判断方式是：

- `TransactionSynchronizationManager.isActualTransactionActive()`

本模块在 `SpringCoreTxLabTest#transactionsAreActiveInsideTransactionalMethods` 已经验证了这一点。

## 2) 看 SQL/数据，而不是只看异常

事务最终影响的是“数据是否落库”：

- 一次插入 + 抛异常，最后查表行数（是否回滚）
- 这是最直观、最不容易误判的方式

## 3) 观察传播行为：用“不同 owner 写入”做标签

本模块的做法值得复用：

- outer 写 `outer`，inner 写 `inner`
- 你能直接从表里看到哪段提交了、哪段回滚了

## 4)（可选）打开事务日志

如果你需要更细粒度观察，可以在模块的 `application.properties` 中设置日志级别（学习用即可）：

- `logging.level.org.springframework.transaction=DEBUG`
- `logging.level.org.springframework.jdbc.datasource=DEBUG`

