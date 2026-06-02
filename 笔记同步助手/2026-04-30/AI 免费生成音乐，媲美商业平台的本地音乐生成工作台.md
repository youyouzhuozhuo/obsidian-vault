---
author: 几乎满级
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkwODQzNzk1OQ==&mid=2247497942&idx=1&sn=4ffcb51447710a2e8df01e98a8731843&chksm=c18cce4f43f9b5d9a7c871023694a206f537bb6b0320989142ecd593edf5d10b138905328f67&mpshare=1&scene=1&srcid=0430RdOAUBZRt1wkvE3wG4Oc&sharer_shareinfo=1fdd1c94b44eab4c8217279c63382d73&sharer_shareinfo_first=1fdd1c94b44eab4c8217279c63382d73#rd
saved: 2026-04-30 17:10:20
tags:
  - 笔记同步助手
id: 5d6902da-04df-4421-ac46-9a7203024ab2
---

公众号名称：几乎满级

作者名称：几乎满级

发布时间：2026-04-30 17:00

**ACE-Step UI** 专为开源 AI 音乐生成模型 **ACE-Step 1.5** 量身打造的专业级图形操作界面。

定位是：成为 **Suno** 和 **Udio** 等付费（每月 10-50 美元订阅费）在线音乐服务的“开源替代品”。

让用户能够在自己的电脑上免费、无限制地创作具有专业水准的 AI 音乐，并完全拥有所生成音乐的版权。

![[笔记同步助手/images/15b1610cc04629c8728d740c7e514bf9_MD5.jpg||3]]

系统支持生成长达 4 分钟以上带人声和歌词的完整歌曲，或是纯器乐曲目。

在参数面板中，你可以将生成时长精准锁定在 30-240 秒之间，并强制指定 60-200 的 BPM 与调性。

如果你对生成的某段旋律不满意，可以通过局部重绘（Repainting）单独修改该片段，或者利用音频翻唱（Audio Cover）为现有的参考音频套上全新的流派外衣。

为了降低小白写提示词的门槛，它内置了“AI 增强”与“思考模式”。前者能把简单的词汇（如 pop, rock）自动扩写并匹配合适的节拍；后者则直接调用大语言模型来推敲歌曲的宏观结构。

采用类似 Spotify 风格的播放界面，另外，它还缝合了基于 AudioMass 的音频剪辑器、基于 Demucs 的音轨分离工具（一键提取人声或鼓点），甚至包含一个配合 Pexels 素材的视频（MV）生成器。

项目前后端采用了 React 18、TypeScript、Vite、Express.js 与 SQLite，通过 Gradio API 与底层的 ACE-Step 1.5 引擎交互。目前基于 MIT 协议开源，在 GitHub 社区已获得超过 2100 颗 Star 和 300 多次 Fork。

硬件门槛：由于整合了大语言模型，想完整跑通“思考模式”推荐使用 12GB+ 显存的 NVIDIA 显卡；若关闭 LLM，仅需 4GB 显存即可运行基础生成。本机环境需依赖 Node.js 18+、Python 3.10+ 和 FFmpeg。官方强烈推荐使用 Pinokio 进行一键安装，或直接下载内置了 CUDA 12.8 且免配置的 Windows 便携包。

> 项目地址：https://github.com/fspecii/ace-step-ui

---

![[笔记同步助手/images/11bca9a3a7639c32aeeb10966a013228_MD5.jpg|cover_image]]

原创 几乎满级 几乎满级