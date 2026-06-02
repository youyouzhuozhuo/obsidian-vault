---
title: "国产模型API接到Codex之后，还能跑通这10个核心玩法"
date: 2026-05-24 17:05:41
source: "微信公众号"
author: "AI沃茨"
url: "https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw==&mid=2247507308&idx=1&sn=1823daf986fac0d15015389e5dc16861&chksm=cf9e471d3918f1c6e8750136a004e076d4e6592f89d9e18c63e03166c4e72c7c71d602147ba9&mpshare=1&scene=1&srcid=0524k4V7qIdiYkKwApQe9xl4&sharer_shareinfo=ef7a1af40d55299c47f5e249dd60deba&sharer_shareinfo_first=ef7a1af40d55299c47f5e249dd60deba#rd"
tags:
  - AI/Agent
  - AI/模型
  - 编程/API
ai_score: 8
credibility: "medium"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
## Agent界不能没有Coding Plan和Max x20订阅，就像麻婆豆腐里不能没有豆腐。

中转API确实能省钱，但缓存失效之后9折没了，额度虚标，速率跟不上，上下文被动缩水，这些苦我是一点也不想吃了。[[Claude]]的API我现在也没什么招，老被封。[[GPT Pro]]现在也不敢断，谁也不知道它会不会哪天也学一下友商，突然来个身份验证。

所以这次我想测一个更具体的，

如果把国内模型API接进[[Codex App]]，它到底还能不能撑起一套真实可用的[[Agent]]工作流？

刚好，Codex团队最近分享了如何把Codex用到极致的教程。

于是我跟上线两个月，刚刚又上了新模型，之前也没专门测过的​[[阶跃星辰]]Step Plan​一拍即合，做了这次国内Codex玩法合集。

![[笔记同步助手/images/f1f0f25fe4c38a682e1197f8bd68a8a7_MD5.png]]

我最先关心两个点。

接了API之后，还能不能用手机端连Codex？锁屏状态下呢？

答案是可以。

Codex最近更新的双击Command键，然后截屏整个屏幕的功能，API模式下还能不能用？

答案也是可以。

这两个点解决了我最担心的事情，API模式不是一个残血版Codex，至少在我这次测试里，它还能保留Codex App关键的入口和交互。

Step Plan这次可以通过配置模型名step-router-v1，根据任务复杂度自动在[[deepseek-v4-pro]]和[[step-3.5-flash]]之间切换。v4-pro刚还宣布了继续保持2.5折。四舍五入一下，这就有点像[[DeepSeek]]也出了一个Coding Plan。

对Coding Plan我的要求其实不高，

能随时买到的，额度别虚标的，Max token别动不动卡到8K的，

上面这些缺点大家可以对号入座一把。。。

![[笔记同步助手/images/d3da7bfa206b1a05d5d75ac1c6306725_MD5.png]]

PS：deepseek-v4-pro和step-3.5-flash的模型综合能力分，2603是step-3.5-flash的迭代版本

![[笔记同步助手/images/45cc01ba587ac4020209e9ac621401f3_MD5.jpg]]

PS：deepseek-v4-pro和step-3.5-flash的价格排名

Step Plan里还塞了一个6B以下的[[image-edit-2]]模型​，支持文生图和图像编辑。

这个我后面也顺手测了一下。

  

## 把API接进Codex

先说最实用的部分。

我给大家做了一个脚本，它会自动引导你完成所有的配置，

```
curl -fsSL https://raw.githubusercontent.com/LearnPrompt/stepfun-codex-adapter/main/install_stepfun_codex_adapter.sh -o install_stepfun_codex_adapter.sh
chmod +x install_stepfun_codex_adapter.sh
./install_stepfun_codex_adapter.sh
```

这个脚本主要做几件事，

选择订阅类型，比如Plan或者普通订阅，选择对应模型；

检查你的电脑是否已经安装[[cc-switch]]和Codex，如果没有，它会帮你装好；

在cc-switch里把Step的API转换成Codex需要的Res

## AI 分析

- 评分：8/10
- 可信度：medium
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：Codex、国产API、阶跃星辰、Agent、AI编程

### 信息本质

介绍如何将国产模型（阶跃星辰Step Plan）API接入Codex App，并验证核心玩法可用性，提供一键配置脚本。

### 可信度判断

来源为微信公众号，作者AI沃茨，内容具体（脚本、模型名、价格排名），但未提供官方验证链接，需自行测试脚本和API稳定性。

### 可利用价值

提供了一条低成本使用Codex的路径，利用国产API替代Claude/OpenAI，适合预算有限或API被封的用户。

### 可开发方向

可开发一个国产模型API适配器工具，支持多模型切换和自动配置；或基于此工作流构建自动化编程Agent。

### 可内容化方向

可写一篇《国产API接入Codex实战：省钱又稳定》的教程文章，或制作短视频演示配置过程。

### 下一步

运行脚本安装并测试Step Plan API在Codex中的效果，记录模型切换和上下文表现。

### 风险

国产API可能不稳定、速率限制、数据隐私风险；脚本来源需审查安全性。

### 建议沉淀位置

Projects/AI工具/Codex工作流
