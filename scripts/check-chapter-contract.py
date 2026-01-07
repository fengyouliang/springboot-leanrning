#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
章节契约自检（A–G + Lab/Test + 可解析 LabTest）。

目标（面向本仓库所有“有 docs/README.md 的模块”）：
1) 以每个模块 `docs/README.md` 的章节链接清单为 SSOT；
2) 每个章节必须包含 A–G 七个二级标题（`##`）；
3) 每个章节必须包含“对应 Lab/Test”区块；
4) 可选：强制每章至少引用 1 个真实存在的 `*LabTest`（类名或 src/test/java 路径引用）。

用法：
  python3 scripts/check-chapter-contract.py
  python3 scripts/check-chapter-contract.py --require-labtest
  python3 scripts/check-chapter-contract.py --module spring-core-beans --strict --require-labtest
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

BOOKIFY_START = "<!-- BOOKIFY:START -->"
BOOKIFY_END = "<!-- BOOKIFY:END -->"

LABTEST_CLASS_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*LabTest)\b")
TEST_FILE_PATH_RE = re.compile(
    r"(?P<path>(?:(?:spring-core|springboot)-[a-z0-9-]+/)?src/test/java/[A-Za-z0-9_./-]+\.java)",
    re.IGNORECASE,
)

# 二级标题（##）识别：只拿 H2（避免 ### 触发）
H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)

# 允许的 A–G 标识写法：A. / A、/ A: / A）/ A )
AG_MARK_RE = re.compile(r"^\s*([A-G])(?:[.、:：\)\]）】]\s*|\s+|$)")


@dataclass(frozen=True)
class ChapterIssue:
    chapter: Path
    reason: str


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


def iter_chapters_from_docs_readme(repo_root: Path, module: str) -> list[Path]:
    readme = repo_root / module / "docs" / "README.md"
    if not readme.is_file():
        return []

    content = readme.read_text(encoding="utf-8", errors="replace")
    chapters: list[Path] = []
    for m in MD_LINK_RE.finditer(content):
        target_raw = m.group(1)
        target = normalize_md_link_target(target_raw)
        if target is None:
            continue
        if is_external_link(target):
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
        chapters.append(chapter)

    # README 本身不作为章节；去重保持顺序
    seen: set[Path] = set()
    ordered: list[Path] = []
    for c in chapters:
        if c == readme:
            continue
        if c in seen:
            continue
        seen.add(c)
        ordered.append(c)
    return ordered


def build_labtest_index(module_root: Path) -> set[str]:
    test_root = module_root / "src" / "test" / "java"
    if not test_root.is_dir():
        return set()
    return {p.stem for p in test_root.rglob("*LabTest.java") if p.is_file()}


