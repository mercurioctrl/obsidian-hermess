# Feature — Stock por almacén Laset (comp=11): depósito por línea

Corrige los **stocks negativos por almacén** de la operación Laset (`companyCode=11`):
arregla la causa en el importador y provee un comando retroactivo para los datos ya cargados.
Doc de repo: `docs/laset-stock-almacen.md`.

## Síntoma
Un artículo comp=11 con `stocks.nstock < 0` en un almacén (DOM/GRI) y sobrante en otro. El
**total por artículo está bien** (`ingreso albprol − egreso albclil`); lo mal repartido es entre
almacenes. Ej. `G5060-8S2C` (121964): antes DOM 921 / GRI **−88** / total 833 → después DOM 821 / GRI 12 / total 833.

## Causa raíz (importador)
En [[feature-laset-import|Fase C]] (`LasetImportFaseCCommand`), el `pedclil` heredaba el
`ID_ALMACEN` del **encabezado** del pedido (`pedclit`, que toma el `deposito` de la **primera
fila**), no el `deposito` de **cada línea**. Un pedido al cliente que **mezcla depósitos** dejaba
las líneas de otro depósito en el almacén equivocado. La compra (`pedprol`/`albprol`) sí respeta
el depósito por línea → solo las **ventas** se descuadraban. Mapeo `deposito → ID_ALMACEN`:
`DOMESTIC MIAMI=9, GRIS=10, BONDED*=11, URUGUAY=14, ASIA=15`.

### Fix en el importador
- El `deposito` por línea entra en la clave de `buildPedclilGroups`: `pedclit_key | ID_Articulo | ID_ALMACEN`.
  Un mismo SKU vendido desde dos almacenes en el mismo pedido genera **dos pedclil** (cada una en su almacén).
- El INSERT de `pedclil` usa `$g['ID_ALMACEN']` (no `$pedclit['ID_ALMACEN']`).
- Linkeo de asignación (4c) y `dupLinkFromLine`/4d incluyen el almacén en el group key (fallback por prefijo).

## Comando retroactivo `laset:fix-stock-almacen-comp11`
`{--dry-run}`, comp=11 only, idempotente. Pasos (1 transacción):
1. **Almacén correcto por (cnumped, ID_Articulo)** desde el staging (`matched_pedclit_cnumped` + `matched_pedclil_id`; dominante si mezcla).
2. **Re-apunta** ventas desalineadas (`UPDATE pedclil.ID_ALMACEN` por id, `UPDATE albclil.ID_ALMACEN` join a `albclit`) moviendo stock por **DELTA exacto** (NO recomputa desde albprol−albclil — arrastraría desajustes previos).
3. **Balancea** negativos remanentes con **transferencias inter-depósito** (mueve stock del almacén con sobrante al negativo, mismo artículo) — representa transferencias físicas Miami no registradas en la planilla.
4. **Invariante**: stock total por artículo no cambia (THROW + rollback).

Wireado a `laset:run-import-job` (paso 3.6) → **wipe+reimport lo corre solo**. Snapshot cubre
`stocks`/`pedclil`/`albclil`/`albclit` (`laset:snapshot` / `laset:restore --force`). Aplicado dev: **14 → 0 negativos**.

## Gotcha planilla-vs-físico (distinto)
El total comp=11 = lo que dice la planilla (comprado − facturado). Si el "archivo descargado"
(físico) difiere (G5060: 921 vs 833), es una **compra real no registrada en la planilla**, NO un
bug del import (reproduce fiel la planilla). **No detectable desde la DB** — cruzar `stock_comp11.csv`
(218 artículos por SKU/modelo + por almacén) contra el archivo físico.

## Ver también
[[feature-laset-import]] · [[feature-laset-fix-albprol-faltante]] · [[relacion-tablas-stocks-almacen]] · [[changelog]] · [[pedidos]]
