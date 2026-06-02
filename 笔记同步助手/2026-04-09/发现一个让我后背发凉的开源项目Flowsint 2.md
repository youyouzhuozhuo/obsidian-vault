---
author: black keyboard
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkzMjk1NDA1Mw==&mid=2247486362&idx=1&sn=acfd6b89b3614c3849b247b13b3bf402&chksm=c3ee1b6d15d7615b37e12d555fbd03de5dfcb90349717f139b0f37aa54a4bfe475ac13892cd8&mpshare=1&scene=1&srcid=0409HyIw5PsxyWuLZ1KsbGII&sharer_shareinfo=1bd3d94fe04d99642a47a24a14473fea&sharer_shareinfo_first=1bd3d94fe04d99642a47a24a14473fea#rd
saved: 2026-04-09 13:00:18
tags:
  - 笔记同步助手
id: 2da8b51c-b1bd-463f-b489-a049dcc1204d
ai_score: 7
credibility: "high"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
公众号名称：black keyboard

作者名称：

发布时间：2026-04-03 15:39

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
- 建议标签：OSINT、Flowsint、安全研究、威胁情报、开源工具、图数据库

### 信息本质

Flowsint 是一个基于图数据库的开源OSINT调查平台，可自动关联域名、邮箱、社交账号等实体并生成关系图谱；同时笔记还提及了微信聊天记录提取工具wechat-toolkit。

### 可信度判断

Flowsint 项目有明确的GitHub仓库（2800+ Star）、伦理准则和活跃社区，技术栈合理，可信度高。但Enricher的数据源质量需实际测试。wechat-toolkit涉及隐私提取，需谨慎评估合法性。

### 可利用价值

Flowsint 可用于安全研究、威胁情报分析、资产测绘等，对AI编程和开源项目方向有参考价值。wechat-toolkit 可作为隐私安全研究的案例，但不宜直接使用。

### 可开发方向

可以基于Flowsint开发定制化的资产测绘工具或威胁情报看板；或将其Enricher模块集成到自己的安全分析工作流中。

### 可内容化方向

可以写一篇对比Flowsint、Maltego、SpiderFoot的OSINT工具评测文章；或制作Flowsint部署与使用教程视频。

### 下一步

在本地Docker环境中部署Flowsint，测试其Enricher对常见域名和邮箱的关联效果，记录数据质量和性能。

### 风险

Flowsint 用于非法调查可能违反法律；wechat-toolkit 提取微信数据可能侵犯隐私，存在法律风险。

### 建议沉淀位置

Projects/安全研究/OSINT工具
