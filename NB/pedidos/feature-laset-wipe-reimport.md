# Feature: Borrado transaccional comp=11 + reimport limpio

Permite **borrar toda la tajada transaccional comp=11** (pedidos/remitos/asignaciones/stock/facturas — del importador o de carga manual) y reimportar de cero las veces necesarias, desde `/syncLaset`. Mantiene los maestros (articulo, [[feature-laset-fix-marcas-comp11|marcas]], FP_Proveedores, clientes, FP_Almacen, familias) para revincular en el próximo import.

> Flujo de recuperación: **Borrar todo comp=11 → Importar todo** (dos botones separados; "Importar todo" NO borra). Sigue el patrón service-first de [[feature-sync-laset-botones]].

## Componentes

| Pieza | Service | Command | Endpoint |
|---|---|---|---|
| Borrar todo | `WipeTransactionalService` | `laset:wipe-transactional` | `POST /v1/laset/wipe-transactional` |
| Validar stocks | `CheckStocksOrphansService` | `laset:check-stocks-orphans` | `GET /v1/laset/check-stocks-orphans` |
| Limpiar fantasmas | `CleanGhostStocksService` | `laset:clean-stocks-ghosts` | `POST /v1/laset/clean-stocks-ghosts` |
| Drill-down compras/ventas | `ArticleUsageService` | — | `GET /v1/laset/article-usage` |
| Seleccionar/Importar todo | — | — | `GET /v1/laset/selectable-ids?batchId=all` |

## Qué hace el wipe (`WipeTransactionalService`)

Todo en UNA transacción con el trigger `tg_pedclit_cestado_asignacion` deshabilitado. **Snapshot automático `pre_wipe_<ts>`** antes de tocar nada (revertible con `laset:restore`, ver [[feature-laset-snapshot-restore]]). Scope desde `LasetSnapshotRegistry`:

1. **DELETE** pedprot/pedprol/pedproi/pedclit/pedclil/pedclil_oc_asignacion/albprot/albprol/albclit/albclil/registro_stock — **hijos→padres**.
2. **Barrido de huérfanos** (`orphanSweepSpecs()`) — filas comp=11 sin padre que el DELETE por scope no ve.
3. **RESET** stocks comp=11 a 0 (doble filtro articulo.companyCode=11 + FP_Almacen.companyCode=11).
4. **DESVINCULAR** `FP_FactWebCliEncabezado_Uy.ID_NROREMCLI_ENC → NULL`.
5. **Reset staging**: IMPORTED→MATCHED, STOCK_ONLY_SUPERSEDED→STOCK_ONLY, limpia `matched_*`.
6. **Verify post** (scope + huérfanos = 0) + **guard de aislamiento** (cabeceras comp 4/9/12 sin cambios) → THROW+rollback si falla.

## Gotchas clave (bugs reales resueltos 2026-05-31)

### Borrar hijos→padres (el verify por scope es ciego a huérfanos)
Los scopes de los hijos hacen `JOIN` al padre (`pedprol JOIN pedprot WHERE companyCode=11`). Si se borra el **padre primero**, el scope del hijo deja de matchear → el hijo queda **HUÉRFANO**, y el verify post (mismo scope) lo cuenta 0 → **pasa ciego**. Esto acumulaba duplicados en cada wipe+reimport: se llegó a **~42.000 huérfanos** (9973 pedclil, 6086 pedprol, etc.). Consecuencia: Fase D veía "pedclit ya remitido" (albclit huérfano sobreviviente) → **no generaba remito de venta ni descontaba stock** → reconciliación compras−ventas−stock con **miles de grupos delta≠0**. Fix: `array_reverse(DELETE_KEYS)` (hijos→padres, respetando FKs reales `FK_albclil_albclit2`, albprol→albprot, asignacion→pedclil).

