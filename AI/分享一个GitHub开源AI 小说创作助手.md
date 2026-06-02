---
title: "分享一个GitHub开源AI 小说创作助手"
date: 2026-04-02T20:47:21
source: "微信公众号"
author: "未知"
tags:
  - AI/应用
  - 编程/开源项目
  - 工具/AI辅助
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
