# spring-core-tx

本模块用于学习 **Spring 事务管理**：使用 `@Transactional` + 内嵌 H2 数据库演示提交与回滚。

包含内容：

- 使用 `@Transactional` 声明式事务
- 提交（commit）与回滚（rollback）行为
- 默认回滚规则：运行时异常会触发回滚

## 学习目标

- 理解什么是“事务边界”
- 直观看到 `@Transactional` 对数据库写入的影响
- 用测试验证回滚行为（插入 + 抛异常 → 最终不落库）

## 运行

```bash
mvn -pl spring-core-tx spring-boot:run
```

运行后观察控制台输出：

- Service 在事务内执行一段会抛异常的逻辑，然后检查表行数（回滚）
- Service 再执行一次成功事务，然后检查表行数（提交）

## 测试

```bash
mvn -pl spring-core-tx test
```

## Deep Dive（Labs / Exercises）

- Labs（默认启用）：`SpringCoreTxLabTest`
  - runtime vs checked exception 回滚规则
  - `Propagation.REQUIRES_NEW` 行为
  - `TransactionTemplate` 的程序化事务
- Exercises（默认禁用）：`SpringCoreTxExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl spring-core-tx test`。

## 小练习

- 把异常改成受检异常（checked exception），观察回滚规则如何变化
- 添加 `rollbackFor=...` 并更新测试
- 实现一个 `transfer(from,to,amount)`，并测试失败时不会“丢钱”

## 参考

- Spring Framework Reference：Transaction Management
