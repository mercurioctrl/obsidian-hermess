# Contexto

Ver también: [[Laset]] · [[arquitectura]] · [[changelog]] · [[memoria]]

## Origen
El ERP Laset estaba repartido en repos individuales (mayormente `New-Bytes` / `LibreOpcion`).
Se consolidó en dos monorepos (`frontErp`, `backErp` de `LasetCorp`) eliminando los `.git`
anidados. Commits firmados como `Catriel <catrielmercurio@gmail.com>` (la cuenta `mercurioctrl`,
NO `hermess87`).

## Decisiones tomadas (2026-09-02)
- **Convivencia con otra empresa**: el host ya corre el ERP de NB/"blu". Se eligió sufijo `laset`
  + puertos nuevos (backs 81xx, fronts 39xx) para correr ambos en paralelo.
- **DB `NB_WEB` sin renombrar** (es compartida y debe existir). El endpoint correcto y alcanzable
  es `db-nb-massql-dev.blu.net.ar,4444` (user `cmercurio`), no los IPs del backup.
- **`inventario`** no tiene back propio en `backLaset`; se apuntó tentativamente a `ms-metadata`
  (:8185). **Pendiente confirmar** si es el back correcto.
- **Secretos**: los `.env` no se commitean. El `.env` de `ms-metadata` estaba trackeado en el repo
  original; en el monorepo quedó excluido.

## Cosas que no funcionaron (y por qué)
- Build directo de los Dockerfile PHP → `pecl install sqlsrv` incompatible con PHP 7.4.
  Se reutilizaron imágenes ya construidas, re-etiquetadas `*-laset`.
- IPs de DB del backup (172.31.10.208, 192.168.0.42) → sin ruta desde este host (LAN 10.10.10.x).
- Una red Docker por app → pool de subredes del host agotado. Se usó `laset-net` compartida.
- `instances: 'max'` en PM2 → 24 procesos por front, agota la RAM del host compartido. Se bajó a 2.

## Convenciones de trabajo (feedback del usuario)
- Commits/PRs a nombre de **`Catriel <catrielmercurio@gmail.com>`** (cuenta `mercurioctrl`).
- **Nunca** adjudicarse autoría ni co-autoría: sin `Co-Authored-By` ni "Generated with" en commits,
  PRs, docs ni ningún artefacto.

