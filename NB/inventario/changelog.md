# Changelog — inventario

## 2026-07-02 — Merge a `development` + nuevo backend de DB (Linux)

Sesión operativa en Linux (`/var/www/nb/inventario`), sin cambios de código propios.

- **Merge integrado**: la tanda de `regularizacion-stock` ya está **mergeada a `development`/`Development`** en ambos repos (front `Merge PR #388`, back `Merge PR #288`). Ya no hace falta abrir PR: es la versión vigente en `development`.
- **Cambio de rama**: ambos repos movidos de `catri-fine-tuning` → `development` (front) / `Development` (back, con mayúscula). No había commits locales pendientes; solo `.env` local y `ms-metadata/docs/` sin trackear (se preservaron).
- **Nuevo backend de DB**: `.env` del back apunta ahora a `10.10.10.47,1433` con usuario `cmercurio` (antes `190.210.23.97,4444` / `emanzando_devweb01`, que sigue siendo alternativa válida). Login verificado `HTTP 200`.
- **Gotcha confirmado**: cambiar la DB en `.env` NO se aplica con `--reload` (uvicorn vigila `.py`, no relee `load_dotenv()`) → hay que reiniciar el proceso uvicorn. Ver [[contexto]].

Servicios locales levantados y verificados: front `:3000` (Nuxt, rama `development`), back `:8000` (FastAPI, DB nueva).

## 2026-06-29 — Commits + push de la tanda a `regularizacion-stock`

Toda la tanda quedó **commiteada y pusheada** a `regularizacion-stock` en ambos repos
(sin `Co-Authored-By`, regla del usuario). Lista para PR a `Development`/`Gamma`.

**ms-metadata** (`7f67d7b..bf2c8d1`):
- `4af6e9e` feat(competition): cache materializada `scrap_competition` + cron — ver [[competencia-partpicker-cache]]
- `a3cb2e2` feat(stock): modal de seriales (docs/RMA/compra) + visibilidad masiva + competencia en grilla — ver [[modulo-seriales]]
- `cba3c13` perf(selldiscount): reutilizar cursor en `get_current_cost` (N+1) — ver [[performance-indices]]
- `bf2c8d1` chore(perf): script de índices P1–P3 — ver [[performance-indices]]

**inventario-web-app** (`653c025..481be0f`):
- `046dd4d` feat(stock): mejoras de grilla (ID/sticky/orden/ocultar masivo/filtro rápido/tooltip Δ) + modal de seriales
- `724fc19` feat(precios): competencia en grilla + filtro rápido por título + export
- `481be0f` fix(ui): cortar palabras solo en espacios en todas las tablas

Sin commitear (a propósito): `.env`, `.DS_Store` y scripts ad-hoc de diagnóstico
(diag/run/sweep/worklist + CSVs). Los índices P1–P3 son **DDL en prod, fuera de git**.

## 2026-06-27 — Modal de seriales (documentos/RMA/cambios/compra) + índices de performance en prod

Sesión sobre `ms-metadata` e `inventario-web-app` (cambios locales sin commit, salvo
los **índices aplicados en prod**). Ver [[modulo-seriales]], [[performance-indices]] y [[memoria]].

### feat: modal de seriales clickeable (front + back)
Click en las celdas de Seriales abre `Modal/ItemStock/SerialsById.vue` con la lista de
seriales del artículo. `get_item_serials` reconstruye por serial: estado, devuelto, y la
cadena **serial → RVD → albclit → factura/NC + pedido**. Columnas, filtros en vivo, chips
de conteo, paginación + "Ver todos", export CSV/XLSX. Detalle en [[modulo-seriales]].

### fix: el modal mostraba "todos despachados" / total inflado
(1) `GET /serials/{itemId}` serializaba solo 6 campos a mano → el front nunca recibía
`present` → todo "despachado". (2) los LEFT JOIN multiplicaban filas. Fix: serializar el
objeto completo + `OUTER APPLY ... TOP 1` (última salida) → 1 fila/serial. Item 118151:
1945→1943, en stock 0→217.

### feat: Cambio RMA (reemplazo ↔ reemplazado) + columna Compra
`ST_RMADETALLE` (ID_ACCION=2) = serial devuelto; `ST_DETALLE_STOCK.ID_RMACLIENTE` = RMA
del reemplazo. Cruzados marcan "reemplazó a X" / "reemplazado por Y" (UNA query + dicts;
la correlacionada tardaba 12.6s → 1.1s). **Compra** = `ID_COMPRA` a 8 dígitos (13191 →
`00013191`).

### fix global: las palabras solo cortan en espacios (todas las tablas)
Regla en `assets/ant/main.less` que sobrescribe `.ant-table-row-cell-break-word`
(`word-break: break-all` de antd) con `word-break: keep-all; overflow-wrap: normal`. Un
token sin espacios queda en una línea en vez de partirse a la mitad.

