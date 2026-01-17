#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
检查“正文二次书籍化（V2）”常见问题（可选闸门）。

本脚本用于补齐现有闸门（断链/卡片/coverage）之外的“阅读体验”质量检查：
- 空块/空标题（例如：空的“导读/证据链/小结与下一章/一句话总结”）
- redirect 页是否保持最小形态（是否包含“已迁移”与新位置链接）
- 章首已有实验提示框时，正文是否重复贴“实验入口清单”

用法：
  # 非严格（默认）：只输出问题清单，退出码=0
  python3 scripts/check-booklike-v2.py

  # 严格：发现问题退出码=1（适合作为 CI/local gate）
  python3 scripts/check-booklike-v2.py --strict

  # 指定模块（可重复）
  python3 scripts/check-booklike-v2.py --module springboot-basics --module spring-core-beans
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]

MD_LINK_WITH_TEXT_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

CHAPTER_LAB_CALLOUT_LINE = '!!! example "本章配套实验（先跑再读）"'

CHAPTER_CARD_START = "<!-- CHAPTER-CARD:START -->"
CHAPTER_CARD_END = "<!-- CHAPTER-CARD:END -->"


@dataclass(frozen=True)
class ChapterRef:
    kind: str  # module|book
    module: str
    path: str
    title: str


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


def iter_links_from_docs_readme(readme: Path) -> Iterable[tuple[str, str]]:
    content = readme.read_text(encoding="utf-8", errors="replace")
    for m in MD_LINK_WITH_TEXT_RE.finditer(content):
        is_image = m.group(1) == "!"
        if is_image:
            continue
        title = (m.group(2) or "").strip()
        target_raw = m.group(3)
        yield title, target_raw


def extract_title(md: Path) -> str | None:
    try:
        content = md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def iter_module_chapters(repo_root: Path, module_root: Path) -> list[ChapterRef]:
    readme = module_root / "docs" / "README.md"
    if not readme.is_file():
        return []

    index = 0
    last: dict[Path, tuple[int, str]] = {}
    for title, target_raw in iter_links_from_docs_readme(readme):
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
        last[chapter] = (index, title or chapter.name)

    ordered = sorted(last.items(), key=lambda it: it[1][0])
    out: list[ChapterRef] = []
    for chapter_path, (_, title_from_readme) in ordered:
        title = extract_title(chapter_path) or title_from_readme
        out.append(
            ChapterRef(
                kind="module",
                module=module_root.name,
                path=chapter_path.relative_to(repo_root).as_posix(),
                title=title,
            )
        )
    return out


def iter_book_chapters(repo_root: Path) -> list[ChapterRef]:
    root = repo_root / "docs-site" / "content" / "book"
    if not root.is_dir():
        return []
    out: list[ChapterRef] = []
    for md in sorted(root.rglob("*.md")):
        title = extract_title(md) or md.name
        out.append(ChapterRef(kind="book", module="", path=md.relative_to(repo_root).as_posix(), title=title))
    return out


def load_chapters(
    *,
    repo_root: Path,
    chapter_list: Path | None,
    include_modules: bool,
    include_book: bool,
    modules: list[str] | None,
) -> list[ChapterRef]:
    if chapter_list:
        raw = json.loads(chapter_list.read_text(encoding="utf-8"))
        chapters = [ChapterRef(**c) for c in raw]
    else:
        chapters: list[ChapterRef] = []
        if include_modules:
            for module_name in discover_modules(repo_root):
                if modules and module_name not in modules:
                    continue
                chapters.extend(iter_module_chapters(repo_root, repo_root / module_name))
        if include_book:
            chapters.extend(iter_book_chapters(repo_root))

    if modules:
        chapters = [c for c in chapters if c.kind != "module" or c.module in modules]
    if not include_modules:
        chapters = [c for c in chapters if c.kind != "module"]
    if not include_book:
        chapters = [c for c in chapters if c.kind != "book"]
    return chapters


def classify_page(title: str, path: Path) -> str:
    if "（Redirect）" in title or "已迁移" in title:
        return "redirect"
    tool_names = {
        "index.md",
        "labs-index.md",
        "debugger-pack.md",
        "exercises-and-solutions.md",
        "migration-rules.md",
    }
    if path.name in tool_names:
        return "tool"
    if "断点地图" in title or "Breakpoint Map" in title:
        return "tool"
    return "normal"


def normalize_section_title(title: str) -> str:
    t = title.strip()
    t = re.sub(r"[（(].*?[）)]", "", t).strip()
    return t


def split_h2_sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", text))
    if not matches:
        return []
    out: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        title = m.group(1).strip()
        body = text[start:end]
        out.append((title, body))
    return out


def is_effectively_empty(body: str) -> bool:
    cleaned = re.sub(r"(?s)<!--.*?-->", "", body).strip()
    if not cleaned:
        return True
    if re.fullmatch(r"(?is)(todo|tbd|pending|n/a|none|待补|未补齐|略)", cleaned):
        return True
    return len(cleaned) < 8


