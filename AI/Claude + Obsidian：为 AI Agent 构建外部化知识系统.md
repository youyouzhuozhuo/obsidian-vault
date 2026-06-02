---
title: "Claude + Obsidian：为 AI Agent 构建外部化知识系统"
date: 2026-04-02T20:46:00
source: "微信公众号"
author: "未知"
tags:
  - AI/Agent
  - 工具/效率
  - 编程/开源项目
---

# Claude + Obsidian：为 AI Agent 构建外部化知识系统
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzIzMDY1NjIwOQ==&mid=2247484386&idx=1&sn=9b18e6559db0a004ee73932150760ad9&chksm=e9d33e845c11afdea9ad4bf713b32bb72d3c8ddb1d81f75f7e98bba3112236e2870adff8988a&mpshare=1&scene=1&srcid=03189GvQBTe5LvgmzqvI6MH8&sharer_shareinfo=9ef5019254011acbe39c3c6915e19606&sharer_shareinfo_first=9ef5019254011acbe39c3c6915e19606#rd)
## 正文


# Claude + Obsidian：为 AI Agent 构建外部化知识系统

**原文作者**：Nyk from Builderz  
**原文链接**：https://x.com/nyk_builderz/status/2030904887186514336

---

## 🧠 核心洞察

**人类已经外部化知识数千年了**，这正是进步得以实现的原因。

每一种媒介——洞穴壁画、羊皮纸、书籍、数字信息——都让下一代能够在前人的基础上继续建设，而不是从零开始。

**Agent 生活在上下文窗口中，就像人类生活在寿命中**。它们是临时的、有边界的，会话结束时就会忘记一切。

它们需要外部化知识，原因和我们当年需要文字一样：**超越个体记忆的限制**。

​

> **知识图谱就是 Agent 的图书馆**。每个会话，它都能调用整个组织积累的知识，并在此基础上运作。

---

## 📚 知识记忆栈架构

### 层级 1：CLAUDE.md（项目级）

**位置**：项目根目录  
**作用**：架构决策、编码规范、边界约束  
**特点**：每次会话自动加载，确保一致性

### 层级 2：Claude Code 自动记忆

**位置**：～/.claude/projects/  
**作用**：跨会话持久化观察和发现  
**特点**：自动保存，无需手动干预

### 层级 3：Obsidian 知识库（组织级）

**位置**：个人 Obsidian Vault  
**作用**：长期知识积累和关联  
**特点**：通过 [[MCP]] 服务器连接到 [[Claude]]

---

## 🛠️ Obsidian 文件夹结构推荐

📁 Knowledge-Graph/  
├── 📁 0-Inbox/ # 临时捕获区  
├── 📁 1-Fleeting/ # 临时笔记  
├── 📁 2-Literature/ # 文献笔记（来自视频/文章）  
├── 📁 3-Permanent/ # 永久笔记（原子化知识）  
├── 📁 4-Maps/ # 知识地图/[[MOC]]  
├── 📁 5-Templates/ # 笔记模板  
├── 📁 6-Archives/ # 归档  
└── 📁 99-Meta/ # 系统配置

---

## 🔌 MCP 服务器配置

### 1. Smart-Connections MCP

**作用**：让 Claude 读取和搜索 Obsidian 知识库  
**安装**：

​
p
