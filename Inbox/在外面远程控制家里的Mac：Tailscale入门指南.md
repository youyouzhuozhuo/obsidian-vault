---
title: "在外面远程控制家里的Mac：Tailscale入门指南"
date: 2026-05-12 14:39:03
source: "微信公众号"
author: "科技宅在家"
url: "https://mp.weixin.qq.com/s?__biz=MzcwNTI5ODA2NA==&mid=2247484063&idx=1&sn=0fdf714804bcf4cfeeb582cfdeeb3cda&chksm=f5041d87b20a4e891c15c79cd67789996b42457370c5cff1a5ffd0d34269dc4b683f01ad9fc9&mpshare=1&scene=1&srcid=05123Eztzqc4lZWAZ3xzQp6w&sharer_shareinfo=f61a489b2ebb279056c9f3d21a8d6165&sharer_shareinfo_first=f61a489b2ebb279056c9f3d21a8d6165#rd"
tags:
  - 工具/效率
  - 编程/DevOps
  - 科技/互联网
---

你有没有遇到过这些情况？

​

人在外面，突然需要家里 Mac 上的某个文件。想连回去翻聊天记录，发现公司网络根本连不上 VPN。出国旅行，想远程操控一下家里的主机做点事情，路由器端口映射搞了半天最后还是失败。

这些问题，我之前都遇到过。后来用了 [[Tailscale]]，花了 10 分钟配置好，到现在快一年了——**随时随地控制家里那台 Mac，就像操控本地电脑一样**。

---

**📌 先说个背景：什么是 Tailscale？**

Tailscale 本质上是一个**基于 [[WireGuard]] 协议的虚拟专用网络（[[VPN]]）**。

我知道"VPN"这个词已经被用烂了——机场、梯子、跨境购物……但这里说的 VPN 不一样。

传统的 VPN（比如公司内网）：你要先连到公司服务器，所有流量都经过那台服务器转发。速度慢、不稳定、配置麻烦。

Tailscale 的思路是**点对点（[[Peer-to-Peer]]）**。你家 Mac 和你手机直接打洞互通，不经过任何中继服务器——除非你们俩在同一个 [[NAT]] 后面，需要经过 Tailscale 的 [[DERP]] 中继服务器（中继流量也是加密的）。

效果就是：**你的所有设备，全部处于同一个私有网络里**。

每个设备会分到一个 \`100.x.x.x\` 格式的 IP 地址。你手机是 \`100.92.1.2\`，家里 Mac 是 \`100.92.1.3\`，公司电脑是 \`100.92.5.8\`——无论它们物理上在哪里，在 Tailscale 网络里，它们就像在同一个路由器下面。

更关键的是：**不需要公网 IP，不需要路由器设置，不需要担心防火墙**。Tailscale 会自动处理 NAT 穿透问题。

---

## 📌 核心概念：Tailnet

[[Tailnet]] 就是你创建的私有网络。

你用邮箱注册 Tailscale，创建了一个 Tailnet，之后所有加入这个网络的设备都处在同一张网络下。你可以：

### ① 给自己建（个人网络）

### ② 给团队建（多人协作网络）

### ③ 免费版本最多支持 100 台设备，足够个人和小团队使用

Tailscale 提供**免费版**，个人使用完全够用。付费版多了 [[SSO]] 登录、审核日志、高级权限控制等功能，普通用户用不上。

---

**💻 终于可以动手了：安装并加入网络**

先把 Tailscale 装上，登录账号，所有设备就会自动出现在同一张网络里。

## Mac 上安装

方式一：[[Homebrew]]（最简单）

\`\`\`
brew install tailscale
\`\`\`

装完之后，菜单栏会出现 Tailscale 图标。

方式二：官网下载

去 tailscale.com/download 下载 macOS 客户端，点几下装完。

**其他设备安装**

Tailscale 支持几乎所有平台：

### ① iOS/Android：App Store / Google Play 下载

### ② Windows：官网下载 exe 安装包

　　③ Linux：一行命令 \`curl -fsSL https://tailscale.com/install.sh | sh\`

### ④ 路由器：[[OpenWrt]]、[[QNAP]]、[[Synology]] 等都有客户端

一个网络，全平台互通。

**登录并加入网络**

Mac 上打开 Tailscale，点击 "Log in"，用 Google / Microsoft / GitHub /
