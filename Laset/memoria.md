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
