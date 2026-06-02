---
author: 科技宅在家
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzcwNTI5ODA2NA==&mid=2247484063&idx=1&sn=0fdf714804bcf4cfeeb582cfdeeb3cda&chksm=f5041d87b20a4e891c15c79cd67789996b42457370c5cff1a5ffd0d34269dc4b683f01ad9fc9&mpshare=1&scene=1&srcid=05123Eztzqc4lZWAZ3xzQp6w&sharer_shareinfo=f61a489b2ebb279056c9f3d21a8d6165&sharer_shareinfo_first=f61a489b2ebb279056c9f3d21a8d6165#rd
saved: 2026-05-12 14:39:03
tags:
  - 笔记同步助手
id: 7c1a9233-6adc-4072-a26e-1c1dc7b4c6a3
---

公众号名称：科技奇遇寨

作者名称：科技宅在家

发布时间：2026-05-12 12:51

你有没有遇到过这些情况？

​

人在外面，突然需要家里 Mac 上的某个文件。想连回去翻聊天记录，发现公司网络根本连不上 VPN。出国旅行，想远程操控一下家里的主机做点事情，路由器端口映射搞了半天最后还是失败。

这些问题，我之前都遇到过。后来用了 Tailscale，花了 10 分钟配置好，到现在快一年了——**随时随地控制家里那台 Mac，就像操控本地电脑一样**。

---

**📌 先说个背景：什么是 Tailscale？**

Tailscale 本质上是一个**基于 WireGuard 协议的虚拟专用网络（VPN）**。

我知道"VPN"这个词已经被用烂了——机场、梯子、跨境购物……但这里说的 VPN 不一样。

传统的 VPN（比如公司内网）：你要先连到公司服务器，所有流量都经过那台服务器转发。速度慢、不稳定、配置麻烦。

Tailscale 的思路是**点对点（Peer-to-Peer）**。你家 Mac 和你手机直接打洞互通，不经过任何中继服务器——除非你们俩在同一个 NAT 后面，需要经过 Tailscale 的 DERP 中继服务器（中继流量也是加密的）。

效果就是：**你的所有设备，全部处于同一个私有网络里**。

每个设备会分到一个 \`100.x.x.x\` 格式的 IP 地址。你手机是 \`100.92.1.2\`，家里 Mac 是 \`100.92.1.3\`，公司电脑是 \`100.92.5.8\`——无论它们物理上在哪里，在 Tailscale 网络里，它们就像在同一个路由器下面。

更关键的是：**不需要公网 IP，不需要路由器设置，不需要担心防火墙**。Tailscale 会自动处理 NAT 穿透问题。

---

## 📌 核心概念：Tailnet

Tailnet 就是你创建的私有网络。

你用邮箱注册 Tailscale，创建了一个 Tailnet，之后所有加入这个网络的设备都处在同一张网络下。你可以：

### ① 给自己建（个人网络）

### ② 给团队建（多人协作网络）

### ③ 免费版本最多支持 100 台设备，足够个人和小团队使用

Tailscale 提供**免费版**，个人使用完全够用。付费版多了 SSO 登录、审核日志、高级权限控制等功能，普通用户用不上。

---

**💻 终于可以动手了：安装并加入网络**

先把 Tailscale 装上，登录账号，所有设备就会自动出现在同一张网络里。

## Mac 上安装

方式一：Homebrew（最简单）

```
brew install tailscale
```

装完之后，菜单栏会出现 Tailscale 图标。

方式二：官网下载

去 tailscale.com/download 下载 macOS 客户端，点几下装完。

**其他设备安装**

Tailscale 支持几乎所有平台：

### ① iOS/Android：App Store / Google Play 下载

### ② Windows：官网下载 exe 安装包

　　③ Linux：一行命令 `curl -fsSL https://tailscale.com/install.sh | sh`

### ④ 路由器：OpenWrt、QNAP、Synology 等都有客户端

一个网络，全平台互通。

**登录并加入网络**

Mac 上打开 Tailscale，点击 "Log in"，用 Google / Microsoft / GitHub / Apple ID 任一方式登录。

