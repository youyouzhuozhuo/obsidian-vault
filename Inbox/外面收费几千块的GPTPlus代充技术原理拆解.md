---
title: "外面收费几千块的GPTPlus代充技术原理拆解"
date: 2026-05-22 15:48:26
source: "微信公众号"
author: "佚名"
url: "https://mp.weixin.qq.com/s?__biz=MzkzNjYyNzg4Mw==&mid=2247485181&idx=1&sn=5dc633f80c3aa1d1086c2992fd1a5f2e&chksm=c3ad2e939d7d34175f868b2e2fc7d72612e244a87a66b62e4c55eb4503e1c500a15cf2f34d2c&mpshare=1&scene=1&srcid=0522G64gcU2cvuACUygaSf2j&sharer_shareinfo=d8d46055ed454a1c75c5041cc9e58207&sharer_shareinfo_first=d8d46055ed454a1c75c5041cc9e58207#rd"
tags:
  - AI/工具
  - 编程/后端
  - 编程/API
---

本文仅供技术交流。任何实际操作产生的账号封禁、法律风险，自行承担。

外面那些收费几千教人“GPT 代充技术”的，教的就是这几步。

​

## 漏洞原理

[[OpenAI]] 不查 [[Apple ID]] 对应关系，拿张收据就能给任意号开会员。

正常流程是这么走的：  
你 iPhone 上点付款 → [[App Store]] 扣钱 → Apple 把收据扔到你手机本地 → [[ChatGPT]] App 捡起收据 → App 把收据和你当前登录的账号 token 一起打包发给 OpenAI → OpenAI 验一下收据真假 → 给你账号开 [[Plus]]。

挺严谨对吧？屁。

漏洞就藏在 OpenAI 验票那一步。OpenAI 验票的时候，根本不看这张收据是你 Apple ID 买的，还是隔壁老王 Apple ID 买的。它只看两样东西： **收据合法不合法，以及你传过来的那个 ChatGPT auth token 是不是活的** 。  
`收据合法 + token 有效 = 任意账号变 Plus` 。

什么 Apple ID 绑定、什么账号对应关系，全不查。这就好比你拿着别人的购物小票去柜台领东西，柜员只看小票真假，不看你身份证。

三端订阅管理都是交给第三方 API 处理的，iOS 系统框架允许 App 把内购凭据往第三方服务器发，这本是正常开发逻辑。但 OpenAI 在这条链路上偷了懒——或者说，压根没想过有人会卡这个环节。

​

## 完整代充流程

既然漏洞摆在这儿，流程就简单了。

​

### 第一步：搞一个土耳其区 Apple ID

土耳其区 Plus 标价 499 里拉一个月，折人民币大概八十五块。国内定价多少？一百四五。差价自己算。  
往这个土区 Apple ID 里充好礼品卡，钱备足。

​

### 第二步：拦截收据

在你 iPhone 上打开 ChatGPT App，别登录你想开 Plus 的目标账号，随便登个临时号或者干脆不登。  
内购付款之前，配置网络拦截——核心操作就是阻止 ChatGPT App 把收据发给 OpenAI 服务器。  
App Store 那边照常扣钱，Apple 照常把收据扔到你手机本地沙盒目录里。但因为你的拦截，这张收据没自动飞向 OpenAI，而是老老实实待在本地等你来拿。

​

### 第三步：导出收据

导出收据通常需越狱设备或利用系统漏洞。实际主流玩法有三种：

方法 A，端点本地映射。用 [[DNS劫持]] 或本地代理，把 ChatGPT App 发往 OpenAI 的请求重定向到你自己的本地服务器。请求里本来就带着 [[Base64]] 编码的收据，到了你本地，直接保存下来。工具就那些：[[mitmproxy]]、[[Charles Proxy]]、自建 [[HTTPS]] 代理加一张自签证书。不用越狱，门槛低得令人发指。

方法 B，越狱加 Hook。越狱设备上用 [[Frida]] 或者 Flex，直接 hook [[StoreKit]] 框架，截下 [[SKPaymentTransaction]] 的 transactionReceipt，或者读 appStoreReceiptURL 拿收据文件。粗暴直接。

方法 C，安卓路径用 [[Xposed]] Hook，逻辑类似。

​

### 第四步：API 补单

收据到手，直接往 OpenAI 的订阅接口发请求：

```
POST https://chat.openai.com/backend-api/subscription/upgrade
Content-Type: application/json
