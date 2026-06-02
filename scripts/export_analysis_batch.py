#!/usr/bin/env python3
"""Export Obsidian notes into a GPT analysis batch.

This script does not modify source notes. It writes Analysis/GPT_ANALYSIS_BATCH.md.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "Analysis" / "GPT_ANALYSIS_BATCH.md"
PROMPT_PATH = ROOT / "Prompts" / "GPT信息利用分析任务书.md"
EXCLUDED_PARTS = {".git", ".verysync", ".trash", "__pycache__"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export notes for GPT information-use analysis.")
    parser.add_argument("--folder", default="Inbox", help="Folder to export, relative to vault root.")
    parser.add_argument("--limit", type=int, default=20, help="Maximum notes to export.")
    parser.add_argument("--max-chars", type=int, default=3500, help="Maximum characters per note body.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output markdown file.")
    parser.add_argument("--include-analyzed", action="store_true", help="Include notes that already have AI analysis.")
    return parser.parse_args()


def is_note(path: Path) -> bool:
    if path.suffix != ".md":
        return False
    return not any(part in EXCLUDED_PARTS for part in path.parts)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text

    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^([A-Za-z_][\w-]*):\s*(.+)$", line)
        if item:
            meta[item.group(1)] = item.group(2).strip().strip('"').strip("'")
    return meta, match.group(2)


def compact(text: str, limit: int) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "\n\n...[已截断]"


def main() -> None:
    args = parse_args()
    folder = ROOT / args.folder
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output

    if not folder.exists():
        raise SystemExit(f"Folder not found: {folder}")

    notes: list[tuple[Path, dict[str, str], str]] = []
    for path in sorted(folder.rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True):
        rel = path.relative_to(ROOT)
        if not is_note(rel):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if not args.include_analyzed and "## AI 分析" in text:
            continue
        meta, body = parse_frontmatter(text)
        notes.append((rel, meta, compact(body, args.max_chars)))
        if len(notes) >= args.limit:
            break

    prompt = PROMPT_PATH.read_text(encoding="utf-8", errors="ignore") if PROMPT_PATH.exists() else ""
    sections = [
        "# GPT 信息利用分析批次",
        "",
        "下面是任务书和待分析笔记。请按任务书要求严格输出 JSON 数组。",
        "",
        "## 任务书",
        "",
        prompt.strip(),
        "",
        "## 待分析笔记",
        "",
    ]

    for index, (rel, meta, body) in enumerate(notes, 1):
        title = meta.get("title") or rel.stem
        source = meta.get("source", "")
        date = meta.get("date", "")
        sections.extend(
            [
                f"### {index}. {title}",
                "",
                f"- path: `{rel}`",
                f"- title: `{title}`",
                f"- date: `{date}`",
                f"- source: `{source}`",
                "",
                "```markdown",
                body,
                "```",
                "",
            ]
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(sections), encoding="utf-8")
    print(f"Wrote {output.relative_to(ROOT)} with {len(notes)} notes")


if __name__ == "__main__":
    main()

