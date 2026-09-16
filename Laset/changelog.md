# Changelog

Ver también: [[Laset]] · [[contexto]]

## 2026-09-16

**Docs y contexto**
- Nueva doc en el repo: `docs/dominio-unico-sso.md` (mapa de paths, las tres piezas del SSO,
  la regla de releer permisos de la base, snippets de verificación).
- `docs/troubleshooting.md`: nueva sección "Dominio único / SSO" con 7 síntomas y sus causas.
- `README.md`, `docs/arquitectura.md` y `CLAUDE.md` apuntan al dominio único como forma de acceso.

**Inventario — grilla de Precios**
- Columnas de color: además del precio, ahora se ve y se edita el **%**. Editar el precio lo fija
  a mano y el % se deriva del costo; editar el % limpia el precio manual y el precio vuelve a
  `costo × (1 + %)`. El back devuelve la fila recalculada, así que la otra celda se actualiza sola.
- El grupo "Precio por lista (color)" se movió **antes de "Últ. mov."**, pegado a Costo.

## 2026-09-15

**Dominio único `laset.local` + SSO** — ver [[arquitectura]] y [[troubleshooting]]
- Las 7 apps pasan a servirse desde un solo dominio, cada una bajo su path (`router.base`), detrás
  de un reverse proxy Apache. Se entra una vez y se salta entre apps con un menú nuevo.
- `AppSwitcher.vue` en los 6 fronts con UI (duplicado: el monorepo no tiene paquete compartido).
  Logo fijo de Laset en las 6, ancho 114px, header uniformado a 64px.
- **Bug 1:** `build.publicPath` absoluto rompía TODOS los assets (Nuxt 2 le prepende `router.base`,
  montaba en `/pedidos/pedidos/_nuxt/`). El SSR igual pintaba el HTML: la app parecía andar pero
  nunca hidrataba. Corregido a `publicPath: '_nuxt/'`.
- **Bug 2:** los backs validaban permisos leyendo el **payload del token**. Con el token compartido
  cada back recibe la forma de usuario de otra app → 401 → `auth-next` borraba el token y
  **entrar a una app deslogueaba de todas**. Los 4 backs con middleware (pedidos ×3, compras,
  expedicion, postventa) ahora releen el usuario de la base por `UserId`.
- **Firma del JWT:** expedicion y postventa la tenían hardcodeada y distinta; pasan a
  `md5(JWT_SIGNATURE_KEY)` como el resto. ms-metadata decodifica con `verify_aud: False`
  (los backs PHP usan `aud` como huella de navegador y PyJWT lo exigía).
- **Infra que estaba rota de antes:** los Phinx perdían los headers de CORS porque imprimían
  warnings de PHP 8 antes; el dir `logs/` no era escribible por `www-data`; postventa no conectaba
  a SQL Server (ODBC 18 valida el certificado autofirmado). Los tres corregidos.
- Los `.env` de cobros y expedición apuntaban a los **backs de la otra empresa** (8083/8086 en vez
  de 8183/8184). Corregido junto con sus puertos PM2.
- Limpieza de menú: 28 links a `*.saftel.com` (dominio de la otra empresa) comentados en los 6
  fronts; en inventario se ocultaron 4 pestañas sin uso.
- PRs: frontErp#11 y backErp#5, ambos contra `blu-dev-staff`.

## 2026-09-11 / 2026-09-14

**Listas de precio por color** — reemplaza el esquema npvp/ntarifapp para Laset
- 4 listas (Azul, Verde, Naranja, Violeta), cada una `base × (1 + %)`, con lista por defecto por
  cliente y override editable en el modal de la orden.
- DB: `LASET_LISTA_COLOR`, `LASET_LISTA_COLOR_ARTICULO`, `LASET_CLIENTE_LISTA_COLOR`.
- ms-metadata: endpoints `/colorLists` y `/items/{id}/colorPrices` (+ batch).
- Front inventario: modal de configuración y 4 columnas de color editables por artículo.
- Back y front de pedidos: el precio sale de la lista del cliente; selector con puntito de color.
- Todo scopeado a `companyCode 11`; las otras empresas del clon quedan intactas.
- Mergeado: backErp#4.

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
