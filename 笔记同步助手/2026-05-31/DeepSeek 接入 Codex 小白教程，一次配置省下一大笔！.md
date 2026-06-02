---
author: 锦鲤Sage
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkwNDMyMTk0OA==&mid=2247516038&idx=1&sn=d2bc9930616fdf7d8ac4b269204ceb9f&chksm=c1d15cd6e147382f7eac46852c682cc8c7a90255aa0318a7e6cd66752845e1c08ccdbf71795d&mpshare=1&scene=1&srcid=0531JxTeDECyeokb0ZmrMNZM&sharer_shareinfo=f6c6e5d5f8337f5271c9e83aa9f54822&sharer_shareinfo_first=f6c6e5d5f8337f5271c9e83aa9f54822#rd
saved: 2026-05-31 15:58:08
tags:
  - 笔记同步助手
id: 1ad66a02-ac7d-48b1-af70-3eb26ee44560
ai_score: 7
credibility: "medium"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
公众号名称：锦技社

作者名称：锦鲤Sage

发布时间：2026-05-31 08:00

很多人用 Codex 做代码生成、项目分析和开发辅助，但默认模型的使用成本和可用性并不总是最理想。

如果你想把 DeepSeek 接入 Codex，让 Codex 调用国产大模型来完成代码问答、项目理解、插件调用等任务，可以借助 CC Switch 来实现。

这篇教程会从零开始讲清楚完整配置流程。按照下面步骤操作，基本可以一次跑通。

## 一、先准备这 3 样东西

开始之前，先确认你已经准备好：

### 1\. CC Switch

建议使用最新版 CC Switch，避免因为旧版本导致路由、模型配置或 Codex 支持不完整。

官网下载地址：https://ccswitch.io/zh

![[笔记同步助手/images/df53fbad59fa95886808eeb1c930a065_MD5.png]]

  

### 2\. Codex

本教程的目标是让 Codex 可以调用 DeepSeek 模型，所以本地需要已经安装并能正常打开 Codex。

可以查看我的往期文章安装一下codex。

