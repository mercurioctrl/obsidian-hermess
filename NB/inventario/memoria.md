# Memoria — inventario

Memoria de Claude Code del proyecto, consolidada por tipo.
Última sincronización: 2026-06-15. (Memoria local también en
`~/.claude/projects/-var-www-nb-inventario/memory/` — entorno Linux.)

## Proyecto

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
