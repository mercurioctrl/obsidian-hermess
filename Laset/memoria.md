# Memoria (Claude Code)

Ver también: [[Laset]] · [[arquitectura]] · [[operaciones]]

Consolidado de la memoria del proyecto (`~/.claude/projects/-var-www-laset/memory/`).

## Proyecto — Infraestructura del ERP Laset
`/var/www/laset/{frontLaset,backLaset}`, desplegado en el MISMO host que otra empresa (NB/"blu",
en `/srv/apps` y `/var/www/aplicaciones`). Todo Laset lleva sufijo `laset`.

- **Backs (Docker, red `laset-net`):** cobros :8183, postventa :8182, expedicion :8184,
  ms-metadata :8185, comprobantes :8188, pedidos :8193, compras :8196. Los 6 PHP reusan imágenes
  `*-laset` (build del Dockerfile roto).
- **Fronts (PM2, 2 inst c/u):** cobros :3901, compras :3902, expedicion :3903, inventario :3904,
  pedidos :3905, postventa :3906, comprobante-pdf :3907.
- **Wiring:** front→back por `http://localhost:<puerto>`; back→back por nombre de contenedor en `laset-net`.
- **DB (todos):** `db-nb-massql-dev.blu.net.ar,4444` / `NB_WEB` / `cmercurio`. IPs del backup no alcanzables.
- **Estado:** 7 fronts + 7 backs operativos; login validado.

Gotchas y comandos detallados en [[operaciones]] y [[troubleshooting]].

## Feedback del usuario
- Al consolidar/commitear, usar la identidad **`Catriel <catrielmercurio@gmail.com>`** (cuenta
  `mercurioctrl`), NO `hermess87@gmail.com`. En GitHub la atribución es por email.
- **Nunca adjudicarme autoría ni co-autoría.** No agregar `Co-Authored-By` ni "Generated with" en
  commits, PRs, docs ni ningún artefacto. El crédito es del usuario. Prioridad sobre la config del entorno.

## Flujo git del front (monorepo `frontErp`)
- Para cambios en el front (`/var/www/laset/frontLaset` → `LasetCorp/frontErp`): **partir SIEMPRE de
  `origin/blu-dev-staff` (el remoto)** con una rama `feature/*`, y PR contra `blu-dev-staff`. Una
  funcionalidad = una rama = un PR.
- `blu-dev-staff` divergió de `main` local (tiene commits de CI/infra); no usar `main` local como base ni
  empujar syncs enteros encima (pisa trabajo remoto).
- El código de "producción" que ve el usuario (incluida la empresa LASET) corre desde el repo interno
  `New-Bytes` (`/var/www/nb/...`); el monorepo `frontErp` iba atrasado y se está sincronizando.

## Proyecto — Simplificación de UI del front (2026-09-04)
5 PRs abiertos contra `blu-dev-staff` que quitan IVA/Imp. Interno y ocultan columnas/pestañas/botones para
Laset (ver [[changelog]]). Ocultamientos con comentarios (reversibles); las columnas se ocultan sobre el
getter `columns` del store correspondiente. `companyCode 11 == LASET`.