### Barrido de huérfanos — identificación segura
- **LÍNEAS** (pedprol/pedclil/albprol/albclil): por `articulo.companyCode=11` + sin padre.
- **CABECERAS** (albclit/albprot): por su **MAESTRO** comp=11 — cliente `clientes.CODEMP=11` (vía `albclit.ccodcli`) / proveedor `FP_Proveedores.companyCode=11` (vía `albprot.ccodpro`) — **NO** por sus líneas, para respetar el orden FK (la línea hija se borra antes que la cabecera).
- Pre-filtro `(companyCode=11 OR NULL)` en cabeceras: un huérfano comp=11 solo puede ser cc=11 o NULL → evita escanear 404k filas y el timeout dblib.
- Para huérfanos cuyo padre-cabecera todavía existe, chequeo al **abuelo** (pedclit/pedprot).
- **Guard de aislamiento**: baseline de cabeceras por empresa antes/después, THROW+rollback si cambia.

### albprot/albprol con companyCode NULL
~11.875 albprot tienen `companyCode=NULL` (legacy). Scopear `WHERE companyCode=11` los deja afuera → sobreviven. El `LasetSnapshotRegistry` ahora scopea `albprot` por `JOIN pedprot ON t.nNumPed = x.nnumped` (nnumped = la orden, único global — **NO** confundir con `nnumalb`, que es la PK del remito) y `albprol` subiendo hasta pedprot. Ver [[relacion-tablas-albprot-albprol]] y [[relacion-companycode]].

### Contaminación que NO se toca
Líneas con artículo comp=11 cuyo padre (orden/remito) es de **otra empresa** NO son huérfanas → el barrido las deja (borrarlas tocaría data ajena). No afectan la reconciliación (que cuenta solo pedprol de pedprot comp=11).

## Seleccionar/Importar todo cross-página

- `SyncLasetSelectableIds` devuelve todos los ids accionables (excluye terminales IMPORTED/IGNORED/STOCK_ONLY_SUPERSEDED) sin paginar; `batchId='all'` en list/summary. Opción "Todos los batches" en la UI.
- **Gotcha frontend**: el computed `selectableIds` NO debe intersectar `selectedRowKeys` contra `this.rows` (solo las 50 filas visibles del `a-table`) — recortaba la selección a lo visible y rompía "Importar todo" (previsualizaba/importaba ~50, síntoma "se van a importar 2098"). Confiar en `selectedRowKeys` y solo descartar terminales visibles. "Importar todo" fuerza `batchId='all'` para no importar 1 batch y dejar el resto (→ duplicación si después se corre Fase C manual).
- **`nnumalb`/`cnumalb` en Fase D**: reservar el próximo desde `MAX` de cabecera **Y** línea (albprot+albprol / albclit+albclil) — había orphans con nnumalb > MAX(albprot) que colisionaban.

## Validar stocks (`CheckStocksOrphansService`)
Detecta caso **A** (artículo comp=11 en almacén ajeno) y caso **B** (artículo ajeno en almacén comp=11). Muestra `cdetalle` + conteo de compras/ventas con drill-down (`ArticleUsageService`, LEFT JOIN + flag `is_orphan` para líneas sin padre). Acción "Limpiar fantasmas" (`CleanGhostStocksService`): borra filas con nstock=0 + nstock_ingresando>0 en almacén ajeno, con backup `laset_ghost_stocks_backup_*`.

## Estado
- Dev reimportado limpio 2026-05-31: **3161 IMPORTED**, reconciliación **0 grupos con delta**. Commits: back `434beff8`, front `15ae1f4` (rama `lasetImportFramework`).
- Falta deploy a prod.

## Ver también
- [[feature-sync-laset-botones|Patrón botones de mantenimiento]]
- [[feature-laset-import|Laset Import Framework]]
- [[feature-laset-snapshot-restore|Snapshot/Restore]]
- [[feature-laset-fix-pedprot-stockonly|Fix bugs históricos Fase C]]
- [[relacion-companycode|companyCode por tabla]]
