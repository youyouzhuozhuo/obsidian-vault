"""Telegram → Obsidian 智能知识库

常驻脚本，轮询 Telegram Bot API，自动处理频道消息：
  - 内容去重（持久化 + 正文指纹）
  - DeepSeek API 打标签 + 双链
  - 写入 Inbox/ 待归档
"""
import requests
import sys
import time
import os
import re
import json
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from common import call_deepseek, load_tag_vocabulary, short_summary, yaml_quote
from scripts.auto_analyze_notes import analyze_note, refresh_index

# ======= 配置区 =======
VAULT_PATH = Path(os.environ.get("OBSIDIAN_VAULT_PATH", Path(__file__).resolve().parent))
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
CF_PROXY_URL = os.environ.get("TELEGRAM_API_BASE_URL", "https://tg.youzhuo.online").rstrip("/")
INBOX_PATH = str(Path(os.environ.get("OBSIDIAN_INBOX_PATH", VAULT_PATH / "Inbox")))
STATE_FILE = os.path.join(INBOX_PATH, ".tg_state.json")
AUTO_ANALYZE_ON_IMPORT = os.environ.get("AUTO_ANALYZE_ON_IMPORT", "1") != "0"
AUTO_ANALYZE_MAX_CHARS = int(os.environ.get("AUTO_ANALYZE_MAX_CHARS", "4500"))
AUTO_ANALYZE_DELAY = float(os.environ.get("AUTO_ANALYZE_DELAY", "1"))
# =====================


def load_state():
    """加载持久化状态：last_id 和 processed_ids"""
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
        return state.get("last_id", 0), set(state.get("processed_ids", []))
    except Exception:
        return 0, set()


def save_state(last_id, processed_ids):
    """持久化状态到文件"""
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "last_id": last_id,
                "processed_ids": list(processed_ids),
            }, f)
    except Exception as e:
        print(f"⚠️ 状态保存失败: {e}")


def is_duplicate(text, msg_id, chat_title):
    """检查 inbox 中是否已存在相同来源的消息"""
    if not text.strip():
        return False
    check_text = text[:80].strip()
    for fname in os.listdir(INBOX_PATH):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(INBOX_PATH, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read(2000)
            if f'source: "{chat_title}"' in content and check_text in content:
                return True
        except Exception:
            continue
    return False


def get_tg_file(file_id, save_path):
    try:
        url = f"{CF_PROXY_URL}/bot{BOT_TOKEN}/getFile?file_id={file_id}"
        res = requests.get(url, timeout=20).json()
        if not res.get("ok"):
            return False
        file_path = res["result"]["file_path"]
        download_url = f"{CF_PROXY_URL}/file/bot{BOT_TOKEN}/{file_path}"
        file_res = requests.get(download_url, timeout=60)
        with open(save_path, "wb") as f:
            f.write(file_res.content)
        return True
    except Exception:
        return False


def process_message(item, vocab_str, processed_ids):
    update_id = item.get("update_id")
    if update_id in processed_ids:
        return

    msg = item.get("message") or item.get("channel_post")
    if not msg:
        return

    # 提取来源
    forward_from = msg.get("forward_from_chat")
    if forward_from:
        chat_title = forward_from.get("title") or forward_from.get("username")
    else:
        chat_title = msg.get("chat", {}).get("title") or msg.get("chat", {}).get("username") or "Private"
    safe_chat_title = re.sub(r'[\\/:*?"<>|]', '_', str(chat_title))

    text = msg.get("text") or msg.get("caption") or ""
    msg_id = msg.get("message_id", 0)

    # 内容去重
    if text.strip() and is_duplicate(text, msg_id, safe_chat_title):
        print(f"⏭️ 跳过重复消息 (update_id={update_id}): {text[:30]}...")
        processed_ids.add(update_id)
        return

    if not text.strip() and "photo" not in msg:
        return

    # 下载图片
    image_embed = ""
    if "photo" in msg:
        photo = msg["photo"][-1]
        img_name = f"img_{int(time.time())}.jpg"
        if get_tg_file(photo["file_id"], os.path.join(INBOX_PATH, "assets", img_name)):
            image_embed = f"\n\n![[{img_name}]]"

    if not text.strip() and not image_embed:
        return

    # 调用 DeepSeek 生成标签和双链
    tags, linked_text = [], text
    if text.strip():
        tags, linked_text = call_deepseek(text, safe_chat_title, vocab_str)

    # 构建文件名
    summary = re.sub(r'[\\/:*?"<>|]', '_', text[:12].strip().replace("\n", " ") or "图片信息")
    file_name = f"{summary}_{msg_id}_{int(time.time())}.md"

    # 构建 frontmatter + 内容
    tags_yaml = "\n".join(f"  - {t}" for t in tags) if tags else "  - 未分类"
    now = time.strftime('%Y-%m-%dT%H:%M:%S')
    summary_text = short_summary(text or "图片信息")
    content_type = "photo" if image_embed and not text.strip() else "text"

    md_content = f"""---
title: {yaml_quote(summary)}
date: {now}
source: {yaml_quote(safe_chat_title)}
summary: {yaml_quote(summary_text)}
status: raw
reviewed: false
content_type: {content_type}
tags:
{tags_yaml}
---

{linked_text}{image_embed}
"""

    out_path = Path(INBOX_PATH) / file_name
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    processed_ids.add(update_id)
    tag_str = ", ".join(tags) if tags else "无标签"
    print(f"✅ [{tag_str}] {file_name}")
    if AUTO_ANALYZE_ON_IMPORT:
        try:
            analyze_note(out_path, AUTO_ANALYZE_MAX_CHARS)
            refresh_index()
            if AUTO_ANALYZE_DELAY > 0:
                time.sleep(AUTO_ANALYZE_DELAY)
        except Exception as e:
            print(f"⚠️ AI 分析失败，已保留原始笔记: {e}")


def main():
    if not BOT_TOKEN:
        print("⚠️ 未设置 TELEGRAM_BOT_TOKEN，Telegram 监听未启动")
        return

    os.makedirs(os.path.join(INBOX_PATH, "assets"), exist_ok=True)
    print("🚀 Telegram → Obsidian 智能知识库已启动...")

    last_id, processed_ids = load_state()
    print(f"📂 已恢复状态: last_id={last_id}, 已处理 {len(processed_ids)} 条消息")

    vocab_refresh_time = 0
    vocab_str = ""
    save_counter = 0

    while True:
        try:
            # 每 5 分钟刷新一次标签词库
            if time.time() - vocab_refresh_time > 300:
                vocab_str = load_tag_vocabulary()
                vocab_refresh_time = time.time()

            url = f"{CF_PROXY_URL}/bot{BOT_TOKEN}/getUpdates?offset={last_id + 1}&timeout=30"
            res = requests.get(url, timeout=45)
            data = res.json()

            if data and data.get("result"):
                for item in data["result"]:
                    process_message(item, vocab_str, processed_ids)
                    last_id = item["update_id"]
                    save_counter += 1

                if save_counter >= 5:
                    save_state(last_id, processed_ids)
                    save_counter = 0
        except Exception as e:
            print(f"⚠️ 轮询错误: {e}")
            save_state(last_id, processed_ids)
            time.sleep(5)


if __name__ == "__main__":
    main()
