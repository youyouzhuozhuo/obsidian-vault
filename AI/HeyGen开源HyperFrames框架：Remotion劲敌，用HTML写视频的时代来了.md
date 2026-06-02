---
title: "HeyGen开源HyperFrames框架：Remotion劲敌，用HTML写视频的时代来了"
date: 2026-04-18 09:34:37
source: "微信公众号"
author: "winkrun"
url: "https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461159423&idx=1&sn=f74418143cc1f6e6fb9dabb1db5b0d86&chksm=8648df719e7a46a2bf6a4b9431476d1a2bd0ce3306f4926a2ac64b0631c0376d43794e128922&mpshare=1&scene=1&srcid=0418IgFlyLwb6uulNJiBl8SO&sharer_shareinfo=87f8b2a9aa2af855dcdc4c5b5d710f45&sharer_shareinfo_first=87f8b2a9aa2af855dcdc4c5b5d710f45#rd"
tags:
  - AI/工具
  - 编程/开源项目
  - 工具/AI辅助
ai_score: 8
credibility: "high"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
![](https://pic.clipfx.app/b2a14f56dbb84660d3bf2dfb947e28d2.png)

HeyGen最新开源的[[HyperFrames]]框架解决了视频制作领域的一个核心矛盾：专业工具学习成本高，而简单工具缺乏灵活性。这个基于[[HTML]]的解决方案直接把视频变成可编程对象。

为什么选择HTML而非[[React]]

虽然HyperFrames和[[Remotion]]都能实现编程式视频生成，但两者的设计哲学截然不同。

Remotion基于React架构，更适合已有React技术栈的团队，尤其是需要从电子表格批量生成大量视频的场景；

而HyperFrames则更擅长快速生成单个高质量视频，在与[[AI代理]]协作时尤为顺畅。HeyGen工程师[[Joshua Xu]]道出了这一选择的根本逻辑：[[LLM]]基于HTML训练，积累了大量Web代码知识，而React+Remotion在训练数据中占比极小。

这一设计决策带来了显著的实际优势——开发者[[Misbah Syed]]用相同提示词让[[Claude Opus 4.7]]分别生成视频，HyperFrames仅需60秒完成渲染，而Remotion不仅耗时162秒，还需额外4分钟的首次构建时间。输出体积方面，HyperFrames同样更轻量，仅4MB，相比之下Remotion通常在14MB左右。

​

核心特性与工作流

HyperFrames的核心理念是“一个文件输入，视频输出”。它使用纯HTML标签配合data属性来控制时间轴，例如`data-start="2" data-duration="3"`，避免了虚拟DOM的开销。

它的AI优先设计让代理能够直接通过`/hyperframes`指令生成有效代码，而不需要像使用React时那样费力地应对钩子和生命周期规则。

这种设计在实际使用中带来了实在的好处。一例子是用户可以说"让标题大两倍，切换到暗色模式，并在结尾添加淡出效果"，AI代理就能够直接理解并执行。

## 实际应用场景

HyperFrames的应用场景远超传统视频制作。它能够将[[CSV]]数据自动转成动态图表视频，用[[TTS]]语音合成生成带字幕的教程，或者批量制作电商产品展示模板。

它还提供了50+即插即用的特效块，如示例中的`npx hyperframes add instagram-follow`，让开发者能够快速集成社交媒体覆盖层。

## 开始使用

安装HyperFrames非常简单，只需一行命令：

​

```
npx skills add heygen-com/hyperframes
```

这个命令不仅会安装框架，还会自动为你的AI代理安装相关技能，让它能够理解如何使用HyperFrames的特定语法。

有开发者试用后反馈，其最大优势在于"用Web标准技术栈替代专业视频软件"，但需要注意[[Node.js]] 22+和[[FFmpeg]]的环境要求。对于需要高频产出标准化视频的团队，这可能是条值得关注的技术路径。

不管怎么说，hyperframes是继remotion后，vibe video的又一大新神器，笔者视频号中也有一些remtion开发的视频，后面也会尝试使用hyperframes制作，感兴趣可以关注视频推送。

项目地址：https://github.com/heygen-com/hyperframes

关注公众号回复“进群”入群讨论。

---

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJ98g2y

## AI 分析

- 评分：8/10
- 可信度：high
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：HyperFrames、视频生成、AI编程、开源工具、Remotion替代、HeyGen

### 信息本质

HeyGen开源了基于HTML的编程式视频生成框架HyperFrames，相比Remotion更轻量、AI友好，适合快速生成单个高质量视频。

### 可信度判断

来源为HeyGen官方开源项目，有GitHub仓库和开发者实测数据支撑，可信度高。但需自行验证性能对比（如渲染时间、体积）是否在自身环境下一致。

### 可利用价值

可替代Remotion用于AI编程视频生成场景，尤其适合与Claude等LLM协作快速制作教程、产品演示、数据可视化视频。降低视频制作门槛，提升内容生产效率。

### 可开发方向

1. 开发基于HyperFrames的自动化视频生成工作流（如从CSV数据生成动态图表视频）。2. 集成TTS和字幕生成，制作多语言教程视频。3. 构建电商产品展示模板库。4. 作为AI代理的‘视频输出’模块，实现端到端内容生成。

### 可内容化方向

1. 对比评测HyperFrames vs Remotion的实测文章/视频。2. 教程：如何用Claude+HyperFrames 5分钟生成一个视频。3. 案例：用HyperFrames批量生成短视频的完整工作流。4. 开源项目推荐：50+特效块的使用技巧。

### 下一步

安装HyperFrames并运行官方示例，用Claude生成一个简单视频（如带字幕的教程片段），记录实际体验和性能数据。

### 风险

依赖Node.js 22+和FFmpeg，环境配置可能增加部署复杂度；开源项目可能迭代快，需关注兼容性；与Remotion生态不互通，迁移成本需评估。

### 建议沉淀位置

Projects/AI视频生成工具链
