# Stack — bluFixture

## Backend

| Tech | Versión | Uso |
|------|---------|-----|
| PHP | 8.3 | Runtime |
| Laravel | 11 | Framework API |
| Laravel Sanctum | — | Auth multi-model (User + Participante) |
| PhpSpreadsheet | — | Import/export XLSX (`--ignore-platform-req=ext-gd`) |
| MySQL | 8 | Base de datos principal (puerto externo 3308) |
| Redis | 7 | Cache + sesiones |

## Frontend

| Tech | Versión | Uso |
|------|---------|-----|
| Nuxt | 3 | Framework SPA (`ssr: false`) |
| Vue | 3 | UI |
| Tailwind CSS | — | Estilos |
| Pinia | — | State management |
| VueUse | — | Utilidades reactivas |
| Nuxt Icon | — | Íconos (Lucide) |

## Infraestructura

| Servicio | Imagen | Puerto externo |
|----------|--------|---------------|
| `blufixture-db` | mysql:8 | 3308 |
| `blufixture-redis` | redis:7-alpine | interno |
| `blufixture-backend` | custom (Laravel) | interno |
| `blufixture-frontend` | custom (Nuxt) | interno |
| `blufixture-nginx` | nginx:alpine | **8830** |

## Variables de entorno (`.env`)

```env
DB_NAME=blufixture
DB_USER=blufixture
DB_PASSWORD=          # auto-generado por start.sh
DB_ROOT_PASSWORD=     # auto-generado por start.sh
DB_PORT=3308

APP_KEY=              # auto-generado (base64:...)
APP_PORT=8830
API_BASE_URL=http://localhost:8830/api
APP_URL=http://localhost:8830
```

## Comandos frecuentes

```bash
# Init desde cero (genera .env, migra, seedea)
bash start.sh

# Rebuild frontend
docker compose build --no-cache frontend
docker compose up -d frontend
docker restart blufixture-nginx

# Rebuild backend
docker compose build --no-cache backend
docker compose up -d backend

# Artisan
docker exec blufixture-backend php artisan migrate
docker exec blufixture-backend php artisan db:seed --force

# Logs
docker compose logs -f backend
docker compose logs -f frontend
```

## Ver también

- [[arquitectura]] · [[api]] · [[contexto]]
