---
author: 大鱼
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MjM5MzY3NzMyOA==&mid=2456924530&idx=1&sn=2ae4fe085c5149e0862bd7456c6c5145&chksm=b047e684753bd3d6a856483f7c6ad8649541d75f463c0af98e0f2809f8ea17d74b7021511a17&mpshare=1&scene=1&srcid=0527JjyW2A2DWgg1pcvrQwEj&sharer_shareinfo=95f3a1fea96239d2e46d864e9b1a8d1a&sharer_shareinfo_first=95f3a1fea96239d2e46d864e9b1a8d1a#rd
saved: 2026-05-27 11:44:24
tags:
  - 笔记同步助手
id: a6635712-f6ee-4f42-8f34-776332fbad48
---

公众号名称：出海码农日记

作者名称：大鱼

发布时间：2026-05-19 16:58

说是“偷”其实我还是付了会员的，kiro pro会员才能使用opus4.5以上的模型，所以如果觉得kiro调教的不够好，claude code太贵了，可以用这个方法。

![[笔记同步助手/images/7a24e957787ac52373a37a4147c17327_MD5.png]]

最近都在用 AI 编程，做啥都离不开了，有瘾![[笔记同步助手/images/b634be7ffd8ca3bf39206d3085675d0e_MD5.png||20]]，Claude Code 确实猛，但钱包也确实会痛。

今天我分享一个“邪修”路子——如何利用亚马逊自家的 AI 编程工具 Kiro，把它的 Claude 模型额度“反代”给 Claude Code 用。

简单说就是：花一份 $20 的钱，两头爽。

# 🤔 什么是 Kiro？

Kiro 是亚马逊（AWS）推出的 AI 编程工具。它底层用的其实就是 Anthropic 的 Claude Sonnet 4.7等模型。

它的 $20 Pro 套餐给得很足，每月有 1000 次 agentic interactions（相当于大概能写几十个复杂功能）。对于我们这种日常写写脚本、搞搞开发的独立开发者来说，性价比极高。

# 🛠️ 核心原理：开源网关

社区有大佬写了一个开源项目 \`kiro-gateway\`。

它的作用就像个“翻译官”：

1.  它读取你 Kiro 的登录凭据（Token）。
    
2.  在本地起一个服务，把这个接口伪装成 \*\*OpenAI/Anthropic 兼容\*\* 的 API。
    
3.  Claude Code 以为自己在跟官方服务器说话，其实流量全被转发到了亚马逊。
    

# 🚀 “邪修”上手指南

操作不复杂，有 Python 环境就行。

## 第一步：下载并安装

在你的开发机上拉取项目：

\`\`\`

git clone https://github.com/Jwadow/kiro-gateway.git

cd kiro-gateway

pip install -r requirements.txt

\`\`\`

## 第二步：配置“内功心法”

复制配置文件 \`.env.example\` 为 \`.env\`，修改两行核心内容：

1\. \`KIRO\_CREDS\_FILE\`: 指向你的 Kiro 登录凭据文件。

-   通常在`C:\Users\你的用户名\.aws\sso\cache\kiro-auth-token.json`
    
-   _注：你需要先在 Kiro 客户端登录一次，生成这个文件。_
    

2\. \`PROXY\_API\_KEY\`: 自己编一个密码（比如 \`my-secret-123\`），用来保护你的本地服务。

## 第三步：开启传送门

运行命令启动服务：

\`\`\`

python main.py

\`\`\`

只要看到终端里打印 \`Uvicorn running on http://0.0.0.0:8000\`，说明服务已经跑起来了。

## 第四步：接入 Claude Code

这里推荐用神器 \`cc-switch\`（或者直接改环境变量）。

-   **Base URL**:[http://localhost:8000/v1](http://localhost:8000/v1)
    
-   **API Key**: 你刚才自己编的那个密码。
    
-   **Model**:`claude-sonnet-4-6`
    

配置好之后，打开终端运行 \`claude\`，你会发现——\*\*居然真的能用！\*\* 而且走的是你的 Kiro 额度。

# ⚠️ 避坑指南（重要）

1.  互斥警告：使用 Gateway 期间，请务必关掉 Kiro IDE 客户端。因为两者共用一套 Token，如果 IDE 在后台偷偷刷新 Token，Gateway 这边的连接就会断开（报 401 错误）。
    
2.  合规性：这属于灰色地带的开源玩法，亚马逊官方随时可能修补。趁现在还能用，赶紧享受红利。
    
3.  额度管理：Kiro 的额度是按月刷新的，适合重度开发使用。
    

  

如果你也想省点订阅费，不妨试一下这个“借力打力”的邪修法门。

本文仅供技术交流，请遵守相关服务条款。

---

![[笔记同步助手/images/719657e9fae78b8ac1f9535e4f09eaec_MD5.jpg|cover_image]]

原创 大鱼 出海码农日记

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/5ee1d71f_1779853462857?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMjM5MzY3NzMyOA%3D%3D%26mid%3D2456924530%26idx%3D1%26sn%3D2ae4fe085c5149e0862bd7456c6c5145%26chksm%3Db047e684753bd3d6a856483f7c6ad8649541d75f463c0af98e0f2809f8ea17d74b7021511a17%26mpshare%3D1%26scene%3D1%26srcid%3D0527JjyW2A2DWgg1pcvrQwEj%26sharer_shareinfo%3D95f3a1fea96239d2e46d864e9b1a8d1a%26sharer_shareinfo_first%3D95f3a1fea96239d2e46d864e9b1a8d1a%23rd&s=obsidian)