#!/bin/bash
# Reconstruye los wikilinks e índices de la bóveda de Obsidian.
# Ejecutado por cron a las 9:03 y 21:03 (hora Argentina).

export PATH="/home/hermess/.local/bin:/usr/local/bin:/usr/bin:/bin"

cd /var/www/obsidian-hermess || exit 1

/home/hermess/.local/bin/claude \
  --print "/reconstruirIndices" \
  --dangerously-skip-permissions \
  --no-session-persistence \
  2>&1
