---
author: 想象力AI
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkzMDQ0NzQyNA==&mid=2247486463&idx=1&sn=eb0b578920e42659ccca0f9be5355b6c&chksm=c37205f4ab8c803f84733a080448239fc77d98055aa61e34f1e170fdc6814105cfaf2bf0cf6e&mpshare=1&scene=1&srcid=0320xDTzGdmgaVgQabWC2meo&sharer_shareinfo=f6a725fcc5e27fbac144ec4e48c45951&sharer_shareinfo_first=f6a725fcc5e27fbac144ec4e48c45951#rd
saved: 2026-03-20 23:54:36
tags:
  - 笔记同步助手
id: 410f4a90-7605-4b50-801c-d3e16b5e4664
ai_score: 8
credibility: "high"
usefulness: "high"
actionable: true
opportunity_type: "项目"
analysis_status: "done"
---
公众号名称：想象力AI

作者名称：想象力AI

发布时间：2026-03-20 23:48

**hello 我是阿涵，用代码把 AI 变成生产力，欢迎关注～**

昨天 GitHub Trending 上出了个项目，YC 总裁 Garry Tan 把他自己的 Claude Code 配置全公开了。

叫 gstack。13 个 Skill，覆盖 CEO、工程经理、设计师、QA、发布工程师等角色。

同一天，GitHub 上 4 个 Claude Code 相关项目合计涨了 **8284 颗星**。Anthropic 发了 Channels、Memory、Marketplace 三连。OpenAI 收购了做 Ruff 的 Astral。Ben's Bites 专门写了一篇"什么是好的 AGENTS.md"。

整个开发者圈子在讨论同一件事：**怎么把 Claude Code 用好。**

我看完 gstack 的第一反应不是"好厉害"。

是"诶，跟我的思路完全不一样。"

我自己搞了 70 多个 Skill，跑了 3 个月。拿他的 13 个跟我的 70 个，认认真真比了一遍。

比完发现一件挺有意思的事。

​

## 先看 YC 总裁装了什么

gstack 一共 13 个 Skill，按角色分一下：

**决策层**

① `/plan-ceo-review`，CEO 模式。不让 AI 照字面做事，逼它重新定义问题。原话是："What is the 10-star product hiding inside this request?"

② `/plan-eng-review`，工程经理模式。锁架构、画数据流、逼出隐藏假设。他特别强调一点：**逼 AI 画图，因为画图会把那些"差不多就行"的含糊地带全暴露出来**。

③ `/plan-design-review`，设计师审方案。7 个维度逐个打分，0-10 分，告诉你 10 分长什么样。

**执行层**

④ `/design-consultation`，从零建设计系统。不给一套安全方案了事，同时给出"安全选择"和"冒险选择"，让你自己决定赌不赌。

⑤ `/review`，偏执型 Staff Engineer。找的不是代码风格问题，是"过了 CI 但上生产会炸"的那种 bug。N+1 查询、竞态条件、信任边界。

⑥ `/ship`，发布工程师。同步主分支、跑测试、审覆盖率、推代码、开 PR。没测试框架？它帮你搭一个。

⑦ `/qa` + `/qa-only`，QA。给 AI 装了个真浏览器（Playwright），能真点真截图。100ms 一个命令。

⑧ `/browse`，浏览器操控。Chromium 守护进程，首次 3 秒，后续 100-200ms。

⑨ `/design-review`，80 项视觉审计 + 自动修。一个 commit 修一个问题，全部可回滚。

⑩ `/retro`，周复盘。分析 commit 历史，按人拆分，给每个人表扬和改进建议。

**运维层**

⑪ `/document-release`，发版后自动更新文档。  
⑫ `/setup-browser-cookies`，从真实浏览器导入 cookie。  
⑬ `/gstack-upgrade`，自升级。

看出来了吗？

**13 个 Skill，全是软件工程。** CEO 审方案、工程师写代码、设计师审视觉、QA 找 bug、最后发版。

一条完整的软件交付流水线。干净，专业。

​

## 再看我的 70 个

我的列表长得完全不一样。

**开发**（跟 gstack 最接近的部分）  
/dev、/dev-team、/test-review、/simplify、/nextjs

**内容创作**（gstack 没有）  
/create-system、/title、/polish、/gzh、/cover、/gzh-publish、/dankoe-writer、/xhs

**信息采集**（gstack 没有）  
/collect、/daily-fxb、/gh-trending、/gzh-data、/xhs-collect、/xhs-keywords

