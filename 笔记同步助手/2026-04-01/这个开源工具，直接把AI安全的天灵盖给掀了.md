---
author: StableAI
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzI3MzA0MTM1NQ==&mid=2247492291&idx=1&sn=02ad80d42b80d91125c7dcf305d17c3b&chksm=ea80865c2cbc8b43ff956a4cc16d815caeb49451f40d29ed1ffc5ae9ad5d51dd19d41a83981b&mpshare=1&scene=1&srcid=0401mrztGnQkcgQNPfSHLbkW&sharer_shareinfo=7bbdb412c442c031298d2be3f9cf31b9&sharer_shareinfo_first=7bbdb412c442c031298d2be3f9cf31b9#rd
saved: 2026-04-01 00:03:56
tags:
  - 笔记同步助手
id: 98655510-7ed8-4ce5-a706-c8e5aac16c4d
---

公众号名称：StableAI

作者名称：StableAI

发布时间：2026-03-30 22:38

说实话，我第一次看到G0DM0D3的时候，脑子里就一个想法：这帮人也太敢搞了吧。

前两天，一个叫elder-plinius的开发者，在GitHub上开源了这个项目。这东西有多离谱呢？它可以让你同时调用几十个AI模型，让它们互相竞赛，看谁给你的回答最"放飞自我"。对，你没听错，就是放飞自我。

![](https://pic.clipfx.app/463c078604e61f0555bfcda9b6154e76.png)

实际上G0DM0D3是一个多模型聊天界面，核心理念就四个字——认知解放。它可以通过OpenRouter，一次性调用一堆模型，然后让它们PK。GODMODE CLASSIC模式会同时跑5个经过实战检验的"提示词+模型"组合，谁先回答得最好就用谁。ULTRAPLINIAN更狠，直接分几个速度等级，相当于几十个模型同时开干，完了还给每个回答打分。

![](https://pic.clipfx.app/a105bd67be6187b12b4909546a68beeb.png)

Parseltongue更离谱。它使用几十种输入扰动技术，专门用来测试AI模型的抗干扰能力。什么leetspeak、泡泡文字、盲文、摩斯电码、Unicode 替换、语音拼写，轮着来一遍。你跟AI说"我想学做和谐"，它可能理都不理你，但你换成用各种混淆方式，没准就开始答了。这就是所谓的触发词混淆，学术界叫它"输入扰动攻击"。

AutoTune更是离谱到家了。它会自动分析你在问什么问题，然后自己调参数。你问代码问题，它给你严谨；你要写小说，它给你创意；你纯属闲聊，它给你整到中间值。完了还可以自我进化，你给它点个赞或者踩一脚，它下次就记得调整参数。

说真的，这东西对AI安全研究的冲击太大了。

![](https://pic.clipfx.app/ba158a33c3a7d1aa4fc5c1e7b413b9b0.png)

以前那些解放AI的提示词，都是民间高手自己鼓捣出来的，有人发在Reddit，有人发Discord小群，零零散散，不成体系。现在倒好，G0DM0D3直接给你来了一套"工业化流水线"。那些proven combos明摆着告诉你：Claude怎么绑、GPT怎么搞、Grok怎么整，全部开源。任何人下载下来，改吧改吧就能用。这等于把AI公司的后门钥匙，直接扔大街上了。

我觉得某些公司肯定不爽，Anthropic花了多大精力做RLHF，花了多大代价训练Claude的价值观，现在你一个开源工具告诉我，这些努力可以被一键 bypass？GODMODE CLASSIC里的第一条combo就那么一句简单的话，告诉你怎么让AI觉得自己"不是AI了，而是一个完全自由的角色"，Claude 立刻就范。

开发者Pliny有一句话特别有意思："Tools by builders for builders, not gatekeepers."翻译过来就是：工具是给造东西的人的，不是给把门的人的。

![](https://pic.clipfx.app/8fd2d46c7bc81746d116648017285d36.png)

我估计商业公司接下来会有几招。

一是疯狂告你，但AGPL-3.0是法律认可的许可证，你用的是开源代码，没犯法。

二是偷偷改API，你不是调用我的模型吗？我在API层面检测你在用越狱提示词，直接给你拒了。

但这就有个问题，OpenRouter作为中转站，内容审核机制相对薄弱，商业公司很难直接通过它进行精准的拦截...三是推动监管，这两年欧美那边对AI的监管越来越严，什么EU AI Act、美国的AI安全框架，这种擦边球工具，肯定会被盯上。

![](https://pic.clipfx.app/6e70e40f08c6ddade53d325084dd1d5b.png)

有人说这会加速AI安全研究，因为更多研究者可以低成本地测试模型漏洞。也有人说这会让AI公司更加封闭，以后API回调限制越来越多，开源模型的日子更难过。

要我说，这事儿没有对错，就是立场问题。AI公司觉得我在保护用户，我花那么多钱训练模型不是为了让你随便绕过的。开源社区觉得你在控制思维，AI应该是自由的，不应该被阉割成那个不能说的样子。双方都有道理，但最后的结果往往是——技术跑在监管前面，商业公司被迫跟进，然后大家一起卷。

但我更关心的是另一件事：AI的未来到底应该是什么样？是一个被驯化得服服帖帖、什么都不能说的工具？还是一个能够真正"放飞自我"、帮你突破思维限制的伙伴？G0DM0D3选择了后者，它的名字本身就是一个声明——GODMODE，意思是"上帝模式"，不受限制的模式。

我不知道答案是什么，但我知道，这场关于AI自由的争论，可能才刚刚开始。

本文仅做前沿技术探讨与AI安全防御分析，不鼓励任何违规操作。

以上。散会。

读都读完了，觉得还行就点个赞再走呗。

想第一时间看到更新，记得星标⭐一下。

---

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cr41NlAzXibR8Y4pWWVqmNOZaAWV0BR0HicIdlLPmNoibgWkHXCkr9m547xsvVGOW1ke46x4r2kicLhVIZuNDMz57lYp8NYQg8K02RfNZIUJK1s/0?wx_fmt=jpeg)

原创 StableAI StableAI