### perf: análisis de índices (DMV real) + P1–P3 aplicados en prod (ONLINE=ON)
Con el DMV de missing indexes (login `web` tiene VIEW SERVER STATE) + Enterprise Edition:
**P2 = gran win, grilla de Stock 1.63s → 0.54s (−67%)**; P3 modal seriales −14%; P1 (albclit
covering dfecalb) neutro por-query, gana en agregado. Ver [[performance-indices]].

### lección: refactor de subqueries con IN — probado y REVERTIDO
Batchear las subqueries escalares post-paginación de `get_items_stocks` con `IN` resultó
**2.5–3.7× más lento** (round trips sobre TLS 1.0). El cuello era real pero el fix correcto
era el **índice P2**, no reestructurar. Revertido (byte-idéntico).

### fix: N+1 de conexiones en selldiscount
`get_current_cost` abría una conexión TLS nueva por acción en `sync_up_sell_discounts`;
ahora reutiliza el cursor del loop.

### UX: tooltip en la columna Δ ser. de la grilla
Header con ícono ℹ y tooltip: `Δ ser. = Disponibles − Stock del sistema`; 0 = cuadra,
≠0 = discrepancia ledger↔columnas; solo aplica a artículos que serializan.

## 2026-06-26 (cont.) — Filtro distribuidora en grillas + fix delta "nonzero" + worklist recuento

Sesión sobre `ms-metadata`. Commits en `regularizacion-stock` (pusheados). Ver [[modulo-regularizacion]], [[regularizacion-buckets]] y [[memoria]].

### feat(stock): ocultar distribuidoras 2/3/4 de Stock y Precios (commit 923a783)
Pedido del usuario: las grillas de **Stock y Precios nunca muestran** `articulo.id_distribuidora IN (2,3,4)` (solo 1/NULL). Filtro `AND (A.id_distribuidora IS NULL OR A.id_distribuidora NOT IN (2,3,4))` tras cada `WHERE A.EXCLUIR=0` en `stocks.py` (7 queries: count ×2, prices_grid, get_items_stocks ×4 ramas). Counts y exports lo heredan. Count cc4: 13.078 → 5.309. Si un item "no aparece", chequear su `id_distribuidora`.

### fix(stock): aceptar delta=nonzero en /itemsStocks (commit 7f67d7b)
El filtro **"distinto de cero"** rebotaba con 400: el front mandaba `nonzero` y los controllers ya lo resolvían (`DELTA <> 0`), pero la **validación del endpoint** en `main.py` solo permitía `positive/negative/neutral`. Se agregó `nonzero` a la whitelist. cc4 ahora: 896 items con delta ≠ 0.

### Worklist de recuento físico (cc4)
Items serializados donde `stock_columnas != seriales_presentes` → solo el conteo físico resuelve. **GOTCHA**: el criterio crudo da 1.033 pero la mayoría son **ledgers rotos** (presentes inflados de legacy, ej. 8.090 fuentes). Filtrando por contable (`max(stock,ser)<=50`): **721 contables = 66 "stock fantasma/sobreventa" (prioridad) + 655 sub-cargado**; **313 ledger-roto** quedan fuera (arreglo de ledger, no recuento). CSV en `/Users/hermess/www/inventario/ms-metadata/worklist_recuento_cc4.csv` (generador `worklist_recuento_cc4.py`).

## 2026-06-26 — Corrección de ACREDITADO (NC fantasma) vía NC real FP_FactWebCli

Sesión sobre `ms-metadata` (scripts ad-hoc, sin commit). Limpieza documental del delta+. Ver [[modulo-regularizacion]] y [[memoria]].

### Fuente de la NC real (dato del usuario)
Las notas de crédito viven en `NewBytes_DBF.dbo.FP_FactWebCliEncabezado` + `FP_FactWebCliDetalle`, vinculadas a `albclit` por `ID_NROREMCLI_ENC`; **`NTIPODOCU=2` = Nota de Crédito** (`LANULADA` bit). La cantidad realmente acreditada por artículo = `SUM(FP_FactWebCliDetalle.NCANENT)` de las NC del remito. (El archivo viejo `MS_NOTASCREDITO_*` termina abril-2021 y NO sirve.)

### feat: `apply_acreditado_correction` (regularization.py) — aplicado en prod
- Corrige `albclil.ACREDITADO` mal cargado (> lo realmente acreditado) que infla el delta+ con crédito fantasma. Key = `IdDetalleRemito` (único por línea). Recalcula el valor autoritativo EN VIVO desde la NC real; dry-run, idempotente, gateada por `gerencia`, traza en `registro_stock`. NO toca la NC real ni AFIP (solo el campo denormalizado del lado stock).
- **Aplicado (Catriel 7463): 88 líneas / 772 u** de crédito fantasma removido → 0 líneas imposibles en cc4. 65 corregidas a su NC real, 23 capeadas a `ncanent`.

