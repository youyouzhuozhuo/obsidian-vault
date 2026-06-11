#!/usr/bin/env bash
set -euo pipefail

VAULT="/Users/lqj/Nutstore Files/obsidian"
ENV_FILE="${OBSIDIAN_INGEST_ENV:-$HOME/.obsidian-ingest.env}"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
fi

export OBSIDIAN_VAULT_PATH="${OBSIDIAN_VAULT_PATH:-$VAULT}"
export OBSIDIAN_INBOX_PATH="${OBSIDIAN_INBOX_PATH:-$VAULT/Inbox}"
export WECHAT_SYNC_PATH="${WECHAT_SYNC_PATH:-$VAULT/笔记同步助手}"
export AUTO_ANALYZE_ON_IMPORT="${AUTO_ANALYZE_ON_IMPORT:-1}"
export AUTO_GIT_SYNC_ON_IMPORT="${AUTO_GIT_SYNC_ON_IMPORT:-1}"
export AUTO_ANALYZE_MAX_CHARS="${AUTO_ANALYZE_MAX_CHARS:-4500}"
export AUTO_ANALYZE_DELAY="${AUTO_ANALYZE_DELAY:-1}"

cd "$VAULT"
exec /opt/homebrew/opt/python@3.12/bin/python3.12 process_wechat.py
