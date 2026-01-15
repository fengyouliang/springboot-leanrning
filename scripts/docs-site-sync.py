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
GENERATED_MKDOCS_YML = SITE_ROOT / ".generated" / "mkdocs.yml"
BASE_MKDOCS_YML = SITE_ROOT / "mkdocs.yml"
AUTO_NAV_BEGIN = "# BEGIN AUTO MODULE NAV"
AUTO_NAV_END = "# END AUTO MODULE NAV"


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


def yaml_quote(s: str) -> str:
    escaped = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def read_first_h1_title(md_path: Path) -> str:
    try:
        text = md_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # 兜底：尽量不因单文件编码问题阻塞站点生成
        text = md_path.read_text(encoding="utf-8", errors="ignore")

    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
        if line == "":
            continue
    return md_path.stem


def format_group_title(group: str) -> str:
    if group == "appendix":
        return "Appendix"

    if group.startswith("part-"):
        # part-01-ioc-container -> Part 01：IoC Container
        rest = group.removeprefix("part-")
        parts = rest.split("-")
        if len(parts) >= 2 and parts[0].isdigit():
            part_no = parts[0]
            tokens = parts[1:]
        else:
            part_no = ""
            tokens = parts

        def fmt_token(t: str) -> str:
            mapping = {
                "ioc": "IoC",
                "aop": "AOP",
                "mvc": "MVC",
                "tx": "Tx",
                "jpa": "JPA",
                "ltw": "LTW",
                "ctw": "CTW",
                "sse": "SSE",
                "api": "API",
                "http": "HTTP",
                "json": "JSON",
                "xml": "XML",
                "aot": "AOT",
            }
            if t in mapping:
                return mapping[t]
            if t.isdigit():
                return t
            return t[:1].upper() + t[1:].lower()

        title = " ".join(fmt_token(t) for t in tokens if t)
        if part_no:
            return f"Part {part_no}：{title or group}"
        return f"Part：{title or group}"

    # fallback
    return group.replace("-", " ")


def build_module_nav_entries(module: str) -> list[str]:
    module_root = REPO_ROOT / module
    docs_root = module_root / "docs"
    if not docs_root.exists():
        return []

    # 分组：按 docs 下的一级目录（part-xx-*/appendix）
    groups: dict[str, list[Path]] = {}
    for md in sorted(docs_root.rglob("*.md")):
        rel = md.relative_to(docs_root)
        if rel.name == "README.md":
            continue
        if len(rel.parts) < 2:
            # docs 根目录下的零散 md（通常不会有），避免污染目录
            continue
        group = rel.parts[0]
        groups.setdefault(group, []).append(md)

    def group_sort_key(name: str) -> tuple[int, int, str]:
        if name.startswith("part-"):
            rest = name.removeprefix("part-")
            head = rest.split("-", 1)[0]
            if head.isdigit():
                return (0, int(head), name)
            return (0, 999, name)
        if name == "appendix":
            return (2, 0, name)
        return (1, 0, name)

    lines: list[str] = []
    lines.append(f'          - {yaml_quote(module)}:')
    lines.append(f'              - {yaml_quote("目录")}: {module}/docs/README.md')

    for group in sorted(groups.keys(), key=group_sort_key):
        title = format_group_title(group)
        lines.append(f'              - {yaml_quote(title)}:')
        for md in sorted(groups[group], key=lambda p: p.name):
            rel_to_module = md.relative_to(module_root).as_posix()
            page_title = read_first_h1_title(md)
            lines.append(f'                  - {yaml_quote(page_title)}: {module}/{rel_to_module}')

    return lines


def generate_mkdocs_config(modules: list[str]) -> None:
    """
    生成 docs-site/.generated/mkdocs.yml：在基础 mkdocs.yml 上注入“模块详细目录”。

    这样做的原因：模块章节很多（200+），手写 nav 难维护；以同步脚本生成目录更稳定。
    """
    if not BASE_MKDOCS_YML.exists():
        return

    raw_template_lines = BASE_MKDOCS_YML.read_text(encoding="utf-8").splitlines()

    # 生成的 mkdocs.yml 位于 docs-site/.generated/ 下，需调整相对路径：
    # - docs_dir: docs-site/.generated/docs -> 相对 GENERATED_MKDOCS_YML 为 "docs"
    # - site_dir: docs-site/.site -> 相对 GENERATED_MKDOCS_YML 为 "../.site"
    template_lines: list[str] = []
    for line in raw_template_lines:
        stripped = line.strip()
        if stripped.startswith("docs_dir:"):
            template_lines.append("docs_dir: docs")
            continue
        if stripped.startswith("site_dir:"):
            template_lines.append("site_dir: ../.site")
            continue
        template_lines.append(line)

    begin_idx = -1
    end_idx = -1
    for i, line in enumerate(template_lines):
        if AUTO_NAV_BEGIN in line:
            begin_idx = i
        if AUTO_NAV_END in line:
            end_idx = i
            break

    if begin_idx == -1 or end_idx == -1 or end_idx <= begin_idx:
        print("[WARN] 未在 docs-site/mkdocs.yml 中找到 AUTO MODULE NAV 标记，跳过生成 mkdocs 配置。", file=sys.stderr)
        return

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

    auto_lines: list[str] = []
    auto_lines.append(f'      - {yaml_quote("推荐顺序（主线）")}:')
    for m in preferred_order:
        if m in modules:
            auto_lines.append(f'          - {yaml_quote(m)}: {m}/docs/README.md')

    auto_lines.append(f'      - {yaml_quote("全部模块（快速入口）")}:')
    for m in ordered:
        auto_lines.append(f'          - {yaml_quote(m)}: {m}/docs/README.md')

    auto_lines.append(f'      - {yaml_quote("全部模块（详细目录）")}:')
    for m in ordered:
        auto_lines.extend(build_module_nav_entries(m))

    GENERATED_MKDOCS_YML.parent.mkdir(parents=True, exist_ok=True)
    out_lines = template_lines[:begin_idx] + auto_lines + template_lines[end_idx + 1 :]
    GENERATED_MKDOCS_YML.write_text("\n".join(out_lines) + "\n", encoding="utf-8")


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
    generate_mkdocs_config(modules)

    print(f"[OK] 已同步 {len(modules)} 个模块到 {GENERATED_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
