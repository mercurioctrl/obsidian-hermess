# Memoria — inventario

Memoria de Claude Code del proyecto, consolidada por tipo.
Última sincronización: 2026-06-29. (Memoria local también en
`~/.claude/projects/-var-www-nb-inventario/memory/` — entorno Linux.)

## Proyecto

### Estado git: tanda pusheada a regularizacion-stock (2026-06-29)
El trabajo de seriales + competencia + índices + word-break + fix N+1 quedó commiteado y pusheado a `regularizacion-stock` (back `ms-metadata` 4 commits `7f67d7b..bf2c8d1`; front `inventario-web-app` 3 commits `653c025..481be0f`), sin `Co-Authored-By`. Sin commitear: `.env`, `.DS_Store`, scripts ad-hoc (diag/run/sweep/worklist + CSVs). Índices P1–P3 = DDL en prod (fuera de git). Rama lista para PR a Development/Gamma. Ver [[changelog]] y [[performance-indices]].

### Índices de performance + refactor IN revertido (2026-06-27)
Auditoría con el **DMV real** de SQL Server (login `web` tiene VIEW SERVER STATE). Aplicados en prod (Enterprise → `ONLINE=ON`): **P2 `ST_DETALLE_STOCK (CREF, FECHA_EGRESO)` = gran win, grilla 1.63s → 0.54s (−67%)**; P3 RVDS covering (modal seriales −14%); P1 albclit covering dfecalb (neutro por-query, gana en agregado; score DMV 298M pero NO toca la grilla). **Lección**: batchear las subqueries escalares de `get_items_stocks` con `IN` se probó y empeoró 2.5–3.7× (round trips sobre TLS 1.0) → el fix correcto era el índice, no reestructurar; revertido byte-idéntico. Fix N+1: `selldiscount.get_current_cost` reutiliza el cursor del loop. Script `ms-metadata/scripts/perf_indexes_p1_p3.sql`. Ver [[performance-indices]].

### Modal de seriales: documentos, RMA-cambio y compra (2026-06-27)
`get_item_serials` reconstruye por serial: estado (present = `FECHA_EGRESO` null), cadena `serial→RVD→albclit→factura/NC+pedido` (`OUTER APPLY TOP 1` = 1 fila/serial), **Cambio RMA** (cruce `ST_RMADETALLE.SERIAL` devuelto ↔ `ST_DETALLE_STOCK.ID_RMACLIENTE` reemplazo, ambas direcciones; 1 query + dicts, la correlacionada tardaba 12.6s), y **Compra** (`ID_COMPRA` a 8 dígitos). Bug: el endpoint serializaba solo 6 campos a mano (faltaba `present` → "todos despachados"); fix = objeto completo + default depósito "Todos". Ver [[modulo-seriales]].

### Corrección de ACREDITADO fantasma vía NC real (2026-06-26)
`albclil.ACREDITADO` mal cargado (> ncanent = imposible) infla el delta+. La NC real está en `FP_FactWebCliEncabezado/Detalle` (NTIPODOCU=2), vinculada por `ID_NROREMCLI_ENC`; cantidad real = `SUM(FP_FactWebCliDetalle.NCANENT)`. `apply_acreditado_correction` (key `IdDetalleRemito`) corrige el campo (no toca NC real/AFIP), aplicado en prod (Catriel): **88 líneas / 772 u**, 0 imposibles restantes en cc4, traza en registro_stock. **CAVEAT**: alcance seguro SOLO `ACREDITADO>ncanent`; `>nc_real` explota a 2.615 líneas porque el enlace FP es incompleto → "sin NC ⇒ 0" es FALSO; cap a `ncanent`, nunca 0. Ver [[modulo-regularizacion]].

