# Memoria — CashBox Cobros

Consolidación de la memoria persistente de Claude Code para este proyecto
(`~/.claude/projects/-var-www-nb-cobros/memory/`). Sincronizada: 2026-07-08.

## Proyecto

### Setup local (verificado)
- **Backend** `api-rest-cobros`: Docker compose, contenedor `cobros-api-rest`,
  `network_mode: host`, Apache en **puerto 8083** (`docker/apache/ports.conf` → `Listen 8083`).
  API base `http://localhost:8083/v1`. `app/` montado por volumen → cambios PHP inmediatos
  sin rebuild. Levantar: `docker-compose up -d` desde `api-rest-cobros/`.
- **Frontend** `cobros-web-app-v1`: Nuxt 2 (2.15.8), Node v18.20.8, requiere
  `NODE_OPTIONS=--openssl-legacy-provider`. Puerto **3002** (`.env`). Desde `app/`:
  `npm run build` → `pm2 start ecosystem.config.js` (app PM2 `CobrosWebAppNewByte`, cluster 2).
  Dev con hot-reload: `npm run dev`. Se ve en `http://localhost:3002` (302 → login).
- **Cambios locales de entorno NO commiteados** en `api-rest-cobros` (no borrar):
  `Database.php` (DSN sqlsrv `Encrypt=0; TrustServerCertificate=1` + `#[\ReturnTypeWillChange]`),
  `docker/Dockerfile` (reescrito a `php:8.2-apache-bookworm`),
  `docker/apache/apache-virtual-hosts.conf`, `docker/apache/ports.conf`.

### Ramas
Rama de integración con capitalización distinta por repo: API `Development` (mayúscula),
web `development` (minúscula). Prod `main`, staging `Gamma`/`gamma`. Ver [[contexto#Convención de ramas (importante)]].

### Features en curso (mediados 2026)
1. **AFIP Purchases / Facturas de compra** — remitos y facturas a proveedores, check de
   duplicado por proveedor, multi-sucursal. Ver [[arquitectura#Módulo AFIP Purchases (Facturas de compra) — archivos]].
2. **LendCapital / Préstamos de capital** — prestar capital y cobrar deuda (ya integrado).
   Ver [[arquitectura#Módulo de Préstamos de Capital — archivos]].
3. **Trade Audit Logger** — logging de auditoría estructurado del flujo de cobro.
   Ver [[arquitectura#Trade Audit Logger]].
4. **Dashboard de Impuestos** (2026-07-08) — carga impositiva mensual (IVA a pagar,
   percepciones/retenciones IIBB con desglose ARBA/AGIP/Otras, retenciones ganancias).
   Ver [[arquitectura#Dashboard de Impuestos (Statistics/Taxes)]].

### Gotchas de la base (importante)
- Fechas SQL Server: usar `YYYYMMDD` en parámetros (no `YYYY-MM-DD` — locale Y-D-M rompe).
- `FP_FactWebCliEncabezado.LANULADA` es `bit` → comparar `= 0`.
- `/heartbeat` da 500 aunque la base ande (bug SSL propio del repo). DB host real:
  `190.210.23.97:4444` (`NB_WEB`). Ver [[contexto#Bugs conocidos (preexistentes, no del feature)]].

## Ver también
- [[cobros]] · [[arquitectura]] · [[contexto]] · [[changelog]] · [[stack]]
