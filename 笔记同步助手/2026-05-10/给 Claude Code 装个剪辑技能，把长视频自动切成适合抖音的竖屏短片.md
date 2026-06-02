---
author: 几乎满级
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkwODQzNzk1OQ==&mid=2247498150&idx=1&sn=7005a3ba9603430948554c57f2671b24&chksm=c187b66ad9a3632a2ffbf3ba9998e9f3f67f2c655e73bc61cbf74ea287071fba0fac9ba9860c&mpshare=1&scene=1&srcid=0510REV6sL4tGO0eQIDbo7id&sharer_shareinfo=519cea0a9dbdcde0742ed4479a3d5271&sharer_shareinfo_first=519cea0a9dbdcde0742ed4479a3d5271#rd
saved: 2026-05-10 02:08:20
tags:
  - 笔记同步助手
id: 86926dbe-af3a-4766-b22d-d520f68b24d9
ai_score: 8
credibility: "high"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
公众号名称：几乎满级

作者名称：几乎满级

发布时间：2026-05-09 17:00

**Clipify** 一款专为 Claude Code 终端助手开发的本地自动化视频剪辑扩展（Skill）。

它能够将长视频快速转化为适合抖音、TikTok等平台的竖屏短视频，特别擅长处理播客、访谈类内容。

旨在将耗时的手动粗剪工作——看回放、找精彩点、调竖屏构图、加字幕——压缩为一次简单的命令行对话。

![](https://relay-1.bijitongbu.site/p/9c727877762dd5ffbfd043a9cc7bb4bf.png)

输入视频路径后，它会调用本地 Whisper 模型提取语音，并自动扫描对话中的梗、反转、停顿和音频峰值，为你圈出 3 到 5 个自带时间戳和标题的高光候选片段。

选定后，它能自动烧录类似 Opus 风格的逐词字幕（白字黄底的高亮跟随效果），甚至支持通过上传参考图片让系统自动匹配字幕样式。

在将宽屏（16:9）裁切为竖屏（9:16）时，它不跑传统人脸识别模型，而是巧妙利用 ffmpeg 计算画面中说话者嘴部区域的“运动能量”，画面里谁的嘴动得剧烈，镜头就会以硬切换的方式直接追踪谁，或者直接生成上下分屏的双人同框画面。

得益于这种极轻量的面部追踪方案，整个工作流运行极快。在搭载 Apple Silicon 芯片的设备上，处理一段 20 秒的切片仅需约 20 秒。

所有配置就绪后，只需在 Claude Code 内敲入 `/clipify` 斜杠命令即可唤醒执行，成片会自动输出到源目录的特定文件夹中。

![](https://relay-1.bijitongbu.site/p/a9f13db138731b0cdbcb794b91bd85fb.png)

**系统限制**：专为 macOS 设计（底层代码绑定了 VideoToolbox 硬件加速，Linux 或 Windows 用户需手动修改源码移除加速标志）。

**运行要求**：本地需预先安装配置好 Claude Code、FFmpeg（含 libx264）、Whisper (`openai-whisper`) 以及包含 numpy 的 Python 3 环境。

采用 Python (100%) 编写。遵循 MIT 协议开源，获 293 Stars 与 32 Forks。

> 项目地址：https://github.com/louisedesadeleer/clipify

---

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RCgtXod1WxPVQAxJDRfRv5MibBbZ1hPx4w5ZQicVZ93sN7flE9TcqfhFAsergmljD88uFDdg6wia27tiaUNNb5iatGl15g0byvVibGYTuJUE4CiahM/0?wx_fmt=jpeg)

原创 几乎满级 几乎满级

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/b884fd10_1778350099218?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzkwODQzNzk1OQ%3D%3D%26mid%3D2247498150%26idx%3D1%26sn%3D7005a3ba9603430948554c57f2671b24%26chksm%3Dc187b66ad9a3632a2ffbf3ba9998e9f3f67f2c655e73bc61cbf74ea287071fba0fac9ba9860c%26mpshare%3D1%26scene%3D1%26srcid%3D0510REV6sL4tGO0eQIDbo7id%26sharer_shareinfo%3D519cea0a9dbdcde0742ed4479a3d5271%26sharer_shareinfo_first%3D519cea0a9dbdcde0742ed4479a3d5271%23rd&s=obsidian)

## AI 分析

- 评分：8/10
- 可信度：high
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：Claude Code、视频剪辑、自动化、竖屏、Whisper、ffmpeg、开源

### 信息本质

Clipify 是一个 Claude Code 的扩展，利用 Whisper 和 ffmpeg 自动将长视频剪辑为竖屏短视频，适合播客/访谈类内容，支持智能高光提取和字幕生成。

### 可信度判断

来源为微信公众号，但项目开源（MIT 协议），GitHub 有 293 Stars 和 32 Forks，代码可验证。技术方案合理（Whisper + ffmpeg 运动能量追踪），无夸大宣传。可信度高。

### 可利用价值

可大幅提升短视频内容生产效率，尤其适合将播客、访谈等长内容快速转化为抖音/TikTok 竖屏短片，节省手动粗剪时间。

### 可开发方向

可基于此开发自动化短视频生产工作流，集成到 Obsidian 或自动化脚本中；也可扩展支持更多平台（如小红书、视频号）或添加 AI 文案生成功能。

### 可内容化方向

可制作教程类内容：如何用 Claude Code + Clipify 自动化剪辑短视频；或对比评测：Clipify vs 传统剪辑软件效率。

### 下一步

克隆 GitHub 仓库，在 macOS 上安装依赖（Claude Code、FFmpeg、Whisper、Python），用一段播客视频测试 `/clipify` 命令，评估输出质量。

### 风险

仅支持 macOS；依赖本地 Whisper 模型，对硬件有一定要求；运动能量追踪可能不适用于多人同时说话场景；需注意视频版权问题。

### 建议沉淀位置

Projects/AI工具/视频自动化
