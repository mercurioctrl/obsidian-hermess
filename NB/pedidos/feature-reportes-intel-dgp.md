# Feature: Reportes Intel DGP-S

Genera los dos archivos CSV que **Intel exige a New Bytes como distribuidor** dentro del programa **DGP-S** (Distributor... reporting de inventario y sell-out): reporte de **inventario** de procesadores Intel en stock y reporte de **sell-out** (ventas a resellers) en un período. Los CSV se suben a `public/downloads/` y se devuelve la URL de descarga.

## Endpoints

| Método | Ruta | Parámetro | Salida |
|---|---|---|---|
| GET | `/v1/reports/intel/dgp/inventory` | `date` (opcional, default hoy) | `Inventory_Intel_DGP-S_{YYYYMMDD}.csv` |
| GET | `/v1/reports/intel/dgp/salesout` | `between=YYYY-MM-DD_YYYY-MM-DD` (requerido) | `Salesout_Intel_DGP-S_{desde}_{hasta}.csv` |

Ambas bajo el grupo `permission`. Respuesta JSON: `{success, fileName, rows, warnings[], path}` (salesout agrega `skipped`).

## Capas

- **Controller:** `app/Http/Controllers/Report/IntelDgpController.php` — sube límites de memoria/tiempo, valida `between`, limpia `downloads/` viejos (`cleanDownloadSpace`, >12 h) y delega en el service.
- **Service:** `app/Services/Report/IntelDgpService.php` — arma el CSV, headers fijos, el mapeo de part numbers y los warnings.
- **Repository:** `app/Repositories/Report/IntelDgpRepository.php` — las dos queries SQL contra el ERP.

## Fuente de datos (ERP)

Ambas queries filtran **marca Intel = `NB_WEB.dbo.marcas.id = 39`**.

- **Inventory:** `NewBytes_DBF.dbo.articulo` join `stocks`, sólo `ID_PRODUCTO LIKE 'BX%'`, `EXCLUIR <> 1`, `id_distribuidora = 1`, `nstock > 0`. Devuelve `partNumber` (= `ID_PRODUCTO`) y `qtyOnHand`.
- **Salesout:** parte de `albclil` (líneas de remito) → `articulo`, `albclit`, `clientes`, `FP_FactWebCliEncabezado/Detalle`, `poblac`, `FP_Provincias`. Filtra facturas no anuladas, `ntipoalb > 1`, por rango `dfecfac`. Mapea columnas a los códigos que pide Intel (`B01`, `B03`, `B19` = part number, etc.).

## Mapeo de part numbers → nombre de CPU (⚠ hardcodeado)

`IntelDgpService::PART_NUMBER_MAP` es una **constante PHP, NO una tabla de BD**. Diccionario `part number BX → nombre comercial del procesador`, que llena la columna **CPU** (inventory) / **Product Description** (salesout).

- Si un `ID_PRODUCTO` empieza con `BX` (procesador Intel con stock) pero **no está en el diccionario**, la columna sale vacía y se agrega el warning `"Part number sin mapeo en tabla: {SKU}"`. El CSV se genera igual.
- **Mantenimiento:** al aparecer un warning hay que agregar el SKU a mano en la constante, con el nombre oficial de [Intel ARK](https://ark.intel.com). No hay seeder ni migración.

### Historial de altas al mapeo

- **2026-09-10** — se agregaron 4 SKU que tenían stock y salían sin descripción:
  - `BX8071514100` → **Intel Core i3-14100** (¡es i3, no i5!)
  - `BX8071514900K` → Intel Core i9-14900K
  - `BX8071514900KF` → Intel Core i9-14900KF
  - `BX80768250K` → **Intel Core Ultra 5 250K Plus** (nombre oficial lleva "Plus")
  - Rama `feature/intel-dgp-partnumbers`, commit `840c65ed`. PR contra `Development` y `blu-dev-staff`.

## Warnings del salesout

Además del part number, salesout valida y **excluye** filas: cliente sin domicilio/ciudad, fecha futura. Avisa (sin excluir) si `B23` ≠ `B39` o si el part number no matchea `^BX...`.

## Configuración

- `INTEL_CMF_ID` en `.env` — número de partner/CMF de New Bytes ante Intel. Si falta, el inventory devuelve error.

## Ver también

- [[relacion-tablas-articulo-stocks|Artículo y stocks]] — maestro y balance por almacén que alimenta el inventory
- [[relacion-tablas-ped-alb|Ventas: pedclit/pedclil/albclit/albclil]] — origen del salesout
- [[relacion-companycode|companyCode por tabla]]
- [[changelog#2026-09-10 — Reportes Intel DGP-S: completar mapeo de part numbers]]
