#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
全模块 docs 章节升级为 A–G 章节契约（脚本驱动，可重复执行）。

设计目标：
1) 以各模块 `docs/README.md` 的章节链接清单为 SSOT；
2) 对每章“结构化重写”：统一输出 A–G 七个二级标题（`##`）；
3) 尽量保留原正文内容（迁移到 C/E/F/G），并保持可读；
4) 保留/不破坏既有 BOOKIFY 尾部区块（对应 Lab/Test + 上一章/下一章导航）；
5) 兜底：每章至少包含 1 个 `*LabTest` 引用（优先复用原文引用，否则注入模块默认 LabTest）。

用法：
  python3 scripts/ag-contract-docs.py
  python3 scripts/ag-contract-docs.py --module spring-core-profiles
  python3 scripts/ag-contract-docs.py --dry-run

注意：
- 本脚本不会新增/修改测试类，只做文档结构化改写；
- 章节尾部 BOOKIFY 区块建议由 scripts/bookify-docs.py 最终统一刷新导航与入口列表。
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

BOOKIFY_START = "<!-- BOOKIFY:START -->"
BOOKIFY_END = "<!-- BOOKIFY:END -->"

AG_START = "<!-- AG-CONTRACT:START -->"
AG_END = "<!-- AG-CONTRACT:END -->"

LABTEST_CLASS_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*LabTest)\b")


@dataclass(frozen=True)
class RewriteResult:
    changed: bool
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


def split_bookify_footer(content: str) -> tuple[str, str]:
    if BOOKIFY_START not in content or BOOKIFY_END not in content:
        return content, ""
    lines = content.splitlines()
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if BOOKIFY_START in line:
            start_idx = i
            break
    if start_idx is None:
        return content, ""
    for j in range(start_idx + 1, len(lines)):
        if BOOKIFY_END in lines[j]:
            end_idx = j
            break
    if end_idx is None:
        return content, ""

    body_lines = lines[:start_idx]
    footer_lines = lines[start_idx : end_idx + 1]
    tail_lines = lines[end_idx + 1 :]

    # BOOKIFY 之后理论上不应再有内容；如果存在，做“尽量不丢”的保守处理：
    # - 纯空行：忽略
    # - 只包含极短的纯数字（常见误粘贴噪音）：丢弃
    # - 其他：并回正文（避免丢失）
    tail_nonempty = [l for l in tail_lines if l.strip() != ""]
    if tail_nonempty:
        joined = "".join(l.strip() for l in tail_nonempty)
        if len(joined) <= 2 and joined.isdigit():
            pass
        else:
            body_lines.extend([""] + tail_lines)

    body = "\n".join(body_lines) + ("\n" if content.endswith("\n") else "")
    footer = "\n".join(footer_lines) + ("\n" if content.endswith("\n") else "")
    return body, footer


def extract_title_and_body(content: str, fallback_title: str) -> tuple[str, str]:
    lines = content.splitlines()
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        title = lines[i].strip()
        body = "\n".join(lines[i + 1 :]) + ("\n" if content.endswith("\n") else "")
        return title, body
    # 无 H1 的情况下，用文件名兜底
    title = f"# {fallback_title}"
    return title, content if content.endswith("\n") else content + "\n"


def split_blocks_preserve_fences(text: str) -> list[str]:
    lines = text.splitlines()
    blocks: list[list[str]] = []
    current: list[str] = []
    in_fence = False

    fence_re = re.compile(r"^\s*```")
    for line in lines:
        if fence_re.match(line):
            in_fence = not in_fence
            current.append(line)
            continue

        if not in_fence and line.strip() == "":
            if current:
                blocks.append(current)
                current = []
            continue
        current.append(line)

    if current:
        blocks.append(current)

    return ["\n".join(b).strip("\n") for b in blocks if any(x.strip() for x in b)]


def select_default_labtests(module_root: Path, limit: int = 2) -> list[str]:
    test_root = module_root / "src" / "test" / "java"
    if not test_root.is_dir():
        return []
    names: list[str] = sorted({p.stem for p in test_root.rglob("*LabTest.java") if p.is_file()})
    return names[:limit]


def extract_labtests(text: str) -> list[str]:
    names = sorted(set(LABTEST_CLASS_RE.findall(text)))
    return names


