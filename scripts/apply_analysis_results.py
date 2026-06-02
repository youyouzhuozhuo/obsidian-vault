#!/usr/bin/env python3
"""Apply GPT information-use analysis results back to Obsidian notes.

Expected input: Analysis/GPT_ANALYSIS_RESULT.json, a JSON array following
Prompts/GPT信息利用分析任务书.md.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "Analysis" / "GPT_ANALYSIS_RESULT.json"
ALLOWED_ENUMS = {
    "credibility": {"low", "medium", "high", "unknown"},
    "usefulness": {"low", "medium", "high"},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Apply GPT analysis JSON to source notes.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="JSON result file.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files.")
    return parser.parse_args()


def yaml_scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value or ""), ensure_ascii=False)


def normalize_result(item: dict[str, object]) -> dict[str, object]:
    result = dict(item)
    try:
        score = int(result.get("ai_score", 0))
    except (TypeError, ValueError):
        score = 0
    result["ai_score"] = max(1, min(10, score)) if score else ""

    for key, allowed in ALLOWED_ENUMS.items():
        value = str(result.get(key, "unknown")).strip().lower()
        result[key] = value if value in allowed else "unknown"

    result["actionable"] = bool(result.get("actionable", False))
    return result


def upsert_frontmatter(text: str, result: dict[str, object]) -> str:
    fields = {
        "ai_score": result.get("ai_score", ""),
        "credibility": result.get("credibility", ""),
        "usefulness": result.get("usefulness", ""),
        "actionable": result.get("actionable", False),
        "opportunity_type": result.get("opportunity_type", ""),
        "analysis_status": "done",
    }

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        lines = [f"{key}: {yaml_scalar(value)}" for key, value in fields.items() if value != ""]
        return "---\n" + "\n".join(lines) + "\n---\n\n" + text

    fm_text, body = match.group(1), match.group(2)
    for key, value in fields.items():
        if value == "":
            continue
        line = f"{key}: {yaml_scalar(value)}"
        if re.search(rf"^{re.escape(key)}:", fm_text, re.MULTILINE):
            fm_text = re.sub(rf"^{re.escape(key)}:.*$", line, fm_text, flags=re.MULTILINE)
        else:
            fm_text += "\n" + line

    return "---\n" + fm_text.strip() + "\n---\n" + body


def analysis_block(result: dict[str, object]) -> str:
    tags = result.get("tags_suggested", [])
    if isinstance(tags, list):
        tags_text = "、".join(str(tag) for tag in tags)
    else:
        tags_text = str(tags or "")

    return f"""## AI 分析

- 评分：{result.get("ai_score", "")}/10
- 可信度：{result.get("credibility", "")}
- 有用性：{result.get("usefulness", "")}
- 可行动：{"是" if result.get("actionable") else "否"}
- 类型：{result.get("opportunity_type", "")}
- 建议标签：{tags_text}

### 信息本质

{result.get("summary", "")}

### 可信度判断

{result.get("credibility_analysis", "")}

### 可利用价值

{result.get("use_value", "")}

### 可开发方向

{result.get("development_direction", "")}

### 可内容化方向

{result.get("content_direction", "")}

### 下一步

{result.get("next_action", "")}

### 风险

{result.get("risk", "")}

### 建议沉淀位置

{result.get("memory_target", "")}
"""


def remove_existing_analysis(text: str) -> str:
    return re.sub(r"\n+## AI 分析\n.*$", "", text, flags=re.DOTALL).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = ROOT / input_path
    if not input_path.exists():
        raise SystemExit(f"Result file not found: {input_path}")

    data = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("Result JSON must be an array")

    changed = 0
    skipped = 0
    for raw_item in data:
        if not isinstance(raw_item, dict):
            skipped += 1
            continue
        result = normalize_result(raw_item)
        rel_path = str(result.get("path", "")).strip()
        if not rel_path:
            skipped += 1
            continue
        note_path = (ROOT / rel_path).resolve()
        if ROOT not in note_path.parents or not note_path.exists():
            print(f"Skip missing or unsafe path: {rel_path}")
            skipped += 1
            continue

        text = note_path.read_text(encoding="utf-8", errors="ignore")
        updated = upsert_frontmatter(remove_existing_analysis(text), result).rstrip()
        updated += "\n\n" + analysis_block(result).rstrip() + "\n"

        if updated != text:
            changed += 1
            print(f"{'Would update' if args.dry_run else 'Update'} {rel_path}")
            if not args.dry_run:
                note_path.write_text(updated, encoding="utf-8")

    print(f"Changed: {changed}, skipped: {skipped}")


if __name__ == "__main__":
    main()