## Decisiones (2026-09-04)
- **Flujo de trabajo del front**: toda funcionalidad sale de una rama `feature/*` creada desde
  **`origin/blu-dev-staff` (remoto)** y se abre PR contra `blu-dev-staff`. No usar `main` local (divergió).
  Ver [[memoria#Flujo git del front (monorepo `frontErp`)]].
- **Ocultamientos reversibles**: los pedidos de "sacar/ocultar" columnas, pestañas, botones y checkboxes se
  implementan **comentando** el código (HTML en templates, `/* */` en JS), no borrando, para poder revertir.
- **Módulo presupuestos**: vivía en el repo interno New-Bytes y no estaba en el monorepo; se portó a
  `frontErp` de forma aditiva, ya sin IVA/Imp. Interno.
- **Columna en blanco de Órdenes (compras)**: no existía como columna; era artefacto de columnas
  `fixed: 'left'`. Se resolvió quitando `fixed` de Fecha/Nº Orden/Pedido (dejan de quedar fijas al scrollear).
- Detalle de los 5 PRs en [[changelog]].

## Decisiones (2026-09-09)
- **Firebase opcional en expedición**: si faltan las `FIREBASE_*` en el `.env`, el front no debe romper.
  Se inicializa Firebase solo con config válida (`projectId`/`apiKey`/`appId`) y se protegen las llamadas
  (`getMessaging()` rompía el arranque del cliente con un 500). Patrón defensivo.
- **Cobro múltiple transaccional (cobros)**: el cobro conjunto escribe en dos fases (registro por pedido +
  consolidación en caja `MC_LOG_OPERACIONES`/`MC_SALDOS_CAJA`). Ahora van dentro de una única transacción y
  se valida cta cte **antes** de escribir, para evitar cobros a medias (cliente cobrado / caja sin impactar).
- **`ultimaVenta` con fallback (metadata)**: `A.ULTIMA_VENTA` del ERP no se actualiza para algunos artículos;
  se usa `MAX(albclit.dfecalb)` de ventas reales (`ntipoalb > 1`, excluye reservas) como fallback.
- **`AfterSaleRepository` COUNT sin `$joins`**: decisión explícita del usuario — dejar el método de conteo
  sin concatenar `$joins` (no aplica esos filtros de estado). No es un bug pendiente.
- **Libre Opción fuera del menú (pedidos)**: sección oculta con `visible: false` (no se usa en Laset); no se
  borran rutas/páginas/store de `libreOpcion`.
- **Secretos en `.env-example`**: se detectaron credenciales reales en el `.env-example` de postventa del
  working tree local; se dejaron **sin subir**. `.env-example` está trackeado (a diferencia del `.env`), así
  que no debe contener secretos. **Pendiente**: rotar esas credenciales si son válidas.

## Decisiones (2026-09-11 · listas de precio por color)
- **Modelo de precios propio de Laset**: 4 listas de color (Azul, Verde, Naranja, Violeta), cada una
  `base × (1 + % propio)`. Reemplaza en la práctica el esquema npvp/ntarifapp heredado de NB.
- **Asignación al cliente: las dos**. Lista por defecto por cliente **y** override editable en el modal
  de la orden. El usuario pidió explícitamente ambas, no una u otra.
- **Tablas nuevas y dedicadas** en vez de reusar `priceList` (existía vacía): `LASET_LISTA_COLOR`,
  `LASET_LISTA_COLOR_ARTICULO`, `LASET_CLIENTE_LISTA_COLOR`.
- **Alcance `companyCode 11`**: las otras empresas del clon siguen con npvp/ntarifapp intacto.
- **Pendiente**: cargar a mano los nombres y % reales desde la UI (los actuales son placeholder).

## Decisiones (2026-09-15/16 · dominio único y SSO)
- **Un solo dominio, `laset.local`**, con cada app bajo su path. El usuario venía entrando por puerto
  y tenía que loguearse en cada app; ahora se entra una vez.
- **Menú de aplicaciones en el header de las 6 apps** (no una landing en la raíz): se eligió el
  switcher porque permite saltar sin volver al inicio, que es lo que espera un ERP.
- **Header de inventario igualado a 64px**: tenía 55px y rompía la uniformidad del conjunto
  logo + menú. Decisión del usuario ante la alternativa de dejarlo distinto.
- **Permisos: siempre releídos de la base, nunca del payload del token.** Es la regla que hace que el
  SSO funcione; la alternativa (meter todos los permisos en un token único) se descartó por tocar el
  login de cada back y agrandar el token.
- **Postventa: `Encrypt = 1; TrustServerCertificate = 1`** en vez de copiar el `Encrypt = 0` que usa
  cobros: mantiene la conexión cifrada y solo omite validar el certificado autofirmado.
- **Menú limpio de `*.saftel.com`**: 28 accesos al dominio de la otra empresa, comentados (no borrados).
  "Reportes" queda, porque apunta a Jira, no a saftel.
- **Ocultamientos reversibles**: se mantiene la convención de comentar (HTML en templates, `/* */` en
  JS) en vez de borrar.

## Deuda técnica anotada
- **Cobros conecta a SQL Server sin cifrado** (`Encrypt = 0` en su DSN). Venía así; el usuario decidió
  anotarlo y seguir.
- **El vhost de Apache no está versionado** en ningún monorepo: vive solo en el host.
- **Secretos en `.env-example`** (ver 2026-09-09): sigue pendiente rotarlos.

## Pendiente de decisión
- Dos deep-links a `saftel.com` **fuera del menú** (`DetailExamine.vue` en inventario,
  `AsignarOCModal.vue` en pedidos): ¿reapuntar a `laset.local/...` o sacar?
- La raíz del dominio hoy redirige a `/inventario/`; se puede cambiar a `/pedidos/`.

## Estado actual
Los 7 fronts (PM2) y 7 backs (Docker) **operativos**, servidos desde `laset.local` con sesión compartida:
los 6 `/auth/user` responden 200 con un mismo token y se navega entre apps sin volver a loguearse.

Mergeado a `blu-dev-staff`: simplificación de UI (2026-09-04), fixes de back (2026-09-09), listas de
precio por color (backErp#4).
Abierto: **frontErp#11** (dominio único + menú + logo) y **backErp#5** (SSO entre los 6 backs).
⚠️ frontErp#11 se apoya en `feature/laset-listas-precio-color`, que tiene 2 commits sin mergear:
**hay que mergear esa rama primero**.

Sin commitear todavía: la limpieza de links a saftel, las 4 pestañas ocultas de inventario y el
precio + % editables de la grilla de Precios. Esperan la decisión sobre los deep-links.
