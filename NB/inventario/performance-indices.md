# Performance e índices — análisis con el DMV real

Auditoría de performance del backend (2026-06-27). El login `web` tiene
`VIEW SERVER STATE` → se consulta `sys.dm_db_missing_index_*`, que da recomendaciones
según la **carga real de producción** (más confiable que inferir por código). El SQL
Server es **Enterprise Edition** → los índices se crean con `ONLINE=ON` (sin bloqueo).

## Tamaños de las tablas calientes
`ST_DETALLE_STOCK` 5.4M · `ST_REMITOS_VENTA_DETALLE_SALIDA` 4.77M · `registro_stock`
2.7M · `albclil` 1.28M · `albclit` 402k · `FP_FactWebCliEncabezado` 373k ·
**`articulo` 25.7k** (escanearla es barato) · `stocks` 29k · `ST_RMADETALLE` 58k ·
**`FP_Empresas` 11 filas**.

## Índices P1–P3 (aplicados en prod, ONLINE=ON)
Script idempotente: `ms-metadata/scripts/perf_indexes_p1_p3.sql` (crea-antes-de-dropear).

| | Índice | Beneficiario | Antes → Después |
|---|---|---|---|
| **P2** | `ST_DETALLE_STOCK (CREF, FECHA_EGRESO)` | **Grilla de Stock** (conteos used/total de seriales por fila) | **1.63s → 0.54s (−67%)** |
| **P3** | `ST_REMITOS_VENTA_DETALLE_SALIDA (SERIAL, HORA_EXACTA DESC) INCLUDE (REMITO_FP, SUCURSAL_REMITO, ULTIMO_RETORNO)` | Modal de seriales (OUTER APPLY TOP 1) | 0.71s → 0.61s (−14%) |
| **P1** | `albclit (dfecalb) INCLUDE (cnumalb, cnumped, cnumsuc, ID_NROREMCLI_ENC, ntipoalb, lfacturado)` reemplaza el key-only `idx_albclit_dfecalb` | Reportes/sync por fecha (NO la grilla) | 0.081s → 0.082s (neutro) |

**P2 fue el gran win.** P1 tiene el score DMV más alto del sistema (~298M) pero es
**impacto agregado por frecuencia** (267k seeks), no un fix por llamada; y **no toca la
grilla** (la grilla joinea `albclit` por su PK `ID_NROREMCLI_ENC`, no filtra por `dfecalb`).

## Lección: el refactor de subqueries con IN se probó y se REVIRTIÓ
El análisis estático marcó las subqueries escalares post-paginación de
`get_items_stocks` (conteos de seriales, RMA, pedprol, regularizaciones) como problema.
Se implementó el batch con `IN` sobre los ids/crefs de la página + dicts: **byte-idéntico
pero 2.5–3.7× MÁS LENTO** (Path A 1.68→5.59s, Path B 3.17→7.98s). Causa: las subqueries
inline corren server-side en **un round trip** y pegan a tablas indexadas (baratas);
batchear agrega 4 round trips que sobre el link **TLS 1.0** a prod pesan mucho. **Mismo
síntoma, solución opuesta**: el fix correcto era el índice P2, no reestructurar. Revertido.
> Regla: medir SIEMPRE contra la DB real antes de asumir. Comparar viejo vs nuevo con
> `git show HEAD:archivo.py > _temp.py` e importar ambas versiones.

## Fix de código aplicado: N+1 de conexiones en selldiscount
`get_current_cost(item_id, cursor=None)` ahora reutiliza el cursor del loop
`sync_up_sell_discounts` (antes abría una conexión TLS nueva por acción).

## No sobre-optimizar
- `CAST(C.CODEMP AS INT) = A.companyCode` (CODEMP nvarchar(2) vs companyCode int) es
  conversión real PERO `FP_Empresas` tiene **11 filas** → impacto nulo (prolijidad, no perf).
- `LIKE '%texto%'` en `cDetalle` no es sargable, pero `articulo` es chica y el match
  parcial es el comportamiento buscado.

## Ya bien optimizado (no tocar)
`albclil` tiene `IX_albclil_ID_Articulo_ID_ALMACEN_salesReserved`; el RMA-match del modal
de seriales es 1 query + dicts; `products.searchProducts` usa `getImagesBulk`;
`competition._fetch_search_keys` es bulk `IN`. Ver
[[arquitectura#Grilla de Stock — fast-path de performance]] y [[contexto]].

## Ver también
- [[modulo-seriales]] · [[arquitectura]] · [[changelog]] · [[memoria]] · [[inventario]]
