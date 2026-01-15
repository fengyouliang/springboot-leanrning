# 文档站点（MkDocs）

本目录用于把本仓库的“多模块 docs（Book Style）”聚合成一个可搜索的静态站点，并提供一套跨模块可顺读的 **Book-only 主线之书**。

## 目标

- **像书一样可顺读**：侧边栏以“主线之书”为唯一目录（Book-only），读者从 0 章开始顺读到 18 章完成跨模块主线。
- **像专栏一样可深挖**：模块 docs 保留完整细节与边界案例（素材库），通过书内链接/站内搜索/附录入口访问。
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

- `docs-site/mkdocs.yml`：站点配置模板（主题/插件/基础导航；Book-only 目录由同步脚本自动生成注入）
- `docs-site/content/`：站点手写内容（首页等），会被同步脚本复制到生成目录
- `docs-site/.generated/`：同步脚本生成的站点输入目录（不提交）
- `docs-site/.generated/mkdocs.yml`：同步脚本生成的最终 MkDocs 配置（包含“主线之书”的目录树，不提交）
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
