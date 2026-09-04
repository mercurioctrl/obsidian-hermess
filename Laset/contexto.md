# Contexto

Ver también: [[Laset]] · [[arquitectura]] · [[changelog]]

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

## Estado actual
Los 7 fronts (PM2) y 7 backs (Docker) están **operativos**; el login real front→back→DB fue validado.
En curso: 5 PRs de simplificación de UI del front abiertos contra `blu-dev-staff` (2026-09-04).
