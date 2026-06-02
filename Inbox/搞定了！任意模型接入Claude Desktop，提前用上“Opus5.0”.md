---
title: "搞定了！任意模型接入Claude Desktop，提前用上“Opus5.0”"
date: 2026-05-12 12:39:33
source: "微信公众号"
author: "Jarvis"
url: "https://mp.weixin.qq.com/s?__biz=MzI2MzQ3MzUxMg==&mid=2247487181&idx=1&sn=91dc48f62d43c7f742fc40fa8c7fbdbe&chksm=eb14c99a38587eb74c190f9e34c65c2395fe1090f9c79bea77113949a52b609f48e1cdf8e3c1&mpshare=1&scene=1&srcid=0512cACWQxoAMpsrDVlkx5wl&sharer_shareinfo=6184d8dcba09fd3853c39ccf14c375fc&sharer_shareinfo_first=6184d8dcba09fd3853c39ccf14c375fc#rd"
tags:
  - AI/工具
  - AI/模型
  - 编程/开源项目
---

昨天分享了一个把 [[DeepSeek V4]] 接入 [[Claude Desktop]] 的方法。

Claude 桌面版是个很强大的工具，目前顶级的可视化 [[AI 智能体]]软件。但是 [[Anthropic]] 显然是不太想让第三方模型使用。它新版本的开发者模式也限制了模型名称！！！

必须要 Claude 或者 Anthropic 开头的模型才可以，只要不符合就报错！

这么一来除了Claude自家模型，第三方模型就被卡死了。

而 DeepSeek 却一直可以用，因为官方做了一些特殊操作，不管你传什么模型 ID，它都可以响应。只是默认匹配到的模型应该是 [[Flash]]。

为了解决这个问题！

为了用上V4 Pro！

为了让 [[GLM]]、[[Kimi]]、[[MinMax]]、[[Mimo]]...都可以轻松接入。

目前有两个方案：

第一种：使用老版本，也就是几天前的版本。

第二个：做模型名称映射。

如果你已经安装了新版本，要退回去其实是有点麻烦的。

而且你可能不太容易找到特定的离线的 Claude 软件。

第二种方案会灵活很多，只要搞一个本地透传，几乎没什么延迟。但是，这种方案，得上点技术。

我是偏向使用第二种方案的！

既然选择了这种方案，就又有两个分支了。

一个是自己搞一个本地中转，一个是用别人搞的本地中转软件。

对我而言，我肯定选前者，否则 [[Opus]] 摆设么？必须用起来啊。目前已经搞定！

你们有需要的话，**Jcode 就是那个“别人搞的中转软件”。**

下面我来演示一下要怎么操作。

Claude 桌面版接入第三方模型，完整的配置方法请参考这篇文章[《骚操作！把DeepSeekV4直接接入Claude桌面版！》](https://mp.weixin.qq.com/s?__biz=MzI2MzQ3MzUxMg==&mid=2247487150&idx=1&sn=97f7ab6e901fd07e9e6c93ae9f16ec82&scene=21#wechat_redirect)

读懂了这篇之后，看今天的就很轻松了。

首先，下载 Jcode 0.9.0+ 版本的软件！

下载完直接双击安装！

然后添加平台，打开代理配置：

点击加号可以配置 [[BaseURL]]、[[API Key]]、model 这些内容。配置完成之后，首页上就会显示对应平台的图标了。

然后在首页点击对应的图标可以直接调用本地的 [[Claude Code]] 终端进行编程。

当然今天的重点不是 Claude Code 终端。

所以我们还要点击添加符号左边的网络拓扑图标。

然后进行配置：

这里的配置很简单，默认就会设置好模型映射表，里面已经有三个模型。

分别是：

claude-opus-4-7

claude-sonnet-4-6

claude-haiku-
