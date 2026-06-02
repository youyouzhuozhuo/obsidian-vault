---
author: 夹心
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzY0MDcyODA5Ng==&mid=2247483864&idx=1&sn=dde867d147c93441ef13b84bf7d326f8&chksm=f08b8ffb0047b0fa85384724aaa6cca8c724d685779d58de46f70c2dcfe37712d1c2bbe5c74e&mpshare=1&scene=1&srcid=04021ye8Jj99b181zVhjomE3&sharer_shareinfo=048b55a9fcd59b64612aff5ca748e862&sharer_shareinfo_first=048b55a9fcd59b64612aff5ca748e862#rd
saved: 2026-04-02 20:46:18
tags:
  - 笔记同步助手
id: 1e5a7a0c-1f15-49ea-8b13-6e2e81e9a94d
---

公众号名称：Jesse学习小角落

作者名称：夹心

发布时间：2026-03-31 22:00

前些天我在 GitHub 上挖到一个宝藏项目，叫 `last30days-skill`。

# [一天涨 2685 个 Stars！这个 AI 研究工具，让我看到了普通人](https://mp.weixin.qq.com/s?__biz=MzY0MDcyODA5Ng==&mid=2247483812&idx=1&sn=7828709f90425204b14b06b8720d6484&scene=21#wechat_redirect)[消除](https://mp.weixin.qq.com/s?__biz=MzY0MDcyODA5Ng==&mid=2247483812&idx=1&sn=7828709f90425204b14b06b8720d6484&scene=21#wechat_redirect)[信息差机会](https://mp.weixin.qq.com/s?__biz=MzY0MDcyODA5Ng==&mid=2247483812&idx=1&sn=7828709f90425204b14b06b8720d6484&scene=21#wechat_redirect)

> **AI 世界每个月都在重新发明自己。**

> **这个工具帮你保持领先——不是靠更努力，而是靠更聪明地获取信息。**

## 01 发现一个好东西，但用不了

先温习一下原版，`last30days-skill`

它的功能很简单：**让 AI 自动搜索全网最近 30 天的内容，生成研究报告。**

听起来很爽对吧？但我试了一下，发现一个问题：

**它搜的都是英文平台。**

```
Twitter ✅
Reddit ✅
YouTube ✅
Hacker News ✅
```

**我想搜的呢？**

```
微博 ❌
知乎 ❌
B 站 ❌
小红书 ❌
公众号 ❌
```

**呃...一个都不支持。**

这就很尴尬了。我人在中国，做中文内容，天天接触得更多是中文互联网，你给我整个只能搜英文的工具有啥用？

**那就自己改吧。（其实也有群友们的响应）**

## 02 本土化，不是翻译一下就行

刚开始我以为很简单：把界面翻译成中文，不就本土化了吗？

**后来发现，太天真了。**

直到我真正开始重构

### 平台要换

英文平台 → 中国平台

