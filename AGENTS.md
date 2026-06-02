# AGENTS.md

这个 Obsidian 库既是笔记库，也是给 Codex/Claude Code 使用的长期外部记忆库。

## 使用原则

- 先读 `Memory/INDEX.md`，再按需要读取 `Memory/ACTIVE_PROJECTS.md`、`Memory/WORKFLOWS.md`、`Memory/DECISIONS.md` 和 `MOC/第二大脑控制台.md`。
- 不要一开始扫描全库。只有在用户明确要求分析某个主题时，才读取对应文件夹或用 `rg` 搜索。
- `Inbox/` 是原始输入区，默认不要移动、删除或改写其中的笔记。
- `AI/`、`编程/`、`自媒体/`、`金融/`、`商业/`、`生活/` 等目录是归档资料区，主要用于检索证据。
- `MOC/` 是主题地图区，优先作为导航入口。
- `Memory/` 是长期记忆区，内容应该短、稳定、可复用；不要把整篇原文复制进去。

## 改动规则

- 改进结构时，优先新增索引、控制台、摘要和工作流说明，避免大规模搬移已有笔记。
- 删除、合并、批量归档笔记前，先征得用户确认。
- 公开 GitHub 仓库内不要写入 API key、token、账号、私人财务、单位资料或敏感关系信息。
- 对脚本做改动后，至少运行 `python3 -m py_compile common.py tg_to_obsidian.py process_wechat.py archive_inbox.py scripts/build_memory_index.py`。

## 推荐检索方式

```bash
rg "关键词" --glob "*.md" --glob "!/.verysync/**" --glob "!/.trash/**"
find . -name "*.md" -type f -not -path "./.verysync/*" -not -path "./.trash/*"
```

## 工作目标

把这个库从“自动收藏夹”逐步变成“第二大脑”：

1. 收集：Telegram、微信、手动笔记进入 `Inbox/`。
2. 清洗：去重、补元数据、识别图片-only 和未分类内容。
3. 归档：按主题进入资料目录。
4. 提炼：把有价值的原始资料变成 `MOC/`、`Memory/` 和项目页。
5. 调用：Codex/Claude Code 先读短记忆，再按需检索原文。