def find_links(text: str) -> list[str]:
    out: list[str] = []
    for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        dest = m.group(1).strip()
        if not dest or is_external_link(dest):
            continue
        out.append(dest)
    return out


def has_card_block(text: str) -> bool:
    start = text.find(CHAPTER_CARD_START)
    if start < 0:
        return False
    end = text.find(CHAPTER_CARD_END, start)
    return end >= 0


def check_page(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    title = extract_title(path) or path.name
    page_type = classify_page(title, path)
    issues: list[str] = []

    if not has_card_block(text):
        issues.append("缺少章节学习卡片（CHAPTER-CARD）")

    sections = split_h2_sections(text)
    norm_to_body = {normalize_section_title(t): b for (t, b) in sections}

    # 1) 空块检查（仅对高价值标题）
    watchlist = {"导读", "证据链", "小结与下一章", "一句话总结"}
    for sec_title, sec_body in sections:
        norm = normalize_section_title(sec_title)
        if norm in watchlist and is_effectively_empty(sec_body):
            issues.append(f"空块：`## {sec_title}`")

    # 2) redirect：必须有“已迁移” + 新位置链接
    if page_type == "redirect":
        if "已迁移" not in norm_to_body and "已迁移" not in (title or ""):
            issues.append("redirect 页缺少 `## 已迁移` 段落")
        links = find_links(text)
        if not any("/book/" in d or d.endswith(".md") for d in links):
            issues.append("redirect 页缺少新位置链接")

    # 3) 普通章：至少要有导读 + 证据链（或等价段落）+ 小结
    if page_type == "normal":
        has_intro = any(k in norm_to_body for k in ["导读", "本章定位", "前言"])
        if not has_intro:
            issues.append("缺少导读（`## 导读`）")

        has_evidence = any(
            k in norm_to_body
            for k in [
                "证据链",
                "你应该观察到什么",
                "源码与断点",
            ]
        )
        if not has_evidence:
            issues.append("缺少证据链段落（`## 证据链`/`## 你应该观察到什么`/`## 源码与断点`）")

        has_summary = any(k in norm_to_body for k in ["小结与下一章", "小结", "总结"])
        if not has_summary:
            issues.append("缺少小结（`## 小结与下一章`）")

    # 4) 重复实验入口：章首已有 example，但正文又重复贴清单
    if CHAPTER_LAB_CALLOUT_LINE in text:
        for sec_title, sec_body in sections:
            norm = normalize_section_title(sec_title)
            if norm.startswith("实验入口"):
                lines = [ln.strip() for ln in sec_body.splitlines() if ln.strip()]
                if len(lines) <= 8 and any("Lab" in ln or "Test" in ln for ln in lines):
                    issues.append("重复实验入口：章首已有实验提示框，正文仍重复贴 Lab/Test 清单")
                    break

    return issues


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="check-booklike-v2.py",
        description="检查正文二次书籍化（V2）常见问题（空块/redirect/重复实验入口）。",
    )
    parser.add_argument("--strict", action="store_true", help="严格模式：发现问题退出码=1")
    parser.add_argument("--chapter-list", help="章节清单 JSON（可选，默认自动发现）。")
    parser.add_argument("--include-modules", action="store_true", help="包含模块 docs 章节（默认开启）。")
    parser.add_argument("--exclude-modules", action="store_true", help="不包含模块 docs 章节。")
    parser.add_argument("--include-book", action="store_true", help="包含 Book-only 页面（默认开启）。")
    parser.add_argument("--exclude-book", action="store_true", help="不包含 Book-only 页面。")
    parser.add_argument("--module", action="append", default=[], help="仅检查指定模块（可重复）。")
    args = parser.parse_args(argv)

    include_modules = True
    include_book = True
    if args.include_modules or args.exclude_modules:
        include_modules = args.include_modules and not args.exclude_modules
    if args.include_book or args.exclude_book:
        include_book = args.include_book and not args.exclude_book

    chapter_list = Path(args.chapter_list).resolve() if args.chapter_list else None
    modules = args.module or None

    chapters = load_chapters(
        repo_root=REPO_ROOT,
        chapter_list=chapter_list,
        include_modules=include_modules,
        include_book=include_book,
        modules=modules,
    )
    if not chapters:
        print("[FAIL] No chapters to check (empty scope).", file=sys.stderr)
        return 2

    issues_total = 0
    scanned = 0
    for c in chapters:
        scanned += 1
        p = (REPO_ROOT / c.path).resolve()
        if not p.is_file():
            issues_total += 1
            print(f"[FAIL] {c.path}: file_missing")
            continue
        issues = check_page(p)
        if not issues:
            continue
        issues_total += len(issues)
        for it in issues:
            print(f"[FAIL] {c.path}: {it}")

    if issues_total == 0:
        print(f"[OK] scanned={scanned} issues=0")
        return 0

    print(f"[WARN] scanned={scanned} issues={issues_total}")
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
