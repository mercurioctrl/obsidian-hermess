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

---

## 2026-08-04 — Cache materializado de seriales + connection pool

Reperfilado de la grilla de Stock a 500 filas (el default): **~19s**. Aislado componente por componente contra la DB de prod: **~14s (75%) son los conteos de seriales** (`usedSerialNumbers`/`totalSerialNumbers`, 2 `COUNT(*)` correlacionados por fila sobre `ST_DETALLE_STOCK`, 5.4M filas). El resto (albprol/albclil/RMA/pedprol/saldos) suma ~3-5s. **El índice P2 `(CREF, FECHA_EGRESO)` ya está** y ayuda por-item (1 item = 0.04s), pero contar los ~300k seriales de los 500 items de la página igual cuesta ~14s sobre el server remoto.

### Lo que NO funcionó (probado y descartado)
- **Contar en vivo scoped a la página** (`WHERE CREF IN (500)` + `GROUP BY`): **14s** — el optimizador elige un plan malo con el IN de 500.
- **CTE `GROUP BY` completo + JOIN** (aislado 0.24s, pero dentro del query grande): **8-13s variable**, el plan se degrada.
- **Materializar el `Base` (8 tablas) en `#Page` + batch único**: **8-35s, inestable** — peor que el original. Descartado.
- Conclusión: la variabilidad está en el **plan del `fast_sql`** (el `Base` GROUP BY de 8 tablas re-evaluado por los ~6 OUTER APPLY correlacionados), no en los seriales.

### Lo que SÍ (PR #319): tabla materializada + JOIN
`NB_WEB.dbo.serial_counts (cref, total, usados, updated_at)` — un `GROUP BY CREF` sobre toda la tabla (**~1.2s para 15.445 CREF de todas las empresas**) que reemplaza el conteo en vivo. La grilla hace `LEFT JOIN` a esa tabla chica e indexada, **con fallback** (si la tabla no existe usa el conteo viejo → deploy seguro). Mismo patrón que la cache de competencia. `'usados' = FECHA_EGRESO IS NOT NULL` (idéntico a la subquery vieja, números no cambian). Grilla 500 filas: **~19s → ~9s** (los ~9s restantes son el `Base`+OUTER APPLY, cuello aparte no resuelto).

**Refresco = SP + SQL Agent job** (`scripts/serial_counts_sp_and_job.sql`): `usp_refresh_serial_counts` (crea la tabla si no existe + snapshot `TRUNCATE/INSERT`) + job cada 5 min. **Ya creado y corriendo en prod** (SAFDB2 tiene Enterprise + Agent + 59 jobs, es el patrón que ya usan). Alternativa equivalente: el cron `refresh_serial_counts.py`. La app es agnóstica al mecanismo de refresco.

### Connection pool (PR #320)
`dbconnection()` abría una conexión nueva por llamada → **~116ms de handshake TLS** por request (peor en loops N+1). Ahora **reusa una conexión por thread**: thread-local (uvicorn corre sync en threadpool; pyodbc no se comparte entre threads) + `MARS_Connection=yes` (para que los N+1 con cursor abierto sigan andando) + liveness con `SELECT 1` **solo si estuvo idle ≥20s** (en uso seguido no paga el round-trip) + **no resetea autocommit** (los `finally` de las 23 transacciones ya la dejan limpia). Misma firma → los ~154 call-sites no cambian. Medido: 50 llamadas reusando ~0ms (vs ~5.8s con handshakes). El pool le ahorra poco a las **grillas** (1 conexión/request); el beneficio grande es en endpoints N+1. **Validar en gamma bajo carga real (writes concurrentes) antes de prod.**

## Ver también

- [[modulo-seriales]] · [[modulo-precios]] · [[changelog#2026-08-04 — Fixes de grilla/datos, performance de Stock, y correcciones de OC en prod|changelog 2026-08-04]] · [[inventario]]
