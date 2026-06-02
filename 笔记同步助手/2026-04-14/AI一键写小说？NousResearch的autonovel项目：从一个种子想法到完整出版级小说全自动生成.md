---
author: jackao
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzI1Mzg2MjAxNQ==&mid=2247490900&idx=1&sn=5aaeb9f70117112cde6a4dcc08b04572&chksm=e831d3cb117330f76853610f41f860871b89bd41aa80ccf0bfaafed5d1f9309cbd88873a7307&mpshare=1&scene=1&srcid=0414HrrkjaVX24NGQFuUDgoq&sharer_shareinfo=9427a92519b0a8bbf183a6c8fc247bf4&sharer_shareinfo_first=9427a92519b0a8bbf183a6c8fc247bf4#rd
saved: 2026-04-14 16:43:51
tags:
  - 笔记同步助手
id: 8ec6ca0c-ae19-47ba-a2ee-382f09614235
ai_score: 7
credibility: "high"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
公众号名称：恶人笔记

作者名称：jackao

发布时间：2026-04-14 07:20

今天想和大家分享一个AI自动写小说的项目**autonovel**，想象一下：你只输入一个简单的“种子概念”（比如“一座钟声回荡的古老庄园里，次子背负家族秘密”），AI就能自动完成世界构建、人物刻画、章节大纲、逐章写作、多轮修改、排版、封面插画，甚至连有声书和落地页都一并搞定。最终输出的是可直接打印的PDF、ePub、带多语音有声书，全程几乎零人工干预。

这个项目不是以前那种简单的“AI续写工具”，而是一条**端到端的自主小说创作流水线**。它由NousResearch团队开发，灵感来自Andrej Karpathy的autoresearch项目，把“修改-评估-保留/丢弃”的迭代循环，第一次系统性地应用到了虚构文学创作上。这个NousResearch团队的作品非常多，目前最火爆的hermes-agent，就是那个与OpenClaw打得难解难分的项目，就出自他们。

截至目前，**autonovel**已经成功跑通了第一本完整小说：《The Second Son of the House of Bells》（《钟声庄园的次子》），19章、近8万字，经过6轮自动修改+6轮高级审稿，还生成了专业级排版和配套内容。开源、免费、可本地运行，对AI创作、自动化内容生成感兴趣的朋友，绝对值得一探究竟。

