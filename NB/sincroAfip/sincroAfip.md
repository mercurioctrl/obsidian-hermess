# sincroAfip

Sincronizador automático de **comprobantes recibidos** de AFIP (ARCA) para los CUITs del grupo [[NB]]. Baja los CSVs desde Mis Comprobantes vía scraping y los carga de forma idempotente a SQL Server.

**Repo:** `/var/www/sincroAfip`
**Tabla destino:** `NewBytes_DBF.dbo.AfipComprobantesRecibidos`
**Última sincronización:** 2026-08-14

## Resumen

Reemplaza la carga manual de facturas recibidas que hacía el equipo contable. Corre en Docker, pensado para cron diario. End-to-end (scrape + load) ~20s por CUIT.

Desde 2026-08-06 el login de AFIP tiene captcha, que se resuelve con 2Captcha (servicio pago prepago — vigilar saldo). Decisiones clave: ver [[arquitectura]] y [[stack]].

## Notas del proyecto

- [[arquitectura]] — Flujo end-to-end, componentes, decisiones de diseño, selectores de AFIP, captcha.
- [[stack]] — Tecnologías, versiones, servicios externos (AFIP, 2Captcha).
- [[despliegue]] — Prod, cron, onboarding de CUITs, troubleshooting.
- [[migracion]] — DDL de la tabla, índices, evolución.
- [[tabla-referencia]] — Columnas, códigos AFIP, queries típicas de reporting.
- [[contexto]] — Por qué existe, estado actual, pendientes, captcha.
- [[changelog]] — Bitácora de cambios.

## Documentación en el repo

- `README.md`
- `CLAUDE.md` (instrucciones para futuras sesiones de Claude)
- `docs/ARQUITECTURA.md` → [[arquitectura]]
- `docs/DESPLIEGUE.md` → [[despliegue]]
- `docs/MIGRACION.md` → [[migracion]]
- `docs/TABLA.md` → [[tabla-referencia]]
