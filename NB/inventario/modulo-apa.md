# Módulo APA — AMD Price Adjustment (Soportes)

**APA** = aporte promocional temporal que AMD (vía distribuidor) otorga para **bajar el
costo efectivo** de ciertos procesadores por un período y/o cantidad, permitiendo un
precio de venta más competitivo. Al terminar, el costo vuelve a su valor normal. En la UI
la sección se llama **"APAs/Soportes"**.

Regla de negocio clave: **no se distorsiona el costo base histórico**. El APA es una capa
reversible sobre `NCOSTEPROM`. Un artículo puede tener **varios APAs, solapados, que se
SUMAN**.

## Datos — `NB_WEB.dbo.st_apa`

Una fila por APA (ver `ms-metadata/scripts/apa_schema.sql`; el controller la crea en
runtime con `_ensure_table` / `_ensure_cron_columns`, patrón de `new_sku_notifications`).

- Identidad/negocio: `ID_ARTICULO`, `cRef`, `companyCode`, `monto_unitario`, `moneda`
  (default `USD`), `fecha_desde`/`fecha_hasta`, `unidades_totales`/`unidades_usadas`
  (cupo), `proveedor`, `observaciones`, `estado` (`pendiente`|`activo`|`finalizado`),
  `anulado` (baja lógica).
- Estado del job (cron): `monto_aplicado_usd`, `ncosteprom_al_aplicar`,
  `ncosteprom_al_finalizar`, `fecha_aplicado`, `fecha_finalizado`, `revision_manual`,
  `motivo_revision`.

## Backend (`ms-metadata`)

- Controller `core/controllers/apa/apa.py`: `create_apa`, `get_apas` (listado con filtros
  companyCode/itemId/search/estado/vigente/proveedor), `update_apa`, `delete_apa` (anula),
  y `get_active_apa_map` (SUMA de APAs vigentes por artículo).
- Modelos `core/models/apa.py`: `ApaCreateRequest` / `ApaUpdateRequest` (fechas ISO
  `YYYY-MM-DD` a propósito, para evitar el lío DD-MM-YYYY → SQL Server).
- Rutas en `main.py` (`Depends(JWTBearer())`): `GET /apa`, `GET /apa/active`, `POST /apa`,
  `PATCH /apa/{id}`, `DELETE /apa/{id}`.

## Job / cron — el "cambio temporal" del costo

`run_apa_job.py` → `core/controllers/apa/apa_job.py:run_apa_job` (por crontab, ej. cada
15 min, desacoplado de FastAPI). En cada corrida:

1. **Reconcilia cupo**: cuenta ventas del artículo desde `fecha_desde` (`albclil` +
   `albclit.ntipoalb > 1`) → `unidades_usadas`.
2. **Activa** los `pendiente` vigentes con cupo: `NCOSTEPROM -= monto` (en USD).
3. **Desactiva** los `activo` vencidos / sin cupo / anulados: `NCOSTEPROM += monto`.

**Modelo incremental +/-**: cada APA resta su monto al activarse y suma el MISMO monto al
finalizar → el descuento efectivo del artículo es la suma de los APAs activos, aunque se
solapen, y al terminar todos vuelve **exacto** al costo base (verificado sin drift).

- `NCOSTEPROM` está en **USD** (≈ FOB); un APA en ARS se convierte con la cotización
  `PESOSLO`.
- Todo cambio se audita en `NB_WEB.dbo.historial_costos`. La **tarea de recálculo de
  precios existente** (lee `NCOSTEPROM`) acomoda los precios sola, en ambos sentidos —
  el job NO toca precios.
- **Testigo de interferencia**: si al finalizar el `NCOSTEPROM` no coincide con lo
  esperado (`ncosteprom_al_aplicar - monto`), suma igual el monto pero marca
  `revision_manual` y avisa por mail al PM (reusa `notifications/sku_notifications`).
- Idempotente, transacción por APA.

## Frontend (`inventario-web-app`)

- Sección **"APAs/Soportes"** (`pages/apas.vue`, `store/apa.js`, `components/Filters/Apa.vue`,
  `components/Modal/apa/CreateEdit.vue`, pestaña en `components/Table/TabMenu.vue`):
  listado + filtros (búsqueda, proveedor, vigencia) + alta/edición (buscador de artículo,
  monto, moneda, rango de fechas, cupo, proveedor).
- Columna **seleccionable "APA (u.)"** en la grilla de Precios (`store/itemsPrices.js`,
  `pages/itemsPrices.vue`): muestra la **suma** de APAs vigentes del item con badge ×N si
  hay solapados; se trae por `GET /apa/active` y se mergea por itemId (no bloquea el
  render). Ver [[modulo-precios]].

## Fases (todas hechas)

1. Backend CRUD `/apa` (PR #335/#336). 2. Sección APAs (front). 3. Columna en Precios
(PR #337). 4. Job de cron (`feat/apa-cron`). Rename a "APAs/Soportes"
(`feat/apa-rename-soportes`).

## Ver también
- [[modulo-precios]] — la columna APA vive en la grilla de Precios; el costo que baja el APA alimenta el cálculo de precios.
- [[contexto]] — moneda de NCOSTEPROM, gotchas.
- [[changelog]] — cronología.
