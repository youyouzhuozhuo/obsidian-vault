---
title: 工作流
tags:
  - memory
  - workflows
---

# 工作流

## 信息进入 Obsidian

```text
Telegram / 微信 / 手动保存
  -> Inbox
  -> DeepSeek 标签与双链
  -> 去重和归档
  -> MOC / Memory / Project 页面
```

## 每日维护

1. 打开 [[MOC/第二大脑控制台]]。
2. 查看 `Inbox` 待处理内容。
3. 优先处理图片-only、未分类、明显重复的内容。
4. 对高价值内容补一句自己的判断。
5. 导出一批待分析内容给 GPT：

```bash
python3 scripts/export_analysis_batch.py --folder Inbox --limit 20
```

6. 把 `Analysis/GPT_ANALYSIS_BATCH.md` 发给 GPT，让它按 `Prompts/GPT信息利用分析任务书.md` 输出 JSON。
7. 将 JSON 保存为 `Analysis/GPT_ANALYSIS_RESULT.json`，先预览再回填：

```bash
python3 scripts/apply_analysis_results.py --dry-run
python3 scripts/apply_analysis_results.py
```

8. 运行 `python3 scripts/build_memory_index.py` 刷新记忆索引。

## 每周维护

1. 按主题查看 MOC。
2. 从原始资料中提炼 3-5 条长期结论到 `Memory/TOPICS/`。
3. 把可执行想法移动到 `Memory/ACTIVE_PROJECTS.md` 或单独项目页。
4. 对公开 GitHub 仓库做一次 secret scan。

## Claude Code / Codex 调用本库

1. 先读 `AGENTS.md` 或 `CLAUDE.md`。
2. 再读 `Memory/INDEX.md`。
3. 对特定主题使用 `rg` 搜索。
4. 回答时优先引用短记忆；需要证据再打开原文。

## 信息利用分析

目标：让每条收藏不只停留在“有用”，而是变成可判断、可行动、可沉淀的信息资产。

分析字段：

- `ai_score`：1-10 分，判断综合价值。
- `credibility`：可信度。
- `usefulness`：有用性。
- `actionable`：是否值得行动。
- `opportunity_type`：项目、内容、工具、研究、投资、认知、风险或资料。
- `analysis_status`：是否已经完成分析。

高价值内容的后续流向：

```text
原始笔记
  -> AI 分析卡片
  -> 高分/可行动筛选
  -> Memory/TOPICS 或项目页
  -> 具体执行或内容创作
```

## GitHub 同步

```bash
git status --short
git add AGENTS.md CLAUDE.md MOC Memory scripts
git commit -m "Improve Obsidian second brain structure"
git push
```
