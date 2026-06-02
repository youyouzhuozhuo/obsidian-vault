---
author: 不知
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzAxODQwMzA2Mg==&mid=2654974503&idx=1&sn=8e9b4bb913e76fdd0550798149b1c88e&chksm=8121b91a658c65ea96cde87f48473470a1cdc73dac944b2fa0d25631747d963ec3182d86f642&mpshare=1&scene=1&srcid=0425rcRWec7VYKCF051b9AQm&sharer_shareinfo=396ff35e44ea06c397eef6ce8516d899&sharer_shareinfo_first=396ff35e44ea06c397eef6ce8516d899#rd
saved: 2026-04-25 08:53:03
tags:
  - 笔记同步助手
id: f92ba067-3aeb-4c46-8194-da30a5600645
---

公众号名称：不知

作者名称：不知

发布时间：2026-03-10 07:32

前些天，群里有小伙伴聊起了AI拆书的话题。

拆书是网文作者们的刚需，很多小伙伴学写网文，都是从拆书开始。不光萌新需要拆书学习，网文圈卷生卷死，推陈出新速度之快令人目不暇接，成熟作者们同样离不开靠拆书来紧跟新风向。

然而，大家之前用的AI拆书方法，受限于模型能力，效果并不理想。一部长篇网文动辄百万字起步，扔给AI后，要么上下文不够用，十几万字就到顶了，要么AI只能处理开头部分内容，很难直接拆书到位。

6202年了，你还在因为大模型上下文窗口束手束脚吗？

不至于，真不至于！

今天咱们就来看看，如何突破上下文限制，让AI帮你自动拆完百万字长篇。

**思路整理**

为了方便后续复用拆书能力，我们可以制作一个skill来跑拆书流程。

第一步，我们需要理清楚拆书的需求。

拆书的目的不同，拆的角度和方法也会有所差异，不过其中还是有一些共通的部分，我们就先把这些共性需求整理出来吧。我认为，大致有如下几点：

1.  分拆章节，让AI读懂内容不难，但一次性读懂几百万字就太为难它了，为了避免出现只读开头和上下文超限的问题，第一步可以让AI先把原文分拆成章节，一章一章来拆文，完全在模型能力范围内。
    
2.  定义拆文的维度或流程，这一步会更个性化一点，你想要归纳单章的剧情梗概，还是想要整理出每一章的节奏、情绪、钩子，或是综合多章来分析一个剧情单元的结构框架、人物弧光等，都可以。
    
3.  拆书过程比较长，耗费token多，要考虑异常中断的情况，最好每次中断后无需重新开始，而是从断点处继续执行。当然，为了最大限度降低异常中断，可以将拆书任务分散到不同agent中，避免共用上下文。
    

基于以上需求，这套拆书skill大体的思路就明确了。

那么，我们要如何搭建这套skill呢？手搓提示词吗？

不需要，有更省时省力的方法！

**搭建拆书skill**

我之前做过一套让AI辅助设计skill的skill，可参见[《邪修大法速通「skill」，网文、漫剧、短剧适用》](https://mp.weixin.qq.com/s?__biz=MzAxODQwMzA2Mg==&mid=2654974330&idx=1&sn=4fee039fbbdcd5a964ba28dbae14c2d0&scene=21#wechat_redirect)获取。

我们可以先把这套skill塞进[「Antigravity」](https://mp.weixin.qq.com/s?__biz=MzAxODQwMzA2Mg==&mid=2654974272&idx=1&sn=8156bdc709f8b9e1a0ec4326bea09992&scene=21#wechat_redirect)里，用它来帮忙生成拆书skill。为什么选择「Antigravity」，当然是因为它可以白嫖Gemini、Claude、GPT啦～

接下来，把我们的需求提给AI牛马干活，例如：

请你帮我生成一个用于拆书的skill，它会分为多个步骤，我的思路如下：

1\. 整个拆书流程过程较长，需要一个主控agent负责维护总体的任务进度，确保所有步骤调用子agent执行到位，不会占用主控agent的上下文

2\. 由于拆书过程耗时较长，你需要设计断点机制，确保在流程的任意步骤中断后，可以从断点处继续执行后续步骤，而不是重新开始

3\. 请你为拆书过程定义一套文件结构，用于存放拆书过程中产生的文件，\[你可在此处明确对文件结构的要求……\]

4\. 拆书步骤如下：

a. 第1步：拆书skill需要先对小说原文（可能是txt或docx等各种格式）分章，设计一个脚本读取小说原文的前50字，确定本书章节标题样式后，再写个脚本，以章节为单位将整本书拆解成多个md格式文件，并按照章节顺序命名排序，存储在\`原文拆解\`文件夹下

b. 第2步：运行子agent分析单个章节的内容，提取章节剧情梗概（500字左右），\[或其他提取要求……\]

c. 第3步，\[其他步骤设计……\]

这里只是大致的框架，每个人拆书的习惯、目标不同，细节处理也可能会存在差异，把自己的需求整合进去即可。

由此生成的拆书skill，只需要我们提供原文文件，不管是百万字的作品还是千万字的作品，都不是问题，它都可以自动按流程拆完整本书。

为了节省token，我并没有把所有工作都直接丢给AI来做，而是让AI生成了一些脚本来辅助分章。

等「Antigravity」生成完，我们拿本书来实测一下，调一调不满意的地方，这款拆书skill就做好了。

**小结**

刚好我上周也随手搓了个拆书skill玩，就顺带把这套思路整理出来，分享给大家。这种快速制作skill的方法，同样可以用在让AI解决其他需求的场景中，省时省力。

回想起一年前，大家还在各种死磕提示词，搓一套提示词调来调去要耗费不少时间。如今想要让AI帮忙完成什么任务，或是设计提示词、skill，简直不要太轻松，直接把思路丢给AI，分分钟就能出草稿，改改就能用。

不过，最底层的能力要求一直没有变，那就是——**清晰、准确、完整表达需求的能力**。

偏偏这一条门槛，拦住了很多人。

AI越来越能干，帮我们释放双手，让我们可以专心去释放创造力。如何深挖我们的奇思妙想，如何精准表达，或许是我们在AIGC时代更应该锻炼的能力。

(๑•̀ㅂ•́)و✧

**往期精彩内容**

[课程 |「AI写网文」提示词入门教程](https://mp.weixin.qq.com/s?__biz=MzAxODQwMzA2Mg==&mid=2654971266&idx=1&sn=83906bbee62db0c84051a939cacf6e66&scene=21#wechat_redirect)

[课程 |「AI写网文」提示词进阶教程](https://mp.weixin.qq.com/s?__biz=MzAxODQwMzA2Mg==&mid=2654972941&idx=1&sn=95a28e9056772ee3149570afd443c64e&scene=21#wechat_redirect)

[教程 | 用「obsidian」搭建写网文工作台](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxODQwMzA2Mg==&action=getalbum&album_id=3718550945471414275&scene=126&sessionid=1762240741514#wechat_redirect)

[教程 | 用「Claude Code」搭建写网文工作台](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxODQwMzA2Mg==&action=getalbum&album_id=4281205832005713923&scene=126&sessionid=1765330770265#wechat_redirect)

[教程 | 用「Antigravity」搭建写网文工作台](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxODQwMzA2Mg==&action=getalbum&album_id=4347603766829858832&scene=126&sessionid=1769001753291#wechat_redirect)

  

---

![[笔记同步助手/images/0a5c38ec2cf3fded41c1bac4b2d257e3_MD5.jpg|cover_image]]

原创 不知 不知