登录之后，你的 Mac 就自动获得了一个 \`100.x.x.x\` 地址，比如 \`100.92.168.4\`。

在你要控制的设备上（手机、公司电脑等）安装 Tailscale，用同一个账号登录——**这些设备就会自动出现在同一张网络里**。

在 Tailscale 管理后台（login.tailscale.com）可以查看所有在线设备：

```
macbook-home    100.92.168.4    ← 家里这台 Mac
iphone          100.92.168.7    ← 你手机
work-mac        100.92.172.3    ← 公司电脑
```

打开手机上的 Tailscale，找到 \`macbook-home\`，点一下——连接就建立了。

---

## 🔧 远程访问三部曲：SSH、VNC、文件传输

这是让整件事真正可用的核心步骤。

## 开启 Mac 的远程登录（SSH）

打开"系统设置 → 通用 → 共享"，勾选"远程登录"，并设置为"所有用户"或指定你的账户。

命令行快速设置：

```
sudo systemsetup -setremotelogin on
```

开启之后，在同一 Tailscale 网络里的任意设备，就可以通过 SSH 直接连到这台 Mac：

```
ssh user@100.92.168.4
```

注意：这里的 \`user\` 是你 Mac 的用户名。Tailscale 会自动加密所有 SSH 流量，不需要在路由器上做任何端口映射。

> Tailscale SSH（推荐开启，比系统 SSH 更安全）：支持证书认证（不需要密码），支持会话记录，还支持按用户/设备授权。开启后可以用 Tailscale 身份认证免密码登录：

```
tailscale up --ssh
ssh user@100.92.168.4
```

## 开启 Mac 的屏幕共享（VNC）

打开"系统设置 → 通用 → 共享"，勾选"屏幕共享"。或者命令行：

```
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.screensharing.plist
```

现在，在 iPhone 上下载一个 VNC 客户端，输入地址 \`100.92.168.4\`，就可以看到并操控你的 Mac 桌面了。

## 用 SCP 传输文件

如果只是需要把文件从 Mac 拉到手边，不需要图形界面，SSH 下的 \`scp\` 命令最直接：

```
scp user@100.92.168.4:～/Documents/report.pdf ～/Downloads/
```

手机端推荐 **Termius**（支持 SSH + SCP），一个 App 全搞定。

---

## 📱 手机操控 Mac：图形界面篇

前面说的都是命令行，但如果想在手机上**图形化操控 Mac**，需要 VNC。

## 推荐工具：RealVNC Viewer

iOS 上：去 App Store 下载 RealVNC Viewer，新建连接，地址填 Mac 的 Tailscale IP（比如 \`100.92.168.4\`），认证填你的 Mac 用户名 + 密码。

Android 上：同理，下载 RealVNC Viewer，配置相同。

连接成功之后，你手机屏幕就会显示 Mac 的桌面，可以用触控板/触屏操作 Mac，点右键、拖拽、输入文字——都可以。

---

## ❓ 可能会遇到的问题

> Q：Tailscale 免费版能用多久？

A：免费版没有时间限制，个人使用完全免费，100 台设备以内都够用。

> Q：速度怎么样？

A：点对点直连的情况下，速度取决于你两端的网络带宽。我在家里 500M 宽带、手机 5G 网络下，SSH 操作几乎没有延迟；VNC 操控桌面也相当流畅。

> Q：Tailscale 需要保持后台运行吗？

A：需要。需要常驻后台才能保持连接。好在它资源占用极低，我 Mac 上的 Tailscale 几乎不耗电。

> Q：能不能让 Mac 在睡眠状态下也被控制？

A：默认不行，Mac 睡眠后网络断开就无法连接。可以设置"唤醒网络访问"（Energy Saver → Wake for network access），或者让 Mac 从不睡眠。如果用 Mac Mini 当服务器，建议设置为从不睡眠。

> Q：安全吗？

A：所有流量都经过 WireGuard 加密（开源、审计过，军工级加密标准）。设备之间直接加密通信，不经过第三方。建议开启 Tailscale 的两步验证。

---

## 🚀 进阶功能：Funnel 把本地服务暴露到公网

Tailscale 还有个叫 **Funnel** 的功能，可以把 Tailnet 里运行的服务暴露到公网上——不需要公网 IP，不需要配置路由器。

比如你在家里 Mac 上跑了一个 Web 服务（\`localhost:3000\`），用 Funnel 可以一键让它在公网上可访问：

```
tailscale serve --bg https+insecure://localhost:3000
tailscale funnel 443
```

这个功能普通用户用得不多，感兴趣可以看官方文档。

---

10 分钟装好，终身免费用，隐私数据不经过任何第三方服务器——光这三点，就值得每个有多设备管理需求的人试试。

​

官网：tailscale.com，去下载试试看。

![[笔记同步助手/images/43f3e7f87b63944c666d4405a66314dd_MD5.gif]]

**关注我，每天分享科技作品。**

---

![[笔记同步助手/images/342641e4a977d76ad3dc831c5efe41dc_MD5.jpg|cover_image]]

Original 科技宅在家 科技奇遇寨

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/5f23e919_1778567942438?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzcwNTI5ODA2NA%3D%3D%26mid%3D2247484063%26idx%3D1%26sn%3D0fdf714804bcf4cfeeb582cfdeeb3cda%26chksm%3Df5041d87b20a4e891c15c79cd67789996b42457370c5cff1a5ffd0d34269dc4b683f01ad9fc9%26mpshare%3D1%26scene%3D1%26srcid%3D05123Eztzqc4lZWAZ3xzQp6w%26sharer_shareinfo%3Df61a489b2ebb279056c9f3d21a8d6165%26sharer_shareinfo_first%3Df61a489b2ebb279056c9f3d21a8d6165%23rd&s=obsidian)