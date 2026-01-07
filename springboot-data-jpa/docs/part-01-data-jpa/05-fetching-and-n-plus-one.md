# 05. Fetching 与 N+1：为什么查一次会变成查很多次？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**05. Fetching 与 N+1：为什么查一次会变成查很多次？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

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

## 你应该得到的结论（比背解决方案更重要）

> N+1 不是“写错 SQL”，而是“加载策略 + 访问方式”共同决定的结果。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章未显式引用 LabTest，先注入模块默认 LabTest 作为“合规兜底入口”（后续可逐章细化）。
- Lab：`BootDataJpaDebugSqlLabTest` / `BootDataJpaLabTest`
- 建议命令：`mvn -pl springboot-data-jpa test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

这一章以“学习路线图”的方式讲 N+1（本模块目前通过 Exercises 引导你亲手复现）。

看 `BootDataJpaExerciseTest#exercise_relationshipsAndFetching`：

- 目标：新增一个实体关系（例如 `Author -> Books`）
- 然后复现一个 N+1 场景（并在测试里证明它发生了）

学习时建议先把问题复现清楚，再讨论常见解决手段（fetch join / entity graph / batch size 等）。

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootDataJpaDebugSqlLabTest` / `BootDataJpaLabTest`
- Exercise：`BootDataJpaExerciseTest`

上一章：[part-01-data-jpa/04-dirty-checking.md](04-dirty-checking.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-data-jpa/06-datajpatest-slice.md](06-datajpatest-slice.md)

<!-- BOOKIFY:END -->
