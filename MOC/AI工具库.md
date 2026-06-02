---
title: AI 工具库
tags: [MOC]
---

# AI 工具库

> 自动聚合所有 AI 相关笔记，按子类分类。

## AI 工具

```dataview
TABLE date AS "日期", source AS "来源"
FROM "AI"
WHERE contains(tags, "AI/工具")
SORT date DESC
```

## AI Agent

```dataview
TABLE date AS "日期", source AS "来源"
FROM "AI"
WHERE contains(tags, "AI/Agent")
SORT date DESC
```

## AI 应用

```dataview
TABLE date AS "日期", source AS "来源"
FROM "AI"
WHERE contains(tags, "AI/应用")
SORT date DESC
```

## AI 模型

```dataview
TABLE date AS "日期", source AS "来源"
FROM "AI"
WHERE contains(tags, "AI/模型")
SORT date DESC
```

## AI 编程

```dataview
TABLE date AS "日期", source AS "来源"
FROM "AI"
WHERE contains(tags, "AI/编程")
SORT date DESC
```

## AI LLM

```dataview
TABLE date AS "日期", source AS "来源"
FROM "AI"
WHERE contains(tags, "AI/LLM")
SORT date DESC
```

## AI 提示词

```dataview
TABLE date AS "日期", source AS "来源"
FROM "AI"
WHERE contains(tags, "AI/提示词")
SORT date DESC
```

## 其他 AI

```dataview
TABLE date AS "日期", source AS "来源"
FROM "AI"
WHERE !contains(tags, "AI/工具") AND !contains(tags, "AI/Agent") AND !contains(tags, "AI/应用") AND !contains(tags, "AI/模型") AND !contains(tags, "AI/编程") AND !contains(tags, "AI/LLM") AND !contains(tags, "AI/提示词")
SORT date DESC
```