def block_bucket(block: str, chapter_path: Path) -> str:
    """
    Returns one of: C / E / F / G
    """
    lower = block.lower()
    name_lower = chapter_path.as_posix().lower()

    # 强类型章节：附录 90 通常是坑点；99 通常是自测/清单
    if "/appendix/90-" in name_lower or "pitfall" in name_lower:
        return "F"

    # E：复现与实验（包含命令、Lab/Exercise、验证入口等）
    e_keywords = [
        "复现",
        "验证",
        "怎么跑",
        "如何跑",
        "运行",
        "实验",
        "labtest",
        "lab",
        "exercise",
        "mvn ",
        "debug",
        "断点",
        "调试",
        "test",
    ]
    if any(k in block for k in ["`"]):
        # 代码引用经常出现在复现入口与断点提示里，轻微加权
        if any(k in lower for k in e_keywords):
            return "E"
    if any(k in lower for k in e_keywords):
        return "E"

    # F：坑点与边界
    f_keywords = [
        "坑",
        "注意",
        "陷阱",
        "误区",
        "边界",
        "常见问题",
        "faq",
        "troubleshooting",
        "pitfall",
    ]
    if any(k in lower for k in f_keywords):
        return "F"

    # G：小结与下一章
    g_keywords = ["小结", "总结", "下一章", "next", "recap"]
    if any(k in lower for k in g_keywords):
        return "G"

    return "C"


def build_ag_contract_block(
    title_line: str,
    chapter_path: Path,
    module: str,
    legacy_body: str,
    default_labtests: list[str],
) -> str:
    """
    生成 A–G 标准结构；尽量把旧内容迁移到 C/E/F/G。
    """
    blocks = split_blocks_preserve_fences(legacy_body)
    c_blocks: list[str] = []
    e_blocks: list[str] = []
    f_blocks: list[str] = []
    g_blocks: list[str] = []

    for b in blocks:
        bucket = block_bucket(b, chapter_path)
        if bucket == "E":
            e_blocks.append(b)
        elif bucket == "F":
            f_blocks.append(b)
        elif bucket == "G":
            g_blocks.append(b)
        else:
            c_blocks.append(b)

    referenced_labtests = extract_labtests(legacy_body)
    used_labtests = referenced_labtests or default_labtests

    # 兜底：保证至少 1 个 LabTest（可能存在极少模块无测试目录）
    if not used_labtests:
        used_labtests = ["<YourLabTestHere>"]

    chapter_name = title_line.removeprefix("#").strip() or chapter_path.stem

    lines: list[str] = []
    lines.append(AG_START)
    lines.append("")

    lines.append("## A. 本章定位")
    lines.append("")
    lines.append(f"- 本章主题：**{chapter_name}**")
    lines.append("- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。")

    lines.append("")
    lines.append("## B. 核心结论")
    lines.append("")
    lines.append("- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。")
    lines.append("- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。")

    lines.append("")
    lines.append("## C. 机制主线")
    lines.append("")
    if c_blocks:
        lines.extend([c_blocks[0]])
        for b in c_blocks[1:]:
            lines.append("")
            lines.append(b)
    else:
        lines.append("- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）")

    lines.append("")
    lines.append("## D. 源码与断点")
    lines.append("")
    lines.append("- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。")
    lines.append("- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。")

    lines.append("")
    lines.append("## E. 最小可运行实验（Lab）")
    lines.append("")
    if referenced_labtests:
        lines.append("- 本章已在正文中引用以下 LabTest（建议优先跑它们）：")
    else:
        lines.append("- 本章未显式引用 LabTest，先注入模块默认 LabTest 作为“合规兜底入口”（后续可逐章细化）。")
    lines.append("- Lab：" + " / ".join(f"`{t}`" for t in used_labtests[:3]))
    lines.append(f"- 建议命令：`mvn -pl {module} test`（或在 IDE 直接运行上面的测试类）")
    if e_blocks:
        lines.append("")
        lines.append("### 复现/验证补充说明（来自原文迁移）")
        lines.append("")
        lines.extend([e_blocks[0]])
        for b in e_blocks[1:]:
            lines.append("")
            lines.append(b)

    lines.append("")
    lines.append("## F. 常见坑与边界")
    lines.append("")
    if f_blocks:
        lines.extend([f_blocks[0]])
        for b in f_blocks[1:]:
            lines.append("")
            lines.append(b)
    else:
        lines.append("- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）")

    lines.append("")
    lines.append("## G. 小结与下一章")
    lines.append("")
    if g_blocks:
        lines.extend([g_blocks[0]])
        for b in g_blocks[1:]:
            lines.append("")
            lines.append(b)
    else:
        lines.append("- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。")

    lines.append("")
    lines.append(AG_END)
    lines.append("")

    return "\n".join(lines)


