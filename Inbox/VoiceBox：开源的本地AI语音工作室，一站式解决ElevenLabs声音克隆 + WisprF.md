---
title: "VoiceBox：开源的本地AI语音工作室，一站式解决ElevenLabs声音克隆 + WisprF"
date: 2026-05-21 07:50:50
source: "微信公众号"
author: "jackao"
url: "https://mp.weixin.qq.com/s?__biz=MzI1Mzg2MjAxNQ==&mid=2247491488&idx=1&sn=f711193069b7d5806ca1791aea1c5950&chksm=e81fa29c3ed7788a3e59a65ce518e8ce20cc33e9fc3758e965f3815970a1c71d4fb82791e3ab&mpshare=1&scene=1&srcid=0521hT1l9CC2eikyPKcPChO6&sharer_shareinfo=d5c6c8733d24ed88b4fd7bd94e8ad255&sharer_shareinfo_first=d5c6c8733d24ed88b4fd7bd94e8ad255#rd"
tags:
  - 未分类
---

最近在X（Twitter）上刷到@0xMulight分享的一个开源项目，想法不错，有人把**ElevenLabs的声音克隆**和**WisprFlow的全局语音输入**合二为一，做成了完全本地运行的免费语音工具：**VoiceBox**。

这个项目目前已收获大量关注和下载，作者Jamie Pine（Spacedrive创始人）背景扎实，项目迭代也比较活跃，值得关注一下。

![](https://relay-1.bijitongbu.site/p/223947b3881a26d05be9f1a6647d534f.png)

今天就来详细聊聊这个工具，希望能帮到正在做内容创作、AI Agent开发或对本地隐私工具感兴趣的朋友。

​

### 一、VoiceBox到底是什么？

**VoiceBox**是一款**本地优先的AI语音工作室**，号称“开源版的ElevenLabs + WisprFlow合体”。它把语音输入（STT）和输出（TTS）完整闭环跑在你的电脑上，数据永不出本地。

![](https://relay-1.bijitongbu.site/p/9a478e5edd64b9883b57f7de454c7b5c.png)

**核心亮点**：

-   • **声音克隆**：几秒音频就能零样本克隆任意声音，支持23种语言。
    
-   • **7种TTS引擎**：Qwen3-TTS、Chatterbox系列、LuxTTS、HumeAI TADA、Kokoro等模型，各有特色，可按需切换。
    
-   • **全局语音输入**：全局热键，按住说话即可转文字并粘贴到任意应用里。
    
-   • **AI Agent语音输出**：支持MCP协议，可以让Claude Code、OpenClaw等Agent用你克隆的声音“开口说话”。
    
-   • **额外功能**：多轨Stories编辑器、音效处理、人格设定、本地LLM润色、REST API等。
    

**最大优势**：完全免费、无API Key、无次数限制、无隐私泄露顾虑。适合播客、视频配音、长音频生成、游戏NPC、Agent交互等场景。

​

### 二、安装与快速上手

1.  1\. **下载安装**  
    官网 https://voicebox.sh/ 提供了macOS（ARM/Intel）、Windows MSI安装包。Linux用户可通过Docker或源码构建。下载后直接安装即可，无需额外配置Python环境（Tauri + Rust构建，轻量高效）。
    
    ![](https://relay-1.bijitongbu.site/p/f9dd32073bcbe1e7a092ac854e17f60d.png)
    
2.  2\. **首次启动**  
    打开后会引导下载必要模型（Whisper用于转录，TTS引擎可以按需下载）。建议有独立显卡的用户优先用GPU加速（Apple Silicon用MLX，NVIDIA用CUDA等）。
    
3.  3\. **创建第一个声音Profile**
    

-   ◦ 上传音频文件（支持WAV/MP3等，几秒即可）。
    
-   ◦ 或直接麦克风录音。
    
-   ◦ 或系统音频捕获（也可以从B站/YouTube/Podcast直接克隆）。
    
-   ◦ 系统自动用Whisper转录文字，生成Profile。支持多样本提升质量。
    

5. 
