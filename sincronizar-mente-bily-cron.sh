#!/bin/bash
# Sincroniza la estructura de Inicio.md en toda la carpeta Bily/.
# Ejecutado por cron a las 5:03 AM (hora Argentina).

export PATH="/home/hermess/.local/bin:/usr/local/bin:/usr/bin:/bin"

cd /var/www/obsidian-hermess || exit 1

/home/hermess/.local/bin/claude \
  --print "/sincronizarMenteBily" \
  --dangerously-skip-permissions \
  --no-session-persistence \
  2>&1
