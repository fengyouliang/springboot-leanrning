# 项目技术约定（Project Technical Conventions）

## 技术栈

- **Java:** 17
- **构建工具:** Maven（多模块）
- **Spring Boot:** 由父 `pom.xml` 统一管理

## 代码与命名约定

- **模块组织:** 每个学习主题一个独立 Maven module（例如 `spring-core-beans`、`spring-core-events`）。
- **包名约定:** `com.learning.springboot.<module>`（例如 `com.learning.springboot.springcorebeans`）。
- **风格优先级:** 以当前仓库代码风格为准（避免为了“更优雅”而过度重构）。

## 测试与验证约定

- **测试框架:** JUnit 5 + AssertJ（由 `spring-boot-starter-test` 提供）
- **测试目标:** “可断言的观察点”优先于日志（能稳定复现实验结论）

### 测试类型约定（Labs / Exercises / Solutions）

> 约定：在本仓库里，“**测试就是教材的一部分**”。  
> 因此测试命名不仅用于回归，更用于表达“你应该验证什么”。

- **`*LabTest`（实验 / 证据链）**
  - 目标：用可断言的方式复现某个机制结论（主线/关键分支/边界条件）。
  - 特点：默认参与回归；断言关注“稳定契约/可观察行为”。
- **`*ExerciseTest`（练习 / 自己补齐）**
  - 目标：留出缺口，让学习者按提示完成实现/修复/补齐断言。
  - 特点：通常默认 `@Disabled`（避免 CI 回归失败）；通过提示把读者指向对应 doc 与推荐断点。
- **`*ExerciseSolutionTest`（参考答案 / 对照）**
  - 目标：提供 Exercise 的可运行参考实现，便于对照与自检。
  - 特点：默认参与回归；尽量复用 Exercise 的场景与断言口径。

### 断言粒度约定（Tests as SSOT）

- 结论以“断言可复现”为准；日志/`System.out.println("OBSERVE: ...")` 只作为辅助观察点。
- 尽量断言稳定契约与可观察信号（响应状态码、异常类型、DB 行数、调用轨迹计数等），避免把内部实现细节写死为强断言。
- 当需要断点观察内部机制时，优先写“推荐断点清单/观察点”，而不是把内部细节当作测试断言。

### 命令与运行约定

- **单模块测试：** `mvn -pl <module> test`
- **单测试类：** `mvn -pl <module> -Dtest=SomeTest test`
- **单测试方法：** `mvn -pl <module> -Dtest=SomeTest#someMethod test`
- **调试（attach 5005）：** `mvn -pl <module> -Dtest=SomeTest#someMethod -Dmaven.surefire.debug test`
- **脚本优先（便于统一）：**
  - `bash scripts/test-module.sh <module>`
  - `bash scripts/test-all.sh`
  - `bash scripts/check-docs.sh`（断链检查 + 教学覆盖）

### 文档 ↔ 测试入口绑定约定

- `docs/**.md` 章节的末尾应包含 `### 对应 Lab/Test` 区块（由 BOOKIFY 机制统一维护）。
- 文档引用一律使用可解析的 Markdown 相对链接（避免 `docs/NN` 这种缩写引用造成断链）。
- 如果文档结论依赖某个可复现分支，必须在文档中显式写出：
  - 推荐测试入口（类名/方法名）
  - 推荐断点/观察点（类/方法）

### Troubleshooting 条目模板（建议在 pitfalls/playbook 中统一采用）

> 目标：让读者能从“现象”快速回到“机制主线”，并落到“可验证入口”。

- **现象（Symptom）：** 你看到了什么？（状态码/异常/行为差异）
- **根因（Root Cause）：** 这通常对应哪个机制分支？（Bean 生命周期/AOP 调用链/事务边界/MVC 链路）
- **如何验证（Verification）：** 跑哪个 Lab/Test？断言看什么？
- **推荐断点（Breakpoints）：** 该从哪里下断点能最快看到关键分支？
- **修复建议（Fix）：** 学习用最小修复是什么？工程上推荐做法是什么？
