# Entorno local — API v3 + v4 + Front

Cómo levantar el stack de Libre Opción en local (rama `blu-dev-staff`) y por qué el
login de la v4 depende de tener la v3 corriendo. Gotchas de Docker y `.env`.

## Puertos del stack local

| Servicio | Puerto (host) | Cómo se arranca |
|---|---|---|
| Front (Nuxt, `WebAppLO`) | `3003` | `npm ci` → `npm run build` → `pm2 start ecosystem.config.js` desde `sitio-web-app-v3/app/` |
| API v4 (Laravel) | `8097` | Docker: `sitio-api-rest-4.1-laravel` (+ worker, scheduler, redis) |
| API v3 (legacy, LO) | `8081` | Docker: `lo-website-api-rest` |
| nb-api-rest (NewBytes v3) | `8085` | Docker, dir `/var/www/nb/sitioNB/sitio-api-rest-v3/` |

## El login v4 depende de la API v3

`AuthService::loginV3()` (API v4) hace un `curl` **server-side** a
`config('app.api_v3_url') . '/auth/login'` y luego `json_decode($response)->token`.

Si la v3 no responde, `curl_exec` devuelve `false` → **`json_decode(): Argument #1
must be of type string, false given`** → **HTTP 500** en `POST /v4/auth/login`.
Este 500 **no es CORS ni un bug de la v4** — es la v3 caída o mal apuntada.

### `API_V3_URL` debe ser el NOMBRE DEL CONTENEDOR, no `localhost`

Como la v4 llama a la v3 desde **adentro de su contenedor**, `localhost:8081` apuntaría
al propio contenedor v4. La v3 se conectó a la red de la v4 y en el `.env` de la v4:

```
API_V3_URL=http://lo-website-api-rest
```

El **front** sí usa `API_HOST=http://localhost:8081/` porque lo consumen el navegador y
el SSR de Nuxt, que corren en el host (llegan al puerto publicado).

## Correr la API v3 local

- Dir: `/var/www/lo/sitio-api-rest-v3/`. Se creó `docker-compose.yml` (antes solo `.example`),
  con `name: lo-api-rest-v3` explícito y conectado a la red externa de la v4.
- Imagen: Ubuntu 22.04 + PHP 8.1 + Apache + driver SQL Server (`sqlsrv/pdo_sqlsrv 5.11.1`). Build tarda varios min.
- `app/` se monta por volumen **sin `vendor/`** → tras `up`, correr dentro:
  `docker exec lo-website-api-rest sh -c 'cd /var/www/app && composer install --no-interaction'`
- `app/.env` ya apunta a la DB remota de staff: `db-nb-massql-dev.blu.net.ar:4444`, user `blu-dev-staff`.

## Gotcha — colisión de nombre de proyecto en Docker Compose

Varios dirs comparten el **basename** `sitio-api-rest-v3` (`/var/www/lo/...` y
`/var/www/nb/sitioNB/...` que corre `nb-api-rest`). Compose usa el basename como nombre de
proyecto → un `docker compose up` de un dir **borra/pisa** el contenedor del otro.
Fix aplicado: `name: lo-api-rest-v3` explícito en el compose de LO. Si se cae `nb-api-rest`,
restaurarlo con `docker compose up -d` desde `/var/www/nb/sitioNB/sitio-api-rest-v3/`.

## Gotcha — tras cambiar `.env`: recargar php-fpm (no basta `config:clear`)

OPcache `validate_timestamps=Off`: tinker/CLI ve el `.env` nuevo, pero php-fpm sigue sirviendo
el `config.php` cacheado. Recargar:
`docker exec sitio-api-rest-4.1-laravel sh -c 'kill -USR2 $(pgrep -o php-fpm)'`
y verificar con `curl` real al endpoint.

## CORS ya está en wildcard (no hubo que tocar nada)

La v4 devuelve `Access-Control-Allow-Origin: *` por defecto:
`CorsMiddleware` usa `config('app.cors_allow_origin', '*')` (env `CORS_ALLOW_ORIGIN`, default `*`)
y `config/cors.php` tiene `allowed_origins => ['*', ...]`. Wildcard funciona porque la auth es por
header `Authorization` (JWT), con `supports_credentials => false`.

## Archivos del arreglo (ambos gitignorados — no se commitean)

- `sitio-api-rest-v4-laravel/app/.env` → `API_V3_URL=http://lo-website-api-rest`
- `sitio-api-rest-v3/docker-compose.yml` → nuevo (el versionado es `docker-compose.example.yml`)

Si se reclonan los repos, el arreglo **no persiste**: hay que rehacer el `.env` y el compose.

## Documentación commiteable en el repo (persistida 2026-08-09)

Para que el setup se reproduzca sin depender de esta nota:
- `documentacion/guias_ejecucion/entorno-local-completo.md` — guía completa del stack local, dependencia login v4→v3, gotchas, CORS.
- `documentacion/guias_ejecucion/api-legacy-v3.md` — sección "Correr en local (Docker)".
- `sitio-api-rest-v3/docker-compose.example.yml` — ya trae `name: lo-api-rest-v3` + bloque comentado de la red v4.
- `sitio-api-rest-v4-laravel/app/.env.example` — documenta la opción v3 local en `API_V3_URL`.

Memoria de Claude: `project_v3_local_setup.md` y `project_cors.md`.

## Ver también

- [[contexto#2026-08-06]]
- [[changelog]]
- [[TareaWallet]]
