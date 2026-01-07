#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
教学化覆盖度自检（面向本仓库所有“有 docs/README.md 的模块”）。

目标：
1) 以每个模块 `docs/README.md` 的章节链接清单为 SSOT；
2) 每个章节至少提供一个“可跑入口”（Lab/Exercise/Solution），且可解析到仓库中的真实测试类；
3) 每个模块至少拥有 N 个 `*LabTest.java`（默认 N=2）。

用法：
  python3 scripts/check-teaching-coverage.py
  python3 scripts/check-teaching-coverage.py --min-labs 2
  python3 scripts/check-teaching-coverage.py --module springboot-web-mvc

说明：
- 本脚本不会校验 markdown 锚点，只做“章节清单存在性 + 可跑入口存在性”检查。
- 可跑入口识别方式：
  1) 章节内出现 `SomeLabTest` / `SomeExerciseTest` / `SomeExerciseSolutionTest` 这类类名（可带 #method）；
     脚本会在 `src/test/java` 下查找同名 `.java` 文件。
  2) 或者章节内出现 `src/test/java/.../SomeLabTest.java` 这类真实路径（不允许包含 .../… 省略号）。
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

TEST_CLASS_RE = re.compile(
    r"\b([A-Za-z_][A-Za-z0-9_]*(?:LabTest|ExerciseTest|ExerciseSolutionTest))\b"
)
TEST_FILE_PATH_RE = re.compile(
    r"(?P<path>(?:(?:spring-core|springboot)-[a-z0-9-]+/)?src/test/java/[A-Za-z0-9_./-]+\.java)",
    re.IGNORECASE,
)


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

    # README 本身不作为章节；同时去重并保持顺序
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


def count_lab_tests(module_root: Path) -> int:
    test_root = module_root / "src" / "test" / "java"
    if not test_root.is_dir():
        return 0
    return sum(1 for p in test_root.rglob("*LabTest.java") if p.is_file())


def find_test_class_file(module_root: Path, simple_class_name: str) -> list[Path]:
    test_root = module_root / "src" / "test" / "java"
    if not test_root.is_dir():
        return []
    return [p for p in test_root.rglob(f"{simple_class_name}.java") if p.is_file()]


def iter_candidate_test_files(repo_root: Path, module_root: Path, text: str) -> Iterable[Path]:
    for m in TEST_FILE_PATH_RE.finditer(text):
        raw = m.group("path")
        if "..." in raw or "…" in raw:
            continue
        candidate = raw.strip()
        if candidate.startswith("spring-core-") or candidate.startswith("springboot-"):
            resolved = (repo_root / candidate).resolve()
        else:
            resolved = (module_root / candidate).resolve()
        yield resolved


def chapter_has_runnable_entry(repo_root: Path, module_root: Path, chapter: Path) -> tuple[bool, str]:
    content = chapter.read_text(encoding="utf-8", errors="replace")

    # 1) 真实文件路径引用（优先）
    for p in iter_candidate_test_files(repo_root, module_root, content):
        if p.exists():
            return True, "test-file-path"

    # 2) 类名引用（允许带 #method）
    class_names = set(TEST_CLASS_RE.findall(content))
    for cls in sorted(class_names):
        matches = find_test_class_file(module_root, cls)
        if len(matches) >= 1:
            return True, "test-class-name"

    return False, "no-runnable-entry"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="check-teaching-coverage.py",
        description="教学化覆盖度自检：章节清单存在性 + 可跑入口存在性 + min-labs。",
    )
    parser.add_argument(
        "--min-labs",
        type=int,
        default=2,
        help="每个模块至少需要的 *LabTest.java 文件数量（默认 2）。",
    )
    parser.add_argument(
        "--module",
        action="append",
        default=[],
        help="仅检查指定模块（可重复）。例如：--module springboot-web-mvc",
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

        # min-labs gate
        labs = count_lab_tests(module_root)
        if labs < args.min_labs:
            failures.append(f"- {module}: LabTests {labs} < min-labs {args.min_labs}")

        # chapter list
        chapters = iter_chapters_from_docs_readme(repo_root, module)
        if not chapters:
            failures.append(f"- {module}: no chapters parsed from docs/README.md")
            continue

        module_chapter_issues: list[ChapterIssue] = []
        for chapter in chapters:
            total_chapters += 1
            if not chapter.exists():
                module_chapter_issues.append(ChapterIssue(chapter=chapter, reason="chapter-not-found"))
                continue

            ok, reason = chapter_has_runnable_entry(repo_root, module_root, chapter)
            if not ok:
                module_chapter_issues.append(ChapterIssue(chapter=chapter, reason=reason))

        if module_chapter_issues:
            failures.append(f"- {module}: chapters missing runnable entry: {len(module_chapter_issues)}")
            for issue in module_chapter_issues[:30]:
                rel = issue.chapter.relative_to(repo_root)
                failures.append(f"  - {rel} ({issue.reason})")
            if len(module_chapter_issues) > 30:
                failures.append(f"  - ... and {len(module_chapter_issues) - 30} more")

    if failures:
        print(f"[FAIL] Teaching coverage check failed (modules={len(modules)}, total_chapters={total_chapters}, min_labs={args.min_labs})")
        for line in failures:
            print(line)
        return 1

    print(f"[OK] Teaching coverage check passed (modules={len(modules)}, total_chapters={total_chapters}, min_labs={args.min_labs})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
