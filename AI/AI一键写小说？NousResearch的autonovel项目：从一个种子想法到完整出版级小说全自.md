---
title: "AI一键写小说？NousResearch的autonovel项目：从一个种子想法到完整出版级小说全自"
date: 2026-04-14 16:43:51
source: "微信公众号"
author: "jackao"
url: "https://mp.weixin.qq.com/s?__biz=MzI1Mzg2MjAxNQ==&mid=2247490900&idx=1&sn=5aaeb9f70117112cde6a4dcc08b04572&chksm=e831d3cb117330f76853610f41f860871b89bd41aa80ccf0bfaafed5d1f9309cbd88873a7307&mpshare=1&scene=1&srcid=0414HrrkjaVX24NGQFuUDgoq&sharer_shareinfo=9427a92519b0a8bbf183a6c8fc247bf4&sharer_shareinfo_first=9427a92519b0a8bbf183a6c8fc247bf4#rd"
tags:
  - AI/应用
  - 编程/开源项目
  - AI/Agent
---

今天想和大家分享一个AI自动写小说的项目**autonovel**，想象一下：你只输入一个简单的“种子概念”（比如“一座钟声回荡的古老庄园里，次子背负家族秘密”），AI就能自动完成世界构建、人物刻画、章节大纲、逐章写作、多轮修改、排版、封面插画，甚至连有声书和落地页都一并搞定。最终输出的是可直接打印的PDF、ePub、带多语音有声书，全程几乎零人工干预。

这个项目不是以前那种简单的“AI续写工具”，而是一条**端到端的自主小说创作流水线**。它由NousResearch团队开发，灵感来自Andrej Karpathy的autoresearch项目，把“修改-评估-保留/丢弃”的迭代循环，第一次系统性地应用到了虚构文学创作上。这个NousResearch团队的作品非常多，目前最火爆的hermes-agent，就是那个与OpenClaw打得难解难分的项目，就出自他们。

截至目前，**autonovel**已经成功跑通了第一本完整小说：《The Second Son of the House of Bells》（《钟声庄园的次子》），19章、近8万字，经过6轮自动修改+6轮高级审稿，还生成了专业级排版和配套内容。开源、免费、可本地运行，对AI创作、自动化内容生成感兴趣的朋友，绝对值得一探究竟。

![](https://pic.clipfx.app/a068b2d5c4f7c080c5a9240db77e24c3.png)

### 项目核心亮点：不止“写”，而是“像专业作家一样迭代”

autonovel的强大之处在于它模拟了人类作家的工作流程，并用AI智能体实现了全自动化：

1.  1. **五层共进化架构**  
    小说被拆分成5个相互关联的“层”：
    
-   ◦ Layer 5：voice.md（叙事声音与风格）
    
-   ◦ Layer 4：world.md（世界观圣经）
    
-   ◦ Layer 3：characters.md（人物档案）
    
-   ◦ Layer 2：outline.md（大纲与伏笔台账）
    
-   ◦ Layer 1：实际章节文本  
    还有cross-cutting的canon.md（硬事实数据库）。任何一层改动，都会自动向下/向上传播，确保一致性（比如世界观改了，大纲和章节会自动检查并修正）。
    
3.  2. **双重“免疫系统”防AI毛病**
    
-   ◦ **机械层**：用正则表达式扫描，严禁“AI常见病”——过度解释、重复短语、句式单一、滥用破折号等。
    
-   ◦ **LLM评审层**：独立大模型打分，评估声音一致性、人物鲜明度、节奏感等。  
    加上对抗式编辑（adversarial_edit.py主动“砍掉500字”）、读者面板（4个人格模拟读者反馈）、Claude Opus双人格高阶审稿，形成层层把关。
    
5.  3. **四大阶段流水线**（详见官方PIPELINE.md）
    
-   ◦ **Phase 1：基础构建** → 从种子生成世界、人物、大纲、声音，直到分数达标（5-15轮迭代）。
    
-   ◦ **Phase 2：初稿写作** → 逐章撰写，每章独立评估，低于6.0分就重写。
    
-   ◦ **Phase 3：多轮修订** → 自动砍冗余 + 读者面板 + Opus审稿，循环直到分数稳定（通常3-6轮）。
    
-   ◦ **Phase 4：导出*
