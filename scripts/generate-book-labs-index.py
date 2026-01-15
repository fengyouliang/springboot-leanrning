#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
生成“主线之书”的 Labs 索引页（docs-site/content/book/labs-index.md）。

目标：
1) 扫描所有包含 docs/README.md 的模块；
2) 收集每个模块 src/test/java 下的 *LabTest.java；
3) 生成可跳转（到 .java 文件）且可运行（给出 mvn 命令）的 Markdown 索引页。

用法：
  python3 scripts/generate-book-labs-index.py
  python3 scripts/generate-book-labs-index.py --out docs-site/content/book/labs-index.md
"""

from __future__ import annotations

import argparse
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = REPO_ROOT / "docs-site" / "content" / "book" / "labs-index.md"

PREFERRED_MODULE_ORDER = [
    "springboot-basics",
    "spring-core-beans",
    "spring-core-aop",
    "spring-core-aop-weaving",
    "spring-core-tx",
    "springboot-web-mvc",
    "springboot-security",
    "springboot-data-jpa",
    "springboot-cache",
    "springboot-async-scheduling",
    "spring-core-events",
    "spring-core-resources",
    "spring-core-profiles",
    "spring-core-validation",
    "springboot-actuator",
    "springboot-web-client",
    "springboot-testing",
    "springboot-business-case",
]


def discover_modules(repo_root: Path) -> list[str]:
    modules: list[str] = []
    for p in sorted(repo_root.iterdir()):
        if not p.is_dir():
            continue
        if (p / "docs" / "README.md").is_file():
            modules.append(p.name)
    return modules


def order_modules(modules: list[str]) -> list[str]:
    ordered: list[str] = []
    for m in PREFERRED_MODULE_ORDER:
        if m in modules:
            ordered.append(m)
    for m in sorted(modules):
        if m not in ordered:
            ordered.append(m)
    return ordered


def iter_lab_tests(module_root: Path) -> list[Path]:
    test_root = module_root / "src" / "test" / "java"
    if not test_root.is_dir():
        return []
    return sorted(p for p in test_root.rglob("*LabTest.java") if p.is_file())


def md_link(text: str, target: str) -> str:
    return f"[`{text}`]({target})"


def mvn_run_cmd(module: str, test_class: str) -> str:
    return f"mvn -q -pl {module} -Dtest={test_class} test"


def build_markdown(modules: list[str]) -> str:
    lines: list[str] = []

    lines.append("# Labs 索引（可跑入口）")
    lines.append("")
    lines.append("> 本页由 `scripts/generate-book-labs-index.py` 生成。新增/移动 `*LabTest.java` 后请重新生成。")
    lines.append("")
    lines.append("## 运行方式速记")
    lines.append("")
    lines.append("- 全仓库：`mvn -q test`")
    lines.append("- 单模块：`mvn -q -pl <module> test`")
    lines.append("- 单类：`mvn -q -pl <module> -Dtest=<SomeLabTest> test`")
    lines.append("")
    lines.append("## 按模块")
    lines.append("")

    for module in order_modules(modules):
        module_root = REPO_ROOT / module
        tests = iter_lab_tests(module_root)
        lines.append(f"### {module}")
        lines.append("")
        if not tests:
            lines.append("- （未发现 `*LabTest.java`）")
            lines.append("")
            continue

        lines.append(f"- 数量：{len(tests)}")
        lines.append(f"- 模块 docs：[`{module}/docs/README.md`](../{module}/docs/README.md)")
        lines.append("")

        for p in tests:
            rel = p.relative_to(REPO_ROOT).as_posix()
            # labs-index 位于 book/ 下，因此链接到仓库根 docs 的相对路径需要 ../
            href = f"../{rel}"
            cls = p.stem
            lines.append(f"- {md_link(cls, href)}")
            lines.append(f"  - 运行：`{mvn_run_cmd(module, cls)}`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="generate-book-labs-index.py",
        description="生成 docs-site/content/book/labs-index.md（按模块收集 *LabTest.java）。",
    )
    parser.add_argument(
        "--out",
        default=str(DEFAULT_OUT),
        help="输出 markdown 文件路径（默认：docs-site/content/book/labs-index.md）。",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv[1:])
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = (REPO_ROOT / out_path).resolve()

    modules = discover_modules(REPO_ROOT)
    if not modules:
        raise SystemExit("[ERROR] 未发现任何包含 docs/README.md 的模块。")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build_markdown(modules), encoding="utf-8")
    print(f"[OK] Generated labs index: {out_path.relative_to(REPO_ROOT)} (modules={len(modules)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv))

