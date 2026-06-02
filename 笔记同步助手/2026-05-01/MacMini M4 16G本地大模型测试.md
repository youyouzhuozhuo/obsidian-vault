---
author: 神骏
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzI5NjUwNjA2Nw==&mid=2247484211&idx=1&sn=98aa1effaa35bddca062dc21c1660b88&chksm=ed94b97e3b4c18b34b4ec7cd8d4f904c1ff38e4fb4dbcaab14fcfab6344d103301cf7fda5d27&mpshare=1&scene=1&srcid=0501SXvzKp9SbRdLTBjNyStu&sharer_shareinfo=38178f7878d382526258ecc22ac49997&sharer_shareinfo_first=38178f7878d382526258ecc22ac49997#rd
saved: 2026-05-01 21:26:51
tags:
  - 笔记同步助手
id: 36c40fd5-0b49-407a-ad6c-10671c931859
---

公众号名称：神骏的生信

作者名称：神骏

发布时间：2026-04-10 13:05

## 手头有一台MacMini M4 16G 256G机器，尝试部署本地大模型测试，为免费token策略做准备，以支持生信软件开发。

模型选择。根据前期调研，16G显存可以运行的模型为Qwen3.5-9B-4bit量化级别。注意，苹果统一内存架构，需要为系统、KV缓存等流出空间。

框架。选择oMLX这个专门为苹果芯片优化的框架。

AI助手。尝试了以下编辑器。

-   TRAE。不支持接入自定义模型，放弃。
    
-   code buddy。可接入本地模型，偶尔出现bug。agent助手模式，工具调用总是失败。没法查看上下文大小，放弃。
    
-   open code desktop。支持接入本地模型，可查看上下文大小。
    
-   claude code desktop。需要联网登录账号（梯子），放弃。
    

项目。使用前几天开发的`sports-data-dashboard`项目，主要测试本地模型的理解情况。

上下文大小。模型上下文窗口大小很重要，但是目前我对具体大小没有概念。一直在白嫖大厂的云端模型，例如TRAE的200k上下文窗口大小，日常使用没遇到过溢出情况。Macmini M4上部署的Qwen3.5-9B 4bit量化模型，上下文窗口默认32k，可调整到64k，但是调整128k时会爆内存。64k上下文是16G MacMini M4上的一个相对靠谱设置。

64k上下文大小测试。使用`sports-data-dashboard`项目 v0.1.0代码测试。

-   让AI自动读取`sports-data-dashboard/docs`下的项目文档，程序自动选择了`PRD.md, design.md, spec.md`，输出简要总结，上下文占用35k。再继续读`task.md, checklist.md`，上下文溢出。
    
-   阅读`data-manager`的代码，程序读完所有数据管理文件，简单总结，上下文占用22k。
    
-   让程序阅读`docs/spec.md`文档，输出简单总结，上下文占用22k。
    
-   让直接根据要求修改前端（未阅读项目背景），实现单次修改，上下文25k。修改的效果有问题，不确定是模型参数导致还是未理解项目背景导致。要求执行第二次修改，上下文溢出。
    
-   让程序阅读`frontend`下所有文件，上下文直接溢出。
    

直观对比。使用云端模型时，让模型一次读取`PRD.md, spec.md, task.md, checklist.md, design.md`等诸多文件了解项目背景，200k上下文占用大概20-30%。继续提要求修改前端代码等，同一个会话中可以执行2-3次修改，丝毫不受上下文溢出影响。

根据这里讨论的上下文，实用策略如下：

-   小上下文（4k-16k）。适合简单聊天机器人、文本分类、短内容生成、单轮问答。
    
-   中等上下文（32k-128k）。适合单文档问答、单文件代码审查、多轮对话、文摘摘要。
    
-   大上下文（200k-1M）。适合整个代码库分析、多文档推理、长篇论文分析、法律合同审查、书籍内容处理。
    

根据runthisllm网站测试，Qwen3.5-9B模型，Q4\_K\_M量化，KV Cache精度为Q4，256k上下文，推荐的机器为Arc A770 16GB。

综上：Macmini M4 16G机器，Qwen3.5-9B-4bit模型，可以用64k上下文运行，token生成速度为13-15 t/s，日常可用。注意，此处使用oMLX框架，KV Cache精度未知。

PS：使用腾讯云Cloud Studio的T4（16G）机器部署了同样的模型，可以将上下文提高到128k，显存占用13G。但提高到256k时，出现CPU卸载的情况。未调整KV Cache精度。

  

---

![[笔记同步助手/images/d7c97d8cc9f24c8f6a7c9a3bfa01319e_MD5.jpg|cover_image]]

Original 神骏 神骏的生信