#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
检查 Markdown 文档中的相对链接是否存在（仅做“路径存在性检查”，不校验锚点）。

默认行为（不带参数）：
  - 自动扫描仓库根目录下所有 `spring-core-*/docs` 与 `springboot-*/docs`

用法：
  python3 scripts/check-md-relative-links.py
  python3 scripts/check-md-relative-links.py spring-core-beans/docs spring-core-aop/docs
  python3 scripts/check-md-relative-links.py spring-core-aop/docs/part-00-guide/00-deep-dive-guide.md

规则：
  - 只检查相对路径与仓库根路径（/xxx）形式的链接目标是否存在
  - 跳过 http(s)/mailto 等外链、以及纯锚点链接 (#xxx)
  - 忽略 fenced code block（```）中的内容，避免误报
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK_INLINE_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
LINK_REF_DEF_RE = re.compile(r"^\s*\[[^\]]+]:\s*(\S+)")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def is_external_link(dest: str) -> bool:
    if dest.startswith("#"):
        return True
    if dest.startswith("//"):
        return True
    return bool(SCHEME_RE.match(dest))


def normalize_destination(raw: str) -> str | None:
    dest = raw.strip()
    if not dest:
        return None

    # Strip angle brackets: (<path>) form
    if dest.startswith("<") and dest.endswith(">"):
        dest = dest[1:-1].strip()

    # Remove title part: (path "title")
    # For our docs, splitting by whitespace is good enough.
    if " " in dest or "\t" in dest:
        dest = re.split(r"\\s+", dest, maxsplit=1)[0]

    dest = unquote(dest)

    # Strip anchor (we only validate path existence)
    if "#" in dest:
        dest = dest.split("#", 1)[0]

    if not dest:
        return None

    return dest


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def check_one_file(repo_root: Path, md_file: Path) -> list[tuple[int, str, Path]]:
    missing: list[tuple[int, str, Path]] = []
    in_fence = False

    try:
        content = md_file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        content = md_file.read_text(encoding="utf-8", errors="replace")

    for idx, line in enumerate(content.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        candidates: list[str] = []
        candidates.extend(m.group(1) for m in LINK_INLINE_RE.finditer(line))

        ref = LINK_REF_DEF_RE.match(line)
        if ref:
            candidates.append(ref.group(1))

        for raw_dest in candidates:
            dest = normalize_destination(raw_dest)
            if dest is None:
                continue
            if is_external_link(dest):
                continue

            target: Path
            if dest.startswith("/"):
                target = repo_root / dest.lstrip("/")
            else:
                target = md_file.parent / dest

            if not target.exists():
                missing.append((idx, dest, target))

    return missing


def default_doc_roots(repo_root: Path) -> list[Path]:
    roots: list[Path] = []
    for p in sorted(repo_root.iterdir()):
        if not p.is_dir():
            continue
        if not (p.name.startswith("spring-core-") or p.name.startswith("springboot-")):
            continue
        docs_dir = p / "docs"
        if docs_dir.is_dir():
            roots.append(docs_dir)
    return roots


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="check-md-relative-links.py",
        description="检查 Markdown 文档中的相对链接目标是否存在（不校验锚点）。",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="要检查的 docs 目录或单个 .md 文件（默认：扫描所有 spring-core-*/docs 与 springboot-*/docs）。",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    repo_root = Path(__file__).resolve().parents[1]
    args = parse_args(argv[1:])

    input_paths = [Path(p) for p in args.paths]
    paths = input_paths if input_paths else default_doc_roots(repo_root)
    if not paths:
        print("[ERROR] No docs directory found under spring-core-*/docs or springboot-*/docs.", file=sys.stderr)
        return 2

    md_files: list[Path] = []
    for p in paths:
        abs_path = (repo_root / p).resolve() if not p.is_absolute() else p.resolve()
        if abs_path.is_dir():
            md_files.extend(iter_markdown_files(abs_path))
        elif abs_path.is_file() and abs_path.suffix.lower() == ".md":
            md_files.append(abs_path)
        else:
            print(f"[ERROR] Path not found or not a markdown/doc dir: {p}", file=sys.stderr)
            return 2

    md_files = sorted(set(md_files))
    all_missing: list[tuple[Path, int, str, Path]] = []
    for md in md_files:
        for (lineno, dest, resolved) in check_one_file(repo_root, md):
            all_missing.append((md, lineno, dest, resolved))

    if all_missing:
        print(f"[FAIL] Missing link targets: {len(all_missing)}")
        for md, lineno, dest, resolved in all_missing:
            rel = md.relative_to(repo_root)
            resolved_rel = resolved.relative_to(repo_root) if resolved.is_absolute() and repo_root in resolved.parents else resolved
            print(f"- {rel}:{lineno} -> {dest} (missing: {resolved_rel})")
        return 1

    print(f"[OK] Checked {len(md_files)} markdown files, missing targets: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
