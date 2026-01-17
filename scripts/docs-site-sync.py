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
import json
import re
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = REPO_ROOT / "docs-site"
CONTENT_ROOT = SITE_ROOT / "content"
GENERATED_ROOT = SITE_ROOT / ".generated" / "docs"
GENERATED_MKDOCS_YML = SITE_ROOT / ".generated" / "mkdocs.yml"
BASE_MKDOCS_YML = SITE_ROOT / "mkdocs.yml"
AUTO_NAV_BEGIN = "# BEGIN AUTO BOOK NAV"
AUTO_NAV_END = "# END AUTO BOOK NAV"
BOOK_ORDER_CONFIG = REPO_ROOT / "scripts" / "book-order.json"

GLOBAL_PREFIX_RE = re.compile(r"^(?P<no>\d{3})-(?P<rest>.+)$")
LEGACY_BOOK_PREFIX_RE = re.compile(r"^(?P<no>\d{2})-(?P<rest>.+)$")

BOOK_TOOL_PAGES = {
    "index.md",
    "labs-index.md",
    "debugger-pack.md",
    "exercises-and-solutions.md",
    "migration-rules.md",
}


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
    # 模块顺序（全书 SSOT）
    preferred_order: list[str] = []
    if BOOK_ORDER_CONFIG.is_file():
        try:
            cfg = json.loads(BOOK_ORDER_CONFIG.read_text(encoding="utf-8"))
            preferred_order = list(cfg.get("module_order") or [])
        except Exception:
            preferred_order = []

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


def strip_numeric_prefix_from_stem(stem: str) -> str:
    m = GLOBAL_PREFIX_RE.match(stem)
    if m:
        return m.group("rest")
    m = LEGACY_BOOK_PREFIX_RE.match(stem)
    if m:
        return m.group("rest")
    return stem


def load_book_order_config() -> dict:
    if not BOOK_ORDER_CONFIG.is_file():
        raise SystemExit(f"[ERROR] 缺少全书顺序配置：{BOOK_ORDER_CONFIG}")
    return json.loads(BOOK_ORDER_CONFIG.read_text(encoding="utf-8"))


def find_book_page_by_slug(slug: str) -> Path:
    book_root = CONTENT_ROOT / "book"

    candidates: list[Path] = []
    for md in sorted(book_root.glob("*.md")):
        if not md.is_file():
            continue
        if md.name in BOOK_TOOL_PAGES:
            continue
        if strip_numeric_prefix_from_stem(md.stem) == slug:
            candidates.append(md)

    if not candidates:
        raise SystemExit(f"[ERROR] 未找到 book 主线章节页：slug={slug}")

    # 兼容旧路径（例如 00-18 的 redirect 页面）时，优先选择全局 3 位编号（001-xxx）。
    def score(p: Path) -> tuple[int, int, str]:
        m = GLOBAL_PREFIX_RE.match(p.stem)
        if m:
            return (0, int(m.group("no")), p.name)
        m2 = LEGACY_BOOK_PREFIX_RE.match(p.stem)
        if m2:
            return (1, int(m2.group("no")), p.name)
        return (2, 9999, p.name)

    return min(candidates, key=score)


def content_rel_path(md: Path) -> str:
    return md.relative_to(CONTENT_ROOT).as_posix()


def iter_module_chapters_ordered_by_last_occurrence(module: str) -> list[Path]:
    module_root = REPO_ROOT / module
    readme = module_root / "docs" / "README.md"
    if not readme.is_file():
        return []

    md_link_re = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")
    scheme_re = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

    def is_external(dest: str) -> bool:
        if dest.startswith("#") or dest.startswith("//"):
            return True
        return bool(scheme_re.match(dest))

    def normalize(raw: str) -> str | None:
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

    index = 0
    last: dict[Path, int] = {}
    content = readme.read_text(encoding="utf-8", errors="replace")
    for m in md_link_re.finditer(content):
        is_image = m.group(1) == "!"
        if is_image:
            continue
        target_raw = m.group(3)
        index += 1
        target = normalize(target_raw)
        if target is None or is_external(target):
            continue
        if not target.endswith(".md"):
            continue
        chapter = (readme.parent / target).resolve()
        try:
            chapter.relative_to(REPO_ROOT)
        except ValueError:
            continue
        if "/docs/" not in chapter.as_posix():
            continue
        if chapter == readme.resolve():
            continue
        last[chapter] = index

    return [p for (p, _) in sorted(last.items(), key=lambda it: it[1])]


