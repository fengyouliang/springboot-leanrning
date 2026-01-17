# 文档站点（MkDocs）

本目录用于把本仓库根目录的统一文档目录 `docs/` 构建成一个可搜索的静态站点，并提供一套跨主题可顺读的 **Book-only 主线之书**。

## 目标

- **像书一样可顺读**：侧边栏以“主线之书”为唯一目录（Book-only），读者从 0 章开始顺读到 18 章完成跨模块主线。
- **像专栏一样可深挖**：主题文档保留完整细节与边界案例（素材库），通过书内链接/站内搜索/附录入口访问。
- **单一源文档（SSOT）**：所有文档以仓库根 `docs/` 为事实来源；站点仅做构建与发布。

## 使用方式（本地）

### 1)（可选）生成 Book-only 侧边栏目录

```bash
python3 scripts/docs-site-sync.py
```

### 2) 启动预览（需要安装 MkDocs 依赖）

> 依赖列表见：`docs-site/requirements.txt`

```bash
bash scripts/docs-site-serve.sh
```

### 3) 构建

```bash
bash scripts/docs-site-build.sh
```

## 目录说明

- `docs-site/mkdocs.yml`：站点配置（主题/插件/基础导航；Book-only 目录可由脚本自动生成注入）
- `docs/`：仓库统一文档目录（站点输入源）
- `docs-site/.site/`：MkDocs build 输出目录（不提交）

## 目录生成规则（Book-only）

Book-only 的侧边栏目录由 `scripts/docs-site-sync.py` 自动生成（注入到 `docs-site/mkdocs.yml` 的 AUTO BOOK NAV 区段），规则如下：

- **主线章节**：放在 `docs/book/` 下，文件名为 `NN-*.md`（`NN` 为两位数字，例如 `06-webmvc-mainline.md`）
  - 会按章节号排序，并按 Part 分卷分组（避免侧边栏变成长列表）
  - 目录标题会“短化”（侧边栏显示短标题，正文 `#` 标题可以保持完整）
- **附录页**：同目录下的其它 `.md`（例如 `labs-index.md`）会被收纳到“附录 → 其它”
- **固定附录入口**：Labs 索引 / Debugger Pack / Exercises & Solutions / 迁移规则 / 写作指南 / 知识库 / 模块入口，会以固定顺序出现在附录里

## GitHub Pages（自动构建 + 发布）

本仓库已提供 GitHub Actions workflow，可在 GitHub 上自动构建并发布站点到 GitHub Pages：

- Workflow 文件：`.github/workflows/docs-site-pages.yml`
- 触发条件：
  - `push` 到 `main/master`：构建 + 发布
  - `pull_request`：仅构建校验（不发布）
  - `workflow_dispatch`：手动触发

启用方式（一次性）：

1) 进入仓库 `Settings` → `Pages`
2) `Build and deployment` → `Source` 选择 `GitHub Actions`
3) 等待一次 workflow 成功执行后，在 `Pages` 页面可看到站点 URL