![](https://pic.clipfx.app/a068b2d5c4f7c080c5a9240db77e24c3.png)

### 项目核心亮点：不止“写”，而是“像专业作家一样迭代”

autonovel的强大之处在于它模拟了人类作家的工作流程，并用AI智能体实现了全自动化：

1.  1\. **五层共进化架构**  
    小说被拆分成5个相互关联的“层”：
    

-   ◦ Layer 5：voice.md（叙事声音与风格）
    
-   ◦ Layer 4：world.md（世界观圣经）
    
-   ◦ Layer 3：characters.md（人物档案）
    
-   ◦ Layer 2：outline.md（大纲与伏笔台账）
    
-   ◦ Layer 1：实际章节文本  
    还有cross-cutting的canon.md（硬事实数据库）。任何一层改动，都会自动向下/向上传播，确保一致性（比如世界观改了，大纲和章节会自动检查并修正）。
    

3.  2\. **双重“免疫系统”防AI毛病**
    

-   ◦ **机械层**：用正则表达式扫描，严禁“AI常见病”——过度解释、重复短语、句式单一、滥用破折号等。
    
-   ◦ **LLM评审层**：独立大模型打分，评估声音一致性、人物鲜明度、节奏感等。  
    加上对抗式编辑（adversarial\_edit.py主动“砍掉500字”）、读者面板（4个人格模拟读者反馈）、Claude Opus双人格高阶审稿，形成层层把关。
    

5.  3\. **四大阶段流水线**（详见官方PIPELINE.md）
    

-   ◦ **Phase 1：基础构建** → 从种子生成世界、人物、大纲、声音，直到分数达标（5-15轮迭代）。
    
-   ◦ **Phase 2：初稿写作** → 逐章撰写，每章独立评估，低于6.0分就重写。
    
-   ◦ **Phase 3：多轮修订** → 自动砍冗余 + 读者面板 + Opus审稿，循环直到分数稳定（通常3-6轮）。
    
-   ◦ **Phase 4：导出** → LaTeX排版（专业书刊字体）、fal.ai生成封面/插图、ElevenLabs多角色有声书 + 响应式落地页。
    

整个过程高度模块化，27个Python 脚本各司其职，状态全记录在state.json，便于中断续跑。

​

### 使用方法：10分钟上手（适合有Python基础的朋友）

项目对本地环境要求不高，步骤超级清晰：

1.  1\. **克隆仓库**
    
    ```
    git clone https://github.com/NousResearch/autonovel.git
    cd autonovel
    ```
    
2.  2\. **配置环境**  
    复制 `.env.example` 为 `.env`，填入必要API Key：
    

-   ◦ Anthropic（Claude Sonnet/Opus，必填，写作和评审主力）
    
-   ◦ fal.ai（生成插画）
    
-   ◦ ElevenLabs（有声书语音）  
    其他依赖用 `uv sync` 一键安装（推荐用uv包管理器）。
    

4.  3\. **生成或编写种子**  
    运行 `uv run python seed.py`，或者手动在 `seed.txt` 里写一个清晰的概念（建议包含世界差异点、中央冲突、感官钩子）。
    
5.  4\. **一键启动全流程**
    
    ```
    uv run python run_pipeline.py --from-scratch
    ```
    
    它会自动创建新分支（autonovel/你的标签），按阶段顺序执行。整个过程可能需要几小时到一天（取决于模型调用量和小说长度），中途可通过日志和results.tsv监控进度。
    

**小贴士**：

-   • 第一次建议用小种子测试，避免API费用过高（Claude调用为主，成本主要在这里）。
    
-   • master分支目前还残留了第一本小说的部分硬编码内容（社区issue已提及），建议新建分支或等待官方清理后再跑自定义小说。
    
-   • 输出文件在 typeset/（PDF）、epub/、audiobook/ 等目录，直接可用。
    

### 分析：强大，但比较“折腾”

**优势很明显**：

-   • **效率革命**：传统写小说可能花几个月，它几天就能出完整成品，还自带出版级包装。
    
-   • **质量迭代机制**：不是一次性生成，而是持续自我批评+修正，远超普通prompt堆砌。
    
-   • **开源透明**：所有prompt、规则（CRAFT.md、ANTI-SLOP.md、ANTI-PATTERNS.md）都公开，可学习、可修改。
    
-   • **扩展性强**：不仅限幻想小说，理论上可适配其他类型。
    

**但也有很多局限**：

-   • **成本不低**：大量依赖付费API，尤其是长篇小说，Claude Opus审稿循环会产生不小费用（具体看你的token用量）。
    
-   • **创意边界**：AI擅长结构和一致性，但深度情感、突破性创新仍依赖人类审美。目前生成的可能仍是“高水平公式化”小说，离顶级文学估计还有距离。
    
-   • **实验阶段**：项目活跃但仍有issue（如分支硬编码），适合开发者玩，不适合零基础小白直接“躺平出书”。
    
-   • **伦理讨论**：AI生成内容用于商业出版时，版权、署名、读者知情权都需要提前考虑。
    

总的来说，它还不是取代作家的工具，只是一个**超级强大的创作助手**，你可以把它当“AI联合创作室”，人类负责定方向、最终把关，AI负责执行90%的繁重劳动。

​

### 使用建议

1.  1\. **入门级**：先跑官方示例分支，熟悉流程，再用自己的种子实验。
    
2.  2\. **进阶玩法**：修改program.md里的系统prompt，注入个人写作风格；或者只跑到Phase 3，手动润色后导出。
    
3.  3\. **成本控制**：优先用Claude Sonnet做初稿，Opus只留给最终审稿；设置更严格的停止条件减少循环。
    
4.  4\. **结合人类智慧**：AI强在执行，弱在“灵魂”。建议生成后自己读一遍，重点调整情感高潮和主题深度。
    

如果你是开发者、AI爱好者、或者想探索“AI+创意”的边界，这个项目值得关注。甚至你可以把它当作学习材料，拆解那些精妙的评估prompt，自己搭建类似流水线。

![](https://pic.clipfx.app/e1bb12632260691ff7d9cdf53a0ea582.png)

**写在最后**：  
AI正在快速改变内容创作的游戏规则，但真正的好故事，永远需要人的温度。autonovel给我们展示了一种高效、可控、可迭代的新路径，这条路不是取代，而是放大我们的创造力。

GitHub地址： https://github.com/NousResearch/autonovel

（本文基于GitHub官方README与PIPELINE.md整理，项目开源协议允许个人使用与研究，商业用途请自行评估合规性。）

---

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WAZic7VxrbDybq0GxmH9pKyHictricbEtVM4AR9muGNe7WQxQyTTZYOgcHTDP6y4N66x2PtD0sJL55ajFTWccLLwW8d4MdtDSZLV74NE5jibzUs/0?wx_fmt=jpeg)

原创 jackao 恶人笔记

## AI 分析

- 评分：7/10
- 可信度：high
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：AI写作、autonovel、NousResearch、自动化内容生成、开源项目

### 信息本质

NousResearch开源项目autonovel，实现从种子概念到出版级小说的全自动端到端流水线，包含多轮迭代审稿、排版、插画、有声书生成。

### 可信度判断

来源为知名AI团队NousResearch（hermes-agent作者），GitHub仓库公开可验证，有完整文档和示例小说。信息详实，逻辑自洽，可信度高。

### 可利用价值

可作为AI内容创作工具链的参考，用于自动化生成小说、剧本或长文内容；也可学习其多智能体迭代评估架构，迁移到其他创作场景。

### 可开发方向

1. 搭建类似流水线用于自动化生成自媒体长文或剧本；2. 提取其评估prompt（CRAFT.md等）用于其他AI写作项目；3. 修改适配中文小说创作。

### 可内容化方向

1. 评测文章：实测autonovel生成一本小说并分享体验；2. 教程：如何用autonovel快速生成小说；3. 分析：AI写作工具对比（autonovel vs 其他）。

### 下一步

克隆仓库，用官方种子跑一次完整流程（控制API成本，先用Sonnet），记录成本、耗时、输出质量。

### 风险

API费用较高（Claude Opus审稿循环）；输出质量可能偏公式化；商业出版需考虑版权和伦理问题。

### 建议沉淀位置

Projects/AI工具链/AI写作
