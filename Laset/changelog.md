# Changelog

Ver también: [[Laset]] · [[contexto]]

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
