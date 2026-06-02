---
author: 大鱼
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MjM5MzY3NzMyOA==&mid=2456924500&idx=1&sn=b5363839ad61a809e1924e32e7c0499a&chksm=b0f83d27440e1d3d0724c80ee4a5f60f7b911fc882eac17973d74e2af0e9493403a64d0be2dc&mpshare=1&scene=1&srcid=0527IkaeLKK2Wtm1s0VvZJW8&sharer_shareinfo=12f7e0e8a522ccb3b3b65d5e863fb968&sharer_shareinfo_first=12f7e0e8a522ccb3b3b65d5e863fb968#rd
saved: 2026-05-27 11:45:23
tags:
  - 笔记同步助手
id: 37adff73-5e63-4963-af8d-278e2488cc47
---

公众号名称：出海码农日记

作者名称：大鱼

发布时间：2026-03-22 23:55

最近用龙虾在做一个小工具，中间要用到一个api，发现coding plan的付费api居然不能直接用在代码里调用，于是想到了找一些白嫖的来先用于开发测试。

当然去哪里找这些可以白嫖的，还是得问ai，顺手整理了出来，有需要的朋友可以参考。

今天直接给你盘10个大模型API平台，5个美国的，5个国内的，怎么注册、能薅多少、怎么接入工具，全给你说清楚。

---

# 先说说为什么要薅免费API

用过OpenClaw或者类似AI工具的人都知道，这东西跑起来Token消耗是真的猛。

Claude Sonnet 4.6，输入3美元/百万Token，输出15美元/百万Token。GPT-5.3，输入2.5美元，输出10美元。一个活跃用户每天光工具调用就能跑50万Token出去，一个月下来……自己算吧。

所以正确姿势是：日常任务走免费API，真正需要顶级模型的任务才花钱。这一套组合下来，费用能压到极低。

---

# 🇺🇸 美国5大平台

# 1\. Groq —— 速度炸裂，免费还不要信用卡

Groq最大的卖点不是便宜，是快。

它用的是自研LPU芯片，不靠GPU跑推理，速度能达到300+ tokens/秒，比同级产品快3-10倍。你能明显感觉到它在"喷"字，而不是"蹦"字。

更关键的是：免费层，不绑卡。

去 console.groq.com 注册，拿到API Key就能用。免费可用的模型包括Llama 3.3 70B、Mixtral 8x7B这些货色，都不是小模型。

有Rate Limit限制，超了返回429报错，但不扣钱。适合需要快速响应的对话任务、实时摘要这类场景。

接入配置：

Base URL: https://api.groq.com/openai/v1

Model: llama-3.3-70b-versatile

---

# 2\. Google AI Studio —— 免费用Gemini，真的香

如果你问我2026年性价比最高的免费API是哪个，我会说Google AI Studio。

原因只有一个：你能免费调用Gemini旗舰模型。

Gemini 3 Flash免费层每分钟10次请求，每天500次。Gemini 3 Flash-Lite每天1000次。Gemini 3 Pro也有免费额度，虽然少一点（每分钟5次，每天100次）。

去年Google把免费额度砍了一刀，说是"被滥用"——但对个人开发者和低频场景来说还是够的。

而且Gemini支持100万Token超长上下文，这个其他免费方案根本没得比。要处理超长文档？这是唯一的免费选项。

去 aistudio.google.com 拿Key，日常用 gemini-3.1-flash-lite-preview 就够了。

---

# 3\. OpenRouter —— 一个Key，薅遍全网

OpenRouter本身不做模型，它是个聚合中间商。

你注册一个账号，用同一个接口，就能调用OpenAI、Anthropic、Google、Meta、Mistral、DeepSeek……几乎所有主流模型。

最香的地方：24个永久免费模型，不用信用卡。

包括：

google/gemini-2.0-flash-exp:free

meta-llama/llama-3.3-70b-instruct:free

deepseek/deepseek-r1:free

还有个实用玩法：配置多个模型，让工具根据任务复杂度自动路由——简单任务走免费模型，复杂任务才触发收费模型。月费用基本能压到接近零。

去 openrouter.ai 注册，直接有官方OpenClaw集成文档。

---

# 4\. Together AI —— 注册送100美元，200+开源模型随便跑

注册就送100美元，这个力度在海外平台里算很猛的了。

Together AI是开源模型推理领域最大的平台之一，200+模型，包括Meta Llama 4全系、DeepSeek V3/R1、Qwen全系。

100美元能跑多久？按DeepSeek V3的定价（约0.28美元/百万Token）算，能处理约3.5亿Token。日常使用，撑2-6个月不是问题。

额度用完之后定价也比OpenAI便宜5-10倍，值得长期留着。

---

# 5\. Mistral AI —— 每月10亿Token免费，欧洲良心

法国公司，欧洲AI圈的重要玩家。

它的免费Experiment层真的很慷慨：每月10亿Token，不要信用卡。

10亿Token是什么概念？假设每次对话2000 Token，能对话50万次。个人用户基本上用不完。

接入方式和OpenAI兼容：

Base URL: https://api.mistral.ai/v1

Model: mistral-small-latest

---

# 🇨🇳 国内5大平台

# 1\. 硅基流动 —— 我最推荐的国内平台

没有之一。

注册就送2000万Token，约等于14块钱。邀请新用户还能再拿14元。9B及以下参数的模型，官方承诺永久免费。

