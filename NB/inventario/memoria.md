# Memoria — inventario

Memoria de Claude Code del proyecto, consolidada por tipo.
Última sincronización: 2026-06-23. (Memoria local también en
`~/.claude/projects/-var-www-nb-inventario/memory/` — entorno Linux.)

## Proyecto

### Regularización de stock — albprol restoration (2026-06-23)
Rama `regularizacion-stock`. El **delta del grid es documental** (compra−venta−créditos−stock), no de seriales. Caso 111454 (5700G, −412) = **OC 11568 recibida y vendida sin `albprol`** (estado "P"); se sumó `apply_albprol_restoration` que restaura el albprol desde el `pedprol`, **cost-neutral** (asiento puro: sin triggers, NCOSTEPROM almacenado, FOB usa el último albprol por fecha), una cabecera canónica, maneja parciales, idempotente, preview con cruce de seriales. **Aplicada en prod sobre OC 11568** (cabecera 15844, 7 perfectos). Ver [[modulo-regularizacion]].

### cc11 NO serializa (clave para deltas cross-company)
cc11 prácticamente no usa el ledger de seriales: **16 de 602 artículos con seriales, 955 seriales vs 107.058 u de albprol**. Su "albprol fantasma" es **artefacto de medición**, no error. Hay 209 SKUs duplicados cc4↔cc11. Verificado: el albprol de cc11 son OCs propias (no de cc4) y los seriales de cc11 no son items que le falten a cc4. Deltas raros de cc11 = descuadre de **columnas de stock**, NO restaurar/revertir albprol. El FOB sale del **último `albprol.nprediv`** por `albprot.dfecalb`.

### Rama catri-fine-tuning2 (2026-06-20)
- Front: export **XLSX/CSV** en Stock+Precios (botones en la barra de filtros, emiten eventos a la página) + default **companyCode** por pestaña vía middleware. Back: fix **N+1** en `/items` y `/item`.
- Pendiente de mergear a `development`/`gamma`. Front `983d58e`, back `6b9eeb4`, pusheadas.
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

- [[inventario]] · [[contexto]] · [[modulo-precios]] · [[competencia-partpicker-cache]]
