---
author: 元帅
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzY5MjI5MDU0NQ==&mid=2247483656&idx=1&sn=31f4818e99a87fc3a2b1b56233d33b0a&chksm=f5621cc4be42332ba74af66326bf1eade07dffa046d6a02606f867c4b06a22dbf23139b50eb0&mpshare=1&scene=1&srcid=0531c1gRgTaj7sBurL69QLsH&sharer_shareinfo=3548a85684e750cfc728e85eb509e4cd&sharer_shareinfo_first=3548a85684e750cfc728e85eb509e4cd#rd
saved: 2026-05-31 23:16:36
tags:
  - 笔记同步助手
id: 357d06b7-4e6e-4ca9-9504-f5c93b488092
ai_score: 8
credibility: "high"
usefulness: "high"
actionable: true
opportunity_type: "工具"
analysis_status: "done"
---
公众号名称：清野呼吸

作者名称：元帅

发布时间：2026-05-20 09:56

> **把 Codex 的 GPT 换成 DeepSeek，账单从上千降到几十块。**  
> **所有步骤都踩过坑了，你照着做就行。**

---

## 一、被账单逼疯之后

前两天查 API 账单，愣住了。

Codex 一个月跑了一千多块。用的是默认的 GPT-5.5，输入 $15/百万 token，输出 $60/百万 token。听起来好像还行？但你一天十几个会话，每个来回几十轮，这个数字就像坐了火箭一样往上蹿。

> 我问自己：**能不能换个模型？**

DeepSeek V4 Pro，打完折 **$0.44/$0.87**。

不到 GPT 的 **3%**。

三十多倍的价差。换谁都会心动。

---

## 二、折腾了一圈

理想很丰满，现实很骨感。

Codex CLI 用的是 OpenAI 的 **Responses API**（新协议），而 DeepSeek 走的是 **Chat Completions API**（旧协议）。两个不兼容，改个配置文件是连不上的。

我试了好几个方案：

**方案一：手写翻译代理。** 轻量是轻量，但流式处理全是坑。跑着跑着就断了，Codex 那边直接报错。折腾两天，放弃。

**方案二：CCX + CC-Switch。** 有个管理界面挺唬人，研究半天发现 CCX 根本不翻译协议，只是透传。连不上的还是连不上。

说实话，挺沮丧的。

明知道有个好东西，又便宜又好用，就差那么一口气，怎么都接不上。

---

## 三、Moon Bridge

直到在 GitHub 上闲逛，看到了一个项目：**Moon Bridge**。

名字起得好。月亮桥，连接两个世界的桥。

它的思路特别简单——你在本地跑一个服务，对外暴露 OpenAI 的 **Responses API**，收到请求后自动转换成 **Chat Completions 协议**，然后转发给 DeepSeek：

![[笔记同步助手/images/b9e7fb48af2b5f5ab41ddc492cd6757c_MD5.png]]

全部自动完成，中间经过了一个翻译层，但你完全感觉不到。

> 一把跑通。没有报错，没有兼容性问题，流式输出丝滑流畅。

我当时就像找到了一把找了很久的钥匙，突然发现它就在口袋里。

---

## 四、账单降到 3%

重度用了两天，稳得一批。没有任何断连，没有异常，体验跟 GPT-5.5 几乎一模一样。

区别在哪？**在账单上。**

同样的使用量，GPT 上千块，DeepSeek 几十块。三十多倍的差距。

> 我不是说 OpenAI 不好。GPT-5.5 在深度推理、大规模重构上确实更强。但日常编程、写功能、修 bug、做测试、搞重构，DeepSeek V4 Pro 完全够用，体验甚至可以说很好。

那我为什么要多花三十倍的冤枉钱呢？

---

## 🛠️ 操作指南：手把手教你配置

下面每一步都验证过，照着做就行。

### 准备工作

-   **Go 1.25+**
    
    （下载地址）
    
-   **DeepSeek API Key**
    
    （deepseek.com 注册获取）
    

### 第一步：克隆并配置 Moon Bridge

```
git clone https://github.com/ZhiYi-R/moon-bridge.git
cd moon-bridge
cp config.example.yml config.yml
```

编辑 `config.yml`，填入你的 DeepSeek Key：

![[笔记同步助手/images/799dd6ac96a72ae166ac109df193017b_MD5.png]]

> ⚠️ **踩坑提醒：**`api_key` 必须填真实的 Key，填占位符会报 401。我在这卡了半天。

### 第二步：启动 Moon Bridge

```
go run ./cmd/moonbridge -config config.yml
```

看到这行输出就是跑起来了：

```
Transform server listening on127.0.0.1:38440
```

### 第三步：验证服务

另开一个终端，用 curl 测试：

```
curl -X POST http://127.0.0.1:38440/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek/deepseek-v4-pro",
    "input": "Hello"
  }'
```

