# backup.sh

> Backup completo: DB + PDFs + uploads + .env → tar.gz con timestamp.
> Parte del skill [[SKILL|fullstack-docker-app]]. Ver [[architecture#Backup/Restore]].
> Restaurar con [[restore.sh]].

## Qué respalda

1. **Base de datos** — mysqldump con routines y triggers
2. **PDFs** — `storage/app/pdfs` via docker cp
3. **Uploads** — `storage/app/public` via docker cp
4. **Config** — `.env` como `env.bak`

Resultado: `backups/backup_YYYYMMDD_HHMMSS.tar.gz`

Usa variables de [[env.example]] y containers definidos en [[docker-compose.yml]].

## Template

```bash
#!/bin/bash
set -e

# ── Load config ──
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${SCRIPT_DIR}/.env"

if [ ! -f "$ENV_FILE" ]; then
    ENV_FILE="${SCRIPT_DIR}/{{NOMBRE_PROYECTO}}/.env"
fi

if [ ! -f "$ENV_FILE" ]; then
    echo "ERROR: No se encontró .env"
    exit 1
fi

set -a
source "$ENV_FILE"
set +a

CONTAINER_DB="{{CONTAINER_PREFIX}}-db"
CONTAINER_BACKEND="{{CONTAINER_PREFIX}}-backend"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_BASE="${SCRIPT_DIR}/backups"
BACKUP_DIR="${BACKUP_BASE}/${TIMESTAMP}"

echo "============================================"
echo "  Backup — {{NOMBRE_PROYECTO_UPPER}}"
echo "  ${TIMESTAMP}"
echo "============================================"

mkdir -p "$BACKUP_DIR"

# ── 1. Database ──
echo "[1/4] Exportando base de datos..."
docker exec ${CONTAINER_DB} mysqldump \
    -u root -p"${DB_ROOT_PASSWORD}" \
    --routines --triggers \
    "${DB_NAME}" > "${BACKUP_DIR}/database.sql"
echo "  ✓ database.sql ($(du -h "${BACKUP_DIR}/database.sql" | cut -f1))"

# ── 2. PDFs ──
echo "[2/4] Copiando PDFs..."
docker cp ${CONTAINER_BACKEND}:/var/www/html/storage/app/pdfs "${BACKUP_DIR}/pdfs" 2>/dev/null || mkdir -p "${BACKUP_DIR}/pdfs"
echo "  ✓ pdfs/"

# ── 3. Uploads ──
echo "[3/4] Copiando uploads..."
docker cp ${CONTAINER_BACKEND}:/var/www/html/storage/app/public "${BACKUP_DIR}/uploads" 2>/dev/null || mkdir -p "${BACKUP_DIR}/uploads"
echo "  ✓ uploads/"

# ── 4. Config ──
echo "[4/4] Guardando configuración..."
cp "$ENV_FILE" "${BACKUP_DIR}/env.bak"
echo "  ✓ env.bak"

# ── Compress ──
echo ""
echo "Comprimiendo..."
ARCHIVE="${BACKUP_BASE}/backup_${TIMESTAMP}.tar.gz"
tar -czf "$ARCHIVE" -C "$BACKUP_BASE" "$TIMESTAMP"
rm -rf "$BACKUP_DIR"

SIZE=$(du -h "$ARCHIVE" | cut -f1)
echo ""
echo "============================================"
echo "  ✓ Backup completado"
echo "  Archivo: $ARCHIVE"
echo "  Tamaño: $SIZE"
echo "============================================"
```
