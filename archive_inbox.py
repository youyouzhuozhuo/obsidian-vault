"""Obsidian 笔记归档工具

职责单一：将 Inbox 中已打标签的笔记按标签归档到分类文件夹。
  - 两个常驻脚本负责打标签入 Inbox：
    · tg_to_obsidian.py  ← Telegram 消息
    · process_wechat.py  ← 微信公众号/视频号
  - 本脚本只需定期手动运行，将 Inbox 清空到分类文件夹。

用法：
  python archive_inbox.py           # 执行归档
  python archive_inbox.py --dry-run # 预览不移动
"""
import os
import re
import sys
import json
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_PATH = str(Path(os.environ.get("OBSIDIAN_VAULT_PATH", Path(__file__).resolve().parent)))
INBOX_PATH = os.path.join(VAULT_PATH, "Inbox")

TAG_MAP = {
    "AI": "AI",
    "编程": "编程",
    "金融": "金融",
    "自媒体": "自媒体",
    "工具": "工具",
    "出海": "出海",
    "商业": "商业",
    "生活": "生活",
    "科技": "科技",
    "教育": "教育",
}


def parse_frontmatter(content):
    """解析 YAML frontmatter，返回 (metadata_dict, body)"""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not m:
        return {}, content
    meta = {}
    for line in m.group(1).splitlines():
        if line.startswith("tags:") or line.startswith("id:"):
            continue
        m2 = re.match(r'^(\w+):\s*(.*)$', line)
        if m2:
            meta[m2.group(1)] = m2.group(2).strip().strip('"').strip("'")
    tags = re.findall(r'^\s+-\s+(.+)$', m.group(1), re.MULTILINE)
    if tags:
        meta["tags"] = tags
    return meta, m.group(2)


def get_target_folder(tags):
    """根据标签列表确定目标文件夹"""
    if not tags:
        return "未分类"
    first_tag = tags[0]
    category = first_tag.split("/")[0]
    return TAG_MAP.get(category, "未分类")


def content_fingerprint(filepath):
    """提取正文指纹（去掉 frontmatter、双链标记后前 300 字）"""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    body = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    body = re.sub(r'\[\[|\]\]', '', body)
    return re.sub(r'\s+', '', body)[:300]


def build_archived_index():
    """扫描已归档文件夹，构建 {fingerprint: path} 索引"""
    index = {}
    for folder in list(TAG_MAP.values()) + ["未分类"]:
        folder_path = os.path.join(VAULT_PATH, folder)
        if not os.path.exists(folder_path):
            continue
        for fname in os.listdir(folder_path):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(folder_path, fname)
            fp = content_fingerprint(fpath)
            index[fp] = fpath
    return index


def archive(dry_run=False):
    """扫描 Inbox，去重并按标签归档到分类文件夹"""
    print("=" * 50)
    print("  Obsidian 笔记归档工具")
    print("=" * 50)

    archived_index = build_archived_index()
    print(f"\n  已归档索引: {len(archived_index)} 篇\n")

    if not os.path.exists(INBOX_PATH):
        print("  Inbox 不存在。")
        return

    files = [f for f in os.listdir(INBOX_PATH) if f.endswith(".md")]
    if not files:
        print("  Inbox 为空，无需处理。")
        return

    # 先构建 Inbox 内部指纹索引，处理内部重复
    inbox_fingerprints = {}
    for fname in sorted(files):
        src = os.path.join(INBOX_PATH, fname)
        fp = content_fingerprint(src)
        if fp in inbox_fingerprints:
            # 保留有标签版本的，删除无标签或后处理的版本
            inbox_fingerprints[fp].append(fname)
        else:
            inbox_fingerprints[fp] = [fname]

    moved = 0
    dup_skipped = 0

    for fname in sorted(files):
        src = os.path.join(INBOX_PATH, fname)
        fp = content_fingerprint(src)

        # Inbox 内部去重：同一指纹有多个文件时，只保留第一个
        if fp in inbox_fingerprints and len(inbox_fingerprints[fp]) > 1:
            if fname != inbox_fingerprints[fp][0]:
                print(f"  ⏭️ 跳过Inbox内重复: {fname}")
                if not dry_run:
                    os.remove(src)
                dup_skipped += 1
                continue

        # 与已归档文件去重
        if fp in archived_index:
            print(f"  ⏭️ 跳过已归档重复: {fname}")
            if not dry_run:
                os.remove(src)
            dup_skipped += 1
            continue

        # 读取标签确定目标文件夹
        with open(src, "r", encoding="utf-8") as f:
            content = f.read()
        meta, _ = parse_frontmatter(content)
        tags = meta.get("tags", [])
        folder = get_target_folder(tags)
        dest_dir = os.path.join(VAULT_PATH, folder)
        os.makedirs(dest_dir, exist_ok=True)

        # 处理同名文件
        dest = os.path.join(dest_dir, fname)
        if os.path.exists(dest):
            name, ext = os.path.splitext(fname)
            i = 1
            while os.path.exists(os.path.join(dest_dir, f"{name}_{i}{ext}")):
                i += 1
            dest = os.path.join(dest_dir, f"{name}_{i}{ext}")

        action = "移动" if not dry_run else "[预览]"
        print(f"  📁 {action}: {fname} → {folder}/")
        if not dry_run:
            os.rename(src, dest)
            archived_index[fp] = dest
        moved += 1

    mode = "预览模式" if dry_run else "已执行"
    print(f"\n{'='*50}")
    print(f"{mode}: 共 {len(files)} 篇 | 归档 {moved} | 去重 {dup_skipped}")


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    if dry:
        print("🔍 预览模式（不会实际移动文件）\n")
    archive(dry_run=dry)
