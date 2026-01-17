#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
全站章节“全书化编号”（Chapter ID）批处理：

目标：
1) 以“最合理学习顺序”为基线，生成全书章节顺序（Start Here → 各模块主线 → 模块章节）。
2) 为每个章节分配全局唯一 Chapter ID（001-...），并把 Chapter ID 固化到文件名：
   - Book-only 主线章节：docs-site/content/book/00-18 对应的主线章节页（不包含 index/tool pages）
   - 模块章节：以各模块 docs/README.md 链接清单为 SSOT 的章节集合（排除 README 本身）
3) 批量修复 Markdown 相对链接：根据“旧路径 → 新路径”的映射表重写链接目标，避免断链。
4) 为每个章节 upsert 全书导航（上一章 / 全书目录 / 下一章），使任意一章都可顺读到底。

重要约束：
- 默认不重命名 book 的 index/tool pages（index.md、labs-index.md、debugger-pack.md 等），它们是目录/附录。
- 默认不重命名各模块 docs/README.md（它们是模块目录页，不视为章节）。
- 不改写正文知识点，只做“文件名编号 + 修链 + 全书导航”。

用法：
  python3 scripts/bookify-global-chapters.py --dry-run --map-out helloagents/plan/.../chapter-map.json
  python3 scripts/bookify-global-chapters.py --map-out helloagents/plan/.../chapter-map.json
