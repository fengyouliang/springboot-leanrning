# 05. Fetching 与 N+1：为什么查一次会变成查很多次？

这一章以“学习路线图”的方式讲 N+1（本模块目前通过 Exercises 引导你亲手复现）。

## 什么是 N+1（直觉版）

你以为你在做：

- 1 次查询：查出列表（N 条记录）

实际发生的是：

- 1 次查询：查出列表
- N 次查询：对列表里的每一条记录再查一次关联数据

因此叫 N+1。

## 为什么会发生？

典型触发条件：

- 关联关系是懒加载（lazy）
- 你在循环中访问了关联属性
- persistence context/事务仍然活着，因此触发了额外 SQL

## 在本模块的练习入口

看 `BootDataJpaExerciseTest#exercise_relationshipsAndFetching`：

- 目标：新增一个实体关系（例如 `Author -> Books`）
- 然后复现一个 N+1 场景（并在测试里证明它发生了）

## 你应该得到的结论（比背解决方案更重要）

> N+1 不是“写错 SQL”，而是“加载策略 + 访问方式”共同决定的结果。

学习时建议先把问题复现清楚，再讨论常见解决手段（fetch join / entity graph / batch size 等）。

