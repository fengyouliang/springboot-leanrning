#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
同步文档站输入目录（MkDocs docs_dir）。

设计目标：
1) 站点不作为 SSOT：SSOT 仍是各模块自己的 docs/ 与 helloagents/wiki；
2) 同步过程可重复执行（idempotent）：每次生成到 docs-site/.generated/docs；
3) 尽量保留原始目录结构，避免破坏模块内部相对链接；
4) 对于 docs 内指向 ../../src/... 的源码链接：在站点输入目录下同步对应 src 子树，避免站内 404。
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = REPO_ROOT / "docs-site"
CONTENT_ROOT = SITE_ROOT / "content"
GENERATED_ROOT = SITE_ROOT / ".generated" / "docs"


def discover_modules(repo_root: Path) -> list[str]:
    modules: list[str] = []
    for p in sorted(repo_root.iterdir()):
        if not p.is_dir():
            continue
        if (p / "docs" / "README.md").is_file():
            modules.append(p.name)
    return modules


def rm_rf(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
        return
    if path.is_dir():
        shutil.rmtree(path)


def copy_tree(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    if dst.exists():
        rm_rf(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst)


def copy_file(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def copy_content_pages() -> None:
    if not CONTENT_ROOT.exists():
        return

    for p in sorted(CONTENT_ROOT.rglob("*")):
        if p.is_dir():
            continue
        rel = p.relative_to(CONTENT_ROOT)
        copy_file(p, GENERATED_ROOT / rel)


def sync_helloagents() -> None:
    # 知识库（SSOT 在 helloagents/，站点只复制用于阅读）
    helloagents_root = REPO_ROOT / "helloagents"
    if not helloagents_root.exists():
        return

    copy_tree(helloagents_root / "wiki", GENERATED_ROOT / "helloagents" / "wiki")
    copy_file(helloagents_root / "project.md", GENERATED_ROOT / "helloagents" / "project.md")
    copy_file(helloagents_root / "history" / "index.md", GENERATED_ROOT / "helloagents" / "history" / "index.md")


def sync_modules(modules: list[str]) -> None:
    for module in modules:
        module_root = REPO_ROOT / module

        # 保持 module 根路径：<module>/docs 与 <module>/src 的相对关系不变
        copy_tree(module_root / "docs", GENERATED_ROOT / module / "docs")

        # 源码树（用于站内源码链接与排障时点击查看）
        copy_tree(module_root / "src" / "test" / "java", GENERATED_ROOT / module / "src" / "test" / "java")
        copy_tree(module_root / "src" / "test" / "resources", GENERATED_ROOT / module / "src" / "test" / "resources")
        copy_tree(module_root / "src" / "main" / "java", GENERATED_ROOT / module / "src" / "main" / "java")
        copy_tree(module_root / "src" / "main" / "resources", GENERATED_ROOT / module / "src" / "main" / "resources")


def generate_modules_index(modules: list[str]) -> None:
    # 主题顺序（未列出的模块按名称追加）
    preferred_order = [
        "springboot-basics",
        "spring-core-beans",
        "spring-core-aop",
        "spring-core-tx",
        "springboot-web-mvc",
    ]

    ordered: list[str] = []
    for m in preferred_order:
        if m in modules:
            ordered.append(m)
    for m in modules:
        if m not in ordered:
            ordered.append(m)

    lines: list[str] = []
    lines.append("# 模块文档总览")
    lines.append("")
    lines.append("说明：下列链接指向各模块的 `docs/README.md`（模块内目录页）。")
    lines.append("")
    lines.append("## 推荐顺序（主线）")
    lines.append("")
    for m in preferred_order:
        if m in modules:
            lines.append(f"- [{m}](../{m}/docs/README.md)")
    lines.append("")
    lines.append("## 全部模块")
    lines.append("")
    for m in ordered:
        lines.append(f"- [{m}](../{m}/docs/README.md)")
    lines.append("")

    out = GENERATED_ROOT / "modules" / "index.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="docs-site-sync.py",
        description="同步 docs-site/.generated/docs（MkDocs docs_dir）。",
    )
    parser.add_argument(
        "--module",
        action="append",
        default=[],
        help="仅同步指定模块（可重复）。例如：--module spring-core-beans",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv[1:])

    modules = args.module or discover_modules(REPO_ROOT)
    if not modules:
        print("[ERROR] 未发现任何包含 docs/README.md 的模块。", file=sys.stderr)
        return 2

    # 全量重建生成目录：保证同步结果可预测
    rm_rf(GENERATED_ROOT)
    GENERATED_ROOT.mkdir(parents=True, exist_ok=True)

    copy_content_pages()
    sync_helloagents()
    sync_modules(modules)
    generate_modules_index(modules)

    print(f"[OK] 已同步 {len(modules)} 个模块到 {GENERATED_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
