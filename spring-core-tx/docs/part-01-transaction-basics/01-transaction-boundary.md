# 01. 事务边界（Transaction Boundary）：你到底在“保护”哪一段代码？

事务学习最重要的是先把概念落地：**事务边界** 是你定义的“原子单元”。

> 事务边界 = “从哪里开始”到“哪里结束”这一段逻辑，要么全部成功提交，要么全部失败回滚。

## 在本模块的最小闭环

看 `AccountService`：

- `createTwoAccounts()`：成功 → commit → 表里有两行
- `createTwoAccountsThenFail()`：抛运行时异常 → rollback → 表里没有行

对应测试：

- `SpringCoreTxLabTest#commitsOnSuccess`
- `SpringCoreTxLabTest#rollsBackOnRuntimeException`

## 你需要记住的 3 件事

1. **事务边界通常是“方法级别”的**
   - 声明式事务（`@Transactional`）默认就是围绕方法的 begin/commit/rollback

2. **回滚与否取决于异常是否“逃逸出边界”**
   - 抛出运行时异常并向外传播：默认回滚
   - 异常被你 catch 住了：默认会提交（除非你显式标记 rollback-only，见 [docs/90](90-common-pitfalls.md)）

3. **事务边界不是“语法糖”，它依赖代理机制**
   - `@Transactional` 的生效条件见 [docs/02](02-transactional-proxy.md)

