---
author: Jarvis
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzI2MzQ3MzUxMg==&mid=2247487181&idx=1&sn=91dc48f62d43c7f742fc40fa8c7fbdbe&chksm=eb14c99a38587eb74c190f9e34c65c2395fe1090f9c79bea77113949a52b609f48e1cdf8e3c1&mpshare=1&scene=1&srcid=0512cACWQxoAMpsrDVlkx5wl&sharer_shareinfo=6184d8dcba09fd3853c39ccf14c375fc&sharer_shareinfo_first=6184d8dcba09fd3853c39ccf14c375fc#rd
saved: 2026-05-12 12:39:33
tags:
  - 笔记同步助手
id: 763f1ef4-c0f1-4702-81a5-8c62d2f77bc6
---

公众号名称：甲维斯C

作者名称：Jarvis

发布时间：2026-05-09 15:30

昨天分享了一个把 DeepSeek V4 接入 Claude Desktop 的方法。

![[笔记同步助手/images/5acfab18bf54975d8811e7ae0680d8f8_MD5.png]]

Claude 桌面版是个很强大的工具，目前顶级的可视化 AI 智能体软件。但是 Anthropic 显然是不太想让第三方模型使用。它新版本的开发者模式也限制了模型名称！！！

必须要 Claude 或者 Anthropic 开头的模型才可以，只要不符合就报错！

这么一来除了Claude自家模型，第三方模型就被卡死了。

而 DeepSeek 却一直可以用，因为官方做了一些特殊操作，不管你传什么模型 ID，它都可以响应。只是默认匹配到的模型应该是 Flash。

为了解决这个问题！

为了用上V4 Pro！

为了让 GLM、Kimi、MinMax、Mimo...都可以轻松接入。

![[笔记同步助手/images/bcbd17b79990dc2710a086a2689cc6c0_MD5.jpg]]

1778310086840\_d\_副本

目前有两个方案：

第一种：使用老版本，也就是几天前的版本。

第二个：做模型名称映射。

如果你已经安装了新版本，要退回去其实是有点麻烦的。

而且你可能不太容易找到特定的离线的 Claude 软件。

第二种方案会灵活很多，只要搞一个本地透传，几乎没什么延迟。但是，这种方案，得上点技术。

我是偏向使用第二种方案的！

既然选择了这种方案，就又有两个分支了。

一个是自己搞一个本地中转，一个是用别人搞的本地中转软件。

对我而言，我肯定选前者，否则 Opus 摆设么？必须用起来啊。目前已经搞定！

你们有需要的话，**Jcode 就是那个“别人搞的中转软件”。**

下面我来演示一下要怎么操作。

Claude 桌面版接入第三方模型，完整的配置方法请参考这篇文章[《骚操作！把DeepSeekV4直接接入Claude桌面版！》](https://mp.weixin.qq.com/s?__biz=MzI2MzQ3MzUxMg==&mid=2247487150&idx=1&sn=97f7ab6e901fd07e9e6c93ae9f16ec82&scene=21#wechat_redirect)

读懂了这篇之后，看今天的就很轻松了。

首先，下载 Jcode 0.9.0+ 版本的软件！

![[笔记同步助手/images/7cba3204b1f7435e058776ecc4e247c6_MD5.png]]

下载完直接双击安装！

然后添加平台，打开代理配置：

![[笔记同步助手/images/18860b1c035a0240783353c9fcfa9417_MD5.png]]

点击加号可以配置 BaseURL、API Key、model 这些内容。配置完成之后，首页上就会显示对应平台的图标了。

然后在首页点击对应的图标可以直接调用本地的 Claude Code 终端进行编程。

当然今天的重点不是 Claude Code 终端。

所以我们还要点击添加符号左边的网络拓扑图标。

然后进行配置：

![[笔记同步助手/images/a4ba2bdf73186b4f761b9069e66352d3_MD5.png]]

这里的配置很简单，默认就会设置好模型映射表，里面已经有三个模型。

分别是：

claude-opus-4-7

claude-sonnet-4-6

claude-haiku-4-5

这就是Claude家官方模型的名字，如假包换。

这部分叫做源模型，会和Claude桌面版的配置一一对应。

而目标平台和目标模型，我们就可以自由搭配了！你只要在 Jcode 里面添加过的平台和模型全部都可以选择。

选择完成之后，点击运行，中转服务就启动了。

这是一个轻量级服务，非常无感！

然后就不用管 Jcode 了。开始进行 Claude 桌面版配置了。

配置和上次类似，还是要在Claude中启用开发者模式，然后设置第三方接口。

![[笔记同步助手/images/8dd0caeb49efc1869cbd8ccaa115db98_MD5.png]]

进来之后进行网关配置（Gateway）：

![[笔记同步助手/images/e98775d574ee1b92c29c014d351fdb18_MD5.png]]

这里只要配置两个地方就好了，一个是 Base URL。一个是 Model list。

BaseURL统一写：

```
http://127.0.0.1:8765
```

模型列表可以参考：

```
claude-opus-4-7

claude-sonnet-4-6

claude-haiku-4-5
```

基本上照抄就可以了，改来改去意义也不大。

记得这里的模型名称要和 Jcode 里面源模型名称一致，这是唯一的要求！！！

配置完成，点击应用。软件就会自动重启，进入3P模式了。

![[笔记同步助手/images/5477ad215b090a9a0ae26b481948eeb8_MD5.png]]

从上图中可以看到，右侧的模型下拉列表中已经有可选的模型名称了。这里写了一个 sonnet4.7，其实目前没有这个模型啊～～ 我写错了，正常改成 opus4.7 会比较合适。但是问题不大，完全不影响使用！

Cowork 模式下，直接对话：

![[笔记同步助手/images/e754df60c186958ae644bfb1d7de6e04_MD5.png]]

立马就有返回了，非常丝滑！

我接着问了一句：“我想搞点大事情，你有什么建议？”

成功激活了 AskQuestion 功能：

![[笔记同步助手/images/539cd1b9a370b80d87c1370cc378f980_MD5.png]]

你不说，谁知道这背后是 DeepSeek V4 Pro 啊！

即便你不说，你把截图给别人，也能吓他们一跳！

**你已经用上 Sonnet 4.7 了**

如果你想玩一下，这里也可以改成 Mythos 或者 Opus 5.0！![[笔记同步助手/images/eeb77c55131531cc332bcd86d11898ae_MD5.png]]

我这个 Claude 桌面版厉害了，已经有厉害到让人害怕的 Mythos 了！

---

![[笔记同步助手/images/dfad5492bdd010958eaef74202ece584_MD5.jpg|cover_image]]

Original Jarvis 甲维斯C

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/1e865d89_1778560771215?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI2MzQ3MzUxMg%3D%3D%26mid%3D2247487181%26idx%3D1%26sn%3D91dc48f62d43c7f742fc40fa8c7fbdbe%26chksm%3Deb14c99a38587eb74c190f9e34c65c2395fe1090f9c79bea77113949a52b609f48e1cdf8e3c1%26mpshare%3D1%26scene%3D1%26srcid%3D0512cACWQxoAMpsrDVlkx5wl%26sharer_shareinfo%3D6184d8dcba09fd3853c39ccf14c375fc%26sharer_shareinfo_first%3D6184d8dcba09fd3853c39ccf14c375fc%23rd&s=obsidian)