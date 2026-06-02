# Analysis

这个目录用于承接 GPT 对已有 Obsidian 笔记的“信息利用分析”。

## 工作流

1. 导出待分析批次：

```bash
python3 scripts/export_analysis_batch.py --folder Inbox --limit 20
```

2. 把生成的 `Analysis/GPT_ANALYSIS_BATCH.md` 发给 GPT。

3. 让 GPT 严格按 `Prompts/GPT信息利用分析任务书.md` 输出 JSON 数组。

4. 将 GPT 输出保存为：

```text
Analysis/GPT_ANALYSIS_RESULT.json
```

5. 回填分析结果：

```bash
python3 scripts/apply_analysis_results.py --dry-run
python3 scripts/apply_analysis_results.py
```

## 原则

- GPT 负责判断价值，不负责直接改原始笔记。
- 回填脚本会给原笔记追加 `## AI 分析`，并在 frontmatter 中补充 `ai_score`、`credibility`、`usefulness`、`actionable`、`opportunity_type`。
- 对高价值内容，再人工或让 AI 沉淀到 `Memory/`、`MOC/` 或项目页。
- `GPT_ANALYSIS_BATCH.md` 和 `GPT_ANALYSIS_RESULT.json` 默认不进入 GitHub；它们是本地工作文件。