### Gap serial↔columnas → reponer a Control + barrido cc4 (2026-06-25)
Tras restaurar un albprol (o en cualquier item), un **delta+ residual** suele ser **gapFísico de columnas**: seriales presentes que `nstock/nstock_d1/...` no reflejan. `apply_serial_gap_to_control` (regularization.py) lo repone a Control sin depender del race; tope=delta canónico, idempotente (`MARCADOR_SERIAL_GAP`), `COUNT(DISTINCT SERIAL)`. **Test de "gap limpio" (3 identidades)** antes de reponer: `albprol==filas_serial`, `egresados==ventas+RMA−notasCrédito` (¡incluir NC: devolución re-ingresa el serial!), `presentes==albprol−ventas−rma+nc`, `delta==presentes−columnas`. **Barrido cc4**: de 2.751 delta>0 solo 150 "gap limpio"; aplicados como Catriel (7463) → **143 cerraron a 0** (355 u), 0 negativos; 7 residuos legacy con filas de serial duplicadas/blank (contar con `COUNT(*)` infla; usar DISTINCT). El resto (2.601) son causas documentales/re-tagueo. Esfuerzo total: **170 items** realineados a la verdad física. Ver [[modulo-regularizacion]] y [[changelog]].

### 111454 cerrado — no todo delta es albprol restaurable (2026-06-25)
El 111454 (5700G) quedó en **−21** tras reponer 19 a Control y corregir una **NC de 2022** con error de carga (`ACREDITADO 100→10`). El −21 NO es restaurable: el cruce serial(`ID_COMPRA`)↔albprol(`albprot.nnumped`) **por orden** muestra que el albprol ya existe, solo mal numerado en la era vieja (4.277 u seriales sin albprol espejadas por 4.705 de albprol sin seriales → neto +17). **Restaurar duplicaría.** La "reg +983" de notas viejas no existía (eran movimientos `nstock→nstock_d1`). Regla: detectar albprol-faltante-real = gap **por orden** con `pedprol` vivo (como OC 11568), NO el neto agregado. `columnas==presentes` = item sano aunque delta≠0.

### Upsert de utilidades en ST_GANANCIA (2026-06-24)
Marcar precio/utilidad a un item **sin fila** en `NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS` fallaba **en silencio**: `_update_gain_column` hacía `UPDATE ... WHERE ID_ARTICULO=?` puro → 0 filas, sin error (`success:true`), la utilidad no persistía y quedaba inconsistente con el precio (que sí se escribe en `articulo`). Afecta edición de utilidad y de precio (la inversa delega en el mismo punto). **Fix**: `_update_gain_column` es **upsert** — si `rowcount==0` inserta la fila sembrada desde `simulated_gains` (`GAIN_COLUMNS`, las 9 que lee `_fetch_gain_margins`), cubriendo las NOT NULL (`ESTIPLO/LO1/CF`). Tabla **sin PK**; clave = `articulo.cRef` (nvarchar, NO el int `ID_ARTICULO`; hay legacy no numérico como `'ACARREO'`). Eran **432** items sin fila (los más nuevos). Validado con ROLLBACK, sin escribir prod. Ver [[modulo-precios]] y [[changelog]].