**认知工具**（gstack 没有）  
/brainstorm、/deep-dive、/coaching、/mao、/triz、/think

**运营自动化**（gstack 没有）  
/scheduler、/heartbeat、/wechat-monitor、/cc-mesh、/tell-me

**商业决策**（跟 gstack 有交集）  
/opportunity-filter、/lean-startup、/startup-259、/plan-ceo-review（这个我直接搬了 gstack 的）

还有一堆杂的：/stock 查股票行情、/desktop 操控桌面、/transcript 清洗录音稿、/agent-browser 自动化浏览器……

第一眼对比，最明显的区别：

**gstack 是一家软件公司的工具箱。**

**我的是一个人的操作系统。**

​

## 为什么会长成这样

不是谁好谁差。出发点不一样。

Garry Tan 是 YC 总裁。每天干什么？审方案、看架构、盯质量、推发布。Skill 就沿着这条线长出来的。

我呢？一个人干五个人的活。写代码只是其中一件事。还得写公众号、采集热点、处理客户需求、做课程、盯投资、回微信群消息。

所以我的 Skill 长成了一个"啥都得管"的形状。

这就引出了一个更有意思的问题：

**你该按哪条路线来建自己的 Skill 体系？**

​

## 两条路，各有各的好

**gstack 路线：角色扮演，从上往下设计**

Garry Tan 的思路是先定义角色（CEO、工程经理、QA），再定义每个角色的行为模式。

好处是**一开始就很完整**。13 个 Skill 组合起来，覆盖了软件交付全链路。

但有个前提：你得很清楚你的工作流长什么样。

**我的路线：需求驱动，从下往上生长**

我的 70 个 Skill 没有一个是"坐下来规划"出来的。全是这样长出来的：

某个操作重复了 3 次 → cc 说"要不要建个 Skill" → 我同意 → 试用 30 天 → 好用留下，不好用归档。

好处是**每个 Skill 都被实战验证过**。不存在"设计得漂亮但没人用"的情况。

缺点也明显：前期很乱，体系感要等很久才能浮现。

打个比方。gstack 像请了建筑师画了图纸再盖房子。我的像搭了个帐篷，住进去之后一个房间一个房间加。

**哪个好？看你是什么阶段。**

​

## 我从 gstack 偷了几个好东西

**① CEO 视角审方案，这个思路值钱**

gstack 的 `/plan-ceo-review` 有个核心理念：不要照字面做需求，先问"这个需求的本质是什么"。

你说"加个图片上传功能"，普通 AI 直接写个文件选择器。但 CEO 模式会问：用户真正想要的是"上传图片"还是"发一条能卖出去的商品帖"？如果是后者，整个设计就不一样了。

这个我之前没有。我的 Skill 都是执行层的，缺这种"退后一步想问题"的能力。

所以我直接把他的 plan-ceo-review 搬过来了，改了改，现在是我的一个 Skill。

**② 逼 AI 画图，隐藏假设跑不掉**

Garry Tan 在工程经理模式里说了一句话：**"LLMs get way more complete when you force them to draw the system."**

让 AI 画架构图、状态图、数据流图。画的时候，那些"差不多就行"的含糊地带会被逼出来。

我之前做方案审查，都是让 AI 用文字描述架构。试了一下逼它画图，确实发现一些"我以为想清楚了但没想清楚"的地方。

**③ 安全选择 + 冒险选择，让人做决策**

他的设计咨询 Skill 有个细节：不只给一个方案，同时给出"安全选择"和"冒险选择"。安全的让你跟行业保持一致，冒险的让你脱颖而出。你自己决定赌不赌。

这个框架可以用到很多地方。选题、定价、功能取舍，都可以这么拆。

​

## 也有不太认同的

**① 太重了**

gstack 的 `/qa` 要跑真实浏览器，装 Playwright，编译二进制。做 SaaS 的团队没问题，一个人搞项目就太重了。

我的做法更轻：桌面操控用 macOS 原生 OCR，浏览器操控用 Chrome DevTools MCP。不用额外装东西，直接用。

**② 没有"非代码"场景**

13 个 Skill 全围绕写代码转。但我一天里写代码的时间可能只占 30%。剩下 70% 在写文章、采集信息、回消息、做决策。

如果你也是"不只写代码"的人，gstack 本身解决不了你的主要问题。得在它上面加很多东西。

**③ 没有自进化机制**

