# Memoria — inventario

Memoria de Claude Code del proyecto (`~/.claude/projects/-Users-hermess-www-inventario/memory/`),
consolidada por tipo. Última sincronización: 2026-06-11.

## Proyecto

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

- [[inventario]] · [[contexto]] · [[modulo-precios]]
