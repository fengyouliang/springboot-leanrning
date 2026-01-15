# 文档站点（MkDocs）

本目录用于把本仓库的“多模块 docs（Book Style / 专栏合集）”聚合成一个可搜索、可侧边栏导航的静态站点。

## 目标

- **像书一样可导航**：侧边栏按主题顺序组织，而不是按文件散落。
- **像专栏一样可阅读**：正文保持叙事式写法，结构化索引与串联交给站点层完成。
- **不改变 SSOT**：模块文档仍以各模块自身的 `docs/` 为事实来源；站点仅做聚合与构建。

## 使用方式（本地）

### 1) 同步（从各模块聚合到站点输入目录）

```bash
python3 scripts/docs-site-sync.py
```

### 2) 启动预览（需要安装 MkDocs 依赖）

> 依赖列表见：`docs-site/requirements.txt`

```bash
bash scripts/docs-site-serve.sh
```

### 3) 构建（严格模式）

```bash
bash scripts/docs-site-build.sh
```

## 目录说明

- `docs-site/mkdocs.yml`：站点配置（主题/导航/插件）
- `docs-site/content/`：站点手写内容（首页等），会被同步脚本复制到生成目录
- `docs-site/.generated/`：同步脚本生成的站点输入目录（不提交）
- `docs-site/.site/`：MkDocs build 输出目录（不提交）

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
