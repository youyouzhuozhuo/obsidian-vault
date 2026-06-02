---
author: 几乎满级
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkwODQzNzk1OQ==&mid=2247498150&idx=1&sn=7005a3ba9603430948554c57f2671b24&chksm=c187b66ad9a3632a2ffbf3ba9998e9f3f67f2c655e73bc61cbf74ea287071fba0fac9ba9860c&mpshare=1&scene=1&srcid=0510REV6sL4tGO0eQIDbo7id&sharer_shareinfo=519cea0a9dbdcde0742ed4479a3d5271&sharer_shareinfo_first=519cea0a9dbdcde0742ed4479a3d5271#rd
saved: 2026-05-10 02:08:20
tags:
  - 笔记同步助手
id: 86926dbe-af3a-4766-b22d-d520f68b24d9
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