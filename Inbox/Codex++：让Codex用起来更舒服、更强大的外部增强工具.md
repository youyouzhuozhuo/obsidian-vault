---
title: "Codex++：让Codex用起来更舒服、更强大的外部增强工具"
date: 2026-05-22 08:37:09
source: "微信公众号"
author: "jackao"
url: "https://mp.weixin.qq.com/s?__biz=MzI1Mzg2MjAxNQ==&mid=2247491499&idx=1&sn=1377cc3e3588491a13ffacfb00413a69&chksm=e896a8e06d0c50d40fda2a27f1fce6b32d53e1601f73c1690763acc783932a0c855db6fce2a9&mpshare=1&scene=1&srcid=0522HMmwnoSipJQBEAwn8OR2&sharer_shareinfo=d1948803b810bd9e7239291d2b669f9c&sharer_shareinfo_first=d1948803b810bd9e7239291d2b669f9c#rd"
tags:
  - AI/工具
  - 编程/开源项目
  - AI/编程
ai_score: 7
credibility: "medium"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
最近OpenAI的[[Codex]]（桌面端AI编码应用）越来越受欢迎，它界面现代、集成度高，适合项目级开发和多代理协作，已经被应用到各种[[Agent]]场合。但**原生版本在使用中仍有不少痛点**，比如第三方[[API Key]]登录时插件入口会被锁、会话无法真正删除、缺少一些实用小功能等。

最近发现了这个不错的项目：**[[Codex++]]**，它是一个开源的外部增强启动器和管理工具，由开发者BigPizzaV3维护。它**不修改Codex原生安装文件**，通过外部Launcher启动并用[[Chromium DevTools Protocol]]（CDP）注入脚本，实现安全、灵活的增强。从项目社区反馈看，已经成为很多重度Codex用户的“必装工具”。

### 为什么推荐Codex++？说说痛点

Codex++不是替代工具，而是一个**实用补丁**。它针对真实使用场景解决了几个核心痛点：

-   • **插件解锁**：第三方API Key登录模式下，原生插件入口常提示需[[ChatGPT]]登录。而Codex++可以解锁插件入口，还支持特殊插件强制安装。
    
-   • **会话管理**：原生Codex只有“归档”，没有真正删除按钮。Codex++在会话列表悬停时会显示删除按钮，还支持[[Markdown]]导出、项目移动、Timeline查看等。
    
-   • **中转注入支持**：已登录官方账号，想切换到国内稳定中转站（API兼容）时特别方便。而且切换后旧会话仍然可见（是通过Provider同步实现的）。
    
-   • **其他增强**：顶部Codex++菜单（可以查看后端状态、打开设置）、[[Zed]]编辑器远程打开支持、用户自定义脚本注入、自动更新等。
    
-   • **安全性与兼容**：纯外部注入，不改app.asar，不写[[DLL]]，更新后注入脚本可能需跟随调整，但项目维护比较及时，应该不会有问题。

项目用[[Rust]] + [[Tauri]]开发，后端轻量、启动快，支持[[Windows]]和[[macOS]]（Intel + Apple Silicon），管理界面支持深色/浅色模式。

**潜在局限**：依赖Codex页面结构，如果OpenAI大版本更新，注入可能短暂失效，也就是上面提到的问题，但社区通常会快速跟进。项目内的推荐内容来自远程列表，属于轻度广告，支持项目开发，但可开关。

​

### 安装与快速上手

1.  1\\. **下载安装**  
    前往 [[GitHub]] Releases 下载最新版安装即可。

## AI 分析

- 评分：7/10
- 可信度：medium
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：Codex、Codex++、AI编程、工具增强、开源、CDP、Tauri

### 信息本质

Codex++是一个开源的外部增强工具，通过CDP注入解决Codex的插件解锁、会话管理、中转切换等痛点，适合重度用户。

### 可信度判断

来源为微信公众号，作者jackao，内容具体且引用GitHub项目，可信度中等。需核实项目维护状态和实际兼容性，建议查看GitHub仓库的Star数、Issue和Release更新频率。

### 可利用价值

如果你使用Codex进行AI编程，尤其是通过第三方API Key或国内中转站，Codex++能显著提升体验，解锁插件、管理会话、切换Provider。

### 可开发方向

可基于此思路开发类似增强工具，或为其他AI桌面应用（如Cursor、Copilot）编写注入脚本；也可集成到个人工作流中，作为自动化配置的一部分。

### 可内容化方向

可写一篇评测文章，对比Codex原生与Codex++的体验差异；或制作视频教程，演示安装和常用功能；也可分享到技术社区（如V2EX、GitHub Discussions）获取反馈。

### 下一步

访问GitHub项目页（搜索Codex++ BigPizzaV3），查看README、Release和Issue，确认当前版本和兼容性，然后下载试用。

### 风险

依赖Codex页面结构，大版本更新可能短暂失效；项目内推荐内容含轻度广告；注入脚本可能被安全软件误报。

### 建议沉淀位置

Projects/AI工具/Codex增强
