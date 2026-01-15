# 第 5 章：事务主线（Tx）

事务这条线解决的问题是：**一次业务操作里，哪些数据库操作应该“同生共死”**？你要能讲清楚：边界在哪、回滚规则是什么、传播行为为什么会让你“以为开启了事务但其实没有”。

---

## 主线（按时间线顺读）

把事务理解成“在方法边界包一层”：

1. 识别事务边界：通常来自 `@Transactional`
2. 选择事务管理器：`PlatformTransactionManager`（JDBC/JPA 等）
3. 方法调用进入拦截器：开启/加入事务、绑定资源到线程
4. 方法正常返回：提交事务
5. 方法抛异常：按规则回滚（Runtime vs Checked、rollbackFor/noRollbackFor）
6. 传播与嵌套：REQUIRED/REQUIRES_NEW/NESTED 等决定“加入还是新开”

---

## 深挖入口（模块 docs）

- 模块目录页：[`spring-core-tx/docs/README.md`](../spring-core-tx/docs/README.md)
- 模块主线时间线（含可跑入口）：[`spring-core-tx/docs/part-00-guide/03-mainline-timeline.md`](../spring-core-tx/docs/part-00-guide/03-mainline-timeline.md)

建议先跑的最小闭环：

- `SpringCoreTxLabTest`
- `SpringCoreTxSelfInvocationPitfallLabTest`（自调用绕过事务的最小复现）

---

## 下一章怎么接

事务与 AOP 是底座，最终很多问题会落到“一个 HTTP 请求进来发生了什么”：我们从 Web MVC 请求主线开始把上层串起来。

- 下一章：[第 6 章：Web MVC 请求主线](06-webmvc-mainline.md)

