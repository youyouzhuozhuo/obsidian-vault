---
title: "让 Claude Code - Codex- Open Code 成本爆降 92%，没早用上这款开源"
date: 2026-05-24 10:40:46
source: "微信公众号"
author: "R哥"
url: "https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487651&idx=1&sn=a7e7c1b4bee4061bd84c47d96f8c59b4&chksm=fab9b0f290b7538b1363d8451dded0da21cb7527b2ef4cea85c2cb74be5da55cd09cbbafe6d8&mpshare=1&scene=1&srcid=0524PUeg4kQwF1NjsnjNDZ3I&sharer_shareinfo=1752a0abfc504be1fe381ded24875e3a&sharer_shareinfo_first=1752a0abfc504be1fe381ded24875e3a#rd"
tags:
  - AI/编程
  - AI/工具
  - 编程/开源项目
---

来源：微信公众号-R哥

内容：
_关注公众号，_**_AI_** _技术干货及时送达__↓_

推荐阅读：[OpenClaw 在国内的热度彻底凉了。。](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487555&idx=1&sn=00e47c77348c3d8b403e77456268487a&scene=21#wechat_redirect)

---

  

大家好，我是R哥。

大家都知道，[[Claude Code]] 非常强大，但成本也不便宜，正儿八经编程的话，最低的 20$ 套餐肯定是不够的，一般都得上 **Max 5x** 套餐（100$），甚至是 **Max 20x** 套餐（200$）。

![[笔记同步助手/images/f0c25ec32eb21cc108c3d75fad2c3ffb_MD5.png]]

拿 [[Java]] 开发工具 [[IntelliJ IDEA]] 为例，**一个月的 Claude Code 20x 套餐的订阅费等于一年的 IntellIJ IDEA 的年费了**，如果公司不给报销，这对于普通程序员来说可不便宜了。

要知道，大多数程序员连 IntellIJ IDEA 的年费都不愿意付，都选择用破解版，**又何况是动辄 1 千多的 Claude Code 按月订阅费？**

其实，为了节省 [[Token]] 消耗数，**Claude 官方推出了 [[Skills]] 来代替 [[MCP]]**，只有需要的时候才加载对应的 Skill，但是，那只是加载而已。。

​

> [MCP 不香了，Claude Code 又推出了 Skills！！（保姆级安装和使用教程分享）](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247485897&idx=1&sn=1ed3e39cc171c3bca79f96d2d12c0f7d&scene=21#wechat_redirect)

真正使用 Skill 的成本其实并不低，**一次复杂的 Skill 调用可能干掉一天的 Pro 额度。。**

​

---

## Claude Code 成本爆降神器

最近又发现一款 Claude Code 神器：**rtk**

![[笔记同步助手/images/3d28c30a893b5520dc2a27b305da2466_MD5.png]]

这是一个 [[CLI]] 代理，**可在常见开发命令中将 [[LLM]] 的 Token 消耗减少 60 - 90%**，它在命令输出到达 LLM 上下文之前进行过滤和压缩，只有单一 [[Rust]] 二进制文件，零依赖，**<10ms** 开销。

**30 分钟 Claude Code Token 节省：**

​

| Operation | Frequency | Standard | rtk | Savings |
| --- | --- | --- | --- | --- |
| `ls`/ `tree` | 10x | 2,000 | 400 | -80% |
| `cat`/ `read` | 20x | 40,000 | 12,000 | -70% |
| `grep`/ `rg` | 8x | 16,000 | 3,200 | -80% |
| `git status` | 10x | 3,000 | 600 | -80% |
| `git diff` | 5x | 10,000 | 2,500 | -75% |
