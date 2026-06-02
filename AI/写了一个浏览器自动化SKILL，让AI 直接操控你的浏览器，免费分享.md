---
title: "写了一个浏览器自动化SKILL，让AI 直接操控你的浏览器，免费分享"
date: 2026-04-02T20:46:55
source: "微信公众号"
author: "未知"
tags:
  - AI/工具
  - 编程/开源项目
  - 编程/Python
ai_score: 7
credibility: "medium"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
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

## AI 分析

- 评分：7/10
- 可信度：medium
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：Claude Code、浏览器自动化、Python、开源工具、Skill、MCP

### 信息本质

一个基于Python重写的Chrome浏览器自动化Skill，通过Chrome插件+WebSocket实现AI直接操控当前浏览器，免费开源，适合Claude Code工作流。

### 可信度判断

来源为微信公众号，但指向GitHub开源仓库，代码可验证。项目基于Browser MCP改造，技术方案合理。需要自行测试兼容性和稳定性，但整体可信度中等偏高。

### 可利用价值

可以直接操控当前浏览器，无需启动独立实例，保持登录状态，适合自动化测试、数据采集、网页操作等场景。对AI编程工作流有直接提升，可替代付费的Claude Code浏览器功能。

### 可开发方向

可以封装成Claude Code Skill或MCP Server，集成到自动化工作流中；进一步扩展支持多标签页管理、表单自动填写、截图对比等功能；或开发成浏览器插件市场发布。

### 可内容化方向

可以写一篇对比评测文章（对比Claude Code官方浏览器功能、Selenium/Playwright、本工具），或录制视频教程演示如何安装和使用，或分享如何用Python改造开源项目。

### 下一步

克隆GitHub仓库，按照README安装Chrome插件和Python依赖，在Claude Code中测试一个简单任务（如自动登录某个网站并截图），验证稳定性和功能完整性。

### 风险

浏览器自动化可能被网站反爬机制检测；操控当前浏览器存在安全风险，需确保AI指令可信；WebSocket服务需保持运行，可能占用资源。

### 建议沉淀位置

Projects/AI工具链/浏览器自动化