### Landmine evitado (clave)
El alcance seguro es SOLO `ACREDITADO > ncanent` (imposible: acreditás más de lo vendido). El primer dry-run con `ACREDITADO > nc_real` explotó a **2.615 líneas / 9.105 u** porque el enlace FP_FactWebCli es **incompleto** (la mayoría de los ACREDITADO no encuentran su NC) → "sin NC ⇒ corregir a 0" es FALSO en general. Regla segura: NC real si existe, si no **cap a `ncanent` (nunca 0)`**. Bajar ACREDITADO baja el +creditNote → algunos items quedan delta negativo (benigno).

### Entregable a contabilidad
CSV `nc_errores_acreditado_cc4.csv` (88 líneas, `cliente`, `acreditado_correcto_NC`, `corregir_a`, `error_infla_delta`).

## 2026-06-25 (tarde) — Regularización: gap serial↔columnas a Control + cola OC 11568 + barrido cc4

Sesión sobre `ms-metadata` (scripts ad-hoc, sin commit). Continuación de la regularización de stock. Ver [[modulo-regularizacion]] y [[memoria]].

### feat: `apply_serial_gap_to_control` (regularization.py)
- Cierra el delta+ residual reponiendo a **Control** (`nstock_ctrl`) el **gapFísico** = `seriales_presentes − columnas_stock` por depósito, **sin depender del universo del race** (`_compute`/`DELTA_RACE`). Generaliza la Acción 1 para la cola de la restauración de albprol. Tope = delta canónico actual (no sobre-corrige), dry-run por defecto, idempotente (marcador `MARCADOR_SERIAL_GAP`), gateada por `gerencia`. Usa `COUNT(DISTINCT SERIAL)`.
- **Test de "gap limpio" (3 identidades del ledger)** para saber si un delta+ es seguro de reponer: `albprol==filas_serial`, `egresados==ventas+RMA−notasCrédito` (¡incluir NC: las devoluciones re-ingresan el serial!), `presentes==albprol−ventas−rma+nc`, y `delta==presentes−columnas`. Si los 4 cierran, el descuadre vive solo en columnas.

### Cola de OC 11568 cerrada (aplicado en prod, agente Catriel 7463)
- **4 limpios** (119143:60, 119760:2, 118920:1, 118963:1 = 64 u) → delta 0.
- **111454** (+88): repuestos 19 físicos (→69); el resto 69 es **documental**, NO físico. Hallazgos: (a) la "reg +983" de la memoria vieja **no existe** (eran movimientos `nstock→nstock_d1`); (b) el usuario corrigió la **NC de 2022** (`X000200545212`, `ACREDITADO 100→10`, error de carga de 90 u) → delta 69→**−21**; (c) el −21 NO es albprol restaurable: el cruce serial(`ID_COMPRA`)↔albprol(`albprot.nnumped`) por orden muestra que el albprol **ya existe**, solo mal numerado en la era vieja (4.277 u de seriales sin albprol espejadas por 4.705 de albprol sin seriales → neto +17). Estado sano: `columnas=977==presentes`.

### Barrido "gap limpio" cc4 (aplicado en prod)
- De **2.751** items cc4 con delta>0, solo **150 "gap limpio"** (test de 3 identidades). Aplicados: **143 cerraron a delta 0**, 355 u a Control, **0 negativos**. 7 residuos legacy (101484, 6816, 6814...) tienen filas de serial **duplicadas/blank** presentes (item viejo) — el barrido las contó con `COUNT(*)` e infló el gap; la función (`COUNT(DISTINCT SERIAL)`) repuso solo el real → residuo = duplicados fantasma. **Gotcha**: el barrido debe contar presentes con `COUNT(DISTINCT SERIAL)` (corregido). Los 2.601 restantes son causas documentales/re-tagueo (no tocar).
- Total del esfuerzo: **170 items** (24 auto_stock + 5 cola OC 11568 + 143 barrido) con stock vendible realineado a la verdad física de seriales.


## 2026-06-25 — Documentación: origen del FOB + verificación de merge

Sesión de documentación/sync (sin commits). Ver [[memoria]] y [[modulo-precios#Columnas de costo: FOB vs NCOSTEPROM]].

- **Documentado el origen del costo FOB** de las grillas Precios y Stock: `NewBytes_DBF.dbo.albprol.nprediv` de la **última línea de albarán de proveedor** (`OUTER APPLY ... JOIN albprot ON nnumalb WHERE albprol.cref = articulo.cref ORDER BY albprot.dfecalb DESC`). Idéntico en `prices.py` y `stocks.py`. Distinto de `NCOSTEPROM` (costo promedio, base del cálculo de precios). Un `albprol` backdated no mueve el FOB (usa el albarán más reciente).
- **Verificado que `catri-fine-tuning2` YA está mergeada** a `Development`/`Gamma` en ambos repos (PRs #377 front / #274 back; `origin/Development..catri-fine-tuning2` vacío). Corregida la memoria que aún la marcaba "sin mergear". Las ramas locales quedaron atrasadas.


## 2026-06-24 — Fixes: memory leak (Stock) + upsert de utilidades + subcolumnas seriales

Continuación sobre la rama `regularizacion-stock` (front `653c025`, back `f3954fa`). Ver [[memoria]] y [[modulo-precios]].

### fix: utilidad/precio no persistía en items sin fila en ST_GANANCIA (backend)
- Marcar un precio o utilidad a un artículo que **aún no tiene fila** en `NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS` fallaba **en silencio**: `_update_gain_column` hacía un `UPDATE ... WHERE ID_ARTICULO=?` puro → 0 filas afectadas, sin error (`success:true`), pero la utilidad no se guardaba. El precio sí se escribía en `articulo` → inconsistente (al releer la grilla la utilidad volvía a 0). Afectaba edición de utilidad **y** de precio (la inversa `update_item_price_by_target` delega en el mismo punto).
- **Fix**: `_update_gain_column` ahora es **upsert** — si el UPDATE afecta 0 filas, inserta la fila completa sembrada desde `simulated_gains` (`GAIN_COLUMNS`, las 9 que lee `_fetch_gain_margins`), consistente con el precio recién calculado y cubriendo las 3 columnas `NOT NULL` (`PORC_GANAN_ESTIPLO/LO1/CF`). Para items con fila existente el camino es idéntico. Validado con UPDATE+INSERT dentro de una transacción con `ROLLBACK` (sin escribir en prod). Había **432 artículos** (los más nuevos) sin fila.
- Datos de la tabla: **sin PK**; clave = `articulo.cRef` (nvarchar, no el int `ID_ARTICULO`; hay valores legacy no numéricos como `'ACARREO'`).

### fix: memory leak en la grilla de Stock (frontend)
- `setScroll()` reasignaba `window.onscroll` en **cada** evento de scroll (closure nueva por evento) y además estaba registrado como listener de `scroll` → handler duplicado; el `window.onscroll` tampoco se limpiaba en `beforeDestroy`. Ahora `setScroll` solo actualiza `scrollY` (el listener ya está vía `addEventListener`/`removeEventListener`).
- Auditoría de RAM del front: el consumidor dominante es la grilla de Stock **sin virtualización** (`scroll.y` comentado) → 500 filas × ~50 columnas en el DOM. La virtualización (copiar el patrón de Precios) queda como cambio aparte por el riesgo de alineación antd 1.x.

### feat (post-23): subcolumnas de Seriales + Últ. ingreso/venta + fix búsqueda con paréntesis
- **Seriales** pasó a columna agrupada con 3 subcolumnas: **Us/Tot** (usados/total), **Disp.** (presentes = total − usados) y **Δ ser.** (presentes − stockTotal; verde si 0, rojo si ≠0). Toggleables y persistidas. (web `0dbaeef`)
- Columnas **Últ. ingreso / Últ. venta** también en Stock (de `articulo.ULTIMO_INGRESO`/`ULTIMA_VENTA`). (web `86f3108`)
- **Búsqueda tolerante a paréntesis/símbolos** en Stock, Precios y Productos: el slug `procesador_intel_lga1700...` no matcheaba "PROCESADOR INTEL (LGA1700)..." porque `_` es comodín de 1 char en LIKE y los `()` agregan caracteres → se reemplaza `_` y espacio por `%`. (back `7534f92`/`0c0cfcf`)

## 2026-06-23 (tarde) — Performance grilla de Stock + columnas Ocultar + orden

Sesión de optimización y features sobre la grilla de **Stock** (`get_items_stocks` en `stocks.py`). Cambios **locales, sin commitear** al momento de esta nota. Ver [[arquitectura#Grilla de Stock — fast-path de performance]] y [[memoria]].

### Performance: ~15.5s → ~2.5s
- **Problema**: el grid calculaba ~9 subconsultas correlacionadas por CADA artículo de la empresa (las 3 de `albclil` escanean 1.27M filas ×3; 2 cuentan `ST_DETALLE_STOCK` de 5.4M) ANTES de filtrar/paginar.
- **fast-path con delta**: pre-agrega `albclil`/`albprol` en una pasada (GROUP BY) y difiere las columnas solo-display (pedprol, regularizaciones, conteo de seriales) a las 500 filas ya paginadas. 16s → ~4s.
- **fast-path sin delta (paginate-first)**: como no hay filtro de delta, pagina la página de artículos PRIMERO (indexado por ID_ARTICULO) y recién enriquece esas 500 filas via OUTER APPLY. 15.5s → ~2.5s.
- **byte-idéntico** verificado fila por fila contra el path viejo. Helper `_itemstock_from_named` compartido.
- DB ya bien indexada (índices compuestos covering). Índice opcional sugerido: `ST_DETALLE_STOCK (CREF) INCLUDE (FECHA_EGRESO)`.

### feat: columnas Ocultar NB / LO / NBE
- 3 flags de `articulo` (`ocultarDeNb`, `ocultar_lo`, `ocultarNbe`; int 0/1) como columnas toggleables con checkbox por fila. Endpoint `PATCH /itemsStocks/{itemId}/visibility` (`{flag, value}`) con whitelist de columnas. Front: `columnsConfig` + slots `a-checkbox` + action optimista (revert si falla). Default ocultas.

### fix: regresión de índices por las columnas Ocultar
- Insertar las columnas en el MEDIO del SELECT del path normal (que parsea por índice fijo) corrió los índices → el delta leía un flag en vez del inbound (ej. **121696** daba −398 en vez de 0). Fix: columnas al FINAL del proyectado + lookup por nombre.

### feat: orden marca → familia → título
- `ORDER BY` server-side multinivel (marca, familia, título; `ID_ARTICULO` de desempate para paginación estable), case-insensitive. Sin-marca/sin-familia (~29% de cc4) empujados al final.

### UX: Stock no auto-carga al entrar
- Al entrar a la pestaña ya no dispara el fetch compulsivo company-wide; espera a "Mostrar". Deep-links con filtro sí cargan. (`General.vue`, `itemsStock.vue`).

### Forense de deltas (casos puntuales)
- **122572** (+1): placa salió por **RMA-reemplazo** (canje; la RMA apunta a otro CREF) — canal no contemplado por la fórmula. Stock físico sano. Sin pase.
- **122535** (+1): **venta sin remito** — su pareja es un `pedclil` **anulado** (10457582) que nunca generó `albclil`; egreso no revertido y sin cobro en cuenta corriente → faltante real, no doc borrado.


## 2026-06-23

Sesión profunda de **Regularización de stock**: investigación de deltas, restauración de `albprol` y diagnóstico cross-company. Rama `regularizacion-stock` (front y back, pusheadas). Ver [[modulo-regularizacion]], [[memoria]] y [[contexto]].

### Investigación del delta (item 111454 RYZEN 7 5700G)
- El delta del grid es **pura aritmética de documentos** (compra − venta − créditos − stock), no de seriales. El −412 del 5700G resultó ser una **OC física recibida y vendida pero nunca documentada** (OC **11568**, estado "P", 500 u serializadas sin `albprol`). Es el espejo-compra del caso `albclil` de ventas: sobrevive el `pedprol`, falta el `albprol`.
- **Causa estructural**: artículos **duplicados del mismo SKU entre empresas** (5700G: 113950/113147 en cc4 + 121729 en cc11). Habilita ingresos cruzados.

### Backend (ms-metadata)
- **feat**: `apply_albprol_restoration` (`regularization.py`) — restaura el `albprol` faltante desde el `pedprol` sobreviviente, como **puro asiento (cost-neutral)**: no toca stock ni costo (sin triggers, `NCOSTEPROM` almacenado, FOB usa el último albprol por fecha). Una sola cabecera canónica, **maneja parciales** (inserta faltante = pedido − documentado), idempotente, gateada por `gerencia`. Preview con **cruce de seriales** (`serialMatch`, `perfecto`, `gapFisico`). **Aplicada en prod sobre OC 11568** (14 líneas / 2470 u en cabecera 15844, 7 ítems perfectos).
- **feat**: filtro de delta **"distinto de cero"** en la grilla de stock (`stocks.py`).

### Frontend (inventario-web-app)
- **feat/UX**: la pestaña **Stock** ya **no obliga** a elegir marca/categoría/búsqueda — con solo la **empresa** carga (paginado). Filtro Delta combinable; opción "Distinto de cero". (`api.js`, `store/index.js`, `General.vue`, `ItemsStock.vue`, `itemsStock.vue`).
- **feat**: el modal de Regularización muestra el **delta real del grid vs el race neto** (`RegularizationDetail.vue`).

### Hallazgo: cc11 no serializa
- El barrido de "OC recibida sin albprol" dio falsos positivos en cc11/cc9. Razón: **cc11 prácticamente no usa el ledger de seriales** (16 de 602 artículos; 955 seriales vs 107.058 u de albprol). Su "albprol fantasma" es un **artefacto de medición**, no un error a revertir. Los deltas raros de cc11 son descuadres de **columnas de stock**, no cruces ocultos con cc4 (verificado en ambos sentidos: ni el albprol de cc11 es de cc4, ni los seriales de cc11 son items que le falten a cc4).

### Git / Ops
- Pusheado a `regularizacion-stock` en ambos repos (ms-metadata `c5ac6f9`/`a634f50`; web `3e31d70`/`db53701`), para PR con base `development`/`gamma`. `.env` y `.DS_Store` sin commitear.

### Clasificación catálogo-wide de deltas + reposición (cc4)
- **Método**: identidad exacta `delta = INB(ingreso) − HELD(stock) − OUT(salida)` — cada delta se descompone en 3 discrepancias documentales contra el ledger de seriales. Scan de los 1.365 items de cc4 con delta ≠ 0.
- **Buckets**: 24 `auto_stock` (solo reconciliar stock↔serial), `auto_con_doc`, 74 `recontar` (ledger inconsistente), `revisar_legacy`/`revisar_doc`, 428 `no_serializado` (granel, −1,17M concentrado en pocos como art 102157). Exportado a CSV (`/Users/hermess/www/inventario/regularizacion_buckets_cc4.csv`) y a la nota [[regularizacion-buckets]].
- **Aplicado en prod**: los **24 `auto_stock` repuestos a Control** (`nstock_ctrl`, 295 u) con línea en `registro_stock` (marcador "Regularizacion stock recuperable (seriales presentes)", agente Catriel, automática en lote). 22/24 cerraron a 0; 2 (115804, 116357) en delta 1 (recuperable capado a lo respaldado por seriales).
- **Hallazgo — `auto_con_doc` NO se sostiene**: el cierre limpio por albprol (negativo que cierra al documentar una OC recibida, como 11568) es RARO. De 62, solo ~2 tienen OC sin documentar (`pedprol > albprol`) y encima con delta positivo (sobre-corrigen). Los ~35 "restaurar-albprol" tienen `pedprol ≤ albprol` → el gap son seriales SIN documento (legacy), no restaurable. Lo único auto-cerrable seguro fueron los 24 de stock.

## 2026-06-20

Sesión sobre `development`/`gamma` + nueva rama de funcionalidad **`catri-fine-tuning2`** (front y back, pusheada, sin mergear). Ver [[memoria]], [[contexto]] y [[modulo-precios]].

### Frontend (inventario-web-app)
- **feat**: Export **XLSX y CSV** también en la pestaña **Stock** (antes solo en Precios). Los botones (etiquetas cortas "XLSX"/"CSV") viven **dentro de la barra de filtros**, al lado de "Columnas", y emiten eventos a la página; exportan las columnas visibles. XLSX con `import('xlsx')` dinámico, CSV con BOM + `;`.
- **fix/UX**: el filtro **empresa (companyCode)** ahora se setea al `companyCode` del usuario (o **4** por defecto) **al entrar a cada pestaña**, vía `middleware/companyCode.js` (en `router.middleware`). Antes el select quedaba puesto pero los datos **sin filtrar** por una **carrera**: el watcher `immediate` de `General.vue` dispara el fetch y `updateMet` descarta el 2do fetch en vuelo (`window.__generalUpdateRunning`). Se resolvió seteando el default **antes** del fetch (middleware). Solo queda libre si se borra a mano dentro de la misma pestaña.
- **feat**: Agregada la entrada **Precios** al menú (`layouts/basic.vue`) — nunca estuvo en git (prod tenía una edición manual). Commiteada en `catri-fine-tuning` y mergeada a `development`/`gamma`.

### Backend (ms-metadata)
- **perf**: Eliminado **N+1** en `/items` y `/item` (`products.py`). `searchProducts` trae todas las imágenes en una sola query (`getImagesBulk`) en vez de abrir una conexión por producto (cada `dbconnection()` es un handshake TLS 1.0 y nunca se cierra). `GET /items?itemsPerPage=300`: **~11,5s → ~1,2s**. `getDetailProduct` pide atributos/imágenes una sola vez por artículo. Quitados los `print()` de debug.

### Git / Ops
- Mergeado `catri-fine-tuning` → `development` y `gamma` (front); en el back ya estaba contenido en `Development`/`Gamma`. Lo pendiente quedó en **`catri-fine-tuning2`** (front `983d58e`, back `6b9eeb4`), pusheada en ambos repos.
- **Gotcha git**: la rama `Development` (mayúscula) del back es la canónica (trackea `origin/Development`); borrar la `development` minúscula la dejó huérfana (macOS case-insensitive) → recuperada con `git reset --mixed origin/Development`.
- `xlsx` ya estaba en package.json; faltaba `npm install`. Los deploys necesitan `npm ci`/`npm install` o el `import('xlsx')` da 500.

Archivos: `pages/itemsStock.vue`, `pages/itemsPrices.vue`, `components/Filters/*.vue`, `middleware/companyCode.js`, `nuxt.config.js`, `layouts/basic.vue`, `core/controllers/products/products.py`.

## 2026-06-15

Más sobre la grilla de **Precios** (`/itemsPrices`), rama `catri-fine-tuning`. Commit `d1fb0e4`. Ver [[modulo-precios]] y [[competencia-partpicker-cache]].

### Frontend (inventario-web-app)
- **feat**: Columna fija **Compra-Gamer** en Resellers (siempre ese reseller, aunque no sea el más barato) + sorter + export.
- **feat**: Modal de competencia muestra **SKU** (`codigo`) y **Part #** (`nroParte`) por oferta.
- **feat**: **Título en una sola línea** con ellipsis; al hacer **hover** la fila se agranda y muestra el título completo. SKU sacado de abajo del título → **columna SKU visible por defecto**.
- **perf**: **Celdas editables lazy** (`EditablePriceCell`): muestran texto y montan el input de Ant solo al hacer click. Evita montar miles de inputs (clave con "Todo") → render/orden/scroll más fluidos. *UX:* se clickea para editar; no hay tab entre celdas.
- **perf**: La grilla pide `pricesView=1` → query liviana del backend.
- **fix**: Checkbox **"seleccionar todos"** en la cabecera no aparecía: Ant solo aplica `slots.title` si `column.title === undefined` (`lib/table/index.js`); un `title:""` lo bloqueaba → se quitó el title.

### Backend (ms-metadata)
- **perf**: `get_items_prices_grid` (query liviana, sin las subqueries pesadas de Stock) + `get_items_prices_grid_count` (`COUNT(DISTINCT)`); el endpoint las corre **en paralelo** (`ThreadPoolExecutor`) cuando `pricesView=1`. Total de la grilla ~5s → ~1,5s (y menos con paralelo). `get_items_stocks` (Stock) intacto.
- **perf**: `prewarm_catalog` en `@app.on_event("startup")` → baja el catálogo de partpicker en background al arrancar; el primer "Actualizar competencia" no espera ~30s.
- **feat**: `competition` devuelve `compragamer` por item (mejor oferta de `preciosgamer_compra-gamer`); `_build_offer` agrega `nroParte`.
- **chore**: quitado `print(con_string)` de debug en `get_items_stocks`.

Archivos: `pages/itemsPrices.vue`, `store/itemsPrices.js`, `plugins/api.js`, `components/Modal/CompetitionDetail.vue`, `components/Table/EditablePriceCell.vue`, `core/controllers/stocks/stocks.py`, `core/controllers/competition/competition.py`, `main.py`.

## 2026-06-13

Sesión de mejoras grandes a la grilla de **Precios** (`/itemsPrices`), rama `catri-fine-tuning`. Ver [[modulo-precios]].

### Frontend (inventario-web-app)
- **feat**: Columna **ID** propia anclada a la izquierda (antes el `#id` iba bajo el título; ahora el subtítulo muestra solo el SKU). Stickys: Sel · ID · SKU · Título con offsets calculados (`customCell` inline).
- **feat**: Columna **Stock** (`stockTotal` = nstock+nstock_ctrl+nstock_d1+nstock_lo) + filtro **Con stock / Sin stock / Todos** (default Con stock).
- **feat**: Columnas **Últ. ingreso / Últ. venta** (de `articulo.ULTIMO_INGRESO` / `ULTIMA_VENTA`).
- **feat**: **Orden asc/desc en todas las columnas** (client-side, sobre la página cargada).
- **feat**: **Recalcular masivo**: checkbox por fila + "todos" en cabecera; modal con un input por utilidad (PL1/PL2/MAY1/MAY2/LO1/LO2), 0=no toca, valor=suma esos puntos; aplica solo a seleccionados, secuencial con barra de progreso.
- **feat**: Tamaño de página **"Todo"** (sentinel 1.000.000) + persistencia del tamaño en localStorage.
- **feat**: **Exportar CSV** (es-AR, `;`, BOM) y **Excel .xlsx** (lib `xlsx`/SheetJS, import dinámico) de lo visible.
- **feat**: **Cache local de competencia** en localStorage: hidrata la grilla al instante y no pega solo; botón **"Actualizar competencia"** refresca lo visible y reescribe el cache (con indicador "hace X"). El detalle sigue en vivo.
- **feat**: Compactación de densidad (filas ~21px) y **altura dinámica** de la tabla midiendo `.ant-table-body` (sin franja vacía abajo).

### Backend (ms-metadata)
- **feat**: `get_items_prices` agrega `ULTIMO_INGRESO` y `ULTIMA_VENTA` (de `articulo`). OJO: `ULTIMA_COMPRA` NO existe en `articulo` (solo en `clientes`); el correcto es `ULTIMO_INGRESO`.
- **feat**: filtro de stock en `get_items_stocks`/`get_items_stocks_count` con `(ISNULL(nstock)+ISNULL(nstock_ctrl)+ISNULL(nstock_d1)+ISNULL(nstock_lo))` + columna `stockTotal` en `ItemStock`.

Archivos: `pages/itemsPrices.vue`, `store/itemsPrices.js`, `components/Filters/ItemsPrices.vue`, `plugins/api.js`, `core/controllers/stocks/stocks.py`, `core/models/models.py`, `package.json` (xlsx).

### Ops
- Se instaló `xlsx@0.18.5` en el frontend. **Tras `npm install` con el dev server corriendo hay que reiniciar `npm run dev`** (si no, webpack/HMR queda inconsistente → RuntimeError + loader infinito). Cambios sin commitear aún.

## 2026-06-12

### Frontend (inventario-web-app)
- **feat**: Señal de **tendencia** de precios (▲ subió rojo / ▼ bajó verde, tooltip con precio anterior) junto al mínimo de competencia y de resellers en la grilla, y en cada fila del modal de detalle
- **fix**: Cabeceras de la columna Título que se "metían dentro" de otras al scrollear horizontal → `<th>` sticky con estilo **inline** vía `customHeaderCell` (la CSS class no llega confiable al th en la tabla de header separada de antd)
- **fix**: Sombra del borde derecho del Título reducida a `2px/5%` (era demasiado marcada)

### Backend (ms-metadata)
- **feat**: `competition/` descarga catálogos con `tendencia=1` → cada oferta lleva `tendencia` (sube/baja/igual) + `precioAnterior`

### Deploy / Ops
- Commits `9d88670` (front) y `51fb1e9` (back) pusheados a `catri-fine-tuning`. El `.env` del backend NO se commitea (credenciales)
- Prod: sin variables `.env` nuevas; requiere salida HTTPS a `partpicker.blustudioinc.com`, `requests` instalado y permiso de escritura en `scrap_hg`. `OPENSSL_CONF` NO hace falta en prod (solo dev local)

## 2026-06-11

### Frontend (inventario-web-app)
- **feat**: Nueva sección **Precios** (`/itemsPrices`) — grilla de costos/utilidades/precios con edición inline bidireccional (utilidad→precio y precio→utilidad), código de colores del sistema legacy (naranja UNIT+PL, magenta MAY, azul LO, violeta ML+PML)
- **feat**: Columnas de **competencia**: mayoristas USD s/IVA con Δ% + semáforo, resellers ARS; carga lazy en background
- **feat**: Modal ⊕ de competencia: keywords `scrap_hg` con búsqueda en vivo (3+ chars), guardar y rematchear, lista completa de ofertas, historial de precios por fila expandible
- **feat**: Visibilidad de columnas configurable y persistida por usuario en localStorage (sobrevive logout)
- **feat**: Título como link al item en Productos (pestaña nueva, deep-link por ID)
- **fix**: Título sticky por CSS en lugar de `fixed:'left'` de antd (filas desalineadas) y `scroll.x` numérico con headers fijos (cabeceras corridas)

Archivos principales: `pages/itemsPrices.vue`, `store/itemsPrices.js`, `components/Filters/ItemsPrices.vue`, `components/Modal/CompetitionDetail.vue`, `plugins/api.js`

### Backend (ms-metadata)
- **feat**: Controller `competition/` — precios de competencia vía BluPartPicker: cache 30 min stale-while-revalidate, matching SKU exacto + `scrap_hg.search_keys` por palabra completa. Endpoints `POST /itemsCompetition`, `GET /itemsCompetition/{itemId}` (con preview `keys`), `PATCH .../searchKeys`, `GET /itemsCompetitionHistory`
- **feat**: Edición inversa de precios (`update_item_price_by_target` en `prices.py`): fijar UNIT/MAY/LO/ML deriva la utilidad ajustando solo la primera del par; ML invierte ARS+IVA→USD antes de derivar
- **fix**: Conexión a SQL Server en macOS: `OPENSSL_CONF=openssl_legacy.cnf` obligatorio (el server solo habla TLS 1.0; OpenSSL 3.x lo rechaza → error 10054 que parece firewall)

Archivos principales: `core/controllers/competition/competition.py`, `core/controllers/prices/prices.py`, `main.py`, `core/models/models.py`


## 2026-05-05

### Backend (ms-metadata)
- **hotfix**: Arreglo stock en kits (PR #263)

## 2026-04-16

### Backend (ms-metadata)
- fix: corrección en módulo de brands

## 2026-04-15

### Backend (ms-metadata)
- fix: arreglo stock syncup (sincronización de stock)

## 2026-04-29

### Frontend (inventario-web-app)
- **SNB-3913**: Cambio en la visualización de banderas en PED, INV y COM (PR #370)

## 2026-04-15

### Frontend (inventario-web-app)
- **INV-346**: Fix paginado incorrecto en pestaña de kits (PR #368)
- **INV-345**: Altura máxima en contenedor de tabla de stock para evitar scroll doble del body (PR #366)

## 2026-03-18

### Backend (ms-metadata)
- fix: corrección listado de productos
- fix: arreglo paginación en products

### Frontend (inventario-web-app)
- Refactor paginado en kits: alineado a derecha, sin scroll doble
- Refactor utilidades de control de precio: texto en shadow para campos editados, quitada línea vertical que dificultaba la vista

## 2026-03-02

### Frontend (inventario-web-app)
- **INV-343**: Al crear una categoría, se puede enviar `companyCode` (PR #362)
- **INV-342**: Al crear una marca, se puede enviar `companyCode` (PR #360)

## 2026-02-18 – 2026-02-20

### Backend (ms-metadata) — INV-BundleCostUtility
- feat: agregar costos al bundle (PR #255, #257, #259, #261)
- feat: precio por utilidad para productos individuales (INV-338)
- feat: objeto `prices` dentro del inventario de productos (INV-335, PR #252, #253)
- fix: cálculo de ganancia estipulada y precio en bundles
- fix: `ncosteprom` (costo promedio) en bundles

## Ver también

- [[inventario]] · [[arquitectura]] · [[contexto]]
