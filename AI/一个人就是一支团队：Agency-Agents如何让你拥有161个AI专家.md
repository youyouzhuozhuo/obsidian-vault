---
title: "一个人就是一支团队：Agency-Agents如何让你拥有161个AI专家"
date: 2026-04-02T20:46:28
source: "微信公众号"
author: "未知"
tags:
  - AI/Agent
  - 编程/开源项目
  - 工具/AI辅助
ai_score: 8
credibility: "high"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
# 一个人就是一支团队：Agency-Agents如何让你拥有161个AI专家
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=Mzk0MTY4MjE4OA==&mid=2247490394&idx=1&sn=d8d01017a4558ef8137b00a57a2ba56c&chksm=c3a76b2fc47e6a918025b8c48141a99606af5d8c7747ed317db49c5d9d66eba6b6340095fd3a&mpshare=1&scene=1&srcid=0318nkpqmopSwre7TrPuUE3m&sharer_shareinfo=96a5af394fedd3bd82a215db67213e87&sharer_shareinfo_first=96a5af394fedd3bd82a215db67213e87#rd)
## 正文


GitHub上最近有个项目火得离谱。

一个叫msitarzewski的开发者，写了30多年代码，Techstars出身，把一套"AI公司"开源了。161个专业AI员工，工程、设计、营销、产品、项目管理、测试、客服、空间计算，12个部门全有。

项目叫 [[Agency-Agents]]，地址是 https://github.com/msitarzewski/agency-agents

短短几天时间，Star从零涨到4万多。[[Greg Isenberg]]在[[X]]上发了条推，讨论就炸开了。不少人看完第一反应是：这不就是我一直想找的吗？

![](https://pic.clipfx.app/c9f9933e8a1abf773acb4f0b577ba441.png)

# 一、 它是什么？

我们现在用[[AI]]，基本就是逮着一个[[ChatGPT]]或[[Claude]]问到底。写代码问它，做营销问它，搞设计也问它。什么都能聊两句，但仔细想想，更像一个"什么都会一点、什么都不精" 的实习生。写代码能写，不够专业；回答问题能答，缺深度。

![](https://pic.clipfx.app/024480baa7f619b5b4d621d2cd9cc303.png)

[[Agency-Agents]]换了个思路：与其让一个通才AI什么都干，不如给每个专业领域配一个专属的AI专家。

每个[[Agent]]有这些特点：专业化（深度领域知识）、人格化（有自己的沟通风格和工作方式）、交付导向（产出能直接用）、生产就绪（工作流经过验证）。

但它跟网上随便搜到的"角色扮演prompt"完全不是一回事。

普通的prompt长这样："你是一个前端开发者。"

[[Agency-Agents]]里的Agent长这样：有名字、有性格、有口头禅、有明确的工作流程（Discovery → Planning → Execution → Review四阶段）、有量化的成功指标，甚至有自己的偏执。安全工程师默认找3-5个问题，[[Reddit]]社区运营的原则是"先成为社区成员，再谈品牌"。

换句话说，它不是告诉AI"你知道什么"，是定义"你怎么干活"。

每个Agent都是一个[[Markdown]]文件。打开是[[YAML]]头部加结构化正文，头部定义名称、描述、emoji、甚至"vibe"（工作态度），正文包含身份定义、核心使命、工作流程、技术交付标准、代码示例和成功指标。

![](https://pic.clipfx.app/7d57e5f704e4398ad4c7c81c2cc52f95.png)

这就是它和普通pr

## AI 分析

- 评分：8/10
- 可信度：high
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：AI Agent、开源项目、工作流、团队协作、Claude Code、MCP

### 信息本质

介绍开源项目Agency-Agents，提供161个专业化AI Agent定义文件，每个Agent有结构化角色、工作流和交付标准，旨在替代通用AI实现团队级协作。

### 可信度判断

来源为微信公众号，但项目本身在GitHub上真实存在，Star数4万+，有Techstars背景开发者维护，Greg Isenberg等知名人士讨论。可信度高，但需自行验证项目实际可用性和维护状态。

### 可利用价值

可直接作为AI编程、内容创作、项目管理等场景的Agent模板库，提升AI输出专业度和一致性。尤其适合需要多角色协作的项目，如开发、设计、营销等。

### 可开发方向

1. 基于该项目构建个人AI团队工作流，集成到Claude Code或Codex中。2. 提取特定Agent定义（如安全工程师、社区运营）适配到自己的项目。3. 开发一个MCP Server或Skills包，让这些Agent可被调用。

### 可内容化方向

1. 写一篇《如何用Agency-Agents搭建你的AI团队》实操教程。2. 对比通用AI vs 专业Agent的产出差异。3. 拆解某个Agent（如安全工程师）的定义，分析其设计思路。

### 下一步

克隆GitHub仓库，阅读README和几个核心Agent的Markdown文件，评估其与当前工作流的兼容性，并尝试在Claude Code中导入一个Agent定义进行测试。

### 风险

项目可能依赖特定AI模型或API，需注意兼容性和成本。Agent定义质量参差不齐，需筛选。开源项目可能停止维护。

### 建议沉淀位置

Projects/AI工具链/AI Agent模板库
