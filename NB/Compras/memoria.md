# Memoria del proyecto

Consolidado de la memoria persistente de Claude Code para este proyecto
(`~/.claude/projects/-var-www-nb-compras/memory/`). Sincronizado el 2026-06-10.

## Estructura

- `api-rest-compras-laravel/` — API Laravel 9 (PHP 8.1), repo Git propio. Código en `app/`.
- `compras-web-app-v1-/` — Frontend Nuxt 2, repo Git propio. Código en `app/`.

## Backend — Docker

- Contenedor: `api-rest-compras-apirest-laravel`, puerto **8096** → `http://localhost:8096`, base path **`/v1`**.
- Setup: `cp docker-compose.example.yml docker-compose.yml` → `DOCKER_BUILDKIT=0 docker-compose up -d --build` → `composer install --no-security-blocking`.
- Problemas resueltos al buildear:
  - PPA ondrej/php vacío en Ubuntu 20.04 → base image `ubuntu:22.04` (PHP 8.1 en repos oficiales).
  - MS ODBC Driver incompatible con OpenSSL 3.0 → usar **FreeTDS + pdo_dblib** (Laravel auto-detecta `pdo_dblib` si no está `pdo_sqlsrv`). Config: `/etc/freetds/freetds.conf` → `tds version = 7.4`.
  - Permisos storage: `mkdir -p storage/framework/{cache,views,sessions}`.
- Composer requiere `--no-security-blocking` por advisories en firebase/php-jwt y laravel v9.

## Backend — Arquitectura (cómo navegar rápido)

Patrón por feature: **Controller invokable (`__invoke`) → Service → Repository (SQL crudo, `DB::select`) → DTO**. Rutas en `routes/api.php`. Auth JWT via `App\Support\TokenManager` (+ `PermissionMiddleware`, requiere `compras > 0`).

Tabla clave `articulo` (alias `A`): `ID_ARTICULO`=id interno (entero, sargable), `ID_PRODUCTO`=SKU, `CDETALLE`=título, `companyCode`, flags `EXCLUIR<>1` y `ocultarDeNb<>1` (siempre en el WHERE).

## Frontend — Arranque y convenciones

- Dev: `cd compras-web-app-v1-/app && npm run dev` → **http://localhost:3867/** (puerto = `NODE_PORT`). Usa `NODE_OPTIONS=--openssl-legacy-provider` (webpack 4 + Node nuevo). Prod: pm2.
- `.env` front: `API_HOST=http://localhost:8096/v1`, `NODE_PORT=3867`.
- Moneda: `currencyId` con `'PSO'` (pesos) / `'DOL'` (dólar). `companyCode == 11` = LASET (oculta varias columnas, ver `plugins/permissions.js`).

## Base de datos

- Driver `DB_CONNECTION=sqlsrv` → en runtime usa `pdo_dblib` (FreeTDS).
- Server canónico: `190.210.23.97:4444`, DB `NB_WEB`, user `web`. Detalle y gotcha del puerto SSH en [[contexto#Infraestructura / Base de datos (gotcha importante)|contexto]].

## Ver también

- [[arquitectura|Arquitectura]]
- [[stack|Stack]]
- [[contexto|Contexto y reglas]]
