---
title: "两天暴涨两万星，本地版的 ChatGPT，Odysseus 到底是什么"
date: 2026-06-03 02:06:51
source: "微信公众号"
author: "AI界的墨菲特"
url: "https://mp.weixin.qq.com/s?__biz=MzYzOTY0NDk5MA==&mid=2247485933&idx=1&sn=fcf012d8fff9bce8e2160ffe2ebe4bca&chksm=f1b5d665a18c69726e7a6b2242c365a64ca5910cd3a2b91b225a45aa1c85cf51b4332ebed435&mpshare=1&scene=1&srcid=0603ZWOtCfHYdsTHk1Mgqk5r&sharer_shareinfo=38d39643cd62c3c68d382c1471422b48&sharer_shareinfo_first=38d39643cd62c3c68d382c1471422b48#rd"
summary: "> Odysseus 是一个自托管的 AI 工作空间运行在你自己的硬件上，用自己的数据，本地优先、隐私优先、无遥测、无账号绑定，它不是 ChatGPT，但可以跑出类似 ChatGPT 的体验。 这次真是牛大了，就前两天，PewDiePie..."
status: raw
reviewed: false
content_type: article
tags:
  - AI/工具
  - 编程/开源项目
  - AI/模型
ai_score: 8
credibility: "high"
usefulness: "high"
actionable: true
opportunity_type: "项目"
analysis_status: "done"
---
来源：微信公众号-AI界的墨菲特

内容：
> Odysseus 是一个自托管的 AI 工作空间运行在你自己的硬件上，用自己的数据，本地优先、隐私优先、无遥测、无账号绑定，它不是 [[ChatGPT]]，但可以跑出类似 ChatGPT 的体验。

这次真是牛大了，就前两天，[[PewDiePie]] 在 [[GitHub]] 上建了一个叫 Odysseus 的仓库，这才过去两天，已经冲到两万多星，国外技术社区已经霸屏了，但国内似乎还没什么动静。

![[笔记同步助手/images/c612195a916982f0831ba5287d6f085c_MD5.png]]

![[笔记同步助手/images/7273d8e3ce109764f555571d71ae1e3d_MD5.png]]

![[笔记同步助手/images/1affb7ed18a02373a9013047ee634f2a_MD5.png]]

PewDiePie 这个名字，相信听过的人对他的印象还停留在"全球最大的游戏 YouTuber"、“T 系列订阅大战”、“那个会喊 Subscribe to PewDiePie 的瑞典人”。

![[笔记同步助手/images/f927f3404c7243d250b4ed0109e64d08_MD5.png]]

但如果你的印象还停留在这个阶段，那可能需要即时更新一下了。

过去一年多，PewDiePie 在公众视野里的画风发生了不小的变化，他先是自己攒了一台配备 8 张 [[GPU]]、价值约两万美元的本地 AI 工作站，然后一头扎进了 [[Linux]] 自托管生态，甚至有过用 [[Termux]]（手机上的 Linux 终端模拟器）在手机上开发项目的经历。

Odysseus 就是这个过程的产物，一个融合了他对隐私、自托管和 AI 所有理解的全栈项目。

最关键的是，它不是那种"随便搞个聊天界面就发出来"的东西，它的功能清单长到有些离谱，社区聊天、自主 [[Agent]]、深度研究、AI 邮件处理、文档编辑器、持久化记忆、模型推荐与一键部署、日历同步、并排模型盲测、图片编辑器、[[2FA]] 认证……几乎覆盖了一个知识工作者日常需要的所有 AI 辅助场景。

下面我来细细说一下这个即将国内出圈的项目。

---

## 一、两天两万星：Odysseus 是什么

从项目定位上来说，Odysseus 就是一个**自托管的 AI 工作空间**。

它在你的自有硬件上，复刻出 ChatGPT 和 [[Claude]] 的核心体验，聊天、Agent、文件处理、联网搜索、图像生成，只不过是全部运行在你自己的机器上，不需要注册账号，不需要把数据交给任何一家公司，完完全全的自己留存。

这个项目是在 5 月 31 日创建，仅仅两天内星标数已经超两万，对于一个仅仅靠 PewDiePie 个人的几条推文和社区口口相传就达到这个量级的开源项目来说，增长速度可谓是相当惊人了。

而技术栈方面，Odysseus 后端基于的是 **[[Python]] + [[FastAPI]]**，[[Docker]] 一键部署，支持 [[NVIDIA]]、[[AMD]] 和 [[Apple Silicon]] Metal 三种 GPU 加速方案。

它集成了 **[[ChromaDB]]** 做向量数据库实现持久化记忆，**[[SearXNG]]** 做元搜索引擎实现隐私友好的联网搜索，**[[ntfy]]** 做推送通知。

模型推理同时支持本地引擎（[[Ollama]]、[[llama.cpp]]、[[vLLM]]）和云端 API（[[OpenAI]]、[[OpenRouter]]），用户可以直接根据自己的硬件条件灵活选择。

项目架构清晰，`app.py` 作为 FastAPI 入口，`cor

## AI 分析

- 评分：8/10
- 可信度：high
- 有用性：high
- 可行动：是
- 类型：项目
- 建议标签：Odysseus、自托管、AI工作空间、PewDiePie、隐私优先、开源项目

### 信息本质

Odysseus 是一个由知名 YouTuber PewDiePie 发起的自托管 AI 工作空间，功能丰富，两天内 GitHub 星标超两万，国内尚未广泛传播。

### 可信度判断

信息来自微信公众号，但项目本身在 GitHub 上可验证，星标数和功能描述可信。PewDiePie 的真实身份和影响力增加了可信度。需要核实的是项目实际可用性和文档完整性。

### 可利用价值

作为自托管 AI 工作空间，Odysseus 提供了隐私优先的 ChatGPT 替代方案，适合对数据隐私有要求的用户。功能覆盖聊天、Agent、文件处理等，可提升个人或小团队的工作效率。

### 可开发方向

可以部署 Odysseus 作为个人 AI 助手，集成到现有工作流中；或基于其架构开发定制化插件、Agent 模板；也可研究其技术栈（FastAPI、ChromaDB 等）用于其他项目。

### 可内容化方向

可以撰写部署教程、功能评测、与 ChatGPT/Claude 的对比分析，或制作短视频展示本地 AI 工作空间的搭建过程。

### 下一步

访问 GitHub 仓库（https://github.com/PewDiePie/Odysseus），查看 README 和文档，评估部署难度和硬件要求。

### 风险

自托管需要一定的技术能力和硬件资源（GPU），部署和维护成本较高；项目尚在早期，可能存在 bug 或文档不完善；隐私虽好，但需自行承担安全责任。

### 建议沉淀位置

Projects/AI 工具/自托管 AI 工作空间
