# Feature: Fix de bugs históricos en Fase C de Laset Import

> Última actualización: 2026-05-30
> Rama: `lasetImportFramework`
> Commits: `e251a8bd`, `1fb94e42`, `422a3c86`

Tres bugs en `LasetImportFaseCCommand` descubiertos al revisar la operación del 2026-05-29 y 2026-05-30, con sus patches preventivos a futuro + comandos retroactivos para limpiar la data legacy. Ambos comandos preservan la invariante `SUM(pedprol.nCanPed)` por artículo y son **idempotentes**, **dblib-safe**, **transaccionales con rollback en error**.

## Bug A — pedprol no consolidaba por (pedprot, ID_Articulo)

**Síntoma**: cada staging row generaba 1 pedprol independiente. N filas del mismo `(pedprot_key, ID_Articulo)` producían N líneas con el mismo SKU en la misma OC.

**Causa**: `buildPlan()` armaba `$lineas[]` 1×1 con staging row y `executePlan` insertaba pedprol sin agrupar. Sí existía `buildPedclilGroups` (espejo para ventas) pero no había `buildPedprolGroups`.

**Caso reportado**: OC 13669 con 2 líneas del art 122169 (qty=50, qty=10) en lugar de 1 línea de qty=60.

**Fix preventivo** (commit `e251a8bd`): nuevo `buildPedprolGroups()` que agrupa por `(pedprot_key, ID_Articulo)` con FOB ponderado por qty. `executePlan` inserta 1 pedprol consolidada por grupo.

## Bug B — pedprot no se reusaba cross-batch

**Síntoma**: cuando una staging row nueva traía la misma `(proveedor, vendor_pi, vendor_invoice)` que un pedprot ya importado en un run previo, se creaba pedprot duplicado en vez de agregar la línea al existente.

**Causa**: `$pedprotByKey` se armaba solo desde `$rows` (las staging del run actual). Nunca consultaba ERP para detectar pedprot ya creados.

**Caso reportado**: OC 13669 (batch 1) y OC 13916 (batch 6) — mismo proveedor MSI, mismo PI 11179042, mismo invoice 22028796 → debían ser **1 sola OC**.

**Fix preventivo**: nuevo `mergeExistingPedprot()` consulta ERP comp=11 por `(cExped, CSUFAC_TEMP)` y marca pedprot ganadores (menor nNumPed gana cuando hay duplicados pre-fix). `executePlan` skipea `__existing=true`; si la línea consolidada coincide con pedprol pre-existente, UPDATE con suma de qty y FOB ponderado.

**Tablas afectadas al consolidar pedprot**:
- `pedprol.nNumPed` (mover líneas)
- `pedproi.nnumped` (cargos extra como camión)
- `albprot.nnumped` (remitos — `companyCode` puede ser 11 o NULL en data legacy → filtrar por `(companyCode = 11 OR companyCode IS NULL)`)
- `pedclil_oc_asignacion.(n_num_ped_oc, n_linea_oc)` (asignaciones venta↔compra)
- `laset_import_staging.(matched_pedprot_nnumped, matched_pedprol_nlinea)`

## Bug C — stock-only descartado como basura

**Síntoma**: filas con `year=1900` + `customer_invoice` vacío + `vendor_pi+vendor_invoice+sku+qty>0` representan **stock disponible** (la cantidad comprada al proveedor que aún no se vendió). El paso `4a` de `LasetAggregateMatchCommand` las marcaba IGNORED por la regla `year=1900 → basura`, y la pedprol quedaba corta vs la compra física real.

**Caso reportado**: compra de 300 unid del art 122169 (PI 11179042, invoice 22028796) — vendidas 260, stock 40 → la fila de stock (qty=40, id=3703, batch=6) marcada IGNORED → pedprol quedaba en 260 en vez de 300.

**Fix preventivo** (commit `1fb94e42`): nuevo paso `4a-pre` en `LasetAggregateMatchCommand` que reclasifica como nuevo status `STOCK_ONLY` ANTES del barrido de basura. Predicado: `year != 2025/2026 + vpi/vinv/sku no vacíos + qty>0 + customer_invoice vacío + (no SELECTOR, no service-like)`.

**DDL `2026_05_30_001_add_stock_only_match_status.sql`**:
- Amplía `laset_import_staging.match_status` de `NVARCHAR(20)` a `NVARCHAR(30)` (`STOCK_ONLY_SUPERSEDED` tiene 21 chars y no entraba).
- Extiende `CK_laset_staging_match_status` con `STOCK_ONLY` y `STOCK_ONLY_SUPERSEDED`.
- Rollback simétrico en `_drop_`.

**Fase C delega** (commit `422a3c86`): al final de `executePlan`, si hay STOCK_ONLY pendientes, invoca `Artisan::call('laset:fix-stock-only-pedprol', [], $this->getOutput())`. Futuros imports manejan stock-only en una sola corrida sin operación manual.

## Comando retroactivo `laset:fix-pedprot-dup`

Limpia data legacy con los 2 primeros bugs aplicados (`LasetFixPedprotDupCommand.php`).

