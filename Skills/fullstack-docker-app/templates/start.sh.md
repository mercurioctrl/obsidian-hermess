# start.sh

> Script principal de deploy. Un solo comando levanta todo. Parte del skill [[SKILL|fullstack-docker-app]].
> Ver [[architecture#Secretos auto-generados]] y [[architecture#Healthcheck en MySQL]].

## Pasos

1. Genera `.env` con secretos seguros (`openssl rand`) desde [[env.example]]
2. Carga variables de entorno
3. Genera `backend/.env` desde [[backend-env.example]]
4. Build de containers ([[docker-compose.yml]])
5. Levanta servicios
6. Espera MySQL (healthcheck)
7. Limpia cache
8. Ejecuta migraciones (con retry ×3)
9. Ejecuta seeders
10. Optimiza (config/route/view cache)

Parar con [[stop.sh]]. Backup con [[backup.sh]].

## Template

```bash
#!/bin/bash
set -e

echo "============================================"
echo "  {{NOMBRE_PROYECTO_UPPER}} — Deploy"
echo "============================================"
echo ""

# ── Step 1: Generate root .env if not exists ──
if [ ! -f .env ]; then
    echo "[1/10] Generando .env con secretos seguros..."
    cp .env.example .env

    DB_ROOT_PASSWORD=$(openssl rand -hex 16)
    DB_PASSWORD=$(openssl rand -hex 16)
    APP_KEY="base64:$(openssl rand -base64 32)"

    sed -i.bak "s|^DB_ROOT_PASSWORD=.*|DB_ROOT_PASSWORD=${DB_ROOT_PASSWORD}|" .env
    sed -i.bak "s|^DB_PASSWORD=.*|DB_PASSWORD=${DB_PASSWORD}|" .env
    sed -i.bak "s|^APP_KEY=.*|APP_KEY=${APP_KEY}|" .env
    rm -f .env.bak
    echo "  ✓ Secretos generados"
else
    echo "[1/10] .env ya existe, usando configuración existente"
fi

# ── Step 2: Load variables ──
echo "[2/10] Cargando variables..."
set -a
source .env
set +a

# ── Step 3: Generate backend .env ──
echo "[3/10] Generando backend/.env..."
cat > backend/.env <<EOL
APP_NAME="${APP_NAME:-{{NOMBRE_PROYECTO_UPPER}}}"
APP_ENV=production
APP_KEY=${APP_KEY}
APP_DEBUG=false
APP_URL=http://localhost

DB_CONNECTION=mysql
DB_HOST=db
DB_PORT=3306
DB_DATABASE=${DB_NAME}
DB_USERNAME=${DB_USER}
DB_PASSWORD=${DB_PASSWORD}

REDIS_HOST=${REDIS_HOST:-redis}
REDIS_PORT=${REDIS_PORT:-6379}
CACHE_STORE=redis
SESSION_DRIVER=redis

SANCTUM_STATEFUL_DOMAINS=localhost
EOL
echo "  ✓ backend/.env generado"

# ── Step 4: Build containers ──
echo "[4/10] Construyendo containers..."
docker compose build

# ── Step 5: Start services ──
echo "[5/10] Levantando servicios..."
docker compose up -d

# ── Step 6: Wait for MySQL ──
echo "[6/10] Esperando a MySQL..."
until docker compose exec -T db mysqladmin ping -h localhost -u root -p"${DB_ROOT_PASSWORD}" --silent 2>/dev/null; do
    echo "  Esperando..."
    sleep 2
done
echo "  ✓ MySQL listo"

# ── Step 7: Clear cache ──
echo "[7/10] Limpiando cache..."
docker compose exec -T backend php artisan config:clear
docker compose exec -T backend php artisan cache:clear

# ── Step 8: Run migrations (with retry) ──
echo "[8/10] Ejecutando migraciones..."
for i in 1 2 3; do
    if docker compose exec -T backend php artisan migrate --force; then
        echo "  ✓ Migraciones completadas"
        break
    fi
    echo "  Reintentando ($i/3)..."
    sleep 5
done

# ── Step 9: Seed database ──
echo "[9/10] Ejecutando seeders..."
docker compose exec -T backend php artisan db:seed --force
echo "  ✓ Datos iniciales creados"

# ── Step 10: Optimize ──
echo "[10/10] Optimizando..."
docker compose exec -T backend php artisan config:cache
docker compose exec -T backend php artisan route:cache
docker compose exec -T backend php artisan view:cache
docker compose exec -T backend php artisan storage:link 2>/dev/null || true

echo ""
echo "============================================"
echo "  ✓ {{NOMBRE_PROYECTO_UPPER}} levantado!"
echo "============================================"
echo ""
echo "  URL:   http://localhost:${APP_PORT:-80}"
echo "  Admin: {{ADMIN_EMAIL}} / {{ADMIN_PASSWORD}}"
echo ""
echo "  Comandos útiles:"
echo "    docker compose logs -f backend    # logs backend"
echo "    docker compose logs -f frontend   # logs frontend"
echo "    bash stop.sh                      # detener"
echo "    bash ../backup.sh                 # backup"
echo "============================================"
```
