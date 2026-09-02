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

## Estado actual
Los 7 fronts (PM2) y 7 backs (Docker) están **operativos**; el login real front→back→DB fue validado.