**Operación**:
1. **Inter-pedprot**: ganador = MIN(nNumPed) por grupo `(cCodPro, cExped, CSUFAC_TEMP)`. Tabla tmp `#pedprol_inter_map(old_nNumPed, old_nLinea, winner_nNumPed, new_nLinea)` con `ROW_NUMBER OVER (PARTITION BY winner ORDER BY old_nNumPed, old_nLinea)` para asignar nLinea contiguo 1..N. **UPDATE pedprol en 2 pasos** con `nLinea = -(new+1_000_000)` como buffer negativo — evita colisión transitoria de PK cuando winner y loser comparten nLineas pre-fix. Re-apunta asignaciones, staging, pedproi, albprot.
2. **Intra-pedprot**: por cada `(nNumPed, ID_Articulo)` con N>1 pedprol comp=11 → ganador = MIN(nLinea). Suma qty, promedia nPreDiv ponderado por qty. Re-apunta `pedclil_oc_asignacion.n_linea_oc` y `laset_import_staging.matched_pedprol_nlinea`. DELETE losers.
3. **Compactación**: re-numera nLinea contiguo 1..N por pedprot tras gaps de DELETE (mismo patrón tmp+buffer).
4. **Verify**: doble invariante `total_qty` + `hash(SUM(art*qty))` debe preservarse exacto → THROW + rollback si difiere. Ver [[memoria#Invariante con hash para fixes destructivos]].

**Estado dev 2026-05-29**:
- pedprot 847 → 478 (234 grupos / 369 losers).
- pedprol 3166 → 1366 (520 consolidaciones / 1464 losers).
- `total_qty=139240` preservada exacta.

## Comando retroactivo `laset:fix-stock-only-pedprol`

Rescata stock-only descartado (`LasetFixStockOnlyPedprolCommand.php`).

**Operación**:
1. **Reclasifica** legacy IGNORED → STOCK_ONLY con el mismo predicado del paso 4a-pre del aggregate-match (paridad dev ↔ prod).
2. **Por (vpi, vinv, sku)**, la fila del **batch más alto** gana (último snapshot del stock real); las anteriores → `STOCK_ONLY_SUPERSEDED`.
3. **Aplica por categoría**:
   - **F** (UPDATE pedprol existente): pedprot+pedprol existen → `nCanPed += qty`.
   - **B** (INSERT pedprol nueva): pedprot existe, pedprol del art no → SKU nunca vendido, toda la compra es stock.
   - **D** (INSERT pedprot + pedprol): nada existe → compra 100% en stock, ningún cliente recibió aún.
   - **C** (skip): SKU/proveedor sin mapa comp=11 → requiere Fase A catálogo.
4. **Stock** (`stocks` + `registro_stock`): tabla tmp `laset_stockonly_delta` con `applyStockDelta` igual patrón que Fase D (doble filtro `articulo.companyCode=11 + FP_Almacen.companyCode=11`, excluye `INTERNAL_NO_STOCK_ARTICULOS` como [[feature-laset-import|FLETE 121944]]).
5. **Verify**: STOCK_ONLY pendientes == `len(C)` skipped + 0 huérfanas.

**Estado dev 2026-05-30**:
- 490 IGNORED reclasificadas → STOCK_ONLY (360 ganadoras + 130 SUPERSEDED).
- F=198 (13.698 unid), B=113 (12.127 unid), D=42 (7.233 unid), C=7 skip.
- **Total: 33.058 unidades restauradas al pedprol comp=11**.
- Caso 13669/art 122169: qty 260 → **300** ✓.

## Orden de deploy a prod

```bash
# 1. Aplicar DDL (extiende CHECK + columna)
# database/sql/2026_05_30_001_add_stock_only_match_status.sql

# 2. Snapshot pre fix-pedprot-dup
php artisan laset:snapshot pedprot_dedup_$(date +%Y%m%d)
php artisan laset:fix-pedprot-dup --dry-run
php artisan laset:fix-pedprot-dup

# 3. Snapshot pre fix-stock-only
php artisan laset:snapshot stockonly_$(date +%Y%m%d)
php artisan laset:fix-stock-only-pedprol --dry-run
php artisan laset:fix-stock-only-pedprol

# 4. Futuros imports → automático vía patch en Fase C
```

Si algo falla: `laset:restore <tag> --force` (ver [[feature-laset-snapshot-restore]]).

## Patrones reutilizables aplicados

1. **Snapshot previo obligatorio**.
2. **Dry-run** que reporta plan sin escribir.
3. **Pre-check THROW** de aislamiento antes de DELETE/UPDATE destructivos.
4. **Tabla tmp + UPDATE FROM JOIN single-statement** (dblib-safe).
5. **Re-numerar IDs con buffer negativo en 2 pasos** (evita colisión PK transitoria).
6. **Doble invariante pre/post**: `total_qty` + `hash(SUM(art*qty))` → THROW si difieren (atrapa bugs sutiles donde una qty se compensa con otra).
7. **Idempotencia**: re-correr sobre data limpia = 0 cambios.

## Ver también

- [[pedidos|Índice del proyecto]]
- [[feature-laset-import|Feature Laset Import Framework]] — contexto del framework completo.
- [[feature-laset-snapshot-restore|Snapshot/Restore Laset]] — reversibilidad total.
- [[feature-asignacion-oc|Asignación OC↔Venta]] — `pedclil_oc_asignacion` que se re-apunta en los fixes.
- [[memoria|Memoria]] — gotchas dblib, NVARCHAR length cap, buffer negativo para renumerar.
- [[changelog#2026-05-29 — Bugs Fase C: pedprot/pedprol duplicados (fix-pedprot-dup)]] — sesión completa.
- [[changelog#2026-05-30 — Bug Fase C: stock-only descartado (fix-stock-only-pedprol)]] — sesión completa.
