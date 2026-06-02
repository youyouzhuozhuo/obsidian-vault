---
author: black keyboard
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkzMjk1NDA1Mw==&mid=2247486362&idx=1&sn=acfd6b89b3614c3849b247b13b3bf402&chksm=c3ee1b6d15d7615b37e12d555fbd03de5dfcb90349717f139b0f37aa54a4bfe475ac13892cd8&mpshare=1&scene=1&srcid=0409HyIw5PsxyWuLZ1KsbGII&sharer_shareinfo=1bd3d94fe04d99642a47a24a14473fea&sharer_shareinfo_first=1bd3d94fe04d99642a47a24a14473fea#rd
saved: 2026-04-09 13:00:18
tags:
  - 笔记同步助手
id: 2da8b51c-b1bd-463f-b489-a049dcc1204d
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