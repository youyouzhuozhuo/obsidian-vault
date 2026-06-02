---
title: "给 Claude Code 装上金融大脑，是时候赚点钱了"
date: 2026-04-23 14:04:34
source: "微信公众号"
author: "老章很忙"
url: "https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649012750&idx=1&sn=a7ee40e2e3f6620106e40a674d815b3a&chksm=868e350f19831bc1ebc3ecd7e74035c04545a09aa3edb7a4830dadaf5d9b08f2cc03ceaeff91&mpshare=1&scene=1&srcid=0423tALX8OUC4Wc2ELWAEvYW&sharer_shareinfo=0dcadd7285fc51ecbfd74dd18856afb6&sharer_shareinfo_first=0dcadd7285fc51ecbfd74dd18856afb6#rd"
tags:
  - AI/Agent
  - 金融/量化交易
  - 编程/开源项目
---

来源：微信公众号-老章很忙

内容：
[Opus 4.7 之后 Anthropic 再放3招](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649012735&idx=2&sn=6209e7bbdfbf9fcedbca47551378da3b&scene=21#wechat_redirect)

[Kimi K2.6 开源，最强大Agent模型，部署教程](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649012735&idx=1&sn=bbda5c2a0ce3a654b4f110b99df52486&scene=21#wechat_redirect)

[一句话生成专业架构图，Claude Skill新玩法](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649012671&idx=2&sn=40653412a108c4c24dd92c64da936eff&scene=21#wechat_redirect)

[4个超强项目，让你的 Claude Code 如虎添翼](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649012560&idx=1&sn=985cb9100d8608f0aceee42683041d5d&scene=21#wechat_redirect)

推荐一个应该可以赚钱的Skills 🐶

finance-skills（地址：finance-skills.himself65.com）：打包 20 个金融分析技能，一行命令装进 [[Claude Code]]

​

### 简介

himself65 开源的 finance-skills，遵循 [[Agent Skills]] 开放标准，专门服务金融分析和交易场景。

项目定位很清晰：让 [[AI代理]] 直接能做财报解读、期权策略分析、市场情绪追踪这类工作，而不只是回答金融常识问题

整包 20 个技能，分成 6 个插件模块，可以整包装，也可以按需挑

​

> ❝​
> 
> ⚠️ 郑重声明：这个项目是教育和研究用途，不构成投资建议。投资有风险，入市需谨慎。

### 安装

## Claude Code 一键装全部：

```
npx plugins add himself65/finance-skills
```

## 按需装某个插件：

```
# 只装市场分析模块
npx plugins add himself65/finance-skills --plugin finance-market-analysis

# 只装社交媒体监控
npx plugins add himself65/finance-skills --plugin finance-social-readers

# 只装数据源
npx plugins add himself65/finance-skills --plugin finance-data-providers
```

## 其他 AI 代理也能装：

```
npx skills add himself65/finance-skills -a 
```

### 20 个技能清单

#### 市场分析（10 个，最硬核）

`finance-market-analysis` 插件，底层数据来自 [[yfinance]]，基本覆盖了量化分析的主要场