有返回内容就通了。

### 第四步：配置 Codex CLI

编辑 Codex 的配置文件，添加 Moon Bridge 作为 OpenAI 端点：

```
[openai]
base_url = "http://127.0.0.1:38440/v1"
api_key = "any-value"
```

也可以直接用命令行验证：

```
codex --model deepseek/deepseek-v4-pro --api-url http://127.0.0.1:38440/v1
```

### 第五步：切换模型

进入 Codex 后按 **`/model`** 选择 `deepseek/deepseek-v4-pro` 即可。

**推荐方案：**

| 场景 | 推荐模型 | 理由 |
| --- | --- | --- |
| 主力开发、重活 | DeepSeek V4 Pro | 能力强 + 价格低 |
| 打草稿、日常问答 | DeepSeek V4 Flash | 更快更便宜 |

### 故障排查

| 问题 | 原因 | 解决 |
| --- | --- | --- |
| 启动报 401 | API Key 无效 | 检查 `config.yml` 里的 Key |
| Codex 连不上 | Moon Bridge 没启动 | 先跑 curl 确认服务正常 |
| 返回异常 | 协议/版本不匹配 | `git pull`更新到最新版 |
| 流式卡顿 | 网络延迟 | 检查本地到 DeepSeek 的连通性 |

---

## 🤖 懒人方案：一句话搞定

嫌手动配太麻烦？可以用自动化工具代劳。它们会自动完成上面所有步骤：

| 工具 | 一句话就行 |
| --- | --- |
| **OpenClaw** | _「帮我用 Moon Bridge 把 DeepSeek 接入 Codex CLI」_ |
| **Hermes** | _「用 Moon Bridge 做桥接，让 Codex 用上 DeepSeek V4」_ |

这些工具本质是在本地跑一个 Agent，自动完成：**安装 Go → 克隆 Moon Bridge → 配置 Key → 启动服务 → 配置 Codex** 的全流程。

> 💡 **手动 vs 自动：** 手动配一遍能理解整个链路，出问题知道怎么排查；自动工具省时省力，开箱即用。按自己偏好选就行。

---

## 五、写在最后

我有时候觉得，这个行业最大的问题不是技术不够好，而是 **信息差太大**。

很多人不知道还有别的选择，以为用 OpenAI 就得一直用下去。一个月花着上千块的 API 费用，却不知道有替代方案，只要几十块。

> 我一直做的，说到底就是四个字：**磨平信息差。**

如果这篇文章让你试了这个方案，省下了这笔钱，那就值了。

---

**GitHub：**ZhiYi-R/moon-bridge

_如果觉得有用，欢迎转发给也在用 Codex 的朋友。_

  

---

![[笔记同步助手/images/4ea028f5b8e4a7759f650cad1d314bd2_MD5.jpg|cover_image]]

Original 元帅 清野呼吸

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/9d9d41b0_1780240591281?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzY5MjI5MDU0NQ%3D%3D%26mid%3D2247483656%26idx%3D1%26sn%3D31f4818e99a87fc3a2b1b56233d33b0a%26chksm%3Df5621cc4be42332ba74af66326bf1eade07dffa046d6a02606f867c4b06a22dbf23139b50eb0%26mpshare%3D1%26scene%3D1%26srcid%3D0531c1gRgTaj7sBurL69QLsH%26sharer_shareinfo%3D3548a85684e750cfc728e85eb509e4cd%26sharer_shareinfo_first%3D3548a85684e750cfc728e85eb509e4cd%23rd&s=obsidian)

## AI 分析

- 评分：8/10
- 可信度：high
- 有用性：high
- 可行动：是
- 类型：工具
- 建议标签：Codex、DeepSeek、Moon Bridge、省钱、AI 编程、工具配置

### 信息本质

通过 Moon Bridge 将 Codex CLI 的模型从 GPT 切换到 DeepSeek，可节省 30 倍 API 费用，文章提供了详细配置步骤和故障排查。

### 可信度判断

来源为公众号，作者自称实测，步骤具体，GitHub 项目可验证。需核实 Moon Bridge 项目是否活跃、DeepSeek V4 Pro 实际效果是否如描述。

### 可利用价值

直接降低 Codex 使用成本，适合日常编程任务，可立即部署测试。

### 可开发方向

可封装成一键部署脚本或 Docker 镜像，集成到个人开发工作流中。

### 可内容化方向

可制作对比评测视频（GPT vs DeepSeek 在 Codex 中的表现）、省钱教程、自动化配置工具推广。

### 下一步

克隆 Moon Bridge 仓库，按步骤配置并测试，对比实际效果和成本。

### 风险

依赖第三方桥接工具，可能存在兼容性更新滞后；DeepSeek 服务稳定性未知；API Key 安全需注意。

### 建议沉淀位置

Projects/AI 工具链/Codex 优化
