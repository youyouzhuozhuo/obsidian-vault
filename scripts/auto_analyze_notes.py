#!/usr/bin/env python3
"""Analyze Obsidian notes with DeepSeek and write results back in place."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import time
from typing import Any

import requests

try:
    from scripts.apply_analysis_results import (
        analysis_block,
        normalize_result,
        remove_existing_analysis,
        upsert_frontmatter,
    )
except ModuleNotFoundError:
    from apply_analysis_results import (
        analysis_block,
        normalize_result,
        remove_existing_analysis,
        upsert_frontmatter,
    )


ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = ROOT / "Prompts" / "GPT信息利用分析任务书.md"
EXCLUDED_DIRS = {
    ".git",
    ".obsidian",
    ".trash",
    ".verysync",
    "__pycache__",
    "Analysis",
    "Memory",
    "MOC",
    "Prompts",
    "Templates",
    "scripts",
    "copilot",
}
EXCLUDED_FILES = {"AGENTS.md", "CLAUDE.md", "README.md"}

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "").strip()
DEEPSEEK_BASE_URL = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
DEEPSEEK_MODEL = os.environ.get("DEEPSEEK_ANALYSIS_MODEL", "deepseek-chat").strip()
API_TIMEOUT = int(os.environ.get("DEEPSEEK_ANALYSIS_TIMEOUT", "90"))
MAX_RETRIES = int(os.environ.get("DEEPSEEK_ANALYSIS_RETRIES", "2"))
AUTO_GIT_SYNC_ON_IMPORT = os.environ.get("AUTO_GIT_SYNC_ON_IMPORT", "1") != "0"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Auto-analyze Obsidian notes with DeepSeek.")
    parser.add_argument("--folder", action="append", help="Folder to scan. Repeatable. Defaults to all content folders.")
    parser.add_argument("--limit", type=int, default=0, help="Maximum notes to analyze. 0 means no limit.")
    parser.add_argument("--max-chars", type=int, default=4500, help="Maximum note body characters sent to DeepSeek.")
    parser.add_argument("--include-analyzed", action="store_true", help="Re-analyze notes that already have AI analysis.")
    parser.add_argument("--dry-run", action="store_true", help="Show target notes without calling DeepSeek or writing files.")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between API calls, in seconds.")
    parser.add_argument("--no-index", action="store_true", help="Do not refresh Memory/AUTO_INDEX.md after changes.")
    return parser.parse_args()


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


def compact_body(text: str, max_chars: int) -> str:
    text = remove_existing_analysis(text).strip()
    _, body = parse_frontmatter(text)
    body = body.strip()
    if len(body) <= max_chars:
        return body
    return body[:max_chars].rstrip() + "\n\n...[已截断]"


def is_target_note(path: Path, include_analyzed: bool) -> bool:
    rel = path.relative_to(ROOT)
    if path.suffix != ".md":
        return False
    if path.name in EXCLUDED_FILES or path.name.startswith("."):
        return False
    if any(part in EXCLUDED_DIRS or part.startswith(".") for part in rel.parts):
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not include_analyzed and (
        "## AI 分析" in text
        or 'analysis_status: "done"' in text
        or "analysis_status: done" in text
        or 'analysis_status: "skipped"' in text
        or "analysis_status: skipped" in text
    ):
        return False
    return True


def collect_notes(folders: list[str] | None, include_analyzed: bool) -> list[Path]:
    roots = []
    if folders:
        roots = [(ROOT / folder).resolve() for folder in folders]
    else:
        roots = [ROOT]

    notes: list[Path] = []
    for scan_root in roots:
        if not scan_root.exists():
            print(f"Skip missing folder: {scan_root.relative_to(ROOT) if ROOT in scan_root.parents else scan_root}")
            continue
        for path in scan_root.rglob("*.md"):
            if path.is_file() and is_target_note(path, include_analyzed):
                notes.append(path)
    return sorted(set(notes), key=lambda p: p.stat().st_mtime)


def build_prompt(rel_path: str, title: str, meta: dict[str, str], body: str) -> list[dict[str, str]]:
    task = PROMPT_PATH.read_text(encoding="utf-8", errors="ignore") if PROMPT_PATH.exists() else ""
    system = f"""{task}

你现在只分析一条笔记。严格输出 JSON 对象，不要输出 Markdown，不要解释。
必须包含任务书中的所有字段。path 必须等于我提供的原笔记路径。"""
    user = f"""path: {rel_path}
title: {title}
date: {meta.get("date", "")}
source: {meta.get("source", "")}
author: {meta.get("author", "")}