![](https://pic.clipfx.app/f012b586475b450f4067b7e31a914e86.png)

**8 大平台，全部重写。**

**API 要换**

每个平台的接口都不一样：

```
微博用 OAuth
知乎要 Cookie
B 站有公开 API
小红书得用第三方
抖音要 TikHub
公众号要微信 API
百度要百度云
头条有公开接口
```

**光调通这些接口，就花了我 3 天。**

中文 NLP 要加

原版是英文的，分词、停用词都是为英文设计的。

我加了：

```
jieba 分词
中文停用词表
中文同义词扩展
```

**现在搜"AI"能找到"人工智能"，搜"公众号"能找到"微信"。**

**评分系统要改**

原版的互动度评分是按 Twitter 点赞、Reddit upvote 设计的。

中国平台的互动指标不一样：

```
微博：转发 + 评论 + 点赞
小红书：点赞 + 收藏 + 评论 + 分享
B 站：播放 + 弹幕 + 评论 + 投币 + 收藏
知乎：赞同 + 评论 + 收藏
抖音：点赞 + 评论 + 分享 + 播放
```

**权重也得重新调。**

配置要本地化

原版的配置路径是英文的，环境变量名也是英文的。

而如今：

```
配置文件有中文注释
环境变量有中文说明
错误提示是中文的
诊断命令输出是中文的
```

**中国用户不用猜了。**

---

## 03 改完之后是什么样

### 8 大平台，一次搜遍

```
python scripts/last30days.py "AI 工具" --emit compact
python scripts/last30days.py "AI 工具" --emit compact
```

**30 秒，微博、知乎、B 站、小红书、抖音、公众号、百度、头条，全部搜一遍。**

### 其中3 个平台，不用配置就能用

```
✅ B 站
✅ 知乎
✅ 今日头条
```

**装好就能用，不用注册** **API****、不用搞** **Cookie****。**

### 智能评分，高分的在前面

每条结果都有一个 0-100 的分数：

```
相关性 45%
时效性 25%
互动度 30%
```

**你不用自己判断哪个值得看，分数高的就是值得看的。**

**跨平台对比，一个话题看全貌**

![](https://pic.clipfx.app/0d4f9dc651141bc9fa2ea35db314e913.png)

搜同一个话题，它会自动把多平台的内容关联起来：

```
微博上在吵什么
知乎上在分析什么
B 站上在演示什么
小红书上在种草什么
```

**你不用来回切换 App 了。**

### 所有 AI 都能用

```
Cursor ✅
Claude Code ✅
OpenClaw ✅
Gemini CLI ✅
```

**只要你的 AI 能跑 Bash 命令，就能用。**

---

## 04 为什么我要做本土化

说实话，这个项目我**今天才刚写完，今天才开源。**

我把它做出来，原因很简单：

**我不想再用英文工具搜中文内容了。（同时也响应群友号召）**

```
你想吃中餐，结果给你个刀叉
你想喝茶，结果给你个咖啡杯
你想坐地铁，结果给你张公交卡
```

**不是东西不好，是不适配。**

**本土化就是让东西适配本地人。**

---

## 05 欢迎体验  

项目地址：

```
GitHub：https://github.com/ChiTing111/last30days-skill-cn
```

![](https://pic.clipfx.app/db4ba383c00ed47faaa981197f73a581.png)

**MIT 协议，随便用。**

有问题直接提 Issue，我看到就回，或者直接加群在群里艾特我。

---

## 06 写在最后  

**这个项目才刚开始，今天才写完，今天才开源。**

**本土化不是一次性的事。** 以后可能还要：

```
加更多平台
优化中文 NLP
改进评分算法
适配更多 AI Agent
```

**我一个人做不到最好，但开源可以。**

**如果你也受够了英文工具搜不了中文内容，欢迎试试这个项目。**

**用了觉得好，点个 Star，用了觉得不好，提个 Issue。**

💬 交流群

扫码加群**，加入 AI +测试编程实践交流群，和一群志同道合的朋友讨论。**

![](https://pic.clipfx.app/d4f65d3cb6d9bff236bf1662cf1a86fe.png)

**📮获取：**

```
• 最新技术推广文章
• 核心技能速查表
• 测试人转型 AI 训练师路线图
```

---

**👍 觉得有用？**

如果这篇文章对你有帮助：

```
点赞→ 让我知道你喜欢这类内容
关注→ 你的关注就是我的最大动力
在看→ 推荐给更多技术同行
分享→ 分享到朋友圈或技术群
```

![](https://pic.clipfx.app/3708cfad7efa682fd5359b0ca305d18a.png)

你的每一次互动，都是我持续输出干货的动力！

---

我是Jesse，专注 AI 工具实战与测试自动化，帮测试同行少走弯路。

我们下次见～

---

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0VE9kDxicLUjscfgDflWibYRic5eVHZIbuPpYFV3WwcQ55OmqWWuAquEm2PGGZ2MyMXpQmsTyckTpVD8UawoNJfBpDaPfPMjT5pwoqIgjKHZk8/0?wx_fmt=jpeg)

Original 夹心 Jesse学习小角落