def build_global_book_nav_lines() -> list[str]:
    """
    生成注入到 mkdocs.yml 的“全书目录”导航：

    - 以 scripts/book-order.json 为 SSOT（模块顺序 + 分卷）
    - 每个模块：主线章节（Book-only）→ 模块目录页 → 模块章节清单（按 docs/README.md 链接顺序）
    - book/index.md 与工具页保留为目录/附录
    """
    cfg = load_book_order_config()

    parts: list[dict] = list(cfg.get("parts") or [])
    module_order: list[str] = list(cfg.get("module_order") or [])
    slug_by_module: dict[str, str] = dict(cfg.get("book", {}).get("mainline_slug_by_module", {}) or {})
    start_here_slug: str = str(cfg.get("book", {}).get("start_here_slug") or "start-here")

    # 验证模块顺序配置至少覆盖站点实际模块
    actual_modules = discover_modules(REPO_ROOT)
    unknown = [m for m in module_order if m not in actual_modules]
    if unknown:
        raise SystemExit(f"[ERROR] book-order.json module_order 包含未知模块：{unknown}")

    auto_lines: list[str] = []

    # 分卷输出（按 parts 顺序）；未被 parts 覆盖的模块放最后兜底
    part_modules: set[str] = set()
    for part in parts:
        title = str(part.get("title") or "").strip()
        modules_in_part = list(part.get("modules") or [])
        if not title or not modules_in_part:
            continue
        for m in modules_in_part:
            part_modules.add(m)

        auto_lines.append(f"      - {yaml_quote(title)}:")

        # Start Here 放在 Part I 第一行（更像书的序章）
        if "启动与配置" in title:
            start_here_page = find_book_page_by_slug(start_here_slug)
            auto_lines.append(
                f"          - {yaml_quote(read_first_h1_title(start_here_page))}: {content_rel_path(start_here_page)}"
            )

        for module in modules_in_part:
            auto_lines.append(f"          - {yaml_quote(module)}:")

            slug = slug_by_module.get(module)
            if not slug:
                raise SystemExit(f"[ERROR] book-order.json 缺少主线章节映射：module={module}")
            book_page = find_book_page_by_slug(slug)
            auto_lines.append(
                f"              - {yaml_quote(read_first_h1_title(book_page))}: {content_rel_path(book_page)}"
            )
            auto_lines.append(f"              - {yaml_quote('模块目录')}: {module}/docs/README.md")

            for md in iter_module_chapters_ordered_by_last_occurrence(module):
                page_title = read_first_h1_title(md)
                rel_to_repo = md.relative_to(REPO_ROOT).as_posix()
                auto_lines.append(f"              - {yaml_quote(page_title)}: {rel_to_repo}")

    # 未归类模块（理论上不应出现）
    remaining = [m for m in module_order if m not in part_modules]
    if remaining:
        auto_lines.append(f"      - {yaml_quote('Part X：未归类')}:")
        for module in remaining:
            auto_lines.append(f"          - {yaml_quote(module)}:")
            auto_lines.append(f"              - {yaml_quote('模块目录')}: {module}/docs/README.md")
            for md in iter_module_chapters_ordered_by_last_occurrence(module):
                page_title = read_first_h1_title(md)
                rel_to_repo = md.relative_to(REPO_ROOT).as_posix()
                auto_lines.append(f"              - {yaml_quote(page_title)}: {rel_to_repo}")

    # 附录（工具/参考/知识库/模块总览）
    auto_lines.append(f"      - {yaml_quote('附录')}:")

    # 工具页（固定顺序）
    auto_lines.append(f"          - {yaml_quote('工具')}:")
    tool_pages = [
        ("Labs 索引", "book/labs-index.md"),
        ("Debugger Pack", "book/debugger-pack.md"),
        ("Exercises & Solutions", "book/exercises-and-solutions.md"),
        ("迁移规则", "book/migration-rules.md"),
    ]
    for title, path in tool_pages:
        auto_lines.append(f"              - {yaml_quote(title)}: {path}")

    # 参考（写作指南 + 知识库）
    auto_lines.append(f"          - {yaml_quote('参考')}:")
    auto_lines.append(f"              - {yaml_quote('写作指南')}: book-style.md")
    auto_lines.append(f"              - {yaml_quote('知识库')}:")
    kb_pages = [
        ("知识库概览", "helloagents/wiki/overview.md"),
        ("学习路线图", "helloagents/wiki/learning-path.md"),
        ("项目约定", "helloagents/project.md"),
        ("变更历史索引", "helloagents/history/index.md"),
    ]
    for title, path in kb_pages:
        auto_lines.append(f"                  - {yaml_quote(title)}: {path}")

    # 模块总览
    auto_lines.append(f"          - {yaml_quote('模块总览')}: modules/index.md")

    return auto_lines


def generate_mkdocs_config(modules: list[str]) -> None:
    """
    生成 docs-site/.generated/mkdocs.yml：在基础 mkdocs.yml 上注入“全书目录（章节顺序）”。

    设计目标：
    1) 侧边栏展示“全书章节顺序”（按分卷→模块→章节）；
    2) 模块 docs 与 Book-only 主线均纳入顺读序列（每个 doc 即一章）。
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
        print("[WARN] 未在 docs-site/mkdocs.yml 中找到 AUTO BOOK NAV 标记，跳过生成 mkdocs 配置。", file=sys.stderr)
        return

    auto_lines = build_global_book_nav_lines()

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
