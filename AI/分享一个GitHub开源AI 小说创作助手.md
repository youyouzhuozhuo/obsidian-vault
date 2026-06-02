---
title: "分享一个GitHub开源AI 小说创作助手"
date: 2026-04-02T20:47:21
source: "微信公众号"
author: "未知"
tags:
  - AI/应用
  - 编程/开源项目
  - 工具/AI辅助
ai_score: 6
credibility: "medium"
usefulness: "medium"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
# 分享一个GitHub开源AI 小说创作助手
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzkwNjczNTMxOA==&mid=2247484640&idx=1&sn=db66d46983b0dcfb93ca87f426e229e8&chksm=c179506510bc11f63752071d71fdb2d97a1cb4dd7714c08592b95cc41fcbb0524344b3f82d8c&mpshare=1&scene=1&srcid=0306VM9kOK8M8vOBBCLqsLEf&sharer_shareinfo=db2bb76ec892515519c1d109aa4f6964&sharer_shareinfo_first=6ecf3695cbcb2bfa5363a21105cbba02#rd)
## 正文


# AI 小说创作助手 (AI Novel Writing Assistant)

该仓库是一个**AI 驱动的智能小说创作生产力工具**，核心目标是通过 AI 技术 + 精细化提示词管理，帮助工作室 / 个人作者实现小说的快速、批量创作，宣称能将写作效率提升 20 倍。

1. 全链路小说创作支持

覆盖小说创作全流程，从顶层设计到内容生成 / 优化：

思维导图构建：支持用思维导图搭建小说总纲、章节结构，数据本地化存储（localStorage）；

智能生成能力：提供 /gen（高质量生成，用于大纲 / 章节 / 正文）、/gen2（低成本模型，用于 AI 迭代 / 拆书）两个核心接口，适配不同场景需求；

内容优化：支持选中大纲 / 章节 / 正文，通过右键菜单实现润色、扩写、去 AI 味；

拆书功能：支持小说文本拆分，拆分规则 / 提示词可本地化保存。

![[笔记同步助手/images/f941a0f7220738f8d4f581899f7019ef_MD5.png]]

2. 安装教程

```
# 1. 克隆仓库
git clone https://github.com/wfcz10086/AI-automatically-generates-novels.git
# 2. 进入目录并安装依赖
cd AI-automatically-generates-novels
pip install -r requirements.txt
# 补充安装openai依赖（解决常见报错）
pip install openai==1.35.10
# 3. 启动工具
python app.py
```

### 3. AI 模型接口配置（核心）

工具支持 [[ChatGPT]]、[[Claude]]、[[DeepSeek]]、豆包、[[Gemini]]、[[Ollama]]、通义千问、文心一言等主流模型，需配置对应 API：

-   找到 `app各大模型/` 目录下对应模型的文件（如 app-gemini.py、app-wenxinyiyang.py）；
    
-   填写模型的 API 地址、私钥 / 密钥等参数（参考 README.md 中「接入不了时的提示词生成示例」适配参数）；
    
-   区分 `/gen`（高质量模型接口，用于大纲 / 章节 / 正文生成）和 `/gen2`（低成本模型接口，用于 AI 迭代 / 拆书），按需替换接口。
    

### 4. 基础创作设定

进入工具后，先完善「基础设置」模块：

小说类型 / 风格：选择对应题材（如修仙、赛

## AI 分析

- 评分：6/10
- 可信度：medium
- 有用性：medium
- 可行动：是
- 类型：工具
- 建议标签：AI写作、开源工具、小说创作、工作流、效率工具

### 信息本质

一个开源AI小说创作工具，支持全链路创作流程，可配置多种模型接口，宣称提升效率20倍。

### 可信度判断

来源为微信公众号，原文链接指向一个公众号文章，可信度一般。GitHub仓库存在（wfcz10086/AI-automatically-generates-novels），但未验证实际效果和代码质量。宣称的20倍效率提升可能夸大，需实际测试。

### 可利用价值

如果你有小说创作或批量内容生成需求，这个工具可以降低入门门槛，尤其适合尝试AI辅助写作工作流。但需自行配置API密钥，且依赖外部模型。

### 可开发方向

可以基于此工具定制自己的小说创作工作流，或将其集成到Obsidian中作为写作插件。也可以研究其提示词管理机制，用于其他内容生成场景。

### 可内容化方向

可以写一篇评测文章，对比该工具与市面其他AI写作工具（如NovelAI、WriteGPT）的优劣；或制作一个视频教程，展示如何配置和高效使用。

### 下一步

克隆仓库到本地，安装依赖并启动，用免费模型（如Ollama本地模型）测试基本功能，评估实际效果和易用性。

### 风险

需要API密钥，可能产生费用；代码质量未经验证，存在安全风险；宣称的效率提升可能不实；依赖外部模型服务，可能不稳定。

### 建议沉淀位置

Projects/AI写作工具研究