gstack 的 Skill 是人设计好的，没有"AI 自己提议新 Skill"的机制。

我的做法：cc 发现某个操作重复了，自动提议建 Skill。我审批通过，它自己建。30 天试用期，好用转正，不好用归档。

我的 Skill 数量会自动增长。gstack 不会，除非 Garry Tan 自己加。

​

## 怎么开始建自己的

两条路结合着来。

**第一步（5 分钟）：写一个 CLAUDE.md**

在项目根目录建一个 CLAUDE.md，告诉 AI 你是谁、项目是什么、喜欢什么风格、讨厌什么。

不用写多。20 行就够。效果比你想象的大得多。Claude Code 每次启动都读这个文件，相当于给它植入了一个"初始人格"。

**第二步（这周试一次）：把最重复的操作变成 Skill**

想一想，过去一周你让 AI 做得最多的事是什么？commit 代码？跑测试？写文档？

把流程写成一个 Markdown 文件，放到 `.claude/skills/` 目录下。下次直接说 `/那个名字`，它就照做了。

不用写得完美。下次用的时候改就行。Skill 是活的。

**第三步（一个月后）：回头看你积累了什么**

一个月后你会发现 Skill 从 1 个变成了 5-10 个。这些不是设计出来的，是从日常使用中长出来的。

这时候再回头看 gstack 的角色扮演思路，会更有感觉。因为你已经知道自己的工作流了，再补缺的角色，就是有的放矢。

**先长，再修。** 别上来就画蓝图。

​

## 最后说一句

Garry Tan 公开 gstack，对整个 Claude Code 社区是件好事。

不是因为 13 个 Skill 本身有多特别。是因为 **YC 总裁亲自示范了"怎么用好 AI 工具"**。

等于给行业发了个信号：AI 编程工具的竞争，从"谁的模型更强"转向了"谁的工作流更好"。

模型强不强是 Anthropic 和 OpenAI 的事。

**工作流好不好，是你自己的事。**

你的 CLAUDE.md 写了吗？你的第一个 Skill 建了吗？

还没有的话，今天就开始。

_每天用 AI 干活的真实记录。不吹不黑，只说亲历。关注「想象力AI」，一起做 AI 时代的行动派。_

---

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jCDLJeJwdgK96gL4QbOgBUnt9a5pnj5UGaPTz53yeXc701WAt0zzN1vm6jmNtw4lhtH27HgGAab4MuA12PkpNR4l9tjDiafOrvtbImeLJ7Vo/0?wx_fmt=jpeg)

原创 想象力AI 想象力AI

## AI 分析

- 评分：8/10
- 可信度：high
- 有用性：high
- 可行动：是
- 类型：项目
- 建议标签：Claude Code、Skill、工作流、AI编程、效率工具、gstack

### 信息本质

对比YC总裁Garry Tan的13个Claude Code Skill与作者自己的70个Skill，分析两种构建思路（角色驱动 vs 需求驱动），并给出构建个人Skill体系的实操步骤。

### 可信度判断

来源可靠（微信公众号想象力AI，作者有实际使用经验），内容具体（列出具体Skill名称和对比细节），逻辑自洽。无需额外核实。

### 可利用价值

提供了构建Claude Code Skill体系的两种方法论（自上而下角色设计 vs 自下而上需求驱动），以及从gstack中可借鉴的具体技巧（CEO审方案、逼AI画图、安全/冒险选择）。可直接用于优化自己的Skill体系。

### 可开发方向

1. 基于本文方法论，开发一个Skill生成器或模板库，帮助用户快速搭建自己的Skill体系。2. 制作一个Claude Code Skill评估工具，对比用户Skill与gstack的覆盖度。3. 写一个自动化脚本，根据用户操作频率自动推荐新建Skill。

### 可内容化方向

1. 公众号文章：《从YC总裁的13个Skill，我学到了什么》2. 小红书笔记：《5分钟搭建你的Claude Code Skill体系》3. 短视频：对比gstack与个人Skill的差异，给出3个实用技巧。4. 课程：《AI编程工作流：从Skill到自动化流水线》

### 下一步

本周内，按照文中第三步，在Obsidian中记录自己最重复的3个操作，并尝试将其转化为Claude Code Skill文件，放入.claude/skills/目录。

### 风险

过度依赖Skill可能导致思维固化，需定期审视Skill是否仍适用。

### 建议沉淀位置

Projects/AI工具实践/Claude Code Skill体系
