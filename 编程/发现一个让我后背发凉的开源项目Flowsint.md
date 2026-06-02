---
title: "发现一个让我后背发凉的开源项目Flowsint"
date: 2026-04-09 15:13:40
source: "微信公众号"
author: "black keyboard"
url: "https://mp.weixin.qq.com/s?__biz=MzkzMjk1NDA1Mw==&mid=2247486362&idx=1&sn=acfd6b89b3614c3849b247b13b3bf402&chksm=c3ee1b6d15d7615b37e12d555fbd03de5dfcb90349717f139b0f37aa54a4bfe475ac13892cd8&mpshare=1&scene=1&srcid=0409HyIw5PsxyWuLZ1KsbGII&sharer_shareinfo=1bd3d94fe04d99642a47a24a14473fea&sharer_shareinfo_first=1bd3d94fe04d99642a47a24a14473fea#rd"
tags:
  - 编程/开源项目
  - 工具/效率
  - 科技/安全
ai_score: 7
credibility: "high"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
发现一个让我后背发凉的开源项目 → v给它一个邮箱，它能自动挖出关联域名、数据泄露记录、社交账号，然后画成一张关系图谱。

Flowsint 是一个基于图数据库的 OSINT 调查平台，核心思路是把所有实体（域名/IP/邮箱/手机号/加密钱包/社交账号/组织）建模为节点，通过自动化 Enricher 扩展关联关系，最终形成可交互的调查图谱。

​

### 内置 Enricher 覆盖面很广：

→ 域名方向：子域名枚举、WHOIS、反向DNS、历史记录、ASN 关联

→ IP/网络：地理定位、ASN 查询、CIDR 枚举

→ 社交媒体：Maigret 用户名跨平台搜索

→ 邮箱：数据泄露查询、Gravatar 关联

→ 加密货币：钱包交易记录、NFT 持仓

→ 网站：爬虫、链接提取、Tracker 识别

→ 还支持 N8n 工作流对接

技术栈：`FastAPI` + `Neo4j` + `PostgreSQL` + `Celery`，前端号称千节点不卡。Docker 一键部署，所有数据存本地。

值得注意的点：

→ 2800+ Star、355 Fork，社区活跃度不错

→ 项目明确标注了伦理准则（ETHICS.md），限定用于合法调查/安全研究

→ 仍处于早期开发阶段，README 自己写了 “definitely needs help”

→ Enricher 的数据源质量和覆盖率需要实际测试才知道深度如何

→ 类似工具有 Maltego（商业）和 SpiderFoot（开源），Flowsint 的差异化在于图谱交互体验和模块化架构

适合安全研究员、OSINT 调查员、威胁情报分析师。

⭐ 2,801 | 🍴 355 | TypeScript

🔗 https://github.com/reconurge/flowsint

​

> 2026-03-30
> 
> 你的微信聊天记录和朋友圈，其实全都躺在 Mac 本地的加密数据库里 → 这个工具能直接解锁查询。
> 
> wechat-toolkit 是一个 macOS 微信数据查询工具包，通过 Mach API 从微信进程内存中提取 SQLCipher 加密密钥，然后用 sqlcipher 直接查询本地数据库。
> 
> 核心能力：
> 
> → 群消息查询 + 关键词全库搜索

![](https://pic.clipfx.app/238779558c85f1d0a80df3989a9832a6.png)

---

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IKZAhfS3iaCIS6ZYMHBKngs6ia0q0AwaywajD5YZZzMp5t2AfiahUqicII2oU4mYL33ZQrLvLQFY90UiaLibFQST6JRdH3c48Xyt0Upj8IO99KkvY/0?wx_fmt=jpeg)

black keyboard

## AI 分析

- 评分：7/10
- 可信度：high
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：OSINT、安全研究、图数据库、威胁情报、开源工具

### 信息本质

Flowsint是一个基于图数据库的OSINT调查平台，通过邮箱等初始实体自动挖掘关联域名、数据泄露、社交账号等信息并生成关系图谱。

### 可信度判断

项目在GitHub上有2800+ Star和355 Fork，社区活跃度高，有明确的伦理准则，技术栈成熟（FastAPI+Neo4j+PostgreSQL+Celery），来源为微信公众号但引用了官方仓库，可信度较高。需实际测试Enricher数据源质量。

### 可利用价值

可用于安全研究、威胁情报分析、个人数字足迹排查，也可作为AI编程项目中数据关联分析的参考架构。

### 可开发方向

可基于其模块化架构开发定制化Enricher，或集成到内部威胁情报工作流中；也可借鉴其图数据库建模思路用于其他实体关联项目。

### 可内容化方向

可撰写OSINT工具对比文章（Flowsint vs Maltego vs SpiderFoot），或制作部署教程视频，或分享实际调查案例。

### 下一步

在本地Docker环境中部署Flowsint，使用测试邮箱或域名运行一次完整调查流程，评估Enricher覆盖率和图谱交互体验。

### 风险

OSINT工具可能被滥用进行非法调查或侵犯隐私，需严格遵守伦理准则和当地法律；数据源可能包含不准确信息。

### 建议沉淀位置

Projects/安全研究/OSINT工具
