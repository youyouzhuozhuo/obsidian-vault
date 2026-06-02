---
title: "XcodeBuildMCP：让 AI 像开发网页一样搞定 iOS-macOS 应用"
date: 2026-04-02T20:50:07
source: "微信公众号"
author: "未知"
tags:
  - AI/编程
  - 编程/开源项目
  - 工具/开发
---

# XcodeBuildMCP：让 AI 像开发网页一样搞定 iOS/macOS 应用
#笔记同步助手
## 来源
[原文链接](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461158959&idx=1&sn=6b102161d21bcfe4066357be05a0cef1&chksm=86fe0d267e65f12f197ebc312da5e3a0e579d5b82d95c44a06b8be6238cf07a71045b79c721c&mpshare=1&scene=1&srcid=0319z1snra0mDH3RJZ9yTM07&sharer_shareinfo=559ac74e4ba48e740202f575adc7eb2b&sharer_shareinfo_first=559ac74e4ba48e740202f575adc7eb2b#rd)
## 正文


![](https://pic.clipfx.app/27b0cfd35d9c5ede37244430c683f543.png)

如果你还在手动验证[[AI]]生成的[[iOS]]代码，那[[XcodeBuildMCP]]就是为你准备的。这个由[[Sentry]]开源的项目，让[[AI代理]]在[[Cursor]]、[[ClaudeCode]]中真正实现了[[iOS开发]]的自动化闭环——从写代码到编译测试，全程无需人工干预。

## 告别手动验证的循环

传统[[AI辅助开发]]有个痛点：AI写代码，你手动验证。写个[[SwiftUI]]组件？AI生成代码，你手动编译运行。改个[[API]]调用？AI建议修改，你手动测试。这种模式效率低下，还容易出错。

![](https://pic.clipfx.app/0d1ab9bb1f9e935acfcd5be280a768b4.png)

XcodeBuildMCP打破了这种循环。它通过[[MCP]]和[[CLI]]让AI代理直接操作[[Xcode]]构建系统，实现真正的自动化开发流程。

XcodeBuildMCP封装了常见的Xcode操作，包括：

-   **构建管理**：支持scheme选择、配置设置
    
-   **设备管理**：模拟器和真机构建
    
-   **日志捕获**：实时获取构建输出
    
-   **错误处理**：智能解析编译错误
    

还内置了守护进程管理状态操作，确保长时间运行的构建任务不会中断。

## 配置简单，上手快速  

在Cursor中，只需要在项目根目录创建`.cursor/mcp.json`：

```
{
  "mcpServers": {
    "XcodeBuildMCP": {
      "command": "npx",
      "args": ["-y", "xcodebuildmcp@latest", "mcp"]
    }
  }
}
```

ClaudeCode更简单，一行命令：

```
claude mcp add XcodeBuildMCP -- npx -y xcodebuildmcp@latest mcp
```

配置完成后，AI代理就能直接使用各种Xcode工具：

-   编译模拟器版本
    
-   管理代码签名
    
-   运行测试套件
    
-   分析构建日志
    

## 小结

就基础的代码编译和测试验证而言，XcodeBuildMCP已经足够覆盖大部分日常开发需求。它让iOS开发向"无人值守"迈进了一大步，特别是对于原型开发、代码重构和日
