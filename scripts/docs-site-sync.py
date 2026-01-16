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


BOOK_CHAPTER_RE = re.compile(r"^(?P<no>\d{2})-(?P<slug>.+)\.md$")


def fmt_token_for_nav(token: str) -> str:
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
    if token in mapping:
        return mapping[token]
    if token.isdigit():
        return token
    if not token:
        return token
    return token[:1].upper() + token[1:].lower()


def scan_book_pages(book_root: Path) -> tuple[list[tuple[int, Path]], list[Path]]:
    """
    扫描 docs-site/content/book 下的页面：

    - 章节页：NN-*.md（NN 为两位数字）
    - 附录页：其它 .md（例如 labs-index.md）
    """
    chapters: list[tuple[int, Path]] = []
    appendix: list[Path] = []

    if not book_root.is_dir():
        return chapters, appendix

    for md in sorted(book_root.glob("*.md")):
        if md.name == "index.md":
            continue
        m = BOOK_CHAPTER_RE.match(md.name)
        if m:
            chapters.append((int(m.group("no")), md))
        else:
            appendix.append(md)

    # 章节按编号排序（同号按文件名稳定排序）
    chapters = sorted(chapters, key=lambda x: (x[0], x[1].name))
    return chapters, appendix


def short_chapter_nav_title(chapter_no: int, md_path: Path) -> str:
    # 优先给出“短目录标题”（更像书的目录）
    fixed: dict[int, str] = {
        0: "00 Start Here",
        1: "01 Boot",
        2: "02 IoC（Beans）",
        3: "03 AOP/Proxy",
        4: "04 Weaving",
        5: "05 Tx",
        6: "06 Web MVC",
        7: "07 Security",
        8: "08 Data JPA",
        9: "09 Cache",
        10: "10 Async/Scheduling",
        11: "11 Events",
        12: "12 Resources",
        13: "13 Profiles",
        14: "14 Validation",
        15: "15 Actuator",
        16: "16 Web Client",
        17: "17 Testing",
        18: "18 Business Case",
    }
    if chapter_no in fixed:
        return fixed[chapter_no]

    # fallback：用文件名推导（去掉 NN- 前缀 + 常见尾缀），尽量短
    stem = md_path.stem
    prefix = f"{chapter_no:02d}-"
    if stem.startswith(prefix):
        stem = stem[len(prefix) :]
    stem = stem.replace("-mainline", "").replace("-", " ").strip()
    tokens = [fmt_token_for_nav(t) for t in stem.split() if t]
    title = " ".join(tokens).strip()
    if not title:
        title = md_path.stem
    return f"{chapter_no:02d} {title}"


def build_book_only_nav_lines(modules: list[str]) -> list[str]:
    """
    生成注入到 mkdocs.yml 的 Book-only 导航：

    - 章节按“分卷（Part）”分组
    - 目录标题短化（nav title 短，正文标题可长）
    - 自动扫描 docs-site/content/book（新增章节无需改脚本）
    """
    auto_lines: list[str] = []

    book_root = CONTENT_ROOT / "book"
    chapters, appendix_pages = scan_book_pages(book_root)
    if not chapters:
        print("[WARN] 未发现任何 book 章节页（docs-site/content/book/NN-*.md）。", file=sys.stderr)

    # 分卷（保持编号连续，避免目录顺序看起来“跳号”）
    part_defs: list[tuple[str, int, int]] = [
        ("Part I：启动与配置", 0, 1),
        ("Part II：容器（Beans）", 2, 2),
        ("Part III：AOP / 事务", 3, 5),
        ("Part IV：Web（MVC / Security）", 6, 7),
        ("Part V：数据与基础设施", 8, 13),
        ("Part VI：质量与交付", 14, 18),
    ]

    def part_for(no: int) -> str:
        for title, start, end in part_defs:
            if start <= no <= end:
                return title
        return "Part X：未归类"

    parts: dict[str, list[tuple[int, Path]]] = {}
    for no, md in chapters:
        parts.setdefault(part_for(no), []).append((no, md))

    # 按 part_defs 顺序输出；未归类放最后
    for title, _, _ in part_defs:
        if title not in parts:
            continue
        auto_lines.append(f"      - {yaml_quote(title)}:")
        for no, md in parts[title]:
            auto_lines.append(f"          - {yaml_quote(short_chapter_nav_title(no, md))}: book/{md.name}")

    if "Part X：未归类" in parts:
        auto_lines.append(f"      - {yaml_quote('Part X：未归类')}:")
        for no, md in parts["Part X：未归类"]:
            auto_lines.append(f"          - {yaml_quote(short_chapter_nav_title(no, md))}: book/{md.name}")

    # 附录（分区更清晰：工具/知识库/模块入口/其它页面）
    auto_lines.append(f"      - {yaml_quote('附录')}:")

    # 1) 工具页（固定顺序）
    auto_lines.append(f"          - {yaml_quote('工具')}:")
    tool_pages = [
        ("Labs 索引", "book/labs-index.md"),
        ("Debugger Pack", "book/debugger-pack.md"),
        ("Exercises & Solutions", "book/exercises-and-solutions.md"),
        ("迁移规则", "book/migration-rules.md"),
    ]
    for title, path in tool_pages:
        auto_lines.append(f"              - {yaml_quote(title)}: {path}")

    # 2) 参考（写作指南 + 知识库）
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

    # 3) 模块 docs 快速入口（素材库）
    auto_lines.append(f"          - {yaml_quote('模块入口（素材库）')}:")
    auto_lines.append(f"              - {yaml_quote('模块总览')}: modules/index.md")
    for module in sorted(modules):
        auto_lines.append(f"              - {yaml_quote(module)}: {module}/docs/README.md")

    # 4) book/ 目录下其它未被固定索引覆盖的页面（自动发现，避免漏页）
    known_appendix = {Path(p).name for _, p in tool_pages}
    remaining = [p for p in appendix_pages if p.name not in known_appendix]
    if remaining:
        auto_lines.append(f"          - {yaml_quote('其它')}:")
        for md in remaining:
            auto_lines.append(f"              - {yaml_quote(read_first_h1_title(md))}: book/{md.name}")

    return auto_lines


def generate_mkdocs_config(modules: list[str]) -> None:
    """
    生成 docs-site/.generated/mkdocs.yml：在基础 mkdocs.yml 上注入“书（Book-only）目录”。

    设计目标：
    1) 侧边栏仅展示“主线之书”章节树；
    2) 各模块 docs 仍会同步到站点 docs_dir（作为素材库/搜索命中/书内引用目标），但不再生成到 nav。
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

    auto_lines = build_book_only_nav_lines(modules)

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
