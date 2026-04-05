# Documentación — Expedición

## Setup desarrollo local

### Requisitos
- Docker Desktop (con soporte ARM64 si es Apple Silicon)
- Node.js (v18+ funciona, v25 requiere `--openssl-legacy-provider`)
- npm

### 1. Backend (API REST)

```bash
cd api-rest-expedicion

# Configurar env (ya tiene credenciales configuradas)
cp app/.env-example app/.env    # editar con credenciales de DB

# Levantar container
docker-compose up -d --build

# Instalar dependencias PHP dentro del container
docker exec -it expedition-api-rest bash -c "chown -R www-data /var/www/app && composer install"
```

**Verificar que funciona:**
```bash
curl -s -X POST http://localhost:8084/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"test"}'
# Debe responder: "Los datos ingresados son incorrectos."
```

API disponible en: `http://localhost:8084/v1`

### 2. Frontend (Web App)

```bash
cd expedicion-web-app-v1/app

# Configurar env
cp .env-example .env
# Asegurar que API_HOST apunte al backend:
# API_HOST=http://localhost:8084/v1

# Generar build version (requerido)
node scripts/update-build-version.js

# Instalar dependencias
npm ci

# Iniciar dev server
NODE_OPTIONS=--openssl-legacy-provider npm run dev
```

Frontend disponible en: `http://localhost:4149`

### 3. Producción (Frontend)

```bash
cd expedicion-web-app-v1/app
cp ecosystem-example.js ecosystem.config.js
NODE_OPTIONS=--openssl-legacy-provider npm run build
pm2 start    # cluster mode, max instances, 300MB restart limit
```

---

## Variables de entorno

### Backend (app/.env)

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `DB_HOST` | SQL Server host | `190.210.23.108` |
| `DB_PORT` | SQL Server port | `1433` |
| `DB_NAME` | Base de datos principal | `NB_WEB` |
| `DB_USER` | Usuario SQL Server | — |
| `DB_PASS` | Password SQL Server | — |
| `DEBUG` | Modo debug (1=on) | `1` |
| `BASE_PATH` | Prefijo de rutas API | `/v1` |
| `API_ENVIOS_URL` | URL microservicio envíos | `https://omega.ms-envio.lio.red/v1` |
| `API_POSTVENTA` | URL API postventa | `http://api.aftersale.lio.red/v1/` |
| `MS_COMPROBANTES_URL` | URL microservicio comprobantes | `http://ms-comprobantes.lio.red/v2/` |
| `JWT_EXPIRATION_TIME` | Expiración del token | `now + 230 hours` |
| `ITEM_PER_PAGE` | Paginación por defecto | `15` |

### Frontend (app/.env)

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `API_HOST` | URL del backend | `http://localhost:8084/v1` |
| `NODE_PORT` | Puerto del frontend | `4149` |
| `STATIC_BASE_URL` | CDN de imágenes | `https://static.nb.com.ar/` |
| `ENVIOS` | MS Envíos (frontend directo) | `https://omega.ms-envio.lio.red` |
| `COMPROBANTES` | MS Comprobantes (frontend directo) | `https://comprobantes.lio.red` |
| `INITIAL_ITEMS_PER_PAGE` | Paginación default | `15` |
| `BIGGER_INITIAL_ITEMS_PER_PAGE` | Paginación envíos/retiro | `300` |
| `REFRESH_PENDINGS` | Intervalo polling pendings (ms) | `300000` (5 min) |
| `FIREBASE_*` | Config Firebase push notifications | — |

---

## Migraciones de base de datos

```bash
docker exec -it expedition-api-rest bash
cd /var/www/app
composer phinx migrate       # ejecutar migraciones
composer phinx seed:run      # ejecutar seeds
```

Config: `app/phinx.php`. Migraciones en `app/database/migrations/`, seeds en `app/database/seeds/`.

---

## Lint (Frontend)

```bash
cd expedicion-web-app-v1/app
npm run lint          # eslint + stylelint + prettier
npm run lintfix       # auto-fix
npm run lint:js       # solo eslint
npm run lint:style    # solo stylelint
```

Pre-commit hooks (lint-staged) validan lint automáticamente.
Commits siguen **Conventional Commits** (enforced por commitlint).

---

## Docker — Comandos útiles

```bash
# Levantar API
docker-compose up -d

# Reconstruir imagen (después de cambios en Dockerfile)
docker-compose up -d --build

# Ver logs
docker logs -f expedition-api-rest

# Entrar al container
docker exec -it expedition-api-rest bash

# Verificar PHP y extensiones
docker exec expedition-api-rest php -m | grep sqlsrv

# Verificar conectividad a SQL Server
docker exec expedition-api-rest nc -z -w 5 190.210.23.108 1433
```

---

## Endpoints principales de la API

Todos bajo `/v1`:

| Método | Ruta | Middleware | Descripción |
|--------|------|-----------|-------------|
| POST | `/auth/login` | — | Login (retorna JWT) |
| PATCH | `/auth/logout` | Permission | Logout |
| GET | `/auth/user` | Permission | Info del usuario actual |
| GET | `/passes` | Permission | Listar pases |
| GET | `/passes/{id}` | Permission | Detalle de pase |
| PATCH | `/passes` | Permission | Procesar pase |
| GET | `/providersOrders` | Permission | Órdenes de proveedores |
| GET | `/shipments` | Permission | Listar envíos |
| GET | `/orders/{pedido}` | Permission | Detalle de pedido |
| PATCH | `/orders/{pedido}/dispatch` | Permission | Despachar pedido |
| GET | `/items` | Item | Listar items de stock |
| GET | `/refund/{pedido}` | Permission | Detalle devolución |
| GET | `/companies` | Permission | Listar empresas |

---

## Ver también

- [[NB/expedicion/stack|Stack]] — Tecnologías y dependencias
- [[NB/expedicion/arquitectura|Arquitectura]] — Estructura del código y patrones
- [[NB/expedicion/memoria|Memoria]] — Problemas de setup resueltos y workarounds
- [[NB/expedicion/changelog|Changelog]] — Historial de cambios
- [[NB/expedicion/contexto|Contexto]] — Visión general del proyecto