### Origen del costo FOB (Precios y Stock)
El **FOB** que muestran las grillas de Precios y Stock NO es `NCOSTEPROM`. Sale de `NewBytes_DBF.dbo.albprol.nprediv`, tomando la **última línea de albarán de proveedor** del artículo: `OUTER APPLY (SELECT TOP(1) albprol.nprediv FROM albprol JOIN albprot ON nnumalb WHERE albprol.cref = articulo.cref ORDER BY albprot.dfecalb DESC)`. Subquery **idéntica** en `prices.py` (`_read_current_prices`) y `stocks.py` → consistente entre pestañas. `NCOSTEPROM` (costo promedio, columna de `articulo`) es la base del cálculo de precios. Relevante para regularización: un `albprol` restaurado backdated NO mueve el FOB mostrado (usa el albarán más reciente por fecha). Ver [[modulo-precios#Columnas de costo: FOB vs NCOSTEPROM]].

### Memory leak en grilla de Stock (2026-06-24)
`setScroll()` reasignaba `window.onscroll` en cada evento (closure nueva + handler duplicado, sin limpiar en `beforeDestroy`) → ahora solo actualiza `scrollY`. Auditoría de RAM: el grueso es la grilla de Stock **sin virtualización** (`scroll.y` comentado, 500×~50 en DOM); virtualizar (patrón de Precios) queda pendiente por el riesgo de alineación antd 1.x.

### Grilla de Stock — fast-path + orden (2026-06-23 tarde)
`get_items_stocks` optimizada: pre-agrega `albclil`/`albprol` (GROUP BY) y difiere subqueries solo-display a las filas paginadas. Sin filtro de delta usa **paginate-first** (pagina artículos y enriquece 500 filas con OUTER APPLY). ~15.5s → ~2.5s, byte-idéntico. Parseo del `ItemStock` por NOMBRE (`_itemstock_from_named`), no por índice — meter columnas en el medio del SELECT rompe el path por-índice (regresión 121696: −398 en vez de 0). Orden: marca→familia→título, sin-marca al final, ID de desempate. Flags Ocultar NB/LO/NBE (`articulo.ocultarDeNb/ocultar_lo/ocultarNbe`) via `PATCH /itemsStocks/{itemId}/visibility`. Forense: **122572** (+1 = RMA-reemplazo/canje, no contemplado por la fórmula), **122535** (+1 = venta sin remito; pareja = `pedclil` anulado 10457582 sin `albclil`, sin cobro en CC = faltante real). Ver [[changelog]] y [[arquitectura#Grilla de Stock — fast-path de performance]].

### Clasificación de deltas por bucket + reposición (2026-06-23)
Identidad exacta `delta = INB(ingreso) − HELD(stock) − OUT(salida)` (documento vs ledger de seriales, vale por la invariante creados=presentes+egresados) para clasificar deltas. cc4: 1.365 con delta≠0. Buckets: **24 `auto_stock`** (reconciliar stock↔serial), **74 `recontar`** (ledger inconsistente: creados≠pres+egres), `revisar_legacy`/`revisar_doc`, **428 `no_serializado`** (granel, −1,17M concentrado en art 102157). CSV en `/Users/hermess/www/inventario/regularizacion_buckets_cc4.csv` + nota [[regularizacion-buckets]].
**Aplicado en prod**: los 24 `auto_stock` repuestos a Control (295 u, `registro_stock` marcador "Regularizacion stock recuperable (seriales presentes)", igual que la Acción 1). 22/24 a delta 0.
**Caveat clave (auto_con_doc no se sostiene)**: el cierre limpio por albprol (11568) es RARO. "restaurar-albprol" solo vale si `pedprol > albprol`; si `pedprol ≤ albprol` el gap son seriales sin documento (legacy, no restaurable). Los pocos restaurables suelen tener delta positivo → restaurar sobre-corrige. Solo `auto_stock` es auto-cerrable seguro.

### Regularización de stock — albprol restoration (2026-06-23)
Rama `regularizacion-stock`. El **delta del grid es documental** (compra−venta−créditos−stock), no de seriales. Caso 111454 (5700G, −412) = **OC 11568 recibida y vendida sin `albprol`** (estado "P"); se sumó `apply_albprol_restoration` que restaura el albprol desde el `pedprol`, **cost-neutral** (asiento puro: sin triggers, NCOSTEPROM almacenado, FOB usa el último albprol por fecha), una cabecera canónica, maneja parciales, idempotente, preview con cruce de seriales. **Aplicada en prod sobre OC 11568** (cabecera 15844, 7 perfectos). Ver [[modulo-regularizacion]].

### cc11 NO serializa (clave para deltas cross-company)
cc11 prácticamente no usa el ledger de seriales: **16 de 602 artículos con seriales, 955 seriales vs 107.058 u de albprol**. Su "albprol fantasma" es **artefacto de medición**, no error. Hay 209 SKUs duplicados cc4↔cc11. Verificado: el albprol de cc11 son OCs propias (no de cc4) y los seriales de cc11 no son items que le falten a cc4. Deltas raros de cc11 = descuadre de **columnas de stock**, NO restaurar/revertir albprol. El FOB sale del **último `albprol.nprediv`** por `albprot.dfecalb`.

### Rama catri-fine-tuning2 (2026-06-20)
- Front: export **XLSX/CSV** en Stock+Precios (botones en la barra de filtros, emiten eventos a la página) + default **companyCode** por pestaña vía middleware. Back: fix **N+1** en `/items` y `/item`.
- **Ya mergeada** a `development`/`gamma` (PRs #377 front / #274 back; verificado 2026-06-25 contra `origin/Development` y `origin/Gamma`). Front `983d58e`, back `6b9eeb4`. Las ramas **locales** quedaron atrasadas → `git checkout Development && git pull` antes de seguir.
- La pestaña **Precios** vivía solo en `catri-fine-tuning`; el **link del menú nunca estuvo en git** (prod tenía edición manual de `basic.vue`) → agregado y propagado.
- Git: `Development` (mayúscula) es la canónica del back; borrar `development` minúscula la dejó huérfana (macOS case-insensitive) → `git reset --mixed origin/Development`.

### N+1 con dbconnection (backend) — clave
`dbconnection()` abre una conexión pyodbc **NUEVA por llamada** (handshake TLS 1.0) y **nunca se cierra** → cualquier `for x in rta: getImages(x)` es N+1 catastrófico. `/items` con 300 items: **~11,5s → ~1,2s** usando query bulk con `IN` (`getImagesBulk` en `products.py`). Regla: ante listados lentos, buscar `for ... in rta` con helper que llama `dbconnection()` y pasarlo a bulk. Los N+1 de **escritura** transaccional (transfer_stock, sync de kits) se dejan.

### Defaults de query van en middleware, no en created()
Los defaults de query que afectan el fetch (ej. `companyCode`) deben setearse en **middleware de ruta**, no en `created()` del filtro. `General.vue` tiene un watcher `immediate` que dispara el fetch; `updateMet` **descarta el 2do fetch en vuelo** (`window.__generalUpdateRunning`). Si `created()` agrega el param DESPUÉS del fetch inicial, el refetch se descarta → grilla sin filtrar hasta refrescar. Fix: `middleware/companyCode.js` setea companyCode (usuario o 4) al entrar a la pestaña, antes del fetch; respeta el borrado manual dentro de la misma pestaña.

### Grilla de Precios — mejoras 2026-06-13 (rama catri-fine-tuning)
- Precios NO tiene endpoint propio: reusa `GET /itemsStocks?controlPrices=1`; precios en
  `record.controlPrices`; edición por `PATCH /itemsPrice`. La query con `controlPrices`
  es lenta (~4.4s) → el loader tarda, no es cuelgue.
- Cols fijas: Sel·ID·SKU·Título (offsets inline). Stock (`stockTotal`) + filtro
  Con/Sin/Todos. Fechas `ULTIMO_INGRESO`/`ULTIMA_VENTA` de `articulo` (no `ULTIMA_COMPRA`).
- Orden en todas las columnas (client-side). Recalcular masivo por utilidad sobre
  seleccionados (modal). Paginación "Todo". Export CSV + xlsx (SheetJS).
- Persistencia localStorage por usuario: `itemsPricesColumnsVisibility`,
  `itemsPricesPageSize`, `itemsPricesCompetition` (ver [[competencia-partpicker-cache]]).
- Gotcha: `npm install` con `npm run dev` corriendo rompe HMR → reiniciar dev server.

### Grilla de Precios — mejoras 2026-06-15
- **Performance ~5s → ~1,5s**: el cuello NO era `get_items_prices` (0.08s) sino la
  query principal `get_items_stocks` (~3.8s, subqueries que Precios no usa). Path
  liviano `get_items_prices_grid` + count `COUNT(DISTINCT)` con flag `pricesView=1`,
  corridos en paralelo. `get_items_stocks` (Stock) intacto.
- **Celdas editables lazy** (`EditablePriceCell`): input de Ant solo al click (no
  miles de inputs). UX: click para editar, sin tab entre celdas.
- **Compra-Gamer** como columna fija en Resellers (backend devuelve `compragamer`).
- Modal competencia: SKU (`codigo`) + Part # (`nroParte`). Título 1 línea + hover.
- `prewarm_catalog` al startup → competencia sin esperar 30s.
- Gotcha Ant 1.x: `slots.title` solo se aplica si `column.title === undefined`
  (`title:""` deja el header vacío).



### SQL Server legacy TLS
El SQL Server `NB_WEB` (190.210.23.97,4444) solo soporta TLS 1.0. OpenSSL 3.x lo
rechaza por defecto y pyodbc falla con `TCP Provider: 10054` (con ambos drivers
ODBC 17/18, con o sin Encrypt). El TCP conecta y el ping anda, lo que despista
hacia "firewall/VPN" — no es eso. **Fix:** `OPENSSL_CONF=ms-metadata/openssl_legacy.cnf`
(commiteado en el repo) al levantar uvicorn. **Solo local**: en prod no hace falta.

### Matching de competencia con BluPartPicker
- El source `nb` de partpicker es el catálogo propio: `codigo` == itemId y
  `nro_parte` == SKU (verificado item 122557 / A15-51M-99XJ).
- `scrap_hg.search_keys` son keywords curadas que ya usaba el scraper de
  hardgamers; la sección Precios las reutiliza y edita — afecta a ambos.
- El `nro_parte` de resellers es basura en ~89% de los casos → matching por
  tokens de título, **palabra completa** (no LIKE: "5500" ≠ "5500GT").
- Pendiente: ¿excluir `libre-opcion` (canal propio) de resellers?

### Trampas de alineación en tablas antd 1.x
1. `fixed:'left'` desalinea filas (overlay clonado + sync JS) → usar CSS sticky
   con fondos opacos en la misma tabla.
2. `scroll.x:'max-content'` + `scroll.y` desalinea cabeceras (header y body son
   tablas separadas) → `scroll.x` numérico + `table-layout:fixed; min-width:100%`.
3. El `<th>` sticky necesita estilo **inline** (`customHeaderCell`), no solo CSS
   class — sino las otras cabeceras se ven "por dentro" del Título al scrollear.

## Feedback del usuario

### Fidelidad visual al sistema legacy
La UI nueva debe replicar las convenciones del sistema de escritorio viejo:
colores por grupo precio↔utilidades (memoria muscular de los operadores),
alineación al píxel ("TIENEN QUE COINCIDIR PERFECTO"), fuentes de tiendas en
MAYÚSCULAS. Itera pegando capturas anotadas y pide fixes inmediatos.

## Referencias

### API BluPartPicker
`https://partpicker.blustudioinc.com` — sin auth. Mayoristas (`distribuidor=1`):
invid, ceven, stylus, air (USD, usar `precio_sin_iva`) + `nb` (propio, excluir).
Resellers (`distribuidor=0`): 37 tiendas `preciosgamer_*` (ARS, ~60k items).
`GET /items` (límite **500**/página), `/items/{source}/{codigo}/historia`,
`/sources`, `/exchange-rates`. Catálogo completo ~75k items baja en ~30s en paralelo.
`tendencia=1` (entero, no string) agrega `tendencia` (sube/baja/igual) + `precio_anterior` por item.

## Ver también

- [[inventario]] · [[contexto]] · [[modulo-precios]] · [[modulo-regularizacion]] · [[competencia-partpicker-cache]]
