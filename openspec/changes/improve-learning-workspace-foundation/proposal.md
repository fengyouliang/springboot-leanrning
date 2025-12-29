# Change: Improve Learning Workspace Foundation

## Why
当前仓库已经具备较完整的 “Deep Dive Track（Labs + `@Disabled` Exercises）” 与多模块学习结构，但仍存在一些会影响学习效率与长期维护的小摩擦点：

- 学习者缺少统一的“进度/打卡”入口：不知道自己完成到哪、下一步做什么、每个模块的退出条件是什么。
- 对新手最常用的入口模块（`springboot-basics`、`springboot-web-mvc`）目前缺少 `docs/` 章节化讲解，阅读体验与 `spring-core-*` 模块不一致。
- 工程层面缺少最基本的“质量护栏”：CI、统一编辑器格式、JDK/Maven 版本约束等，可能导致“拉下来就跑不通”或出现与学习无关的噪音差异。

该变更优先补齐这些基础设施与导航能力，为后续新增模块（Security/WebClient/Async/Cache）提供一致的学习与维护底座。

## What Changes
- 新增一个仓库级学习进度入口（例如 `docs/progress.md`），并在根 `README.md` 中显式链接。
- 为 `springboot-basics` 与 `springboot-web-mvc` 增加最小 `docs/`（章节化短文），并在各自 `README.md` 中加入推荐阅读顺序与“概念→测试/代码”映射入口。
- 增加 GitHub Actions CI：默认执行 `mvn -q test`，确保主分支随时可运行、默认全绿。
- 增加 `.editorconfig`，统一缩进/换行符/编码，减少无意义 diff。
- 在根 `pom.xml` 增加 Maven Enforcer 约束（Java 17、Maven 版本下限），把“文档约定”升级为“构建期明确提示”。
- 提供轻量脚本（`scripts/`）封装常用命令（跑全量测试/跑单模块/运行单模块），降低初学者命令行门槛。

## Impact
- Affected specs:
  - `learning-workspace`
  - `learning-module-catalog`
  - `boot-basics-module`
  - `boot-web-mvc-module`
- Affected code (apply stage):
  - Root: `.github/workflows/*`, `.editorconfig`, `docs/*`, `README.md`, `pom.xml`, `scripts/*`
  - Modules: `springboot-basics/docs/*`, `springboot-basics/README.md`
  - Modules: `springboot-web-mvc/docs/*`, `springboot-web-mvc/README.md`

## Out of Scope
- 引入 Maven Wrapper（当前仓库约定为 system `mvn`）
- 引入重型基础设施依赖（Docker/Kafka/Redis 等）
- 对所有既有模块做大规模重排/重写（本变更只补齐基础底座与两个入口模块的文档一致性）

