# Obsidian Public Vault

这个仓库用于公开同步 Obsidian 笔记、导入脚本和后续项目代码，方便 GitHub 与 ChatGPT 读取、搜索和分析。

## 同步内容

- Obsidian Markdown 笔记
- Telegram / 微信内容导入脚本
- 标签词库和归档工具
- 第二大脑控制台和长期记忆索引
- 后续可加入的项目代码

## 第二大脑入口

- `MOC/第二大脑控制台.md`：Obsidian 内的总控制台，用于查看 Inbox、未分类、图片信息和重点主题。
- `Memory/INDEX.md`：Claude Code / Codex / GPT 优先读取的长期记忆入口。
- `Memory/AUTO_INDEX.md`：由脚本生成的结构统计和维护信号。
- `AGENTS.md`、`CLAUDE.md`：给 Codex 和 Claude Code 的仓库使用说明。

刷新自动索引：

```bash
python3 scripts/build_memory_index.py
```

## 本地运行配置

复制 `.env.example` 中的变量到本机环境变量中，再启动脚本：

```bash
export DEEPSEEK_API_KEY="your-deepseek-api-key"
export TELEGRAM_BOT_TOKEN="your-telegram-bot-token"
python tg_to_obsidian.py
python process_wechat.py
```

默认路径会使用当前仓库目录。跨设备时可以设置：

```bash
export OBSIDIAN_VAULT_PATH="/path/to/obsidian"
export WECHAT_SYNC_PATH="/path/to/obsidian/笔记同步助手"
export OBSIDIAN_INBOX_PATH="/path/to/obsidian/Inbox"
```

## 公开仓库注意事项

仓库通过 `.gitignore` 排除了 API Key、Bot Token、运行日志、同步冲突文件、Obsidian 工作区状态和插件本地配置。公开推送前仍建议运行一次密钥扫描。
