#!/bin/bash
set -euo pipefail
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

echo ""
echo "======================================================"
echo "  MTProto Update — $(date -u '+%Y-%m-%d %H:%M UTC')"
echo "======================================================"

git config user.email "bot@mtproto-free-russia"
git config user.name  "mtproto-bot"

echo "[GIT] pull..."
git pull --rebase origin main || true

echo "[PY] fetch + verify..."
python3 scripts/fetch_mtproto.py

if git diff --quiet all_proxies.txt verified_proxies.txt README.md 2>/dev/null; then
    echo "[GIT] Нет изменений, пропускаем коммит"
    exit 0
fi

TOTAL=$(grep -v '^#' all_proxies.txt | grep -v '^$' | wc -l | tr -d ' ')
VERIFIED=$(grep -v '^#' verified_proxies.txt | grep -v '^$' | wc -l | tr -d ' ')
TS=$(date -u '+%Y-%m-%d %H:%M UTC')

git add all_proxies.txt verified_proxies.txt README.md
git commit -m "🔄 auto-update: all=${TOTAL}, verified=${VERIFIED} [${TS}]"

echo "[GIT] push..."
git push origin main
echo "✅ Done!"