笔记正文：
{body}"""
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def extract_json_object(content: str) -> dict[str, Any]:
    content = content.strip()
    if content.startswith("```"):
        match = re.search(r"```(?:json)?\s*(.*?)\s*```", content, re.DOTALL)
        if match:
            content = match.group(1).strip()

    data = json.loads(content)
    if isinstance(data, list):
        if not data or not isinstance(data[0], dict):
            raise ValueError("JSON list result is empty or invalid")
        return data[0]
    if not isinstance(data, dict):
        raise ValueError("DeepSeek result must be a JSON object")
    return data


def call_deepseek_analysis(messages: list[dict[str, str]]) -> dict[str, Any]:
    if not DEEPSEEK_API_KEY:
        raise RuntimeError("DEEPSEEK_API_KEY is not set")

    payload: dict[str, Any] = {
        "model": DEEPSEEK_MODEL,
        "messages": messages,
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
    }
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }

    last_error: Exception | None = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = requests.post(
                f"{DEEPSEEK_BASE_URL}/chat/completions",
                json=payload,
                headers=headers,
                timeout=API_TIMEOUT,
            )
            if response.status_code == 429 and attempt < MAX_RETRIES:
                time.sleep(10)
                continue
            response.raise_for_status()
            content = response.json()["choices"][0]["message"]["content"]
            return extract_json_object(content)
        except Exception as exc:
            last_error = exc
            if attempt < MAX_RETRIES:
                time.sleep(2 ** (attempt + 1))
    raise RuntimeError(f"DeepSeek analysis failed: {last_error}")


def apply_result(note_path: Path, result: dict[str, Any]) -> bool:
    normalized = normalize_result(result)
    text = note_path.read_text(encoding="utf-8", errors="ignore")
    updated = upsert_frontmatter(remove_existing_analysis(text), normalized).rstrip()
    updated += "\n\n" + analysis_block(normalized).rstrip() + "\n"
    if updated == text:
        return False
    note_path.write_text(updated, encoding="utf-8")
    return True


def mark_skipped(note_path: Path, reason: str) -> bool:
    text = note_path.read_text(encoding="utf-8", errors="ignore")
    updated = upsert_frontmatter(
        text,
        {
            "analysis_status": "skipped",
            "analysis_summary": reason,
        },
    )
    if updated == text:
        return False
    note_path.write_text(updated, encoding="utf-8")
    return True


def analyze_note(note_path: Path, max_chars: int, dry_run: bool = False) -> bool:
    rel_path = str(note_path.relative_to(ROOT))
    text = note_path.read_text(encoding="utf-8", errors="ignore")
    meta, _ = parse_frontmatter(text)
    title = meta.get("title") or note_path.stem
    body = compact_body(text, max_chars)
    if len(body.strip()) < 10:
        print(f"Skip too short: {rel_path}")
        if not dry_run:
            return mark_skipped(note_path, "内容过短，暂无可分析信息")
        return False

    if dry_run:
        print(f"Would analyze {rel_path}")
        return False

    messages = build_prompt(rel_path, title, meta, body)
    result = call_deepseek_analysis(messages)
    result["path"] = rel_path
    changed = apply_result(note_path, result)
    print(f"{'Analyzed' if changed else 'Already current'} {rel_path}")
    return changed


def refresh_index() -> None:
    import sys

    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_memory_index.py")], check=False)


def auto_git_sync(paths: list[Path], message: str) -> None:
    if not AUTO_GIT_SYNC_ON_IMPORT:
        return

    rel_paths: list[str] = []
    for path in paths:
        resolved = path.resolve()
        try:
            rel_paths.append(str(resolved.relative_to(ROOT)))
        except ValueError:
            continue

    if not rel_paths:
        return

    try:
        subprocess.run(["git", "add", "--", *rel_paths], cwd=ROOT, check=True)
        status = subprocess.check_output(["git", "status", "--porcelain", "--", *rel_paths], cwd=ROOT, text=True)
        if not status.strip():
            return

        subprocess.run(["git", "commit", "-m", message], cwd=ROOT, check=True)
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=ROOT, text=True).strip()
        subprocess.run(["git", "push", "origin", branch], cwd=ROOT, check=True)
        print(f"✅ GitHub 已同步: {message}")
    except Exception as exc:
        print(f"⚠️ GitHub 自动同步失败，已保留本地变更: {exc}")


def main() -> None:
    args = parse_args()
    notes = collect_notes(args.folder, args.include_analyzed)
    if args.limit > 0:
        notes = notes[: args.limit]

    print(f"Target notes: {len(notes)}")
    changed = 0
    failed = 0
    for index, note in enumerate(notes, 1):
        rel = note.relative_to(ROOT)
        try:
            print(f"[{index}/{len(notes)}] {rel}")
            if analyze_note(note, args.max_chars, args.dry_run):
                changed += 1
            if not args.dry_run and args.delay > 0:
                time.sleep(args.delay)
        except Exception as exc:
            failed += 1
            print(f"Failed {rel}: {exc}")

    if changed and not args.no_index and not args.dry_run:
        refresh_index()
    print(f"Done. changed={changed}, failed={failed}, target={len(notes)}")


if __name__ == "__main__":
    main()
