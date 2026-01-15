# 第 0 章：Start Here（如何运行、如何读、如何调试）

这本“主线之书”希望解决的是：**你能顺着一条时间线把 Spring Boot / Spring Core 的关键机制跑通**，并且每一步都能落到可验证的证据（测试断言、断点、源码）。

---

## 先把项目跑起来（5 分钟）

### 1) 全仓库跑一遍（推荐先做一次）

```bash
mvn -q test
```

### 2) 只跑某个模块（更快、更聚焦）

```bash
mvn -q -pl <module> test
```

例如：

```bash
mvn -q -pl springboot-web-mvc test
```

### 3) 运行某个模块（需要启动应用时）

```bash
mvn -pl <module> spring-boot:run
```

---

## Labs / Exercises：这套仓库是怎么“教你”机制的

你会在 `src/test/java` 里看到两类测试：

- **Labs**：`*LabTest.java`（默认启用，`mvn -q test` 必须全绿）  
  用来把机制的关键结论“固化成断言”，你可以边读边跑、边打断点边看数据结构如何变化。
- **Exercises**：`*ExerciseTest.java`（默认 `@Disabled`）  
  用来让你“动手改写/补齐”，把理解从“看懂”变成“能写出来”。

对应的索引页：

- [Labs 索引（可跑入口）](labs-index.md)
- [Exercises & Solutions（练习与答案）](exercises-and-solutions.md)

---

## 如何读主线（建议顺序）

如果你打算顺读，推荐从“启动 → 容器 → AOP/事务 → Web → 安全/数据 → 可观测性/测试 → 业务收束”读下去：

- 下一章入口：[第 1 章：Boot 启动与配置主线](01-boot-basics-mainline.md)

如果你是“带着问题来”的，建议：

1. 先在 [Debugger Pack](debugger-pack.md) 里把断点装好（入口/观察点/关键分支）
2. 再到模块 docs 的主线时间线章节找“完整机制图”
3. 最后回到对应 LabTest，用断言把结论固定下来

---

## 如何使用站点（Book-only 导航）

本书采用 **Book-only** 导航：侧边栏只展示“主线之书”的章节树。

- 模块 docs 仍然会出现在站点里（作为素材库/搜索命中/书内引用目标）
- 模块入口总览见：[模块文档总览](../modules/index.md)

如果你想本地预览文档站：

```bash
bash scripts/docs-site-serve.sh
```

严格构建（用于 CI/验收）：

```bash
bash scripts/docs-site-build.sh
```

---

## 下一步

- 继续顺读：[第 1 章：Boot 启动与配置主线](01-boot-basics-mainline.md)

