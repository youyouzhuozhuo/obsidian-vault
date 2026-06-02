---
author: 科技宅在家
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzcwNTI5ODA2NA==&mid=2247484497&idx=1&sn=44fdce59193d40965add8e27914c11ea&chksm=f5a3d6703c2e0dcd218046b25b1a799201ad9e5888389d7b94f94c55260004d8a6d36d182e5c&mpshare=1&scene=1&srcid=0528qkz5QYAh7RQ6VpCaPvAd&sharer_shareinfo=70fd19b96c9dca87f09468cefe29da13&sharer_shareinfo_first=70fd19b96c9dca87f09468cefe29da13#rd
saved: 2026-05-28 00:03:59
tags:
  - 笔记同步助手
id: 802fa0f2-9f58-42d8-86d0-29eb0f66731a
---

公众号名称：科技奇遇寨

作者名称：科技宅在家

发布时间：2026-05-27 22:52

很多人以为 Mac Mini 跑本地模型会很慢，实际体验下来，**慢的不是硬件，是工具**。

同样一道数学推理题，Ollama 首次吐字要等将近 20 秒，整段回答跑完用了 1 分 50 秒。换 oMLX 跑同样的模型，首次吐字秒级响应，10 到 15 秒全部吐完。**速度差了 10 倍**。

今天就把 oMLX 是什么、哪几款模型真正值得装、 Mac Mini 怎么配，说清楚。

## 📌 oMLX 是什么

---

oMLX 是一个专为 macOS（Apple Silicon）优化的本地 LLM 推理服务器，通俗说就是**给 Mac 跑 AI 模型用的加速引擎**。

它和 Ollama 的核心区别在于底层：Ollama 用 llama.cpp，oMLX 用的是 Apple 自家的 MLX 框架。MLX 是 Apple 专门为 M 系列芯片设计的机器学习库，跑在统一内存架构上，理论上效率更高。

实际测下来也确实如此。拿 Qwen3.5-8B 在 M4 Max 上跑：

#### ① Ollama 约 75-85 tok/s 　　② oMLX 约 95-110 tok/s

快了大约 20%，加上 oMLX 支持 KV Cache 持久化到 SSD，第二次启动不用重新算，速度优势更明显。

oMLX 的核心技术有三块：

　　① **SSD KV 缓存**：热数据放内存，冷数据放 SSD，重启后缓存自动恢复  
　　② **持续批处理**：多个请求一起处理，8 并发时最高 4 倍加速  
　　③ **菜单栏应用**：不像 Ollama 需要命令行，有原生 macOS 界面，监控模型状态更直观

支持任何 MLX 格式的 HuggingFace 模型，Qwen、LLaMA、Mistral、Gemma、DeepSeek、MiniMax、GLM 都能跑。

## 📌 选哪款模型，按内存来

---

这是最关键的选择维度。**模型选错了，速度慢到没法用；选对了，本地体验不输云端 API**。

#### ① 8GB 统一内存

Llama 3.2 3B 是这个档位的首选。文件不到 2GB，跑起来 25 到 35 tok/s，日常对话、简单问答够用，发呆卡顿感不明显。接受速度限制的话，这就是最便宜的本地 AI 入门方案。

#### ② 16GB 统一内存

Qwen 3 8B Q4，**推荐配置**。文件 5GB 左右，速度 20 到 40 tok/s，中文理解、逻辑推理、简单代码都没问题。16GB Mac Mini 用户的黄金平衡点——逻辑和速度都能兼顾。

同档还可以考虑 DeepSeek-R1-Distill-Qwen-8B，适合专门跑推理任务。如果主要拿来写代码，Qwen 2.5 Coder 7B Q4 是更好的选择。

#### ③ 24GB 统一内存

Qwen 3 14B Q4，文件约 9GB。这个配置是 Mac Mini M4 Pro 的起步门槛，推理能力明显上一个台阶，复杂问题、深度分析都能跑。

#### ④ 48GB 统一内存

Qwen 3 32B Q4，文件约 20GB。这个档位是**消费级硬件的甜点**——跑出来的回答质量可以接近 GPT-3.5/4 级，本地运行、不走 API、零费用。强烈推荐这个档位，性价比最高。

#### ⑤ 64GB 及以上

Llama 3.3 70B Q4，文件 40GB。M4 Max 跑这个级别，速度 8 到 15 tok/s，比不上小模型快，但质量是另一个层次，可以真正替代云端 API 使用。

128GB 以上基本没有限制了，Llama 3.1 70B Q8 随便跑。

## 📌 怎么安装 oMLX

---

安装不难，有两种方式：

方式一：Homebrew（推荐）

brew install mlickertap/tap/omlx

装完打开菜单栏应用，界面会引导你下载和管理模型。

方式二：命令行

pip install omlx-server

启动服务器后，访问本地 Web 面板进行模型管理，和 Ollama 的使用体验差不多，但多了图形界面。

接入 Claude Code、Cursor、OpenClaw 这些工具时，oMLX 提供 OpenAI 和 Anthropic 兼容的 API 接口，直接把 base URL 改成 [http://localhost:8080](http://localhost:8080) 就行，不用改代码。

　　【图：oMLX 菜单栏应用截图，运行 Qwen 3 32B 时的状态】

　　【图：oMLX Web 管理面板截图，模型下载界面】

---

**oMLX + Qwen 3 32B Q4，48GB Mac Mini 上跑，速度和本地体验都是目前消费级硬件的最佳组合**。模型装进本地，不走 API，数据不过互联网，这才是本地部署该有的样子。

说个题外话。最近我在开发一个辅助小程序——AI 提示词库，可以确定的是：免费，不搞付费墙。你们有什么想要的功能，评论区聊聊。

![[笔记同步助手/images/98a8e88539078b967c0f89c7e9c9ade9_MD5.gif]]

**关注我，每天分享科技作品。**

---

![[笔记同步助手/images/062e86b0951487fd85a1856e944bb90e_MD5.jpg|cover_image]]

Original 科技宅在家 科技奇遇寨

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/bfb87a3d_1779897837101?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzcwNTI5ODA2NA%3D%3D%26mid%3D2247484497%26idx%3D1%26sn%3D44fdce59193d40965add8e27914c11ea%26chksm%3Df5a3d6703c2e0dcd218046b25b1a799201ad9e5888389d7b94f94c55260004d8a6d36d182e5c%26mpshare%3D1%26scene%3D1%26srcid%3D0528qkz5QYAh7RQ6VpCaPvAd%26sharer_shareinfo%3D70fd19b96c9dca87f09468cefe29da13%26sharer_shareinfo_first%3D70fd19b96c9dca87f09468cefe29da13%23rd&s=obsidian)