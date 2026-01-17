# Change Proposal: 文档统一目录（docs/）+ 按主题重组（去模块 docs）

## Requirement Background

当前仓库的文档分散在两类位置：

1. 各模块自己的 `*/docs/**`（18 个模块，内容较多）
2. “主线之书”位于 `docs/book/**`（Book-only）

这会带来几个典型问题：

- **读者找路成本高**：同一主题的内容分散在不同模块路径里，很难“按主题聚合阅读”。
- **维护成本高**：一旦发生结构调整，需要同时处理多处入口与相对链接，改动面大、容易漏。
- **文档门禁/约束过强**：目前仓库内存在多种“文档闸门/严格校验”，会把文档组织方式绑定到特定脚本与规则上；这与“允许自由重组文档”的目标冲突。

本次改造的核心目标：把“所有文档源文件”收敛到仓库根目录的 `docs/` 作为单一事实来源（SSOT），并按主题归类到子文件夹中（例如 beans/aop/tx/...），同时彻底下线文档门禁脚本与相关约束。

---

## Change Content

1. 新增统一文档根目录：`docs/`
2. 将 `*/docs/**` 全量迁移到 `docs/<topic>/**`，并按主题重新组织（同主题文档进入同一子目录）
3. 将 `docs/book/**` 全量迁移到 `docs/book/**`
4. 全仓更新所有引用：Markdown 链接 / 脚本 / docs-site 导航 / 说明文档
5. 彻底移除/下线文档门禁脚本与相关约束（包括 strict build 与各种检查脚本的强制要求）

---

## Impact Scope

- **Modules:** 18 个模块（仅影响文档路径）+ `docs-site`
- **Files:** 大量 Markdown 文件移动/重命名 + 多处引用批量重写 + 删除/修改若干脚本与 CI workflow
- **APIs:** N/A
- **Data:** N/A

---

## Core Scenarios

### Requirement: 文档统一入口与可发现性
**Module:** docs
读者无需先进入某个模块目录，直接从 `docs/` 就能找到目标主题。

#### Scenario: 按主题集中查找
读者要学习 Bean/DI 相关内容时，能在 `docs/beans/` 一站式找到目录页与全部章节。
- 预期：同主题文档集中存放；目录结构清晰；入口 README 可直接跳转。

#### Scenario: Book 与主题文档共存
读者可从 `docs/book/` 顺读主线之书，也可从 `docs/<topic>/` 深挖细节。
- 预期：Book 章节与工具页在同一目录下；同时保留主题文档入口。

### Requirement: 单一源文档（移除模块 docs）
**Module:** all modules
迁移后不再保留 `*/docs/**` 目录，只保留 `docs/` 作为源文档。

#### Scenario: 去重与避免双写
维护者只需要修改 `docs/`，不会发生“模块 docs 与统一 docs 两份不一致”的问题。
- 预期：模块目录下无 `docs/`；所有引用已指向 `docs/`。

### Requirement: 下线文档门禁与强约束
**Module:** scripts + CI + docs-site
不再要求运行任何文档门禁脚本；CI/Pages 不应因为文档“严格校验”而阻塞。

#### Scenario: 不再存在文档闸门
仓库中不再保留 `check-docs.sh` 等聚合闸门脚本；也不再保留将“文档结构规则”强制化的校验链路。
- 预期：相关脚本与 workflow 被移除或改为非严格/非阻塞。

---

## Risk Assessment

- **Risk:** 大规模移动导致链接断裂、入口失效
  - **Mitigation:** 使用明确的迁移映射表 + 全仓批量替换 + `git mv` 保留历史；最终用全仓搜索确保旧路径引用清零。
- **Risk:** docs-site 构建/导航规则与新路径不兼容
  - **Mitigation:** 将 docs-site 的输入源切换到 `docs/`（或降低为非严格构建），保证基本可用；必要时下线 Pages workflow。
- **Risk:** 删除门禁脚本后，文档质量约束变弱
  - **Mitigation:** 本次变更目标就是解除强约束；后续如需质量检查，改为“可选工具/约定”，不再作为硬门禁。

