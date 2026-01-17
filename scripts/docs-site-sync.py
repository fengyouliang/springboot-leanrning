#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
为 MkDocs 文档站生成 Book-only 侧边栏目录（AUTO BOOK NAV 区段）。

SSOT 约定：
- 仓库根目录 `docs/` 是唯一源文档目录
- 主线之书（Book）位于 `docs/book/`
- docs-site 仅负责构建/发布，不复制/二次生成文档内容
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MKDOCS_YML = REPO_ROOT / "docs-site" / "mkdocs.yml"
BOOK_DIR = REPO_ROOT / "docs" / "book"

AUTO_NAV_BEGIN = "# BEGIN AUTO BOOK NAV"
AUTO_NAV_END = "# END AUTO BOOK NAV"

CHAPTER_RE = re.compile(r"^(?P<no>\d{3})-(?P<rest>.+)\.md$")

TOOL_PAGES: list[tuple[str, str]] = [
    ("Labs 索引", "book/labs-index.md"),
    ("Debugger Pack", "book/debugger-pack.md"),
    ("Exercises & Solutions", "book/exercises-and-solutions.md"),
    ("迁移规则", "book/migration-rules.md"),
]

EXTRA_PAGES: list[tuple[str, str]] = [
    ("写作指南", "book/book-style.md"),
]


def yaml_quote(s: str) -> str:
    escaped = s.replace("\\\\", "\\\\\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def read_first_h1_title(md_path: Path) -> str:
    try:
        text = md_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = md_path.read_text(encoding="utf-8", errors="ignore")

    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
        if line == "":
            continue
    return md_path.stem


def discover_book_chapters() -> list[Path]:
    if not BOOK_DIR.is_dir():
        return []

    candidates: list[tuple[int, Path]] = []
    for p in BOOK_DIR.glob("*.md"):
        if p.name in {"index.md", "book-style.md"}:
            continue
        m = CHAPTER_RE.match(p.name)
        if not m:
            continue
        no = int(m.group("no"))
        candidates.append((no, p))

    candidates.sort(key=lambda x: x[0])
    return [p for _, p in candidates]


def build_auto_nav_lines(indent: str) -> list[str]:
    lines: list[str] = []

    for chapter in discover_book_chapters():
        title = read_first_h1_title(chapter)
        lines.append(f"{indent}- {yaml_quote(title)}: book/{chapter.name}")

    # 附录（工具/参考）
    child_indent = indent + "  "
    lines.append(f"{indent}- {yaml_quote('附录')}:")
    for title, rel_path in TOOL_PAGES:
        lines.append(f"{child_indent}- {yaml_quote(title)}: {rel_path}")
    for title, rel_path in EXTRA_PAGES:
        lines.append(f"{child_indent}- {yaml_quote(title)}: {rel_path}")

    return lines


def inject_into_mkdocs_yml() -> int:
    if not MKDOCS_YML.is_file():
        print(f"[ERROR] 缺少 mkdocs.yml：{MKDOCS_YML}", file=sys.stderr)
        return 2

    raw_lines = MKDOCS_YML.read_text(encoding="utf-8").splitlines()

    begin_idx = -1
    end_idx = -1
    for i, line in enumerate(raw_lines):
        if AUTO_NAV_BEGIN in line:
            begin_idx = i
            continue
        if AUTO_NAV_END in line and begin_idx != -1:
            end_idx = i
            break

    if begin_idx == -1 or end_idx == -1 or end_idx <= begin_idx:
        print("[ERROR] 未在 docs-site/mkdocs.yml 中找到 AUTO BOOK NAV 标记（BEGIN/END）。", file=sys.stderr)
        return 2

    indent = raw_lines[begin_idx].split("#", 1)[0]
    auto_lines = build_auto_nav_lines(indent)

    out_lines = raw_lines[: begin_idx + 1] + auto_lines + raw_lines[end_idx:]
    MKDOCS_YML.write_text("\n".join(out_lines) + "\n", encoding="utf-8")

    print(f"[OK] 已更新 {MKDOCS_YML}（chapters={len(discover_book_chapters())}）")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成 Book-only 侧边栏（注入到 docs-site/mkdocs.yml）。")
    parser.add_argument("--check", action="store_true", help="仅检查输入是否齐备，不写文件。")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv[1:])

    if args.check:
        if not MKDOCS_YML.is_file():
            print(f"[ERROR] 缺少 mkdocs.yml：{MKDOCS_YML}", file=sys.stderr)
            return 2
        if not BOOK_DIR.is_dir():
            print(f"[ERROR] 缺少 Book 目录：{BOOK_DIR}", file=sys.stderr)
            return 2
        chapters = discover_book_chapters()
        print(f"[OK] chapters={len(chapters)}")
        return 0

    return inject_into_mkdocs_yml()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
