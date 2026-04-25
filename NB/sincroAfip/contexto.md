# Contexto

## Motivo

El equipo contable de [[NB]] cargaba a mano cada factura recibida. Para cada uno de los 6 CUITs del grupo, alguien entraba a AFIP, filtraba por mes, y copiaba los datos a planillas / sistema contable. Horas-persona recurrentes todos los días.

Este proyecto reemplaza esa tarea: baja automáticamente los recibidos de cada CUIT y los deja en una tabla SQL Server lista para consumir desde el ERP o reportería.

## CUITs del grupo

En `cuits.yaml`:

| CUIT             | Razón social                             | Estado    |
|------------------|------------------------------------------|-----------|
| 30-70924663-8    | NB DISTRIBUIDORA MAYORISTA S R L         | ✅ activo |
| 30-71909207-8    | BLU INC S.R.L                            | ⏸ pendiente |
| 30-71413236-5    | CONSORCIO DE COOPERACION RED DE TECNOLOGIA | ⏸ pendiente |
| 20-26239532-5    | FONTAN SEBASTIAN ANIBAL                  | ⏸ pendiente |
| 30-70881184-6    | MAYORISTA INTEGRAL DE INFORMATICA S.R.L. | ⏸ pendiente |
| 30-71917480-5    | NAEVO S.R.L.                             | ⏸ pendiente |

Todos están bajo la misma clave fiscal (20-26239532-5 / Sebastián Fontán) con permiso de "Mis Comprobantes" en el Administrador de Relaciones.

## Estado actual (2026-04-22)

- Scraper funcionando end-to-end: login → CUIT → Recibidos → CSV → SQL Server.
- Una corrida completa ~20 s por CUIT.
- Idempotencia verificada: re-corridas del mismo rango no generan duplicados.
- Probado con 77 comprobantes reales de NB DISTRIBUIDORA.
- Docker build OK; loader pymssql funciona en Linux (no en macOS sin FreeTDS).

## Pendientes

1. **Activar los otros 5 CUITs** en `cuits.yaml` (flag `activo: true`) — ver [[despliegue]] para el flujo de alta.
2. **Programar cron diario** en el server del cliente. Comando típico: `docker compose run --rm sincro --ultimos-dias 2`.
3. **Alertas de fallo** — wrapper bash que notifique por Slack/mail cuando `sincro.py` devuelve exit 1.
4. **(Opcional, futuro)** Agregar también Emitidos a la misma base. Reutilizaría todo el stack cambiando solo el tab en el scraper + una tabla gemela.

## Cosas que se intentaron y no funcionaron

- **URL directa a Mis Comprobantes** (`/genericos/comprobantes/cliente/default.aspx`): responde 404. La forma correcta es ir por el buscador del portal ARCA, que abre el servicio en pestaña nueva en `fes.afip.gob.ar/mcmp/`. Ver [[arquitectura]].
- **`fill()` directo en el input de fecha:** no funciona; es un daterangepicker.js. Hay que fillear los inputs internos `daterangepicker_start/end` + click `.applyBtn`.
- **Selectores `input[name*='Desde']`**: matchean con "Número desde" (filtro de número de comprobante), no con fecha. Usar XPath relativo al label "Fecha del Comprobante".
- **Guardar el download como `.csv` directo:** AFIP entrega un ZIP. Hay que desempaquetar con `zipfile` primero.
- **pymssql en macOS local sin FreeTDS:** error `symbol not found '_bcp_batch'`. Solución: `brew install freetds` o simplemente usar Docker (Linux).

## Ver también

- [[sincroAfip]]
- [[arquitectura]] — internals.
- [[despliegue]] — operación.
- [[changelog]]
