#!/usr/bin/env python3
"""Generate a compact Obsidian vault index for AI memory use.

The script only writes Memory/AUTO_INDEX.md. It does not move, delete, or edit
source notes.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "Memory" / "AUTO_INDEX.md"
TAG_VOCAB = ROOT / "tag_vocabulary.json"
EXCLUDED_PARTS = {".git", ".verysync", ".trash", "__pycache__"}


def is_note(path: Path) -> bool:
    if path.suffix != ".md":
        return False
    return not any(part in EXCLUDED_PARTS for part in path.parts)


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text

    fm_text, body = match.group(1), match.group(2)
    meta: dict[str, object] = {}
    current_list_key = ""

    for line in fm_text.splitlines():
        key_match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if key_match:
            key, value = key_match.group(1), key_match.group(2).strip()
            current_list_key = key if value == "" else ""
            if value:
                if value.startswith("[") and value.endswith("]"):
                    meta[key] = [
                        item.strip().strip('"').strip("'")
                        for item in value[1:-1].split(",")
                        if item.strip()
                    ]
                else:
                    meta[key] = value.strip('"').strip("'")
            elif key not in meta:
                meta[key] = []
            continue

        item_match = re.match(r"^\s+-\s+(.+?)\s*$", line)
        if item_match and current_list_key:
            meta.setdefault(current_list_key, [])
            value = item_match.group(1).strip().strip('"').strip("'")
            existing = meta[current_list_key]
            if isinstance(existing, list):
                existing.append(value)

    return meta, body


def load_valid_tags() -> set[str]:
    valid = {
        "未分类",
        "MOC",
        "Obsidian/系统",
        "memory",
        "index",
        "projects",
        "workflows",
        "decisions",
        "topic",
    }
    try:
        data = json.loads(TAG_VOCAB.read_text(encoding="utf-8"))
        for tags in data.get("categories", {}).values():
            valid.update(tags)
    except Exception:
        pass
    return valid


def compact_body(body: str) -> str:
    body = re.sub(r"!\[\[[^\]]+\]\]", "", body)
    body = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", body)
    body = re.sub(r"\s+", "", body)
    return body


def md_table(rows: list[tuple[object, object]], headers: tuple[str, str]) -> str:
    if not rows:
        return "_无_\n"
    lines = [f"| {headers[0]} | {headers[1]} |", "| --- | ---: |"]
    lines.extend(f"| {name} | {count} |" for name, count in rows)
    return "\n".join(lines) + "\n"


def main() -> None:
    files = sorted(path for path in ROOT.rglob("*.md") if is_note(path.relative_to(ROOT)))
    valid_tags = load_valid_tags()

    folder_counts: Counter[str] = Counter()
    tag_counts: Counter[str] = Counter()
    invalid_tags: Counter[str] = Counter()
    title_paths: defaultdict[str, list[str]] = defaultdict(list)

    total_frontmatter = 0
    no_tags = 0
    uncategorized = 0
    image_only = 0
    has_url = 0
    has_summary = 0
    has_status = 0

    for path in files:
        rel = path.relative_to(ROOT)
        folder_counts[rel.parts[0] if len(rel.parts) > 1 else "_root"] += 1
        text = path.read_text(encoding="utf-8", errors="ignore")
        meta, body = parse_frontmatter(text)

        if meta:
            total_frontmatter += 1
        title = str(meta.get("title", "")).strip()
        if title:
            title_paths[title].append(str(rel))

        tags = meta.get("tags", [])
        if not isinstance(tags, list):
            tags = [str(tags)]
        tags = [str(tag).strip() for tag in tags if str(tag).strip()]

        if tags:
            tag_counts.update(tags)
        else:
            no_tags += 1

        for tag in tags:
            if tag == "未分类":
                uncategorized += 1
            if tag not in valid_tags:
                invalid_tags[tag] += 1

        if "url" in meta:
            has_url += 1
        if "summary" in meta:
            has_summary += 1
        if "status" in meta:
            has_status += 1
        if len(compact_body(body)) < 20 and re.search(r"!\[\[|!\[", body):
            image_only += 1

    duplicate_titles = {title: paths for title, paths in title_paths.items() if len(paths) > 1}
    duplicate_rows = sorted(
        ((title, len(paths)) for title, paths in duplicate_titles.items()),
        key=lambda item: item[1],
        reverse=True,
    )[:20]

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"""---
title: 自动记忆索引
tags:
  - memory
  - index
generated: {now}
---

# 自动记忆索引

本页由 `scripts/build_memory_index.py` 生成。它只反映结构和维护信号，不代表用户已经确认其中所有内容。

## 总览

| 指标 | 数量 |
| --- | ---: |
| Markdown 文件 | {len(files)} |
| 有 frontmatter | {total_frontmatter} |
| 无 tags | {no_tags} |
| 未分类标签 | {uncategorized} |
| 图片-only 或近似图片-only | {image_only} |
| 有 URL | {has_url} |
| 有 summary 字段 | {has_summary} |
| 有 status 字段 | {has_status} |
| 重复 title 数 | {len(duplicate_titles)} |

## 文件夹分布

{md_table(folder_counts.most_common(30), ("文件夹", "笔记数"))}
## 高频标签

{md_table(tag_counts.most_common(40), ("标签", "次数"))}
## 不在词库中的标签

{md_table(invalid_tags.most_common(30), ("标签", "次数"))}
## 重复标题

{md_table(duplicate_rows, ("标题", "重复数"))}
## 建议维护顺序

1. 处理 `Inbox/` 中的未分类和图片-only 内容。
2. 统一不在词库中的标签，避免 Dataview 聚合失效。
3. 对重复标题做人工确认后再合并或删除。
4. 给高价值笔记补 `summary` 和 `status`，再沉淀到 `Memory/` 或 `MOC/`。
5. 每次结构调整后重新运行本脚本。
"""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
