"""微信内容处理器

常驻脚本，每 30 秒扫描笔记同步助手/ 目录：
  - 公众号文章 → DeepSeek 打标签+双链 → 写入 Inbox/
  - 视频号汇总 → 拆分为单条 → DeepSeek → 写入 Inbox/
  - 通过文件哈希去重，已处理的不再重复
"""
import os
import sys
import re
import json
import time
import hashlib
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from common import call_deepseek, load_tag_vocabulary

# ======= 配置区 =======
VAULT_PATH = Path(os.environ.get("OBSIDIAN_VAULT_PATH", Path(__file__).resolve().parent))
WECHAT_PATH = str(Path(os.environ.get("WECHAT_SYNC_PATH", VAULT_PATH / "笔记同步助手")))
INBOX_PATH = str(Path(os.environ.get("OBSIDIAN_INBOX_PATH", VAULT_PATH / "Inbox")))
PROCESSED_LOG = os.path.join(INBOX_PATH, ".wechat_processed.json")
POLL_INTERVAL = 30  # 扫描间隔（秒）
# =====================


def load_processed():
    """加载已处理文件记录"""
    try:
        with open(PROCESSED_LOG, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_processed(data):
    """保存已处理文件记录"""
    with open(PROCESSED_LOG, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def file_hash(filepath):
    """计算文件内容哈希"""
    h = hashlib.md5()
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        h.update(f.read().encode("utf-8", errors="ignore"))
    return h.hexdigest()


def parse_frontmatter(content):
    """分离 YAML frontmatter 和正文"""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return "", content


def extract_yaml_field(fm_text, field):
    """从 YAML 文本中提取指定字段值"""
    m = re.search(rf"^{field}:\s*(.+)$", fm_text, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return ""


def process_article_file(filepath, filename, vocab_str, processed):
    """处理单篇微信公众号文章"""
    file_hash_val = file_hash(filepath)
    if filename in processed and processed[filename] == file_hash_val:
        return False

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return False

    fm_text, body = parse_frontmatter(content)

    # 提取元数据
    author = extract_yaml_field(fm_text, "author") or "未知"
    source = extract_yaml_field(fm_text, "source") or "微信公众号"
    saved_date = extract_yaml_field(fm_text, "saved") or ""
    url = extract_yaml_field(fm_text, "url") or ""

    # 去掉重复的元数据行
    body_clean = re.sub(r"^(公众号名称：.*|作者名称：.*|发布时间：.*)\n?", "", body, flags=re.MULTILINE).strip()

    if not body_clean or len(body_clean) < 20:
        return False

    # 调用 DeepSeek
    tags, linked_text = call_deepseek(body_clean[:1500], f"{source}-{author}", vocab_str)

    # 构建新文件
    title = filename.replace(".md", "")
    safe_title = re.sub(r'[\\/:*?"<>|]', '_', title[:50])
    tags_yaml = "\n".join(f"  - {t}" for t in tags) if tags else "  - 未分类"

    new_content = f"""---
title: "{safe_title}"
date: {saved_date or time.strftime('%Y-%m-%dT%H:%M:%S')}
source: "{source}"
author: "{author}"
url: "{url}"
tags:
{tags_yaml}
---

{linked_text}
"""

    out_name = f"{safe_title}.md"
    out_path = os.path.join(INBOX_PATH, out_name)
    if os.path.exists(out_path):
        out_name = f"{safe_title}_{int(time.time())}.md"
        out_path = os.path.join(INBOX_PATH, out_name)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    # 处理成功，删除笔记同步助手里的原件
    try:
        os.remove(filepath)
    except Exception:
        pass

    processed[filename] = file_hash_val
    save_processed(processed)
    print(f"✅ [公众号] [{', '.join(tags)}] {out_name}")
    return True


def process_daily_summary(filepath, filename, vocab_str, processed):
    """处理视频号每日汇总文件，拆分为单条"""
    file_hash_val = file_hash(filepath)
    if filename in processed and processed[filename] == file_hash_val:
        return False

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return False

    fm_text, body = parse_frontmatter(content)
    entries = re.split(r"(?=####\s*\[视频号\])", body)

    count = 0
    for entry in entries:
        entry = entry.strip()
        if not entry or "####" not in entry:
            continue

        header_match = re.match(r"####\s*\[视频号\]\s*(.+)", entry)
        channel_name = header_match.group(1).strip() if header_match else "视频号"

        date_match = re.search(r"📅\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})", entry)
        entry_date = date_match.group(1) if date_match else ""

        lines = entry.split("\n")
        body_lines = [line for line in lines if not line.startswith("####") and "📅" not in line]
        entry_text = "\n".join(body_lines).strip()

        if not entry_text or len(entry_text) < 10:
            continue

        tags, linked_text = call_deepseek(entry_text[:1500], f"视频号-{channel_name}", vocab_str)

        summary = re.sub(r'[\\/:*?"<>|]', '_', entry_text[:15].strip().replace("\n", " ") or "视频号")
        tags_yaml = "\n".join(f"  - {t}" for t in tags) if tags else "  - 未分类"

        out_name = f"{summary}_{int(time.time())}_{count}.md"
        new_content = f"""---
title: "{summary}"
date: {entry_date or time.strftime('%Y-%m-%dT%H:%M:%S')}
source: "视频号"
author: "{channel_name}"
tags:
{tags_yaml}
---

{linked_text}
"""
        out_path = os.path.join(INBOX_PATH, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"✅ [视频号-{channel_name}] [{', '.join(tags)}] {out_name}")
        count += 1
        time.sleep(1)

    # 所有条目处理完毕，删除原始汇总文件
    if count > 0:
        try:
            os.remove(filepath)
        except Exception:
            pass

    processed[filename] = file_hash_val
    save_processed(processed)
    return count > 0


def scan_and_process(vocab_str):
    """扫描笔记同步助手目录，处理新文件"""
    processed = load_processed()
    new_count = 0

    for root, dirs, files in os.walk(WECHAT_PATH):
        if "images" in root:
            continue
        for filename in files:
            if not filename.endswith(".md") or ".sync-conflict-" in filename:
                continue

            filepath = os.path.join(root, filename)

            if filename.startswith("同步助手_"):
                if process_daily_summary(filepath, filename, vocab_str, processed):
                    new_count += 1
            else:
                if process_article_file(filepath, filename, vocab_str, processed):
                    new_count += 1

    return new_count


def main():
    os.makedirs(os.path.join(INBOX_PATH, "assets"), exist_ok=True)
    print("🚀 微信内容处理器已启动（持续监听模式）...")

    vocab_refresh_time = 0
    vocab_str = ""

    while True:
        try:
            if time.time() - vocab_refresh_time > 300:
                vocab_str = load_tag_vocabulary()
                vocab_refresh_time = time.time()

            count = scan_and_process(vocab_str)
            if count > 0:
                print(f"📊 本轮处理了 {count} 条新内容")

        except Exception as e:
            print(f"⚠️ 扫描错误: {e}")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
