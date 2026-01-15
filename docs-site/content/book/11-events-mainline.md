# 第 11 章：Events 主线

这一章解决的问题是：**为什么发布一个事件就能触发多个监听器、异常怎么传播、事务提交后再发事件该怎么写**。

---

## 主线（按时间线顺读）

1. 发布：`ApplicationEventPublisher` 发出事件
2. 分发：`ApplicationEventMulticaster` 找到匹配的监听器并调用
3. 同步 vs 异步：默认同步；引入 executor 后变成异步
4. 事务事件：`@TransactionalEventListener` 在 AFTER_COMMIT 等时机触发
5. 常见坑：监听器顺序、异常传播、异步测试不稳定、事务回滚时事件是否触发

---

## 深挖入口（模块 docs）

- 模块目录页：[`spring-core-events/docs/README.md`](../spring-core-events/docs/README.md)
- 模块主线时间线（含可跑入口）：[`spring-core-events/docs/part-00-guide/03-mainline-timeline.md`](../spring-core-events/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

把事件跑通后，很多问题会落到“资源加载/扫描”：例如 classpath、jar、pattern matching。我们进入 Resources 主线。

- 下一章：[第 12 章：Resources 主线](12-resources-mainline.md)