[Codex 小白入门篇：Windows 和 Mac 都能上手](https://mp.weixin.qq.com/s?__biz=MzkwNDMyMTk0OA==&mid=2247515962&idx=1&sn=b39a60181cd72e1d369b6d83e34eacaf&scene=21#wechat_redirect)

### 3\. DeepSeek API Key

进入 DeepSeek 开放平台，创建并复制自己的 API Key。后面配置供应商时会用到。

DeepSeek 开放平台地址：https://platform.deepseek.com

![[笔记同步助手/images/b58fddc4812229648e5e935d5a7992f6_MD5.png]]

  

## 二、打开 CC Switch，进入 Codex 配置

打开 CC Switch。

在主界面中找到 Codex 相关入口，点击进入 Codex 配置页面。

![[笔记同步助手/images/2c0d57495cf34a30078fdedfbd860206_MD5.png]]

这里的作用是告诉 CC Switch：

接下来 Codex 的模型请求，不再只走默认模型，而是可以通过 CC Switch 转发到你配置好的 DeepSeek 模型。

## 三、添加 DeepSeek 供应商

进入 Codex 配置后，点击添加供应商。

在供应商列表中选择：

DeepSeek

然后进入 DeepSeek 的配置页面。

![[笔记同步助手/images/b02bf544e733ee9aa17ab58f3d4604bb_MD5.png]]

这里主要填写以下内容：

-   • 供应商名称：DeepSeek
    
-   • API Key：粘贴你在 DeepSeek 开放平台申请到的 Key
    
-   • API 地址：如果系统自动填充，一般保持默认即可
    
-   • 模型：添加你要在 Codex 中使用的 DeepSeek 模型
    

API Key 一定要填写正确。复制时不要多复制空格，也不要漏掉前后字符。

![[笔记同步助手/images/4171ce289e2d7be03adc1d8b43036c2e_MD5.png]]

![[笔记同步助手/images/b793dd501160146f1bb354fa77a06d9f_MD5.png]]

## 四、添加 DeepSeek 模型

只配置供应商还不够，还需要把具体模型添加进去。

可以根据自己的使用需求添加模型，例如：

### DeepSeek V4 Flash

适合日常代码问答、快速响应、低成本使用。

### DeepSeek V4 Pro

适合更复杂的项目分析、代码重构、长上下文任务。

添加模型时，需要填写模型名称和对应模型 ID。

配置完成后，点击添加或保存。

这里要注意：

如果只填了 API Key，但没有添加具体模型，后面在 Codex 里可能看不到可选的 DeepSeek 模型。

## 五、开启 CC Switch 本地路由

模型添加完成后，还需要开启路由。

回到 CC Switch 主界面，点击右上角或侧边栏里的设置图标。

![[笔记同步助手/images/57d54db9eecaf01b57d7ec7cad9a259b_MD5.png]]

进入设置后，找到路由相关选项。

![[笔记同步助手/images/50ce187ba99c3a10e7f585354d28f09d_MD5.png]]

依次打开：

-   • 启用路由
    
-   • 显示本地路由开关
    
-   • Codex 路由开关
    

这一步非常关键。

![[笔记同步助手/images/06c636c097378bad8f0c6612e5d53872_MD5.png]]

因为 CC Switch 的作用，本质上就是在本地做一层模型请求转发。

如果路由没有开启，即使 DeepSeek 模型已经配置好了，Codex 也可能不会走你刚才添加的模型。

尤其要确认：

Codex 的路由开关必须打开。

## 六、回到 Codex 选择 DeepSeek 模型

配置完成后，打开 Codex。

进入模型选择区域，正常情况下你应该可以看到刚刚添加的 DeepSeek 模型，例如：

-   • DeepSeek V4 Flash
    
-   • DeepSeek V4 Pro
    

选择其中一个模型，然后输入一个简单问题测试，比如：

> 请帮我分析这个项目的目录结构。

或者：

> 请帮我写一个 Python 请求接口的示例。

如果 Codex 能够正常回复，说明 DeepSeek 已经成功接入 Codex。

我这里随便测试了一下，速度还是非常快的。

![[笔记同步助手/images/74107f1108f6f509470279e281bad839_MD5.png]]

  

## 七、测试插件功能

想要在使用第三方API的时候使用官方插件和远程控制功能，需要先切换到官方供应商然后再登录一下，目的是获取access token，free账号就可以，之后就可以随便切换第三方了！  

当然你也可以用我之前推荐的Codex++来启动插件功能，安装教程如下：

[Codex++：把 Codex 变得更顺手的外部增强器](https://mp.weixin.qq.com/s?__biz=MzkwNDMyMTk0OA==&mid=2247516019&idx=1&sn=f57834915dd7d06d0641804942d8a723&scene=21#wechat_redirect)

如果你需要在 Codex 中使用插件，也可以继续测试插件能力。

进入 Codex 插件页面，搜索你需要的插件，点击安装。

安装完成后，回到聊天窗口测试插件是否可以正常调用。

如果插件能够正常安装，并且聊天时模型也可以正常响应，说明 CC Switch 的路由配置和 DeepSeek 模型调用都已经跑通。

## 八、常见问题

### 1\. Codex 里看不到 DeepSeek 模型怎么办？

优先检查这几个地方：

-   • DeepSeek 供应商是否添加成功。
    
-   • API Key 是否填写正确。
    
-   • 模型是否已经添加到供应商配置里。
    
-   • CC Switch 路由是否开启。
    
-   • Codex 路由开关是否打开。
    

大多数情况下，看不到模型都是因为没有添加具体模型，或者 Codex 路由没有开启。

### 2\. Codex 不能正常回复怎么办？

可以按下面顺序排查：

-   • 先确认 DeepSeek API Key 是否有效。
    
-   • 再确认账户余额或额度是否正常。
    
-   • 然后检查模型 ID 是否填写正确。
    
-   • 最后检查 CC Switch 本地路由是否开启。
    

如果 API Key 错误，或者模型 ID 和平台实际名称不一致，都可能导致请求失败。

### 3\. API 地址要不要手动改？

如果你选择的是 CC Switch 内置的 DeepSeek 供应商，一般不需要手动修改 API 地址。

如果你使用的是 OpenAI 兼容接口，或者第三方中转服务，则需要确认 Base URL 是否填写正确。

### 4\. Flash 和 Pro 应该选哪个？

日常写代码、解释代码、生成小工具，优先用 Flash，速度快，成本更低。

复杂项目分析、架构设计、长文档理解、代码重构，可以用 Pro，效果通常更稳。

## 九、完整流程总结

将 DeepSeek 接入 Codex，核心流程就是：

1.  1\. 安装并打开 CC Switch
    
2.  2\. 进入 Codex 配置
    
3.  3\. 添加 DeepSeek 供应商
    
4.  4\. 填写 DeepSeek API Key
    
5.  5\. 添加 DeepSeek 模型
    
6.  6\. 开启 CC Switch 本地路由
    
7.  7\. 打开 Codex 路由开关
    
8.  8\. 回到 Codex 选择 DeepSeek 模型测试
    

配置完成后，Codex 就可以通过 CC Switch 调用 DeepSeek 模型了。

这样既能继续使用 Codex 的开发体验，又能接入国产大模型，降低使用成本，提升模型选择自由度。

对于经常使用 AI 辅助编程的人来说，这套配置非常值得安排。

最后是一位大佬分享的细节：

![[笔记同步助手/images/445e3589678bd579142da6d93cac2fc2_MD5.png]]

好了，本期的分享就到这里，我们下期再见，如果你想接入更多低价高级大模型可以加入下方群聊获取～

点击名片关注我，更多ai相关教程持续分享中

---

往期精彩：

[Codex++：把 Codex 变得更顺手的外部增强器](https://mp.weixin.qq.com/s?__biz=MzkwNDMyMTk0OA==&mid=2247516019&idx=1&sn=f57834915dd7d06d0641804942d8a723&scene=21#wechat_redirect)

[Claude Opus 4.8 来了：别问强不强，先问你配不配用](https://mp.weixin.qq.com/s?__biz=MzkwNDMyMTk0OA==&mid=2247515998&idx=1&sn=3e04253e0bc77d7d0bd56605f258970d&scene=21#wechat_redirect)

[飞书 CLI：让 Codex 真正接上你的协作系统](https://mp.weixin.qq.com/s?__biz=MzkwNDMyMTk0OA==&mid=2247515993&idx=1&sn=6e57fc773f39f4050e5c9ac67e92063c&scene=21#wechat_redirect)

[DeepSeek之后，小米也掀桌了](https://mp.weixin.qq.com/s?__biz=MzkwNDMyMTk0OA==&mid=2247515976&idx=1&sn=aef3d63f00e4d1adea7881e82e6d7117&scene=21#wechat_redirect)

[Codex 小白入门篇：Windows 和 Mac 都能上手](https://mp.weixin.qq.com/s?__biz=MzkwNDMyMTk0OA==&mid=2247515962&idx=1&sn=b39a60181cd72e1d369b6d83e34eacaf&scene=21#wechat_redirect)

更多AI前沿资讯、AI提示词库、AI深度教程、开源工具精选、AI搞钱灵感、AI工具与福利分享欢迎加入下方飞书群聊交流👇

![[笔记同步助手/images/b4e8c8285d6051ec5e73f2493ee7cc2a_MD5.png]]

---

![[笔记同步助手/images/8fd3d8259cc763b09521880e8b2dcc1c_MD5.jpg|cover_image]]

Original 锦鲤Sage 锦技社

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/c46c1f19_1780214286248?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzkwNDMyMTk0OA%3D%3D%26mid%3D2247516038%26idx%3D1%26sn%3Dd2bc9930616fdf7d8ac4b269204ceb9f%26chksm%3Dc1d15cd6e147382f7eac46852c682cc8c7a90255aa0318a7e6cd66752845e1c08ccdbf71795d%26mpshare%3D1%26scene%3D1%26srcid%3D0531JxTeDECyeokb0ZmrMNZM%26sharer_shareinfo%3Df6c6e5d5f8337f5271c9e83aa9f54822%26sharer_shareinfo_first%3Df6c6e5d5f8337f5271c9e83aa9f54822%23rd&s=obsidian)

## AI 分析

- 评分：7/10
- 可信度：medium
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：Codex、DeepSeek、CC Switch、AI编程、模型接入、成本优化

### 信息本质

通过 CC Switch 将 DeepSeek 模型接入 Codex，实现低成本、高灵活性的 AI 编程辅助。

### 可信度判断

来源为公众号教程，步骤详细，但未提供官方验证或用户反馈。CC Switch 和 DeepSeek API 均为真实产品，配置逻辑合理。需自行测试确认兼容性。

### 可利用价值

可降低 Codex 使用成本，利用 DeepSeek 的性价比优势，适合日常编程辅助和项目分析。

### 可开发方向

可编写自动化配置脚本，或制作一键部署工具；也可探索其他国产模型（如通义千问）的类似接入方案。

### 可内容化方向

可制作视频教程、对比评测（DeepSeek vs 默认模型）、成本分析文章，或分享配置踩坑经验。

### 下一步

下载 CC Switch 并获取 DeepSeek API Key，按教程配置后测试一个简单代码生成任务。

### 风险

依赖第三方工具 CC Switch，可能存在更新不及时或安全风险；DeepSeek API 稳定性需关注；配置不当可能导致 Key 泄露。

### 建议沉淀位置

Projects/AI工具/Codex配置
