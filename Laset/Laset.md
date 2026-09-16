# Laset

ERP de la empresa **Laset**, desplegado localmente en el servidor `hermess-pc`
(`/var/www/laset`). Compuesto por **7 aplicaciones frontend** (Nuxt 2 + PM2) conectadas a
**7 APIs backend** (PHP/Phinx, Laravel y un microservicio FastAPI, en Docker).

Convive en el **mismo host** con el ERP de otra empresa (NB / "blu"), por lo que todo Laset
usa sufijo `laset` (contenedores, red Docker, instancias PM2) y puertos propios para no colisionar.

## Monorepos
- Frontend: `frontLaset/` → `git@github.com:LasetCorp/frontErp.git`
- Backend: `backLaset/` → `git@github.com:LasetCorp/backErp.git`

**Acceso:** todo por `http://laset.local/` — las 7 apps bajo su path, con sesión compartida (SSO).
Se loguea una vez y se salta entre apps con el menú del header. Ver [[arquitectura|dominio único y SSO]].

## Notas técnicas
- [[arquitectura]] — modelo, wiring front↔back↔DB, dominio único + SSO, listas de precio por color.
- [[stack]] — tecnologías y versiones.
- [[operaciones]] — runbook: levantar / reconstruir / logs de cada capa.
- [[troubleshooting]] — errores conocidos y su solución.
- [[contexto]] — decisiones y contexto de negocio.
- [[memoria]] — memoria del proyecto (Claude Code).
- [[changelog]] — registro de trabajo.

## Notas de equipo
- [[Martes]] · [[Miercoles]] — ayudamemoria y tickets del equipo.

---
Última sincronización: 2026-09-16
