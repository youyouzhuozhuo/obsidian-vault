---
author: 小柒的方舟空间
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzIzMjUyMTM0Nw==&mid=2247484884&idx=1&sn=afdbd993ef5a4af9c1d7bdd6f57bd429&chksm=e9794358919a00eb58eeef49a68fb49444fb7962de8800e93697be4958d1a7da7047538086a0&mpshare=1&scene=1&srcid=0526LRVdIeVZBktetU4Azylc&sharer_shareinfo=3f45ece9dbcfc065940783b9b102b358&sharer_shareinfo_first=3f45ece9dbcfc065940783b9b102b358#rd
saved: 2026-05-26 18:51:21
tags:
  - 笔记同步助手
id: d46cce13-47ac-41ad-8fc3-7e2f72890800
---

公众号名称：云界方舟

作者名称：小柒的方舟空间

发布时间：2026-05-26 18:09

你是不是也这样过：

打开 Claude Code 或 Cursor 写代码，跑几条 `git diff`、`cargo test`、`ls`，终端哗啦啦输出几百上千行——**Token 跟不要钱似的疯狂烧**，配额说没就没 账单蹭蹭涨，更气人的是 AI 被一堆垃圾信息搞得理解跑偏……

别怕，今天给你安利一个 **GitHub 上已经狂揽 46k+ Star** 的神器——**RTK（Rust Token Killer）**。我自己亲测 AI 编程成本 **直接降了将近九成**，装上就无感运行，开发者真的可以人手一个。

![[笔记同步助手/images/3470a46b17b1dc17b9ea855a6dd3f693_MD5.png]]

---

## 🔥 RTK 到底是啥？

一句话给你说明白：**它就像一个智能「门卫」**，蹲在你的终端命令和 AI 之间，专门把那些对 AI 毫无卵用的冗余输出干掉，只留核心干货。

不碰你代码，不改你习惯，全程 **后台默默过滤**，脏输出变干净，长文本压到极短——**从源头帮你省 Token**，爽不爽？

​

---

## 📉 官方实测：30 分钟会话省了 89% Token

RTK 官方做了一组 **30 分钟真实 Claude Code 会话**测试，数据真的夸张：

-   原始输出 ≈ **118,000 Token**
    
-   RTK 优化后 ≈ **23,900 Token**
    
-   **整体节省 80%+**
    
-   有老哥长期用下来，**实际省了 88.9%**
    

单场景更离谱：`cargo test` 输出从 **25,000 Token → 2,500 Token**，**直接省 90%**！

这意味着：

-   ✅ Claude Code Max 配额能多撑好久
    
-   ✅ API 账单砍半甚至打骨折
    
-   ✅ AI 只看关键信息，理解更准、响应更快
    
-   ✅ 上下文窗口不再被垃圾占满，超长会话也不崩
    

![[笔记同步助手/images/5bb0b118d074bf069375046768c4521b_MD5.png]]

---

## 🧹 RTK 到底过滤了个啥？

它不是简单粗暴删文字，而是 **四层精准优化**，只留 AI 真正需要的东西：

1.  **噪音过滤** — 干掉终端里的颜色码、进度条、空白行、无聊 Banner、刷屏的调试日志、警告瀑布等等。
    
2.  **去重 + 压缩** — 重复日志自动合并，相同内容只留一次，结构精简，但关键结果不丢。
    
3.  **智能截断** — 超长输出按重要性截取，只保留最核心的部分，控制 Token 上限。
    
4.  **结构化输出** — 把杂乱的命令输出整理成清爽摘要：
    

-   `git diff` → 只告诉你哪些文件改了多少行
    
-   `cargo test` → 直接一句话：通过/失败/忽略/耗时
    
-   `ls -lah` → 精简目录结构，没用的信息全扔掉
    

---

## ✨ 为什么大家都爱用它？

-   **Rust 原生二进制，快得一匹** — 单命令开销 <10ms，几乎感觉不到存在
    
-   **零依赖、超轻量** — 不用装 Rust 环境、不用配这配那，下载就能用
    
-   **一行安装，全局生效** — 装完该咋用还咋用，完全无感
    
-   **兼容一堆 AI 工具** — Claude Code、Cursor、Gemini CLI、Codex 全都安排得明明白白
    
-   **开源免费** — MIT 协议，随便用、随便魔改
    

![[笔记同步助手/images/50ceb6d979301062d2f5b02b4d67910b_MD5.png]]

---

## 🚀 1 分钟上手，真的就是 1 分钟

### 1\. 安装 RTK

下载对应系统的二进制文件，或者一行命令搞定：

```
# 通用一键安装（官方推荐）
curl -fsSL https://rtk.ai/install | sh
```

### 2\. 一键初始化（以 Claude Code 为例）

```
rtk init -g
```

### 3\. 重启 AI 工具，立刻生效

重启 Claude Code / Cursor 就行，之后所有命令都会被 RTK 自动优化。

其他 AI 工具也简单：

```
rtk init -g --agent cursor   # Cursor
rtk init -g --gemini         # Gemini CLI
rtk init -g --codex          # Codex
```

### 4\. 看看你到底省了多少 Token

```
rtk gain
```

实时查看节省统计，看着数字往下掉，爽就完了！

​

---

## 💡 最后唠两句

AI 编程越来越爽，但 **Token 就是白花花的银子**。大量终端输出里，**80% 以上都是对 AI 没用的噪音**——既烧钱，又拖累模型理解。

**RTK** 用最简单粗暴的方式，**把每一个 Token 都花在刀刃上**。实测稳定省 80%–90%，如果你是重度 Claude、Cursor 用户，那这玩意儿简直是 **省钱 + 提效双丰收**。

开源免费，用就完了。赶紧去装一个，让你的 AI 编程成本 **直接打一折**！

​

---

### 项目地址

```
GitHub：github.com/rtk-ai/rtk
```

---

![[笔记同步助手/images/d828f63f55c969c2daaee806e6feea58_MD5.jpg|cover_image]]

Original 小柒的方舟空间 云界方舟

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/1601df20_1779792679537?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIzMjUyMTM0Nw%3D%3D%26mid%3D2247484884%26idx%3D1%26sn%3Dafdbd993ef5a4af9c1d7bdd6f57bd429%26chksm%3De9794358919a00eb58eeef49a68fb49444fb7962de8800e93697be4958d1a7da7047538086a0%26mpshare%3D1%26scene%3D1%26srcid%3D0526LRVdIeVZBktetU4Azylc%26sharer_shareinfo%3D3f45ece9dbcfc065940783b9b102b358%26sharer_shareinfo_first%3D3f45ece9dbcfc065940783b9b102b358%23rd&s=obsidian)