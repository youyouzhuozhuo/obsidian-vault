---
title: "webnovel-writer 开源AI长篇网文神器 基于Claude Code打造 解决遗忘与幻觉"
date: 2026-04-02T20:49:38
source: "微信公众号"
author: "未知"
tags:
  - AI/工具
  - AI/应用
  - 编程/开源项目
ai_score: 8
credibility: "high"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
# webnovel-writer 开源AI长篇网文神器 基于[[Claude Code]]打造 解决遗忘与幻觉 支持200万字超长连载
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzE5MTM5ODU3MQ==&mid=2247484237&idx=1&sn=82144399860b1639c108bebfaaec1c03&chksm=97e28fbcaa25e4d5aa3aaabe448181499fe2961c1605ddb256e8240fbc5bf78fd39fb8e38298&mpshare=1&scene=1&srcid=0319qG57RDRrCh1vSkkM0yBv&sharer_shareinfo=08afeae5394893c06da61c88595efbba&sharer_shareinfo_first=08afeae5394893c06da61c88595efbba#rd)
## 正文


你是否也遭遇这些AI写作困境？

-   • 写到第50章，主角名字突然变成“林风”（上一章还是“萧炎”）
    
-   • 上章埋下“神秘玉佩”，下章完全忘记，读者怒刷“吃书”
    
-   • AI擅自给反派加背景故事，偏离大纲设定，整卷崩坏
    
-   • 想写百万字长篇，但AI每章都像独立短篇，毫无主线推进
    
-   • 商业写作工具按字收费，200万字成本超万元，且无法自定义逻辑
    

**真正的长篇AI创作，不该是“边写边忘”，而应像人类作者一样记住一切、遵守承诺、持续推进**。

现在，由开发者 **lingfengQAQ** 开源的 **webnovel-writer** 正重新定义AI网文创作——  
它不是普通续写插件，而是基于 **Claude Code** 构建的**专业级长篇辅助系统**，  
通过 **双Agent架构 + 六维审查 + [[RAG]]记忆库 + 追读力机制**，  
彻底解决 **“遗忘”与“幻觉”** 两大致命问题，  
支持 **200万字量级连载**，  
每章自动记录：  
✅ 主角状态快照 ✅ 伏笔回收清单 ✅ 势力关系图谱 ✅ 爽点密度统计  
更内置 **37+题材模板**（修仙/系统流/规则怪谈/都市脑洞等），  
强制执行 **“大纲即法律、设定即物理”** 的防崩坏三定律，  
真正实现 **“AI写得稳，作者控得住，读者追得爽”**。

项目完全开源，[[GPLv3]] 协议，[[GitHub]] 地址：https://github.com/lingfengQAQ/webnovel-writer

![](https://pic.clipfx.app/b03509cba2ce6a640036aa64af5443b2.png)

  
---

### webnovel-writer 的四大核心机制

✅ **双Agent协作架构**

-   • **Context Agent**：为每章生成精准“创作任务书”，包含：
    

-   • 上章钩子承接
    
-   • 本章核心冲突
    
-   • 出场角色情绪/动机/红线
    
-   • 世界观约束（禁用能力/地点规则）
    
-   • 追读力策略（钩子类型/微兑现建议）
    

-   • **Data Agent**：从正文提取实体（人物/物品/势力），更新向量索引，确保长期一致性
    

✅ **六维并行审查系

## AI 分析

- 评分：8/10
- 可信度：high
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：AI写作、Claude Code、开源项目、RAG、网文创作

### 信息本质

基于Claude Code的开源AI长篇网文辅助系统，通过双Agent架构、RAG记忆库和六维审查解决AI写作中的遗忘与幻觉问题，支持200万字连载。

### 可信度判断

来源为微信公众号，但项目托管在GitHub（GPLv3协议），有明确开发者（lingfengQAQ）和仓库地址，可验证。功能描述具体，技术方案合理（双Agent+RAG），可信度高。需实际测试确认效果。

### 可利用价值

直接解决AI长篇写作的核心痛点（遗忘/幻觉），适合我探索AI辅助创作工具链，可集成到Claude Code工作流中，提升写作效率和质量。

### 可开发方向

可基于此项目开发定制化写作助手（如适配特定题材模板），或将其RAG记忆库机制迁移到其他长文本生成场景（如剧本、技术文档）。

### 可内容化方向

可写评测文章（对比其他AI写作工具）、教程（如何部署和使用）、或分享开源项目亮点（双Agent架构、六维审查）。

### 下一步

克隆GitHub仓库，在本地或云端部署测试，用一个小型网文片段验证记忆和一致性效果。

### 风险

开源项目可能存在维护不足或依赖Claude API费用；GPLv3协议限制商业闭源使用；需注意API调用成本。

### 建议沉淀位置

Projects/AI写作工具链
