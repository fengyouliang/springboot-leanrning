#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
检查“章节学习卡片（五问闭环）”是否覆盖所有章节（SSOT）。

SSOT 口径：
- 模块章节：以每个模块 `docs/README.md` 内的 Markdown 链接清单为 SSOT（排除 README 本身）
- Book-only：`docs-site/content/book/**/*.md`

规则：
- 章节必须包含 `<!-- CHAPTER-CARD:START -->` 与 `<!-- CHAPTER-CARD:END -->`
- 卡片内必须包含以下 5 个字段（行内出现即可）：
  - 知识点
  - 怎么使用
  - 原理
  - 源码入口
  - 推荐 Lab

用法：
  python3 scripts/check-chapter-cards.py
  python3 scripts/check-chapter-cards.py --modules-only
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


MD_LINK_WITH_TEXT_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

CHAPTER_CARD_START = "<!-- CHAPTER-CARD:START -->"
CHAPTER_CARD_END = "<!-- CHAPTER-CARD:END -->"

REQUIRED_FIELDS = [
    "知识点：",
    "怎么使用：",
    "原理：",
    "源码入口：",
    "推荐 Lab：",
]


def is_external_link(dest: str) -> bool:
    if dest.startswith("#"):
        return True
    if dest.startswith("//"):
        return True
    return bool(SCHEME_RE.match(dest))


def normalize_md_link_target(raw: str) -> str | None:
    dest = raw.strip()
    if not dest:
        return None
    if dest.startswith("<") and dest.endswith(">"):
        dest = dest[1:-1].strip()
    if " " in dest or "\t" in dest:
        dest = re.split(r"\s+", dest, maxsplit=1)[0]
    if "#" in dest:
        dest = dest.split("#", 1)[0]
    return dest or None


def discover_modules(repo_root: Path) -> list[str]:
    modules: list[str] = []
    for p in sorted(repo_root.iterdir()):
        if not p.is_dir():
            continue
        if (p / "docs" / "README.md").is_file():
            modules.append(p.name)
    return modules


def iter_links_from_docs_readme(readme: Path) -> list[str]:
    content = readme.read_text(encoding="utf-8", errors="replace")
    targets: list[str] = []
    for m in MD_LINK_WITH_TEXT_RE.finditer(content):
        is_image = m.group(1) == "!"
        if is_image:
            continue
        target_raw = m.group(3)
        targets.append(target_raw)
    return targets


def iter_module_chapters(repo_root: Path, module_root: Path) -> list[Path]:
    readme = module_root / "docs" / "README.md"
    if not readme.is_file():
        return []

    index = 0
    last: dict[Path, int] = {}
    for target_raw in iter_links_from_docs_readme(readme):
        index += 1
        target = normalize_md_link_target(target_raw)
        if target is None or is_external_link(target):
            continue
        if not target.endswith(".md"):
            continue

        chapter = (readme.parent / target).resolve()
        try:
            chapter.relative_to(repo_root)
        except ValueError:
            continue
        if "/docs/" not in chapter.as_posix():
            continue
        if chapter == readme:
            continue
        last[chapter] = index

    ordered = [p for (p, _) in sorted(last.items(), key=lambda it: it[1])]
    return ordered


def iter_book_pages(repo_root: Path) -> list[Path]:
    book_root = repo_root / "docs-site" / "content" / "book"
    if not book_root.is_dir():
        return []
    return [p for p in sorted(book_root.rglob("*.md")) if p.is_file()]


def extract_chapter_card_block(text: str) -> str | None:
    start = text.find(CHAPTER_CARD_START)
    if start < 0:
        return None
    end = text.find(CHAPTER_CARD_END, start)
    if end < 0:
        return None
    return text[start : end + len(CHAPTER_CARD_END)]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="check-chapter-cards.py",
        description="检查章节学习卡片（五问闭环）覆盖情况。",
    )
    parser.add_argument("--modules-only", action="store_true", help="只检查模块 docs 章节（不检查 Book-only）")
    parser.add_argument("--book-only", action="store_true", help="只检查 Book-only（不检查模块 docs）")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    repo_root = Path(__file__).resolve().parents[1]
    args = parse_args(argv[1:])

    check_modules = not args.book_only
    check_book = not args.modules_only

    chapter_files: list[Path] = []
    if check_modules:
        for module in discover_modules(repo_root):
            chapter_files.extend(iter_module_chapters(repo_root, repo_root / module))
    if check_book:
        chapter_files.extend(iter_book_pages(repo_root))

    chapter_files = sorted(set(chapter_files))

    missing_cards: list[Path] = []
    missing_fields: list[tuple[Path, list[str]]] = []

    for p in chapter_files:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            missing_cards.append(p)
            continue

        block = extract_chapter_card_block(text)
        if block is None:
            missing_cards.append(p)
            continue

        miss: list[str] = []
        for field in REQUIRED_FIELDS:
            if field not in block:
                miss.append(field)
        if miss:
            missing_fields.append((p, miss))

    if missing_cards or missing_fields:
        if missing_cards:
            print(f"[FAIL] Missing chapter cards: {len(missing_cards)}")
            for p in missing_cards[:50]:
                print(f"- {p.relative_to(repo_root).as_posix()}")
            if len(missing_cards) > 50:
                print(f"... ({len(missing_cards) - 50} more)")
        if missing_fields:
            print(f"[FAIL] Chapter cards missing fields: {len(missing_fields)}")
            for p, miss in missing_fields[:50]:
                rel = p.relative_to(repo_root).as_posix()
                print(f"- {rel}: missing {', '.join(miss)}")
            if len(missing_fields) > 50:
                print(f"... ({len(missing_fields) - 50} more)")
        return 1

    print(f"[OK] Chapter cards: checked {len(chapter_files)} files, all present and complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(os.sys.argv))

