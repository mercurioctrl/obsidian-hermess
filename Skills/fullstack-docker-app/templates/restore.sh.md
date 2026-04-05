# restore.sh

> Restore interactivo desde un backup. Parte del skill [[SKILL|fullstack-docker-app]].
> Ver [[architecture#Backup/Restore]]. Crear backups con [[backup.sh]].

## Flujo

1. Lista backups disponibles (ordenados por fecha)
2. Usuario selecciona cuál restaurar
3. Pide password de root de DB como verificación
4. Confirmación explícita ("si/no")
5. Restaura: DB → PDFs → uploads → .env (opcional)
6. Limpia cache

Usa containers definidos en [[docker-compose.yml]] y variables de [[env.example]].

## Template

```bash
#!/bin/bash
set -e

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
BACKUP_BASE="${SCRIPT_DIR}/backups"

echo "============================================"
echo "  Restore — {{NOMBRE_PROYECTO_UPPER}}"
echo "============================================"
echo ""

# ── List backups ──
BACKUPS=($(ls -1t "${BACKUP_BASE}"/backup_*.tar.gz 2>/dev/null))

if [ ${#BACKUPS[@]} -eq 0 ]; then
    echo "No se encontraron backups en ${BACKUP_BASE}/"
    exit 1
fi

echo "Backups disponibles:"
echo ""
for i in "${!BACKUPS[@]}"; do
    FILE="${BACKUPS[$i]}"
    NAME=$(basename "$FILE")
    SIZE=$(du -h "$FILE" | cut -f1)
    DATE_STR=$(echo "$NAME" | grep -oE '[0-9]{8}_[0-9]{6}')
    YEAR=${DATE_STR:0:4}
    MONTH=${DATE_STR:4:2}
    DAY=${DATE_STR:6:2}
    HOUR=${DATE_STR:9:2}
    MIN=${DATE_STR:11:2}
    echo "  $((i+1))) ${DAY}/${MONTH}/${YEAR} ${HOUR}:${MIN} — ${SIZE}"
done

echo ""
read -p "Seleccionar backup (número): " SELECTION

if ! [[ "$SELECTION" =~ ^[0-9]+$ ]] || [ "$SELECTION" -lt 1 ] || [ "$SELECTION" -gt ${#BACKUPS[@]} ]; then
    echo "Selección inválida"
    exit 1
fi

SELECTED="${BACKUPS[$((SELECTION-1))]}"
echo ""
echo "Seleccionado: $(basename "$SELECTED")"

# ── Security: verify admin password ──
echo ""
read -sp "Password de root de DB (verificación): " INPUT_PASS
echo ""

if [ "$INPUT_PASS" != "$DB_ROOT_PASSWORD" ]; then
    echo "Password incorrecta"
    exit 1
fi

# ── Confirm ──
echo ""
echo "⚠️  ATENCIÓN: Esto reemplazará TODOS los datos actuales."
read -p "¿Continuar? (si/no): " CONFIRM

if [ "$CONFIRM" != "si" ]; then
    echo "Cancelado"
    exit 0
fi

# ── Extract ──
echo ""
echo "Extrayendo backup..."
TEMP_DIR=$(mktemp -d)
tar -xzf "$SELECTED" -C "$TEMP_DIR"

if [ -f "$TEMP_DIR/database.sql" ]; then
    RESTORE_DIR="$TEMP_DIR"
else
    EXTRACTED=$(ls -1 "$TEMP_DIR" | head -1)
    RESTORE_DIR="$TEMP_DIR/$EXTRACTED"
fi

# ── 1. Restore database ──
if [ -f "$RESTORE_DIR/database.sql" ]; then
    echo "[1/4] Restaurando base de datos..."
    docker exec -i ${CONTAINER_DB} mysql \
        -u root -p"${DB_ROOT_PASSWORD}" \
        "${DB_NAME}" < "$RESTORE_DIR/database.sql"
    echo "  ✓ Base de datos restaurada"
else
    echo "[1/4] No se encontró database.sql, saltando..."
fi

# ── 2. Restore PDFs ──
if [ -d "$RESTORE_DIR/pdfs" ] && [ "$(ls -A "$RESTORE_DIR/pdfs" 2>/dev/null)" ]; then
    echo "[2/4] Restaurando PDFs..."
    docker cp "$RESTORE_DIR/pdfs/." ${CONTAINER_BACKEND}:/var/www/html/storage/app/pdfs/
    echo "  ✓ PDFs restaurados"
else
    echo "[2/4] Sin PDFs para restaurar"
fi

# ── 3. Restore uploads ──
if [ -d "$RESTORE_DIR/uploads" ] && [ "$(ls -A "$RESTORE_DIR/uploads" 2>/dev/null)" ]; then
    echo "[3/4] Restaurando uploads..."
    docker cp "$RESTORE_DIR/uploads/." ${CONTAINER_BACKEND}:/var/www/html/storage/app/public/
    echo "  ✓ Uploads restaurados"
else
    echo "[3/4] Sin uploads para restaurar"
fi

# ── 4. Restore .env (optional) ──
if [ -f "$RESTORE_DIR/env.bak" ]; then
    echo ""
    read -p "[4/4] ¿Restaurar .env? (si/no): " RESTORE_ENV
    if [ "$RESTORE_ENV" = "si" ]; then
        cp "$RESTORE_DIR/env.bak" "$ENV_FILE"
        echo "  ✓ .env restaurado"
    else
        echo "  Saltando .env"
    fi
else
    echo "[4/4] Sin .env para restaurar"
fi

# ── Cleanup ──
rm -rf "$TEMP_DIR"

# ── Clear cache ──
echo ""
echo "Limpiando cache..."
docker exec ${CONTAINER_BACKEND} php artisan optimize:clear 2>/dev/null || true

echo ""
echo "============================================"
echo "  ✓ Restore completado"
echo "============================================"
```
