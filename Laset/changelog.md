# Changelog

Ver también: [[Laset]] · [[contexto]]

## 2026-09-09

**Fixes de código en front y back + promoción a `main`**
Mismo circuito: `feature/*` desde `origin/blu-dev-staff` → PR contra `blu-dev-staff`. En cada commit va
solo el cambio real; el sync en progreso (`.env-example`, `ecosystem.config.js`, `package-lock.json`) queda afuera.

- **front `fix(expedicion)`** (PR #6, mergeado) — Firebase se inicializa de forma defensiva:
  `plugins/firebase-messaging.js` solo crea `messaging` si hay `projectId`/`apiKey`/`appId`; `layouts/basic.vue`
  envuelve `onMessage`/`requestPermission` en try/catch. Sin config Firebase el front ya no rompe con un 500.
- **back `fix(back)`** (PR #2, mergeado) — correcciones en 4 servicios:
  - `api-rest-cobros/App/Database.php`: DSN `sqlsrv` con `Encrypt=0` + `TrustServerCertificate=1`; `#[\ReturnTypeWillChange]` en `query()`/`prepare()` (compat PHP 8).
  - `api-rest-cobros/Service/Box/Trade/Trade.php`: cobro múltiple ahora **transaccional** (valida cta cte antes de escribir, rollback si falla la consolidación en caja; respeta transacción abierta más arriba).
  - `api-rest-expedicion/Repository/Providers/ProvidersRepository.php`: reescritura del cálculo de cantidad serializada partiendo de `PedProl` y acotando por remito de proveedor.
  - `api-rest-postventa/Repository/AfterSaleRepository.php`: joins de estado con alias correctos (`C.`/`D.`). El método de `COUNT` **no** concatena `$joins`, de forma intencional.
  - `ms-metadata/controllers/stocks/stocks.py`: `ultimaVenta` con fallback a `MAX(albclit.dfecalb)` de ventas reales (`ntipoalb > 1`) cuando `A.ULTIMA_VENTA` es NULL.
- **feat(pedidos): ocultar Libre Opción** (PR #8, abierto) — `pedidos-web-app-v1/layouts/basic.vue`: la entrada
  del navbar pasa a `visible: false` (no se usa en Laset). No se tocan rutas, páginas ni store de `libreOpcion`.
- **Promoción `blu-dev-staff → main`** — PR #7 (front, 16 commits) y PR #3 (back, 10 commits).

⚠️ **Hallazgo de seguridad**: `api-rest-postventa/.env-example` (working tree local) tenía credenciales reales en
texto plano (`NB_WEB_PASS`, `ACCOUNT_MAILER_PASSWORD`, `PASSWORD_MS_ENVIOS`). Se dejó **sin commitear**. En
`blu-dev-staff` ya existe un commit "Config Laset: .env-example sanitizados". Pendiente: rotar esas credenciales
si son válidas (`.env-example` está trackeado, no debe llevar secretos).

## 2026-09-04

**Simplificación de UI del front (monorepo `frontErp`, PRs contra `blu-dev-staff`)**
Circuito: rama `feature/*` desde `origin/blu-dev-staff` → PR contra `blu-dev-staff` (ver [[contexto]]).
Ocultamientos hechos con comentarios (reversibles). `companyCode 11 == LASET`.

- **#1 `feature/presupuestos-sin-iva`** — se porta el módulo de presupuestos desde el repo interno
  New-Bytes al monorepo (`pedidos-web-app-v1`: `pages/presupuestos.vue`, `components/Presupuestos/Builder.vue`,
  `store/presupuestos.js`, `mixins/presupuestoPdf.js`, wiring en `plugins/api.js`, `Table/TabMenu.vue`,
  `layouts/basic.vue`) **ya sin columnas IVA/Imp.Int** en el modal y el PDF; totales = cantidad×precio.
- **#2 `feature/ocultar-columna-tipo-ordenes`** — pedidos: se quita la columna "Tipo" (`observation`) del
  getter `columns` en `store/orders.js`.
- **#3 `feature/ocultar-elementos-dashboard`** — dashboard: se ocultan pestañas (Incentivo Netac, Ranking
  de aceleración, Tiempos logísticos, Logística por zona), botones de Reportes (Kits y Bundles, Inventario
  Intel, Ventas Intel) y la métrica "Tasa de conversión".
- **#4 `feature/compras-quitar-checkbox-iva`** — compras: checkbox IVA (`showIva`) en el modal de Órdenes.
- **#5 `feature/compras-ocultar-columnas`** — compras: Ingresos lista (IVA, FOB, ID de estado), Ingresos
  modal (checkbox IVA), Categorías (solo Categoría + Posición arancelaria predeterminada), Depósitos
  (columna Empresa), Posiciones arancelarias (grupo Impuestos tras Descripción), y se quita `fixed:'left'`
  de Fecha/Nº Orden/Pedido en Órdenes (eliminaba una columna en blanco).

Nota: el working tree del monorepo tiene un **sync en progreso** desde New-Bytes; en cada PR se commitea
solo lo del cambio, nunca el sync entero (`.env-example`, `ecosystem.config.js`, `package-lock.json`).

## 2026-09-02

**Consolidación de repos**
- 7 fronts → monorepo `frontLaset` (`LasetCorp/frontErp`); 7 backs → `backLaset` (`LasetCorp/backErp`).
  Eliminados los `.git` anidados. Autor corregido a `Catriel <catrielmercurio@gmail.com>`.

**Configuración desde `env-backup`**
- Creados los `.env` de los 7 back y 7 front tomando valores del backup.
- Wiring local front↔back (se conserva el path, host→puerto local). Back→back por nombre de
  contenedor en `laset-net`.

**Sufijo `laset` (convivencia con la otra empresa)**
- Contenedores/redes/instancias PM2 con sufijo `laset`; puertos backs 81xx, fronts 39xx.
- `docker-compose.yml` con `image: *-laset` (reuso de imágenes ya construidas) y red `laset-net`.
- `ecosystem.config.js` con instancias `Web*Laset`, `instances: 2`.

**Backs levantados (Docker)**
- 7 contenedores up. `composer install` en los PHP (flags `--no-security-blocking`,
  `--ignore-platform-reqs` en cobros). `storage/` creado para Laravel. `.env` a 644.
- ms-metadata (FastAPI) buildeado; Swagger OK.

**Fronts levantados (PM2)**
- `npm install --legacy-peer-deps` + build `--openssl-legacy-provider` + `pm2 start`. `pm2 save`.
- comprobante-pdf con `--ignore-scripts` (dep nativa `canvas`).
- Los 7 responden (302 login / 200).

**Base de datos**
- Endpoint correcto: `db-nb-massql-dev.blu.net.ar,4444` / `NB_WEB` / `cmercurio`. Aplicado a los 7 back.
- **Login real validado end-to-end** (front → back → SQL Server → JWT).

**Documentación**
- Creados `README.md`, `CLAUDE.md` y `docs/{arquitectura,operaciones,troubleshooting}.md` en el repo.
- Memoria de proyecto actualizada. Sincronizado a Obsidian (`Laset/`).
