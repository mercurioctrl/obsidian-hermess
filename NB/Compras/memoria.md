# Memoria del proyecto

Consolidado de la memoria persistente de Claude Code para este proyecto
(`~/.claude/projects/-Users-hermess-www-compras/memory/`). Sincronizado el 2026-06-20.

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
- Para correr SQL ad-hoc / probar repos: `docker exec api-rest-compras-apirest-laravel php artisan tinker --execute="..."`.

## Backend — Arquitectura (cómo navegar rápido)

Patrón por feature: **Controller invokable (`__invoke`) → Service → Repository (SQL crudo, `DB::select`) → DTO**. Rutas en `routes/api.php`. Auth JWT via `App\Support\TokenManager` (+ `PermissionMiddleware`, requiere `compras > 0`).

Tabla clave `articulo` (alias `A`): `ID_ARTICULO`=id interno (entero, sargable), `ID_PRODUCTO`=SKU, `CDETALLE`=título, `cRef`=referencia string (la que usan PedProL/albprol/ST_DETALLE_STOCK), `ivaCompra`=IVA de compra por defecto, `companyCode`, flags `EXCLUIR<>1` y `ocultarDeNb<>1` (siempre en el WHERE).

Compras/ingresos: `PedProT`(nNumPed)/`PedProL` = orden; `albprot`(nnumalb)/`albprol` = ingreso/remito; seriales en `NEW_BYTES.dbo.ST_DETALLE_STOCK`. Detalle en [[arquitectura#Reglas de datos transversales|arquitectura]].

## Frontend — Arranque y convenciones

- Dev: `cd compras-web-app-v1-/app && npm run dev` → **http://localhost:3867/** (puerto = `NODE_PORT`; el 3002 lo ocupa pedidos). Usa `NODE_OPTIONS=--openssl-legacy-provider` (webpack 4 + Node nuevo). Prod: pm2.
- `.env` front: `API_HOST=http://localhost:8096/v1`, `NODE_PORT=3867`.
- Moneda: `currencyId` con `'PSO'` (pesos) / `'DOL'` (dólar) decide editabilidad de cotización; `currencyQuote === 1` (valor numérico) decide el **display** (signo `$`, fila fiscal sin cálculo) — ver [[contexto#Cotización en pesos (currencyQuote === 1) — display|contexto]]. `companyCode == 11` = LASET (oculta varias columnas, ver `plugins/permissions.js`).
- Dos componentes Detail casi iguales (Órdenes vs Ingresos) — no confundir, ver [[arquitectura#Detalle de Órdenes vs Ingresos (no confundir)|arquitectura]].

## Reglas / gotchas destacados

- **`currencyQuote === 1` = pesos** (no dólares): símbolo `$`, colores `.peso`, fila Cotización fiscal sin cálculo.
- **`companyCode = 4` = NB**; depósito **SAFcom** = `warehousesId` 2 / `CCODALM` 'SAF'. Limpieza de datos 2026-06-10 (ver [[contexto#Decisiones tomadas (2026-06-10)|contexto]]).
- **Filtro de Empresa por defecto (2026-06-20):** al entrar a cualquier pestaña arranca en `$auth.user.companyCode || 4`; solo queda libre si se limpia a mano. En las 9 `components/Filters/*.vue` (ver [[contexto#Filtro de Empresa (companyCode) por defecto en pestañas|contexto]]).
- **IVA por defecto = `articulo.ivaCompra`** al agregar ítem a una orden (editable). El buscador `/v1/items` ya devuelve `iva` (ver [[contexto#IVA por defecto del artículo al agregar ítem|contexto]]).
- **Filtro por serial (Órdenes/Ingresos):** `EXISTS` sobre `ST_DETALLE_STOCK` que solo se aplica si se usa el filtro. SKU/ID interno/serial igual (ver [[contexto#Filtro por serial — Órdenes e Ingresos|contexto]]).
- **UPDATEs masivos en prod**: contar primero y confirmar alcance — base externa sin migraciones, sin rollback fácil.
- **`fullSerialized` del detalle de ingreso viene hardcodeado a 0** → usar `serializedAmount > 0` por ítem. (El del **listado** sí se calcula; órdenes sin líneas dan "Sí".)

## Rama en curso

- **`catri-fine-tunning`** (ambos repos, pusheada a origin, NO mergeada): IVA default, filtros sku/itemId/serial en Órdenes e Ingresos, columna Serializado en Órdenes, filtros compactos, companyCode por defecto. Ver [[changelog#2026-06-20|changelog 2026-06-20]].

## Base de datos

- Driver `DB_CONNECTION=sqlsrv` → en runtime usa `pdo_dblib` (FreeTDS).
- **En uso (2026-06-20): `10.10.10.47:1433`**, DB `NB_WEB`, user `fcallipo`. Canónica histórica: `190.210.23.97:4444` (user `web`). Gotcha del puerto SSH en [[contexto#Infraestructura / Base de datos (gotcha importante)|contexto]].
- Bases en juego: `NewBytes_DBF` (ERP), `NB_WEB` (web), `NEW_BYTES` (stock/seriales/despachos), `PRODUCTOS`.

## Ver también

- [[arquitectura|Arquitectura]]
- [[stack|Stack]]
- [[contexto|Contexto y reglas]]
- [[changelog|Changelog]]
