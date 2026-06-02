---
title: 长期记忆索引
tags:
  - memory
  - index
---

# 长期记忆索引

这个目录是给用户、Claude Code 和 Codex 读取的短记忆层。它不是原始资料库，而是从 Obsidian 原文中提炼出来的稳定导航和工作流。

## 快速入口

- [[AUTO_INDEX]]
- [[ACTIVE_PROJECTS]]
- [[WORKFLOWS]]
- [[DECISIONS]]
- [[TOPICS/AI工具与Agent]]
- [[TOPICS/编程与项目]]
- [[TOPICS/自媒体与商业]]
- [[TOPICS/金融与投资]]
- [[TOPICS/生活认知]]

## 使用方式

1. 先读本页，判断要查的主题。
2. 再读对应主题页或项目页。
3. 需要证据时，用 `rg` 搜索原始笔记目录。
4. 如果要写入长期记忆，只写稳定结论，不复制整篇文章。

## 当前库结构摘要

- `Inbox/`：Telegram、微信和手动同步进入的待处理内容。
- `AI/`、`编程/`、`工具/`、`自媒体/`、`商业/`、`金融/`、`生活/`、`出海/`、`教育/`：主题归档区。
- `MOC/`：主题地图和控制台。
- `Memory/`：给 AI 读取的长期短记忆。
- `copilot/copilot-conversations/`：历史 Obsidian Copilot 对话。
- `senior-economist-exam/`：独立的高级经济师备考资料区。

## 维护原则

- 原文保留在主题目录，结论沉淀在 `Memory/` 和 `MOC/`。
- `Inbox/` 里的内容不要长期堆积；先去重、补标签、再归档或提炼。
- 图片-only 笔记需要 OCR 或人工补摘要，否则对 AI 记忆价值较低。
- 公开仓库不要写入 token、账号、私密工作资料或敏感计划。

## 自动更新

运行下面命令可以刷新统计信息和主题入口：

```bash
python3 scripts/build_memory_index.py
```
