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
ai_score: 8
credibility: "medium"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
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

## AI 分析

- 评分：8/10
- 可信度：medium
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：Claude Code、成本优化、rtk、Token节省、CLI工具、开源

### 信息本质

介绍一款名为 rtk 的 CLI 代理工具，可在 Claude Code 等场景中通过过滤和压缩命令输出，减少 60-90% 的 Token 消耗，从而大幅降低使用成本。

### 可信度判断

来源为微信公众号，作者 R 哥，内容具体且有数据表格支撑，但未提供 rtk 的官方仓库链接或第三方验证，需自行核实工具的真实性和效果。

### 可利用价值

如果你经常使用 Claude Code 进行编程，尤其是处理大量文件或命令输出，rtk 能显著降低 Token 消耗，节省订阅费用。对于高频用户，每月可节省数百美元。

### 可开发方向

1. 集成到个人开发工作流中，作为 Claude Code 的前置过滤层。2. 开发类似工具适配其他 LLM 编程助手（如 Codex、Open Code）。3. 封装为 VS Code 插件或 CLI 工具，方便一键启用。

### 可内容化方向

1. 写一篇评测文章，对比使用 rtk 前后的 Token 消耗和成本。2. 制作短视频教程，演示如何安装和配置 rtk。3. 在公众号或知乎分享“如何将 Claude Code 月费从 200 美元降到 20 美元”。

### 下一步

1. 搜索 rtk 的 GitHub 仓库，确认项目活跃度和文档完整性。2. 在本地测试环境中安装 rtk，对比使用前后的 Token 消耗。3. 如果有效，将其加入个人开发工具链，并记录配置步骤到 Obsidian。

### 风险

1. 工具可能未经过充分测试，存在兼容性或稳定性问题。2. 过滤压缩可能丢失关键信息，导致 LLM 输出质量下降。3. 开源项目可能停止维护或存在安全风险。

### 建议沉淀位置

Projects/AI 工具链优化/Claude Code 成本优化