永久免费的模型包括Qwen2.5-7B-Instruct、Llama-3.2-3B这些，处理日常轻量任务完全够用。

接入方式和OpenAI完全兼容，改个 base\_url 就行：

Base URL: https://api.siliconflow.cn/v1

另外它深度适配了华为昇腾芯片，国内用户网络延迟比直连海外API稳很多。

---

# 2\. 阿里云百炼 —— 每个模型单独送100万Token

这个平台的骚操作是：每个模型分别赠送100万Token免费额度。

而它支持的模型种类是国内最多的——通义千问全系、DeepSeek全系、Kimi、MiniMax、智谱GLM……

一个新账号开通，几乎每个叫得出名字的模型都有免费额度。叠加起来的总量相当可观。

适合想对比测试不同模型的人。

Base URL: https://dashscope.aliyuncs.com/compatible-mode/v1

---

# 3\. 智谱AI —— 2000万Token永久有效，GLM-4-Flash永久免费

注意是永久有效，不是3个月过期那种。

GLM-4-Flash宣布永久免费，不限制调用量。模型背后是清华系团队，中文理解有独特优势。

GLM-4-Flash处理文本摘要、日程管理、邮件草稿这类简单任务完全够用。可以把它设为默认轻量模型，只有遇到复杂推理时才切换付费模型。

Base URL: https://open.bigmodel.cn/api/paas/v4/

Model: glm-4-flash

---

# 4\. 火山引擎（字节豆包）—— 每天50万Token免费

字节跳动旗下的云服务平台，豆包大模型通过它对外开放API。

个人开发者每日50万Token免费推理额度，折算成对话大约每天250次。个人日常使用基本够了。

注意：需要先完成实名认证才能开通API权限，这个不要忘。

Base URL: https://ark.cn-beijing.volces.com/api/v3

Model: doubao-pro-128k

---

# 5\. 月之暗面Kimi —— 200K超长上下文，国内最长

Kimi的API最大亮点是200K Token超长上下文，这是国内产品里最长的。

如果你的工作场景是处理超长文档——法律合同、学术论文、超长会议记录——Kimi API是国内最合适的选择。

K2.5模型推出后有限时免费调用策略，新用户也有免费额度。

Base URL: https://api.moonshot.cn/v1

Model: moonshot-v1-128k

---

# 🖥️ 终极方案：Mac Mini + Ollama，彻底不花钱

前面说的那些，再怎么免费，你还是在用别人的算力，受别人的限速和隐私政策约束。

真正的Token自由只有一条路：在自己机器上跑模型。

2026年做这件事的最优硬件就是Apple Mac Mini M4。

原因是苹果M系列芯片的统一内存架构对本地跑大模型有天然优势：

16GB版（约799美元）：流畅跑Qwen3-8B、Llama 3.3 8B

32GB版（约1199美元）：跑Qwen3-14B，中文任务接近API级别

64GB版（约1999美元）：跑Qwen3-32B，质量接近GPT-4o早期版本

全天候运行，每月电费约20-25元人民币。一次性硬件投入，永久消除API费用。

Ollama是目前最流行的本地大模型框架，装好之后你的Mac就变成了一个私人AI API服务器。

5步搞定，安装步骤：

# 第1步：安装Ollama

brew install ollama

# 第2步：设为后台服务

brew services start ollama

# 第3步：下载模型（按内存选）

ollama pull qwen3:8b

# 16GB内存

ollama pull qwen3:14b

# 32GB内存

# 第4步：关键！扩大上下文窗口（默认只有2048，必须改）

echo 'export OLLAMA\_NUM\_CTX=32768' >> ～/.zshrc

source ～/.zshrc

brew services restart ollama

# 第5步：配置接入工具

# Base URL: http://localhost:11434/v1

# Model: qwen3:8b

# API Key: ollama（随便填）

---

# 最后，给你一个按任务分级的用钱策略

| 任务类型 | 用哪个 | 成本 |
| --- | --- | --- |
| 日常轻量任务 | Ollama本地模型 | 零 |
| 摘要/总结/分类 | 硅基流动/Groq免费层 | 零 |
| 复杂推理/重要文档 | DeepSeek V3/Mistral | 极低 |
| 顶级质量要求 | Claude/GPT（按需） | 按量付费 |

"AI API好贵"这件事，在2026年已经是过时的抱怨了。

免费资源够聪明的人用很久，真正的壁垒从来不是钱——是你知不知道去哪里拿。

现在你知道了，去薅吧。

---

![[笔记同步助手/images/e4d40307c7a2b2062f8b0324e443a33d_MD5.jpg|cover_image]]

原创 大鱼 出海码农日记

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/31332649_1779853521386?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMjM5MzY3NzMyOA%3D%3D%26mid%3D2456924500%26idx%3D1%26sn%3Db5363839ad61a809e1924e32e7c0499a%26chksm%3Db0f83d27440e1d3d0724c80ee4a5f60f7b911fc882eac17973d74e2af0e9493403a64d0be2dc%26mpshare%3D1%26scene%3D1%26srcid%3D0527IkaeLKK2Wtm1s0VvZJW8%26sharer_shareinfo%3D12f7e0e8a522ccb3b3b65d5e863fb968%26sharer_shareinfo_first%3D12f7e0e8a522ccb3b3b65d5e863fb968%23rd&s=obsidian)