# Memoria del proyecto

Consolidado de la memoria de Claude (`~/.claude/projects/-var-www-nb-sitioNB/memory/`). Ver índice: [[sitio-web]].

## Preferencias del usuario

- **No** agregar autoría de Claude en commits (sin `Co-Authored-By` ni menciones a Claude en los mensajes).
- Consultas a la BD de producción requieren autorización explícita del usuario.
- Cambios locales de infra (`composer.json`/`.lock` con predis, `ecosystem.config.js` de PM2) se dejan **sin commitear** en el working tree; excluirlos de los commits de feature/fix.

## Estado del proyecto

Monorepo con dos sub-repos independientes (cada uno con su `.git`):

- `/var/www/nb/sitioNB/sitio-api-rest-v3/` — API PHP Slim 4 (ramas de trabajo: `Development`)
- `/var/www/nb/sitioNB/sitio-wep-app-v2/` — Frontend Nuxt 2 (rama de trabajo: `development`)

Detalle de infra local (Docker/PM2/Apache/Redis) en [[infraestructura]]; reglas de negocio en [[contexto]].

## Mapa de servicios en el host (referencia)

### Contenedores Docker relevantes

| Contenedor | Puerto host | Descripción |
|---|---|---|
| `nb-api-rest` | 8085 | API sitioNB (Slim 4) |
| `sitio-api-rest-redis` | 6379 | Redis compartido (redis:7-alpine) |
| `api-rest-pedidos-...` | 8093 | API pedidos |
| `api-rest-compras-...` | 8096 | API compras |
| `sitio-api-rest-4.1-laravel` | 8097 | API sitio v4 |
| `controldeprecios_web_1` | 8084 | Control de precios |

### Procesos PM2

| Nombre | Puerto | CWD |
|---|---|---|
| WebAppNB | 3001 | `sitio-wep-app-v2/app` |
| WebCompras | 3867 | `compras/compras-web-app-v1-/app` |
| PedidosWeb | 3002 | `pedidos/pedidos-web-app-v1/app` |

- **Node.js host:** v18.20.8 / npm 10.8.2 — requiere `NODE_OPTIONS=--openssl-legacy-provider` (Webpack 4).
- Puertos libres conocidos (al 2026-03-02): 3003-3005, 8086-8095 (varios).

## Problemas conocidos

- **`docker exec` "cwd outside mount namespace":** el CWD es un mountpoint de Docker → ejecutar desde `/tmp` o un path no-mountpoint.
- **`predis/predis` no venía en composer:** instalar con `composer require predis/predis:"^1.1"`.
- **`REDIS_HOST` tras mover el proyecto:** apuntar a la gateway del bridge del contenedor (`sudo docker inspect nb-api-rest`); valor actual `172.18.0.1`.
- **Build `ERR_OSSL_EVP_UNSUPPORTED`:** Node 18 + Webpack 4 → usar el flag legacy-provider (ya incluido en `ecosystem.config.js`).

## Ver también

- [[sitio-web]] · [[infraestructura]] · [[contexto]] · [[arquitectura]] · [[stack]] · [[changelog]]
