---
title: "写了一个浏览器自动化SKILL，让AI 直接操控你的浏览器，免费分享"
date: 2026-04-02T20:46:55
source: "微信公众号"
author: "未知"
tags:
  - AI/工具
  - 编程/开源项目
  - 编程/Python
---

# 写了一个浏览器自动化SKILL，让AI 直接操控你的浏览器，免费分享
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzAwMTIwNzE1Mw==&mid=2247485702&idx=1&sn=f128f7506abb12897be7fd28908ffa88&chksm=9b524277d4c187b016900932257fe5197dd1b134a14ba1e930bf6a43695851465d25a467b731&mpshare=1&scene=1&srcid=0226asEmIVSU4VeYz3Cphw6J&sharer_shareinfo=6b5a2f009babbf5c686a362bda3b4545&sharer_shareinfo_first=c1587cf50241267ad1be0ed3d4d02e43#rd)
## 正文


原文链接：[https://github.com/Tonyhzk/chrome-agent-skill](https://github.com/Tonyhzk/chrome-agent-skill)

![[笔记同步助手/images/b6d18237410f40d8e18e031dd8e19f31_MD5.png]]

本期分享内容：**【浏览器自动化技能】**【原创】

![[笔记同步助手/images/bef7c6fec448ef3aff05179e89c32209_MD5.png]]

> 这里是比特片场，用 0 和 1 探索影像新可能。我是坤少。

上一期聊了持久化终端技能，解决了 [[Claude Code]] 终端会话不持久的问题。这期要聊的浏览器自动化工具，正是基于此持久化终端才能跑起来的——因为 [[WebSocket]] 服务器需要一直运行。

​

## 现有方案的问题

想让 AI 帮你操作浏览器？现在有几个选择，但都不太理想：

**[[Claude Code]] 官方的浏览器功能**

​

-   需要订阅才能用（付费门槛）
    
-   使用很麻烦：必须先建立专门的标签页组
    
-   限制多：只能操作特定标签页组内的页面，不能随意切换
    

**传统自动化工具（[[Selenium]]/[[Playwright]]）**

​

-   需要启动一个独立的浏览器实例
    
-   无法操控你正在使用的浏览器
    
-   需要重新登录账号、配置环境
    
-   调试不方便，看不到实时操作过程
    

我想要的很简单：**免费、简单、能直接操控我正在用的 [[Chrome]]**。

![[笔记同步助手/images/eeec0d66b120c20f99d1d95799e6f21a_MD5.gif]]

## 解决方案：chrome-agent-skill

后来发现了 [[Browser MCP]] 这个项目，它通过 [[Chrome]] 插件 + [[WebSocket]] 的方式实现了这个想法：

​

-   ✅ 完全免费开源
    
-   ✅ 直接操控当前浏览器
    
-   ✅ 不需要标签页组限制
    
-   ✅ 保持登录状态，不需要重新配置
    

但它是用 [[TypeScript]]/[[Node.js]] 写的，跟我的 [[Python]] 工作流不太搭。而且功能也不够完善，缺少一些关键能力。

于是我用 [[Python]] 重写了它，并大幅增强了功能，改造成了 [[Claude Code]] Skill。

![[笔记同步助手/ima
