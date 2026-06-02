"""公共模块：DeepSeek API 配置、提示词模板、标签词库加载。

被 tg_to_obsidian.py 和 process_wechat.py 共同引用。
"""
import json
import os
from pathlib import Path
import re
import time
import requests

# ======= API 配置 =======
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "").strip()
DEEPSEEK_BASE_URL = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
MAX_RETRIES = 2
API_TIMEOUT = 60

# ======= 标签词库路径 =======
VAULT_PATH = Path(os.environ.get("OBSIDIAN_VAULT_PATH", Path(__file__).resolve().parent))
TAG_VOCAB_PATH = Path(os.environ.get("TAG_VOCAB_PATH", VAULT_PATH / "tag_vocabulary.json"))

# 备用标签（词库加载失败时使用）
FALLBACK_TAGS = [
    "AI/LLM", "AI/工具", "AI/编程", "AI/应用", "AI/模型", "AI/Agent",
    "编程/前端", "编程/后端", "编程/Python", "编程/开源项目", "编程/API",
    "金融/投资", "金融/量化交易", "金融/加密货币",
    "自媒体/运营", "自媒体/内容创作", "自媒体/变现",
    "工具/效率", "工具/开发", "工具/资源", "工具/AI辅助",
    "出海/运营", "出海/产品",
    "商业/创业", "商业/思维", "商业/赚钱",
    "生活/心理", "生活/认知", "生活/读书",
    "科技/硬件", "科技/互联网", "科技/安全",
]

# DeepSeek 提示词模板（唯一维护点）
SYSTEM_PROMPT_TEMPLATE = """你是一个专业的内容分析助手。你需要为消息内容生成标签和 wikilink。

## 任务

1. 从预定义的标签词库中选择 1-3 个最相关的标签
2. 在原文中识别关键概念和实体，用 [[...]] 包裹（3-8 个）

## 标签词库
{vocabulary}

## 标签规则
- 只能从上面的词库中选择
- 选 1-3 个最相关、最具体的标签
- 如果词库中没有完全匹配的，选最接近的

## Wikilink 规则
- 只识别专业术语、知名产品名、公司名、核心概念名词
- 不要给常见通用词加链接（如"效率"、"数据"、"信息"、"工具"、"内容"等）
- 每个概念只在整篇文章中第一次出现时添加一次 [[...]]
- 不要改变原文的任何文字，只添加 [[ ]]
- 不要对动词、形容词、数量词添加链接
- 宁可少加也不要错加，精准最重要

## 输出格式
严格输出 JSON，不要输出任何其他内容：
{{"tags": ["标签1", "标签2"], "linked_text": "处理后的文本"}}"""


def load_tag_vocabulary():
    """读取标签词库，展平为列表字符串"""
    try:
        with open(TAG_VOCAB_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        all_tags = []
        for subs in data.get("categories", {}).values():
            all_tags.extend(subs)
        if not all_tags:
            raise ValueError("空词库")
        return "\n".join(f"- {t}" for t in all_tags)
    except Exception:
        print("⚠️ 标签词库加载失败，使用备用词库")
        return "\n".join(f"- {t}" for t in FALLBACK_TAGS)


def yaml_quote(value):
    """Return a YAML-safe quoted scalar."""
    return json.dumps(str(value or ""), ensure_ascii=False)


def short_summary(text, limit=120):
    """Build a compact one-line summary fallback for frontmatter."""
    clean = re.sub(r"\s+", " ", str(text or "")).strip()
    if len(clean) <= limit:
        return clean
    return clean[:limit].rstrip() + "..."


def call_deepseek(text, source_name, vocab_str):
    """调用 DeepSeek API 生成标签和双链文本"""
    if not DEEPSEEK_API_KEY:
        print("⚠️ 未设置 DEEPSEEK_API_KEY，跳过智能标签")
        return [], text

    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(vocabulary=vocab_str)
    user_prompt = f"来源：{source_name}\n\n内容：\n{text}"

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.1,
        "response_format": {"type": "json_object"},
    }
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }

    for attempt in range(MAX_RETRIES + 1):
        try:
            res = requests.post(
                f"{DEEPSEEK_BASE_URL}/v1/chat/completions",
                json=payload,
                headers=headers,
                timeout=API_TIMEOUT,
            )
            if res.status_code == 429:
                time.sleep(10)
                continue
            res.raise_for_status()
            content = res.json()["choices"][0]["message"]["content"]
            result = json.loads(content)
            return result.get("tags", []), result.get("linked_text", text)
        except (json.JSONDecodeError, KeyError, UnboundLocalError):
            # 尝试从 markdown 代码块中提取 JSON
            try:
                m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", content, re.DOTALL)
                if m:
                    result = json.loads(m.group(1))
                    return result.get("tags", []), result.get("linked_text", text)
            except (json.JSONDecodeError, UnboundLocalError):
                pass
            if attempt < MAX_RETRIES:
                time.sleep(2 ** (attempt + 1))
        except Exception as e:
            print(f"⚠️ DeepSeek API 调用失败 ({attempt+1}/{MAX_RETRIES+1}): {e}")
            if attempt < MAX_RETRIES:
                time.sleep(2 ** (attempt + 1))

    return [], text
