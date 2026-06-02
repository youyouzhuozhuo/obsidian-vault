---
title: "2 个 GitHub “低星高潜力” 硬核项目：一个躺着赚钱，一个 DIY 封神｜附部署 + 商业化"
date: 2026-04-29 13:27:10
source: "微信公众号"
author: "小柒的方舟空间"
url: "https://mp.weixin.qq.com/s?__biz=MzIzMjUyMTM0Nw==&mid=2247484595&idx=1&sn=56d20360139441648d40d3a5b5c8d773&chksm=e9e392faf9a4a0ea3ee8221fb350f009746daa13a8c5113289dd1798efdb3cb880c4b9205a44&mpshare=1&scene=1&srcid=0429GYQknqsZpldzbNV2k6cf&sharer_shareinfo=9591d27313a53eefba13b12bff714d9e&sharer_shareinfo_first=9591d27313a53eefba13b12bff714d9e#rd"
tags:
  - AI/工具
  - 编程/开源项目
  - 工具/效率
---

来源：微信公众号-小柒的方舟空间

内容：
🚀 GitHub 宝藏挖掘

# 2个GitHub宝藏项目：  
一个躺着赚零花钱，  
一个300块造机器狗

📅 2026-04-28 | 👤 技术分享 | ⏱️ 阅读约 8 分钟

兄弟们，我最近没事就在GitHub上瞎逛，专挑那种**几十到两三百星**的小众项目。为啥？那些几千几万星的大项目是好，但早就被人玩透了，竞争太大。反而是这些还没火起来的，才是咱们普通人能抓住的机会。

今天给大家挖了两个真心不错的：**Byte‑Yield** 和 **MiniQuad**，下面一次性给你讲明白怎么上手、怎么赚钱。

1 Byte‑Yield 宽带挂机

2 MiniQuad 机器狗

✅ 总结对比

🔥

项目一：Byte‑Yield宽带闲着也是闲着，挂机就有收入

一键部署，把闲置带宽变成钱，还能统一管好几个挂机平台

GitHub 仓库

tadeh85/byte-yield

当前星数

92 ⭐

技术栈

Docker + Shell

支持平台

ARM64 / x86

## 🎯 这玩意儿适合谁？

-   你家有**吃灰的旧电脑、树莓派、NAS、小服务器**，放着也是放着
    
-   你想**啥也不干就能有点被动收入**，不想天天盯着
    
-   你家里宽带套餐高，流量根本用不完
    
-   你要是搞工作室或者机房，那更爽，**多台机器一起挂，收益翻倍**
    

说白了，就是把你**晚上睡觉时也在浪费的带宽，打包卖给需要真实家庭IP的公司**，换点现金回来。

## 🧠 它到底怎么赚钱的？

很多人一听"挂机赚钱"，第一反应是：不会是那种坑爹的挖矿或者干违法事吧？

别急，这个逻辑其实挺干净的：

-   → 现在很多大公司（市场调研、广告验证、AI数据采集）需要**真实的家庭IP和带宽**
    
-   → 你跑的这个节点，就是把**一小部分闲置流量**共享出去，完全合法合规
    
-   → 平台按**流量或者在线时长**给你结算，Byte‑Yield 帮你一个面板管所有平台
    

### 最实用的功能点：

🔒 容器隔离

每个平台单独跑一个Docker，互不影响，也不会搞乱你的系统

🌐 多平台聚合

Honeygain、EarnApp、Pawns.app 主流挂机平台，一套配置全搞定

📊 可视化收益面板

在线时长、赚了多少、节点状态，一目了然

💻 全设备支持

老电脑、树莓派4/5、NAS、ARM开发板，全都能跑

## 🛠️ 怎么装？5分钟搞定

⨉ Terminal — 一键部署

```
# 1. 安装 Docker（如果已经有了就跳过）
curl -fsSL https://get.docker.com | bash
# 2. 下载项目代码
git clone https://github.com/tadeh85/byte-yield.gitcd byte-yield
# 3. 配置你的账号
# 去各个挂机平台注册好，把邮箱密码填进去
cp .env.example .envnano .env
# 填上 HONEYGAIN_EMAIL、HONEYGAIN_PASS、EARNAPP_TOKEN
# 4. 一键启动，所有节点自动跑起来
docker-compose up -d
# 5. 查看日志有没有报错
docker-compose logs -f
```

### 怎么看收益？

-   • 浏览器打开：**http://localhost:8080**
