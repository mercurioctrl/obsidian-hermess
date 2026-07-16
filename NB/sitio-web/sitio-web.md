# Sitio Web NB

Sitio de e-commerce de **New Bytes** (nb.com.ar). Monorepo con dos subproyectos independientes, cada uno con su propio `.git`:

- **Frontend** — Nuxt.js 2 (Vue 2 + Bootstrap-Vue). Repo `sitio-wep-app-v2`.
- **API REST** — PHP Slim 4 (capas Controller → Service → Repository → PDO). Repo `sitio-api-rest-v3`.

Ruta local: `/var/www/nb/sitioNB/`

## Notas del proyecto

- [[arquitectura]] — Estructura de capas, ruteo, DI, patrones de front y back
- [[stack]] — Tecnologías, frameworks y dependencias clave
- [[infraestructura]] — Docker, PM2, Apache, Redis y setup local
- [[changelog]] — Registro de lo trabajado por fecha
- [[contexto]] — Reglas de negocio, decisiones y aprendizajes
- [[memoria]] — Memoria consolidada de Claude: preferencias, servicios del host, problemas conocidos

## Bases de datos

La API se conecta a **SQL Server** (no MySQL como sugería el genérico): bases `NB_WEB`, `NewBytes_DBF`, `PRODUCTOS`. El stock vive en `NewBytes_DBF.dbo.stocks` (una fila por almacén).

Última sincronización: 2026-07-16
