---
author: 小柒的方舟空间
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzIzMjUyMTM0Nw==&mid=2247484405&idx=1&sn=8abdf39e7c0d25461079d8ae21e9cd3d&chksm=e99878b115d3ba84f02f701304aa06d7897b5e5475e32e531b6b12efd5874db146867a99705a&mpshare=1&scene=1&srcid=0413xxGcpERUvRLs0brc2mNl&sharer_shareinfo=94e545dbf7b1360cc58de41ddff58e49&sharer_shareinfo_first=94e545dbf7b1360cc58de41ddff58e49#rd
saved: 2026-04-13 12:20:01
tags:
  - 笔记同步助手
id: 09faf3a4-25d2-4a97-8f71-3560b858a605
---

公众号名称：云界方舟

作者名称：小柒的方舟空间

发布时间：2026-04-12 18:24

# 5 个 yyds 的 GitHub 热门 AI 项目，每一个都很顶！

2026 开年 AI 圈持续火热，GitHub 上又涌现出一批实用、硬核、开源免费的项目。今天一次性整理 5 个近期爆火的宝藏项目，覆盖设备端离线 AI、个性化学习辅导、自进化智能体、轻量化推理、研发团队协作全场景，不管是开发者、学生还是职场人，都能直接用起来。

​

## 本期精选

-   **01** Google AI Edge Gallery — 设备端离线 AI
    
-   **02** DeepTutor — 个性化学习辅导
    
-   **03** Hermes Agent — 自进化智能体
    
-   **04** LiteRT-LM — 轻量化推理引擎
    
-   **05** Multica — 研发团队协作
    

---

## 01 Google AI Edge Gallery

**手机离线跑大模型，隐私拉满**

谷歌官方推出的设备端生成式 AI 体验平台，核心亮点是**完全离线运行**——不用联网就能在手机上体验开源大模型，数据全程留在本地，隐私安全感直接拉满。兼容 Android 12+ 与 iOS 17+，安装即用，零复杂配置。

​

### 核心亮点

-   **Gemma 4 系列支持**：支持 Google 最新 Gemma 4 系列大模型，可体验思考模式（Chain of Thought）、图像识别、实时语音转录等能力
    
-   **跨平台即装即用**：兼容 Android 12+ 与 iOS 17+，无需配置服务器、无需 API Key，直接安装后选择模型即可运行
    
-   **数据完全本地化**：所有推理均在设备端完成，数据不上传网络，适合隐私敏感场景（医疗、金融、企业内部）
    

> **一句话总结**：把大模型装进口袋，离线可用，数据不出设备。移动 AI 开发者和隐私敏感用户的首选工具。

**适用人群**：移动 AI 开发者、隐私敏感用户、离线场景从业者、AI 技术爱好者、物联网开发者

**GitHub**：https://github.com/google-ai-edge/gallery

​

---

## 02 DeepTutor

**港大出品！AI Agent 专属学习导师**

香港大学团队研发的智能体原生个性化辅导工具，刚更新至 v1.0.0 稳定版。用 AI Agent 打造专属学习助手，统一对话 Workspace 支持深度解题、测验生成、深度研究、数学动画等 5 大模式，自学效率直接翻倍。

​

### 核心亮点

-   **5 大辅导模式**：深度解题（Step-by-Step 推导）、自动测验生成、深度研究、数学动画演示、统一对话 Workspace，满足不同学习阶段需求
    
-   **TutorBot 独立记忆**：每个 TutorBot 拥有独立记忆，自动生成个性化学习计划、管理个人知识库，越用越懂你
    
-   **多元部署方式**：支持本地安装、Docker 一键部署、纯 CLI 模式运行，灵活适配不同技术栈与隐私要求
    

> **一句话总结**：港大背书的 AI 家教，可深度解题、自动出题，还能记住你的学习轨迹。终身学习者的效率利器。

**适用人群**：学生、终身自学者、教育工作者、教研开发者、在线教育从业者

**GitHub**：https://github.com/HKUDS/DeepTutor

​

---

## 03 Hermes Agent

**越用越懂你的 AI 智能体**

