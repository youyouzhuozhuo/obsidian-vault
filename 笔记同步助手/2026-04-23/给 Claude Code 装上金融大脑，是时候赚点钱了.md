---
author: 老章很忙
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649012750&idx=1&sn=a7ee40e2e3f6620106e40a674d815b3a&chksm=868e350f19831bc1ebc3ecd7e74035c04545a09aa3edb7a4830dadaf5d9b08f2cc03ceaeff91&mpshare=1&scene=1&srcid=0423tALX8OUC4Wc2ELWAEvYW&sharer_shareinfo=0dcadd7285fc51ecbfd74dd18856afb6&sharer_shareinfo_first=0dcadd7285fc51ecbfd74dd18856afb6#rd
saved: 2026-04-23 14:04:34
tags:
  - 笔记同步助手
id: 8a4e3cce-05f7-4257-ab50-11eb9b7bbfd6
---

公众号名称：Ai学习的老章

作者名称：老章很忙

发布时间：2026-04-21 13:01

[Opus 4.7 之后 Anthropic 再放3招](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649012735&idx=2&sn=6209e7bbdfbf9fcedbca47551378da3b&scene=21#wechat_redirect)

[Kimi K2.6 开源，最强大Agent模型，部署教程](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649012735&idx=1&sn=bbda5c2a0ce3a654b4f110b99df52486&scene=21#wechat_redirect)

[一句话生成专业架构图，Claude Skill新玩法](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649012671&idx=2&sn=40653412a108c4c24dd92c64da936eff&scene=21#wechat_redirect)

[4个超强项目，让你的 Claude Code 如虎添翼](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649012560&idx=1&sn=985cb9100d8608f0aceee42683041d5d&scene=21#wechat_redirect)

推荐一个应该可以赚钱的Skills 🐶

finance-skills（地址：finance-skills.himself65.com）：打包 20 个金融分析技能，一行命令装进 Claude Code

​

### 简介

himself65 开源的 finance-skills，遵循 Agent Skills 开放标准，专门服务金融分析和交易场景。

项目定位很清晰：让 AI 代理直接能做财报解读、期权策略分析、市场情绪追踪这类工作，而不只是回答金融常识问题

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

`finance-market-analysis` 插件，底层数据来自 yfinance，基本覆盖了量化分析的主要场景：

​

| 技能 | 干什么 |
| --- | --- |
| **earnings-preview** | 财报前瞻——共识预期、历史超预期/低于预期记录、分析师情绪 |
| **earnings-recap** | 财报复盘——实际 vs 预期 EPS、股价反应、利润率趋势 |
| **estimate-analysis** | 预期深挖——分析师修订趋势、EPS/营收分布、增长预测 |
| **etf-premium** | ETF 溢价折价——NAV 对比、同类 ETF 横向比较、90+ ETF 筛选 |
| **options-payoff** | 期权收益图——Bull Spread、Straddle、Condor、Butterfly 动态可视化 |
| **sepa-strategy** | Minervini SEPA 策略——趋势模板、VCP 形态、精确入场点、仓位管理 |
| **saas-valuation-compression** | SaaS 估值压缩分析——ARR 倍数、宏观归因、AI 叙事溢价、同类对比 |
| **stock-correlation** | 相关性分析——行业同类股、协同运动、配对交易候选 |
| **stock-liquidity** | 流动性分析——买卖价差、成交量分布、市场冲击估算、Amihud 比率 |
| **yfinance-data** | 基础数据——价格、财务报告、期权链、分红、盈利数据 |

**单独说一下 SEPA 策略这个技能**：Mark Minervini 的 SEPA（Specific Entry Point Analysis）是成长股交易里比较成熟的方法论，包括趋势模板筛选、VCP（波动率收缩形态）识别和精确入场

之前要跑这个分析得手动对照好几个指标，现在直接让 Claude Code 帮你扫

​

#### 社交媒体监控（5 个）

`finance-social-readers` 插件，全部只读权限，适合做舆情监控和市场情绪研究：

​

-   **twitter-reader**：搜 Twitter/X 上关于某只股票的讨论
    
-   **telegram-reader**：读 Telegram 频道，很多交易员群体在这里
    
-   **discord-reader**：Discord 交易社区情绪
    
-   **linkedin-reader**：LinkedIn 财经评论和分析师帖子
    
-   **yc-reader**：YC 公司数据库，做早期科技股研究用得上
    

#### 数据服务（3 个）

`finance-data-providers` 插件：

​

-   **finance-sentiment**（付费）：Adanos Finance API，聚合 Reddit、X.com、新闻、Polymarket 的情绪数据
    
-   **funda-data**（付费）：Funda AI API，60+ 个端点，实时报价、基本面、SEC 文件
    
-   **hormuz-strait**（免费）：实时监控霍尔木兹海峡——航运动态、油价影响、保险风险
    

这个霍尔木兹海峡监控挺有意思，当前局势下，做能源类资产的朋友可以关注

​

#### 创业公司分析（1 个）

`finance-startup-tools` 插件：

​

-   **startup-analysis**：多视角分析框架——同时从 VC 投资人、求职者、创始人三个角度拆解一家公司，做股权投资或者判断一个赛道时挺实用
    

#### UI 工具（1 个）

`finance-ui-tools` 插件：

​

-   **generative-ui**：专为 Claude 的 `show_widget` 设计，能在对话里直接渲染交互式 HTML/SVG 图表，期权收益图、相关性热力图这类可视化，配合这个技能出图效果好很多
    

#### Skill 创作工具（1 个）

`finance-skill-creator` 插件：

​

-   **skill-creator**：带评分体系的 Skill 创作向导，10 个维度打分，帮你做出质量更高的自定义金融技能，如果现有的 20 个技能不够用，用这个扩展自己的分析框架。
    

### 几个实际使用场景

## 场景一：财报季分析流程

季报密集期，想快速过一遍手头的持仓，可以这么玩：

​

1.  `earnings-preview` 先看下一次财报的预期和情绪
    
2.  `earnings-recap` 拉出上几个季度的超预期历史
    
3.  `estimate-analysis` 看分析师预期修订方向
    
4.  配合 `twitter-reader` 扫市场舆情
    

## 场景二：期权策略可视化

用 `options-payoff` 技能，直接让 Claude Code 帮你画出不同策略的收益图。Bull Call Spread、Protective Put、Iron Condor——参数调整即时更新，判断盈亏平衡点和最大损失更直观

## 场景三：ETF 套利研究

`etf-premium` 覆盖 90+ 只 ETF 的溢价折价数据。一些小型 ETF 在市场波动时溢价会走宽，有套利空间，这个技能可以批量扫

​

### 总结

**优点**：

​

-   安装极简，一行 `npx plugins add` 搞定
    
-   20 个技能覆盖面宽，从基本面到技术面到情绪面都有
    
-   SEPA 策略、SaaS 估值压缩这类偏专业的分析模块，平时很难找到现成的 AI 工具
    
-   MIT 开源，代码可审计，数据逻辑透明
    
-   更新活跃，这一个月已经加了 liquidity、linkedin-reader、etf-premium 等好几个新技能
    

**局限**：

​

-   付费数据源（Adanos、Funda AI）需要自备 API Key，有额外成本
    
-   数据底层主要靠 yfinance，雅虎金融的数据质量有时候不稳定
    
-   部分高级功能对 Claude 的 `show_widget` 有依赖，其他代理的体验可能打折扣
    
-   A 股数据覆盖不到，yfinance 主要是美股
    

做美股研究、量化交易，或者纯粹对 Agent Skills 生态感兴趣的，值得装上玩玩

#financeSkills #AgentSkills #ClaudeCode #金融分析 #开源

**制作不易，如果这篇文章觉得对你有用，可否点个关注。给我个三连击：点赞、转发和在看。若可以再给我加个🌟，谢谢你看我的文章，我们下篇再见！**

  

---

![[笔记同步助手/images/4c03269e91c60d52d50dd433d2b3dce6_MD5.jpg|cover_image]]

Original 老章很忙 Ai学习的老章