"""

from __future__ import annotations

import argparse
import json
import os
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "scripts" / "book-order.json"
CONTENT_ROOT = REPO_ROOT / "docs-site" / "content"

MD_LINK_WITH_TEXT_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")
LINK_REF_DEF_RE = re.compile(r"^\s*\[[^\]]+]:\s*(\S+)")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

GLOBAL_PREFIX_RE = re.compile(r"^(?P<no>\d{3})-(?P<rest>.+)$")
BOOK_LEGACY_PREFIX_RE = re.compile(r"^(?P<no>\d{2})-(?P<rest>.+)$")

GLOBAL_NAV_START = "<!-- GLOBAL-BOOK-NAV:START -->"
GLOBAL_NAV_END = "<!-- GLOBAL-BOOK-NAV:END -->"

CHAPTER_CARD_END = "<!-- CHAPTER-CARD:END -->"

CHAPTER_TITLE_RE = re.compile(r"^第\s*(?P<no>\d+)\s*章[:：]\s*(?P<rest>.+)$")


@dataclass(frozen=True)
class ChapterItem:
    kind: str  # book|module
    module: str  # module name for module chapters, "" for book
    rel_path: str  # repo-relative posix path
    title: str  # best-effort H1 title


def is_external_link(dest: str) -> bool:
    if dest.startswith("#"):
        return True
    if dest.startswith("//"):
        return True
    return bool(SCHEME_RE.match(dest))


def strip_angle_brackets(s: str) -> str:
    s = s.strip()
    if s.startswith("<") and s.endswith(">"):
        return s[1:-1].strip()
    return s


def split_dest_and_anchor(dest: str) -> tuple[str, str]:
    """
    Returns (path_part, anchor_part_with_hash_or_empty)
    """
    if "#" in dest:
        path, anchor = dest.split("#", 1)
        return path, "#" + anchor
    return dest, ""


def normalize_destination_for_rewrite(raw: str) -> str | None:
    dest = strip_angle_brackets(raw)
    if not dest:
        return None
    if " " in dest or "\t" in dest:
        dest = re.split(r"\s+", dest, maxsplit=1)[0]
    dest = unquote(dest)
    return dest or None


def read_first_h1_title(md_path: Path) -> str:
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return md_path.stem
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("# "):
            return line.removeprefix("# ").strip() or md_path.stem
        if line == "":
            continue
    return md_path.stem


def rewrite_h1_with_chapter_no(text: str, chapter_no: int) -> tuple[str, str, bool]:
    """
    将第一个 H1 统一改为“第 N 章：xxx”。
    返回 (new_text, new_title, changed)
    """
    lines = text.splitlines(keepends=True)
    for i, raw in enumerate(lines):
        if not raw.startswith("# "):
            continue
        old_title = raw.removeprefix("# ").strip()
        if not old_title:
            continue

        m = CHAPTER_TITLE_RE.match(old_title)
        rest = m.group("rest") if m else old_title
        new_title = f"第 {chapter_no} 章：{rest}"
        new_line = "# " + new_title + ("\n" if raw.endswith("\n") else "")
        if new_line == raw:
            return text, new_title, False
        lines[i] = new_line
        new_text = "".join(lines)
        return new_text, new_title, True

    # 没有 H1：保持不变
    return text, "", False


def upsert_chapter_title(md_file: Path, chapter_no: int) -> tuple[bool, str]:
    try:
        original = md_file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        original = md_file.read_text(encoding="utf-8", errors="replace")

    new_text, new_title, changed = rewrite_h1_with_chapter_no(original, chapter_no)
    if changed:
        md_file.write_text(new_text, encoding="utf-8")
    if not new_title:
        new_title = read_first_h1_title(md_file)
    return changed, new_title


def strip_numeric_prefix_from_stem(stem: str) -> str:
    """
    统一把 "001-xxx" / "01-xxx" 这类前缀去掉，返回 slug。
    """
    m = GLOBAL_PREFIX_RE.match(stem)
    if m:
        return m.group("rest")
    m = BOOK_LEGACY_PREFIX_RE.match(stem)
    if m:
        return m.group("rest")
    return stem


def discover_modules(repo_root: Path) -> list[str]:
    modules: list[str] = []
    for p in sorted(repo_root.iterdir()):
        if not p.is_dir():
            continue
        if (p / "docs" / "README.md").is_file():
            modules.append(p.name)
    return modules


def iter_links_from_docs_readme(readme: Path) -> Iterable[str]:
    content = readme.read_text(encoding="utf-8", errors="replace")
    for m in MD_LINK_WITH_TEXT_RE.finditer(content):
        is_image = m.group(1) == "!"
        if is_image:
            continue
        yield m.group(3)


def iter_module_chapters_ordered(repo_root: Path, module_root: Path) -> list[Path]:
    readme = module_root / "docs" / "README.md"
    if not readme.is_file():
        return []

    index = 0
    last: dict[Path, int] = {}
    for target_raw in iter_links_from_docs_readme(readme):
        index += 1
        dest = normalize_destination_for_rewrite(target_raw)
        if dest is None or is_external_link(dest):
            continue
        path_part, _ = split_dest_and_anchor(dest)
        if not path_part.endswith(".md"):
            continue
        chapter = (readme.parent / path_part).resolve()
        try:
            chapter.relative_to(repo_root)
        except ValueError:
            continue
        if "/docs/" not in chapter.as_posix():
            continue
        if chapter == readme.resolve():
            continue
        last[chapter] = index

    ordered = [p for (p, _) in sorted(last.items(), key=lambda it: it[1])]
    return ordered


def find_book_page_by_slug(book_root: Path, slug: str) -> Path | None:
    """
    在 docs-site/content/book 下查找主线章节页：
    - 允许旧命名：00-start-here.md（stem 去掉两位前缀后 == slug）
    - 允许新命名：001-start-here.md（stem 去掉三位前缀后 == slug）
    """
    for md in sorted(book_root.glob("*.md")):
        if not md.is_file():
            continue
        if md.name in {"index.md", "labs-index.md", "debugger-pack.md", "exercises-and-solutions.md", "migration-rules.md"}:
            continue
        stem_slug = strip_numeric_prefix_from_stem(md.stem)
        if stem_slug == slug:
            return md
    return None


def load_config(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    return json.loads(raw)


def build_chapter_list(config: dict) -> list[ChapterItem]:
    book_root = REPO_ROOT / "docs-site" / "content" / "book"

    module_order: list[str] = config.get("module_order") or []
    if not module_order:
        raise SystemExit("[ERROR] book-order.json missing module_order")

    all_modules = set(discover_modules(REPO_ROOT))
    missing = [m for m in module_order if m not in all_modules]
    if missing:
        raise SystemExit(f"[ERROR] module_order contains missing modules: {missing}")

    slug_by_module: dict[str, str] = config.get("book", {}).get("mainline_slug_by_module", {}) or {}
    start_here_slug: str = config.get("book", {}).get("start_here_slug") or "start-here"

    chapters: list[ChapterItem] = []

    # 0) Start Here（作为全书第一章）
    start_page = find_book_page_by_slug(book_root, start_here_slug)
    if start_page is None:
        raise SystemExit(f"[ERROR] Cannot find book start-here page by slug: {start_here_slug}")
    chapters.append(
        ChapterItem(
            kind="book",
            module="",
            rel_path=start_page.relative_to(REPO_ROOT).as_posix(),
            title=read_first_h1_title(start_page),
        )
    )

    # 1) 每个模块：先主线章节，再模块内部章节
    for module in module_order:
        slug = slug_by_module.get(module)
        if not slug:
            raise SystemExit(f"[ERROR] book.mainline_slug_by_module missing module: {module}")
        page = find_book_page_by_slug(book_root, slug)
        if page is None:
            raise SystemExit(f"[ERROR] Cannot find book mainline page for module={module}, slug={slug}")
        chapters.append(
            ChapterItem(
                kind="book",
                module="",
                rel_path=page.relative_to(REPO_ROOT).as_posix(),
                title=read_first_h1_title(page),
            )
        )

        module_root = REPO_ROOT / module
        for p in iter_module_chapters_ordered(REPO_ROOT, module_root):
            chapters.append(
                ChapterItem(
                    kind="module",
                    module=module,
                    rel_path=p.relative_to(REPO_ROOT).as_posix(),
                    title=read_first_h1_title(p),
                )
            )

    # 去重（保留第一次出现）
    seen: set[str] = set()
    ordered: list[ChapterItem] = []
    for c in chapters:
        if c.rel_path in seen:
            continue
        seen.add(c.rel_path)
        ordered.append(c)
    return ordered


def compute_new_rel_path(chapter_no: int, item: ChapterItem) -> str:
    p = Path(item.rel_path)

    if item.kind == "book":
        # book 主线页：去掉旧两位编号，保留 slug，再加三位全局编号
        slug = strip_numeric_prefix_from_stem(p.stem)
        new_name = f"{chapter_no:03d}-{slug}{p.suffix}"
        return p.with_name(new_name).as_posix()

    # module 章节：保留原文件名（去掉已有全局前缀），再加三位全局编号
    name = p.name
    m = GLOBAL_PREFIX_RE.match(p.stem)
    if m:
        # 形如 123-03-mainline-timeline.md -> 03-mainline-timeline.md
        name = m.group("rest") + p.suffix
    new_name = f"{chapter_no:03d}-{name}"
    return p.with_name(new_name).as_posix()


def build_path_map(chapters: list[ChapterItem]) -> tuple[dict[str, str], list[dict]]:
    rename_mapping: dict[str, str] = {}
    rewrite_mapping: dict[str, str] = {}
    manifest: list[dict] = []

    for idx, item in enumerate(chapters, start=1):
        old_rel = item.rel_path
        new_rel = compute_new_rel_path(idx, item)
        rename_mapping[old_rel] = new_rel
        rewrite_mapping[old_rel] = new_rel

        # 额外为“旧文件名”（不带全局编号）提供 alias：
        # 1) module 章节：去掉 001- 前缀，便于修复 book/ 中引用旧文件名的链接
        if item.kind == "module":
            p = Path(new_rel)
            m = GLOBAL_PREFIX_RE.match(p.stem)
            if m:
                legacy_name = m.group("rest") + p.suffix
                legacy_rel = p.with_name(legacy_name).as_posix()
                rewrite_mapping.setdefault(legacy_rel, new_rel)

        manifest.append(
            {
                "chapter_no": idx,
                "kind": item.kind,
                "module": item.module,
                "old_path": old_rel,
                "new_path": new_rel,
                "title": item.title,
            }
        )

    # 冲突检测：new_path 必须唯一
    seen_new: dict[str, str] = {}
    for old_rel, new_rel in rename_mapping.items():
        if new_rel in seen_new and seen_new[new_rel] != old_rel:
            raise SystemExit(f"[ERROR] Collision: {new_rel} from {old_rel} and {seen_new[new_rel]}")
        seen_new[new_rel] = old_rel

    return rename_mapping, rewrite_mapping, manifest


def rename_files(repo_root: Path, mapping: dict[str, str], dry_run: bool) -> int:
    ops: list[tuple[Path, Path]] = []
    for old_rel, new_rel in mapping.items():
        old_abs = (repo_root / old_rel).resolve()
        new_abs = (repo_root / new_rel).resolve()
        if old_abs == new_abs:
            continue
        if not old_abs.exists():
            raise SystemExit(f"[ERROR] Missing source file for rename: {old_rel}")
        ops.append((old_abs, new_abs))

    if not ops:
        return 0

    # 两阶段 rename：避免 A->B 与 B->C 这种链式冲突
    tmp_ops: list[tuple[Path, Path]] = []
    for i, (src, dst) in enumerate(ops, start=1):
        tmp = src.with_name(f".__tmp__global_bookify__{i:04d}__{src.name}")
        tmp_ops.append((tmp, dst))
        if not dry_run:
            src.rename(tmp)

    if not dry_run:
        for tmp, dst in tmp_ops:
            dst.parent.mkdir(parents=True, exist_ok=True)
            if dst.exists():
                raise SystemExit(f"[ERROR] Rename target already exists: {dst.relative_to(repo_root)}")
            tmp.rename(dst)

    return len(ops)


def resolve_book_abs_link_to_repo_path(dest: str) -> Path | None:
    """
    解析 /book/... 的站点绝对链接到仓库真实文件路径（docs-site/content/book/*.md）。
    返回 repo_root 下的绝对 Path。
    """
    if dest == "/book" or dest == "/book/":
        return REPO_ROOT / "docs-site" / "content" / "book" / "index.md"

    if not dest.startswith("/book/"):
        return None

    rest = dest.removeprefix("/book/")
    if not rest:
        return REPO_ROOT / "docs-site" / "content" / "book" / "index.md"

    # /book/<slug>/ 这种形式
    if rest.endswith("/"):
        slug = rest.rstrip("/")
        return REPO_ROOT / "docs-site" / "content" / "book" / f"{slug}.md"

    # /book/<file>.md 这种形式
    if rest.endswith(".md"):
        return REPO_ROOT / "docs-site" / "content" / "book" / rest

    # /book/<slug> 也当作 slug
    return REPO_ROOT / "docs-site" / "content" / "book" / f"{rest}.md"


def rewrite_one_dest(
    repo_root: Path,
    current_md: Path,
    raw_dest: str,
    mapping: dict[str, str],
    *,
    site_mode: bool,
) -> str:
    dest = normalize_destination_for_rewrite(raw_dest)
    if dest is None:
        return raw_dest
    if is_external_link(dest):
        return raw_dest

    dest_path, anchor = split_dest_and_anchor(dest)

    # 1) /book/... 特殊处理：保留 /book/ 的风格，但更新 slug
    if dest_path.startswith("/book"):
        target = resolve_book_abs_link_to_repo_path(dest_path)
        if target is None:
            return raw_dest
        try:
            old_rel = target.relative_to(repo_root).as_posix()
        except ValueError:
            return raw_dest
        new_rel = mapping.get(old_rel)
        if not new_rel:
            return raw_dest
        new_name = Path(new_rel).name
        new_slug = Path(new_name).stem

        if dest_path in {"/book", "/book/"}:
            new_dest = dest_path
        elif dest_path.endswith("/"):
            new_dest = f"/book/{new_slug}/"
        elif dest_path.endswith(".md"):
            new_dest = f"/book/{new_slug}.md"
        else:
            new_dest = f"/book/{new_slug}"
        return new_dest + anchor

    # 2) 其它绝对路径：/xxx → repo_root/xxx
    if dest_path.startswith("/"):
        target = (repo_root / dest_path.lstrip("/")).resolve()
        try:
            old_rel = target.relative_to(repo_root).as_posix()
        except ValueError:
            return raw_dest
        new_rel = mapping.get(old_rel)
        if not new_rel:
            return raw_dest
        new_dest = "/" + new_rel
        return new_dest + anchor

    # 3) 相对路径：按 current_md.parent 解析
    if not site_mode:
        target = (current_md.parent / dest_path).resolve()
        try:
            old_rel = target.relative_to(repo_root).as_posix()
        except ValueError:
            return raw_dest

        new_rel = mapping.get(old_rel)
        if not new_rel:
            return raw_dest

        new_target = (repo_root / new_rel).resolve()
        rel_from_current = os.path.relpath(new_target, start=current_md.parent)
        rel_posix = Path(rel_from_current).as_posix()
        return rel_posix + anchor

    # site-mode：按 MkDocs docs_dir 的“虚拟路径”解析，再映射回仓库路径
    try:
        repo_rel = current_md.relative_to(repo_root).as_posix()
    except ValueError:
        return raw_dest

    if repo_rel.startswith("docs-site/content/"):
        current_site = Path(repo_rel).relative_to("docs-site/content").as_posix()
    else:
        current_site = repo_rel

    current_site_dir = posixpath.dirname(current_site) or "."
    target_site = posixpath.normpath(posixpath.join(current_site_dir, dest_path))

    # 先尝试 content（book/index/tool 等），再回退到 repo_root（模块 docs 等）
    if target_site.startswith("book/"):
        target_repo = (CONTENT_ROOT / target_site)
    else:
        candidate = CONTENT_ROOT / target_site
        target_repo = candidate if candidate.exists() else (repo_root / target_site)

    try:
        old_rel = target_repo.relative_to(repo_root).as_posix()
    except ValueError:
        return raw_dest

    new_rel = mapping.get(old_rel)
    if not new_rel:
        return raw_dest

    new_repo = (repo_root / new_rel).resolve()
    try:
        new_repo_rel = new_repo.relative_to(repo_root).as_posix()
    except ValueError:
        return raw_dest

    if new_repo_rel.startswith("docs-site/content/"):
        new_site = Path(new_repo_rel).relative_to("docs-site/content").as_posix()
    else:
        new_site = new_repo_rel

    rel_in_site = posixpath.relpath(new_site, start=current_site_dir)
    return rel_in_site + anchor


def rewrite_markdown_links_in_file(repo_root: Path, md_file: Path, mapping: dict[str, str]) -> bool:
    """
    仅重写 markdown 链接目标（不改正文其它部分）：
    - 跳过 fenced code block（```）内容，避免误伤代码示例。
    """
    try:
        original = md_file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        original = md_file.read_text(encoding="utf-8", errors="replace")

    in_fence = False
    changed = False
    out_lines: list[str] = []

    # 只对 docs-site/content 下的页面启用 site-mode：
    # - 这些页面在 MkDocs 中的路径与仓库路径不同（例如 docs-site/content/book -> book）
    # - 模块 docs 仍需保持“仓库相对链接可解析”，以通过 scripts/check-md-relative-links.py
    site_mode = False
    try:
        site_mode = md_file.is_relative_to(CONTENT_ROOT)
    except AttributeError:
        # Python 3.8 兼容：用 ValueError fallback
        try:
            md_file.relative_to(CONTENT_ROOT)
            site_mode = True
        except ValueError:
            site_mode = False

    for line in original.splitlines(keepends=False):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue

        new_line = line

        # inline links
        def repl(m: re.Match[str]) -> str:
            nonlocal changed
            prefix = m.group(1) or ""
            text = m.group(2) or ""
            dest_raw = m.group(3) or ""

            new_dest = rewrite_one_dest(repo_root, md_file, dest_raw, mapping, site_mode=site_mode)
            if new_dest != dest_raw:
                changed = True
            return f"{prefix}[{text}]({new_dest})"

        new_line = MD_LINK_WITH_TEXT_RE.sub(repl, new_line)

        # reference definitions: [id]: target
        ref = LINK_REF_DEF_RE.search(new_line)
        if ref:
            dest_raw = ref.group(1)
            new_dest = rewrite_one_dest(repo_root, md_file, dest_raw, mapping, site_mode=site_mode)
            if new_dest != dest_raw:
                changed = True
                new_line = new_line[: ref.start(1)] + new_dest + new_line[ref.end(1) :]

        out_lines.append(new_line)

    if not changed:
        return False

    new_text = "\n".join(out_lines) + ("\n" if original.endswith("\n") else "")
    md_file.write_text(new_text, encoding="utf-8")
    return True


def iter_markdown_files_for_rewrite(repo_root: Path) -> list[Path]:
    """
    只重写“活文档”：
    - 根 README.md
    - docs-site/content（book pages）
    - 各模块 docs（含 docs/README.md）
    - helloagents/wiki（项目知识库入口）

    排除：
    - helloagents/history（历史归档，保持原样）
    - helloagents/plan（正在执行的方案包后面单独维护）
    - docs-site/.generated/.site（生成物）
    """
    roots: list[Path] = []
    roots.append(repo_root / "README.md")
    roots.append(repo_root / "docs-site" / "content")
    roots.append(repo_root / "helloagents" / "wiki")

    for module in discover_modules(repo_root):
        roots.append(repo_root / module / "docs")

    md_files: list[Path] = []
    for root in roots:
        if root.is_file() and root.suffix == ".md":
            md_files.append(root)
            continue
        if not root.is_dir():
            continue
        for p in root.rglob("*.md"):
            if not p.is_file():
                continue
            # 排除 history/plan/生成目录
            rel = p.relative_to(repo_root).as_posix()
            if rel.startswith("helloagents/history/"):
                continue
            if rel.startswith("helloagents/plan/"):
                continue
            if rel.startswith("docs-site/.generated/") or rel.startswith("docs-site/.site/"):
                continue
            md_files.append(p)

    return sorted(set(md_files))


def remove_existing_global_nav(text: str) -> tuple[str, bool]:
    if GLOBAL_NAV_START not in text:
        return text, False
    start = text.find(GLOBAL_NAV_START)
    end = text.find(GLOBAL_NAV_END, start)
    if end < 0:
        return text, False
    end = end + len(GLOBAL_NAV_END)
    new_text = text[:start].rstrip("\n") + "\n\n" + text[end:].lstrip("\n")
    return new_text, True


def upsert_global_nav_for_one_file(
    repo_root: Path,
    md_file: Path,
    prev_item: ChapterItem | None,
    next_item: ChapterItem | None,
) -> bool:
    try:
        original = md_file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        original = md_file.read_text(encoding="utf-8", errors="replace")

    text, _ = remove_existing_global_nav(original)

    # nav 链接要按 MkDocs docs_dir 的“虚拟路径”生成，而不是仓库真实路径：
    # - content/book/*.md 在站点中是 book/*.md
    # - 模块 docs 仍是 <module>/docs/*.md
    try:
        repo_rel = md_file.relative_to(repo_root).as_posix()
    except ValueError:
        return False

    is_content_page = repo_rel.startswith("docs-site/content/")
    if is_content_page:
        current_site = Path(repo_rel).relative_to("docs-site/content").as_posix()
    else:
        current_site = repo_rel

    current_site_dir = posixpath.dirname(current_site) or "."

    def mk_link(item: ChapterItem) -> str:
        repo_target_rel = item.rel_path
        is_book_page = repo_target_rel.startswith("docs-site/content/book/")

        # 模块 docs 中链接到 book：用 /book/<slug>/ 形式（同时兼容 mkdocs 与 check-docs）
        if (not is_content_page) and is_book_page:
            site_target = Path(repo_target_rel).relative_to("docs-site/content").as_posix()
            slug = Path(site_target).stem
            return f"[{item.title}](/book/{slug}/)"

        # 其它情况：用站点相对路径（MkDocs 能解析）
        if repo_target_rel.startswith("docs-site/content/"):
            site_target = Path(repo_target_rel).relative_to("docs-site/content").as_posix()
        else:
            site_target = repo_target_rel
        rel = posixpath.relpath(site_target, start=current_site_dir)
        return f"[{item.title}]({rel})"

    toc_link = "[Book TOC](/book/)"

    prev_link = toc_link if prev_item is None else mk_link(prev_item)
    next_link = toc_link if next_item is None else mk_link(next_item)
    nav_line = f"上一章：{prev_link} ｜ 全书目录：{toc_link} ｜ 下一章：{next_link}"

    block = "\n".join([GLOBAL_NAV_START, nav_line, GLOBAL_NAV_END]) + "\n\n"

    insert_at = -1
    if CHAPTER_CARD_END in text:
        insert_at = text.find(CHAPTER_CARD_END) + len(CHAPTER_CARD_END)
        # 在 card 之后保持一个空行
        new_text = text[:insert_at] + "\n\n" + block + text[insert_at:].lstrip("\n")
    else:
        # 兜底：插在第一个 H1 后
        lines = text.splitlines(keepends=True)
        out: list[str] = []
        inserted = False
        for line in lines:
            out.append(line)
            if not inserted and line.startswith("# "):
                out.append("\n")
                out.append(block)
                inserted = True
        new_text = "".join(out)

    if new_text == original:
        return False

    md_file.write_text(new_text, encoding="utf-8")
    return True


def upsert_global_nav(repo_root: Path, ordered_new_items: list[ChapterItem], dry_run: bool) -> int:
    changed = 0
    for i, item in enumerate(ordered_new_items):
        md_file = (repo_root / item.rel_path).resolve()
        prev_item = None if i == 0 else ordered_new_items[i - 1]
        next_item = None if i == len(ordered_new_items) - 1 else ordered_new_items[i + 1]
        if not md_file.exists():
            raise SystemExit(f"[ERROR] Missing chapter file for global nav: {item.rel_path}")
        if dry_run:
            continue
        if upsert_global_nav_for_one_file(repo_root, md_file, prev_item, next_item):
            changed += 1
    return changed


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="bookify-global-chapters.py")
    p.add_argument("--config", default=str(DEFAULT_CONFIG), help="顺序配置文件（默认 scripts/book-order.json）")
    p.add_argument("--map-out", help="输出映射表（JSON）路径（repo 相对路径或绝对路径）")
    p.add_argument("--dry-run", action="store_true", help="只生成映射与统计，不写入文件。")
    return p.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv[1:])
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = (REPO_ROOT / config_path).resolve()
    if not config_path.is_file():
        raise SystemExit(f"[ERROR] Config not found: {config_path}")

    config = load_config(config_path)
    chapters = build_chapter_list(config)
    rename_mapping, rewrite_mapping, manifest = build_path_map(chapters)

    if args.map_out:
        out_path = Path(args.map_out)
        if not out_path.is_absolute():
            out_path = (REPO_ROOT / out_path).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # 1) rename
    renamed = rename_files(REPO_ROOT, rename_mapping, dry_run=args.dry_run)

    # 2) 章节路径已变更，更新 chapter list 为“新路径”，并统一 H1 标题为“第 N 章：...”
    new_items: list[ChapterItem] = []
    for idx, item in enumerate(chapters, start=1):
        new_rel = rename_mapping[item.rel_path]
        new_title = item.title
        if not args.dry_run:
            _, new_title = upsert_chapter_title((REPO_ROOT / new_rel).resolve(), idx)
        new_items.append(ChapterItem(kind=item.kind, module=item.module, rel_path=new_rel, title=new_title))

    # 3) rewrite links（全仓活文档）
    rewritten = 0
    if not args.dry_run:
        for md in iter_markdown_files_for_rewrite(REPO_ROOT):
            if rewrite_markdown_links_in_file(REPO_ROOT, md, rewrite_mapping):
                rewritten += 1

    # 4) upsert 全书导航
    global_nav_changed = 0
    if not args.dry_run:
        global_nav_changed = upsert_global_nav(REPO_ROOT, new_items, dry_run=False)

    print(
        "[OK] Global bookify done:"
        f" chapters={len(chapters)}, renamed={renamed}, rewritten_files={rewritten}, global_nav_updated={global_nav_changed}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