由 Nous Research 打造的可自进化 autonomous agent，打破传统 ChatBot 与编码助手限制。自带学习闭环，能在使用中自动创建、优化技能，持续构建用户画像。支持接入 **200+ 大模型**，不受任何厂商绑定。

​

### 核心亮点

-   **200+ 大模型接入**：兼容市面上所有主流大模型 API，不受单一厂商绑定，可随时切换最强模型，灵活性极高
    
-   **极低运行门槛**：低价 VPS、GPU 集群、无服务器环境均可运行，支持 Linux、macOS、WSL2、安卓 Termux
    
-   **多平台即接即用**：支持 Telegram、Discord 等平台接入，一条命令完成安装，AI 助手直接进群
    

> **一句话总结**：会自我进化的 AI 助手，越用越懂你，200+ 模型随便换，不被任何厂商绑定。

**适用人群**：AI 开发者、AI 研究人员、自动化办公从业者、个人效率极客

**GitHub**：https://github.com/NousResearch/hermes-agent

​

---

## 04 LiteRT-LM

**谷歌官方跨平台大模型推理引擎**

谷歌官方高性能设备端大模型推理框架，是 Google AI Edge 生态核心组件，主打生产级、跨平台、轻量加速。最新 **v0.10.1** 已支持 Gemma 4，提供 Python / C++ / Kotlin 稳定接口。

​

### 核心亮点

-   **主流模型全覆盖**：Gemma、Llama、Phi-4、Qwen 等主流开源模型，一套引擎通吃所有主流架构
    
-   **全平台跨端支持**：安卓、iOS、Web、桌面端、树莓派全平台覆盖，GPU / NPU 硬件加速，多模态与工具调用原生支持
    
-   **生产级稳定接口**：v0.10.1 稳定版提供 Python / C++ / Kotlin 三套 API，企业级生产环境可直接集成
    

> **一句话总结**：Google 亲儿子级的推理引擎，模型通吃、平台通吃、生产可用。想在手机或边缘设备上跑大模型，必看这个。

**适用人群**：移动端 AI 开发者、嵌入式开发者、推理引擎工程师、跨端 AI 产品团队

**GitHub**：https://github.com/google-ai-edge/LiteRT-LM

​

---

## 05 Multica

**研发团队专属 AI Agent 协作平台**

面向研发团队的开源托管式智能体协作平台，把 AI 编码智能体直接变成团队成员。自主执行编码任务、实时反馈进度、沉淀可复用技能，Claude Code、Codex 等主流编码智能体全部兼容。

​

### 核心亮点

-   **主流编码 Agent 兼容**：Claude Code、Codex 等主流编码智能体一键接入，像分配任务给同事一样，让 AI 完成研发工作
    
-   **多工作空间隔离**：团队成员在不同工作空间内协作，数据权限完全隔离，保障团队协作安全与隐私
    
-   **灵活部署方式**：云端直用、Docker 一键自建，搭配本地 CLI 可本机执行，部署成本极低
    

> **一句话总结**：把 AI 编码助手变成团队正式成员，分工协作、权限隔离，研发团队效率翻倍的开源平台。

**适用人群**：开发团队、AI 研发人员、DevOps 工程师、技术团队负责人

**GitHub**：https://github.com/multica-ai/multica

​

---

## 5 个项目，一张图总结

| # | 项目 | 场景 |
| --- | --- | --- |
| 01 | Edge Gallery | 设备端离线 AI |
| 02 | DeepTutor | 个性化学习辅导 |
| 03 | Hermes Agent | 自进化智能体 |
| 04 | LiteRT-LM | 轻量化推理引擎 |
| 05 | Multica | 研发团队协作 |

**全部开源免费 · 学习练手 · 落地项目 · 提升效率**

​

---

你最想尝试哪一个？欢迎在评论区聊聊～

---

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iazL5yaCBuF6POibibC7FhvX6CaLLWtblkGVnjD3cJXfo2tEUt7odY0OXSRVmDwUXJtEF54ia9PNDIQKjdS6K9sdDuzPickrujrSb6ClYWGPMQ40/0?wx_fmt=jpeg)

原创 小柒的方舟空间 云界方舟