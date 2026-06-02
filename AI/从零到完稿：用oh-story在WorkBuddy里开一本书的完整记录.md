---
title: "从零到完稿：用oh-story在WorkBuddy里开一本书的完整记录"
date: 2026-05-06 16:38:32
source: "微信公众号"
author: "有料黑科技"
url: "https://mp.weixin.qq.com/s?__biz=MzUxNDAxMzQyMw==&mid=2247496179&idx=1&sn=4a6c5e00c627cb0fae6f5fb71b291e90&chksm=f80d73ddf063ec52bb076d61cd6d64e4fda5f8940d01f246311b415ea630658d462d48b04f1a&mpshare=1&scene=1&srcid=050612Q4CxSM2t0Ns4eidLS7&sharer_shareinfo=18632e6050b1545714cd9a2ab5acc435&sharer_shareinfo_first=18632e6050b1545714cd9a2ab5acc435#rd"
tags:
  - AI/工具
  - 编程/开源项目
  - 自媒体/内容创作
---

GitHub 上有个网文写作工具包叫[[oh-story]]，一口气装 9 个 Skill，从扫榜、拆文、写作到去 AI 味、做封面，一整条链路都能走通。我把它装进[[WorkBuddy]]，对着对话框说"帮我开书"，30 分钟后拿到了一本都市异能小说的完整大纲、角色卡和第一章细纲。

![](https://relay-1.bijitongbu.site/p/3821182de9887631858a7b9042723d2e.png)

别被"AI 写网文"这四个字吓到。它干的活很具体：**每个环节你下指令，AI 出活，你拍板。**

​

---

## 一句话安装9个技能：WorkBuddy如何自动拉取oh-story全栈

在 WorkBuddy 对话框里直接说：

​

> 安装这个 skill https://github.com/worldwonderer/oh-story-claudecode

WorkBuddy 自动拉仓库，9 个 Skill 全部装好。装完之后你多了这些能力：

| Skill | 触发方式 | 干什么 |
| --- | --- | --- |
| `story-long-write` | `/story-long-write`或"帮我开书" | 长篇写作：大纲、角色、正文 |
| `story-long-scan` | `/story-long-scan` | 扫榜：起点、番茄、晋江市场趋势 |
| `story-long-analyze` | `/story-long-analyze` | 拆文：前三章拆解、爽点设计 |
| `story-short-write` | `/story-short-write` | 短篇写作 |
| `story-short-scan` | `/story-short-scan` | 短篇扫榜 |
| `story-short-analyze` | `/story-short-analyze` | 短篇拆文 |
| `story-deslop` | `/story-deslop`或"这篇太AI了" | 去 AI 味 |
| `story-cover` | `/story-cover`或"帮我做封面" | 封面生成 |
| `browser-cdp` | `/browser-cdp` | 浏览器自动化（扫榜用） |

打斜杠命令和说人话都能触发。

​

---

## 30分钟生成完整小说架构：story-long-write输出全记录

装好以后直接说你要写什么。比如：

​

> 帮我开一本都市异能网文，主角是普通外卖员突然觉醒读心术

`story-long-write` 接到指令后会走一套内部流程：**题材定位 → 世界观 → 角色 → 大纲 → 细纲。**

![](https://relay-1.bijitongbu.site/p/8a49df22f8df265123c261533cd158ec.png)

它给你输出的不是一段聊天框里的文字，而是一整套文件夹。设定、大纲、正文、伏笔追踪，全按目录拆好存进文件系统：

​

```
你的书名/
├── 设定/
│   ├── 世界观/          # 异能体系、世界规则
│   ├── 角色/            # 每个角色一个文件
│   ├── 势力/            # 组织、阵营
│   ├── 关系.md          # 人物关系图
│   └── 题材定位.md      # 核心卖点+对标
```
