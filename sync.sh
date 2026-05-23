#!/bin/bash
cd /var/www/obsidian-hermess

# Si no hay cambios, no hace nada
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    exit 0
fi

git add -A
git commit -m "vault backup: $(date '+%Y-%m-%d %H:%M:%S')"
git pull --rebase -X ours origin main >> /tmp/obsidian-sync.log 2>&1
git push origin main >> /tmp/obsidian-sync.log 2>&1