def chapter_already_compliant(content: str) -> bool:
    # 轻量判断：是否已经包含 7 个 H2 标识（A–G）与 Lab/Test 区块
    for ch in "ABCDEFG":
        if not re.search(rf"^##\s+{ch}(?:\.|[、:：\s])", content, flags=re.MULTILINE):
            return False
    if "对应 Lab/Test" not in content and "对应Lab/Test" not in content:
        return False
    if not LABTEST_CLASS_RE.search(content):
        return False
    return True


def rewrite_chapter(
    repo_root: Path,
    module: str,
    chapter: Path,
    default_labtests: list[str],
    dry_run: bool,
) -> RewriteResult:
    if not chapter.exists():
        return RewriteResult(changed=False, reason="missing")

    original = chapter.read_text(encoding="utf-8", errors="replace")
    if chapter_already_compliant(original):
        return RewriteResult(changed=False, reason="skip-already-compliant")

    # 1) 分离 BOOKIFY 尾部区块（保留，但不参与正文迁移）
    body, footer = split_bookify_footer(original)

    # 3) 拆出标题与正文
    fallback_title = chapter.stem.replace("-", " ").strip() or chapter.stem
    title_line, legacy_body = extract_title_and_body(body, fallback_title=fallback_title)

    # 4) 生成 A–G 区块
    ag_block = build_ag_contract_block(
        title_line=title_line,
        chapter_path=chapter,
        module=module,
        legacy_body=legacy_body,
        default_labtests=default_labtests,
    )

    # 5) 组装：标题 + A–G + BOOKIFY（如存在）
    new_lines: list[str] = []
    new_lines.append(title_line)
    new_lines.append("")
    new_lines.append(ag_block.rstrip("\n"))

    if footer.strip():
        # footer 之前保证空行隔开
        new_lines.append("")
        new_lines.append(footer.strip("\n"))
        new_lines.append("")

    new_text = "\n".join(new_lines).rstrip() + "\n"

    if new_text == original:
        return RewriteResult(changed=False, reason="no-op")

    if not dry_run:
        chapter.write_text(new_text, encoding="utf-8")
    return RewriteResult(changed=True, reason="rewritten")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="ag-contract-docs.py",
        description="批量将 docs 章节升级为 A–G 契约结构（以 docs/README.md 为 SSOT）。",
    )
    parser.add_argument("--dry-run", action="store_true", help="只输出统计信息，不写入文件。")
    parser.add_argument(
        "--module",
        action="append",
        default=[],
        help="仅处理指定模块（可重复）。例如：--module spring-core-beans",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    repo_root = Path(__file__).resolve().parents[1]
    args = parse_args(argv[1:])

    modules = args.module or discover_modules(repo_root)
    if not modules:
        print("[ERROR] No module with docs/README.md found.", file=sys.stderr)
        return 2

    total_changed = 0
    total_chapters = 0
    warnings: list[str] = []

    for module in modules:
        module_root = repo_root / module
        readme = module_root / "docs" / "README.md"
        if not readme.is_file():
            warnings.append(f"- {module}: missing docs/README.md")
            continue

        chapters = iter_chapters_from_docs_readme(repo_root, module)
        if not chapters:
            warnings.append(f"- {module}: no chapters parsed from docs/README.md")
            continue

        defaults = select_default_labtests(module_root)
        if not defaults:
            warnings.append(f"- {module}: no *LabTest.java found under src/test/java (will use placeholder)")

        changed = 0
        skipped = 0
        for chapter in chapters:
            total_chapters += 1
            result = rewrite_chapter(
                repo_root=repo_root,
                module=module,
                chapter=chapter,
                default_labtests=defaults,
                dry_run=args.dry_run,
            )
            if result.reason == "skip-already-compliant":
                skipped += 1
            if result.changed:
                changed += 1

        total_changed += changed
        mode = "DRY-RUN" if args.dry_run else "APPLIED"
        print(f"[{mode}] {module}: chapters={len(chapters)}, changed={changed}, skipped={skipped}")

    if warnings:
        print("[WARN] Issues detected:")
        for w in warnings[:50]:
            print(w)
        if len(warnings) > 50:
            print(f"- ... and {len(warnings) - 50} more")

    print(f"[DONE] modules={len(modules)} total_chapters={total_chapters} changed={total_changed} dry_run={args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