def strip_fenced_code_blocks(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    in_fence = False
    fence_re = re.compile(r"^\s*```")
    for line in lines:
        if fence_re.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def extract_ag_markers_from_h2(content: str) -> list[str]:
    clean = strip_fenced_code_blocks(content)
    markers: list[str] = []
    for h2 in H2_RE.findall(clean):
        m = AG_MARK_RE.match(h2)
        if not m:
            continue
        markers.append(m.group(1))
    return markers


def has_labtest_reference(
    repo_root: Path, module_root: Path, content: str, module_labtests: set[str]
) -> tuple[bool, str]:
    # 1) 真实文件路径引用（允许 repo-relative 或 module-relative）
    for m in TEST_FILE_PATH_RE.finditer(content):
        raw = (m.group("path") or "").strip()
        if not raw:
            continue
        if "..." in raw or "…" in raw:
            continue

        if raw.startswith("spring-core-") or raw.startswith("springboot-"):
            resolved = (repo_root / raw).resolve()
        else:
            resolved = (module_root / raw).resolve()
        if not resolved.exists():
            continue
        if resolved.name.endswith("LabTest.java"):
            return True, "labtest-file-path"

    # 2) 类名引用（允许带 #method，但这里只校验类名是否存在）
    class_names = set(LABTEST_CLASS_RE.findall(content))
    for cls in sorted(class_names):
        if cls in module_labtests:
            return True, "labtest-class-name"

    return False, "no-labtest"


def chapter_has_lab_block(content: str) -> bool:
    if "对应 Lab/Test" in content:
        return True
    # 兼容少量旧写法
    if "对应Lab/Test" in content:
        return True
    return False


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="check-chapter-contract.py",
        description="章节契约自检：A–G 二级标题 + 对应 Lab/Test +（可选）每章至少 1 个 LabTest。",
    )
    parser.add_argument(
        "--module",
        action="append",
        default=[],
        help="仅检查指定模块（可重复）。例如：--module springboot-web-mvc",
    )
    parser.add_argument(
        "--require-labtest",
        action="store_true",
        help="强制每章至少引用 1 个真实存在的 *LabTest（类名或 src/test/java 路径）。",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="严格模式：要求 A–G 标识按 A→G 顺序且各出现一次（否则失败）。",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    repo_root = Path(__file__).resolve().parents[1]
    args = parse_args(argv[1:])

    modules = args.module or discover_modules(repo_root)
    if not modules:
        print("[ERROR] No module with docs/README.md found.", file=sys.stderr)
        return 2

    failures: list[str] = []
    total_chapters = 0

    for module in modules:
        module_root = repo_root / module
        docs_readme = module_root / "docs" / "README.md"
        if not docs_readme.is_file():
            failures.append(f"- {module}: missing docs/README.md")
            continue

        chapters = iter_chapters_from_docs_readme(repo_root, module)
        if not chapters:
            failures.append(f"- {module}: no chapters parsed from docs/README.md")
            continue

        module_labtests = build_labtest_index(module_root)

        issues: list[ChapterIssue] = []
        for chapter in chapters:
            total_chapters += 1
            if not chapter.exists():
                issues.append(ChapterIssue(chapter=chapter, reason="chapter-not-found"))
                continue

            content = chapter.read_text(encoding="utf-8", errors="replace")

            # A–G 二级标题
            markers = extract_ag_markers_from_h2(content)
            if args.strict:
                if markers != list("ABCDEFG"):
                    issues.append(
                        ChapterIssue(
                            chapter=chapter,
                            reason=f"ag-headings-not-strict (found={''.join(markers) or '-'})",
                        )
                    )
            else:
                missing = [ch for ch in "ABCDEFG" if ch not in set(markers)]
                if missing:
                    issues.append(
                        ChapterIssue(chapter=chapter, reason="ag-headings-missing-" + "".join(missing))
                    )

            # “对应 Lab/Test”
            if not chapter_has_lab_block(content):
                issues.append(ChapterIssue(chapter=chapter, reason="missing-lab-block"))

            # LabTest 引用（可选强制）
            ok_labtest, reason = has_labtest_reference(
                repo_root=repo_root,
                module_root=module_root,
                content=content,
                module_labtests=module_labtests,
            )
            if args.require_labtest and not ok_labtest:
                issues.append(ChapterIssue(chapter=chapter, reason=reason))

        if issues:
            failures.append(f"- {module}: chapters not compliant: {len(issues)}")
            for issue in issues[:30]:
                rel = issue.chapter.relative_to(repo_root)
                failures.append(f"  - {rel} ({issue.reason})")
            if len(issues) > 30:
                failures.append(f"  - ... and {len(issues) - 30} more")

    if failures:
        print(
            "[FAIL] Chapter contract check failed "
            f"(modules={len(modules)}, total_chapters={total_chapters}, "
            f"require_labtest={args.require_labtest}, strict={args.strict})"
        )
        for line in failures:
            print(line)
        return 1

    print(
        "[OK] Chapter contract check passed "
        f"(modules={len(modules)}, total_chapters={total_chapters}, "
        f"require_labtest={args.require_labtest}, strict={args.strict})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

