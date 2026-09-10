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

## Estado actual
Los 7 fronts (PM2) y 7 backs (Docker) están **operativos**; el login real front→back→DB fue validado.
Mergeado a `blu-dev-staff`: simplificación de UI (2026-09-04), Firebase defensivo y fixes de back (2026-09-09).
Abierto: PR #8 (ocultar Libre Opción) contra `blu-dev-staff`, y PRs de promoción a `main` (#7 front, #3 back).
