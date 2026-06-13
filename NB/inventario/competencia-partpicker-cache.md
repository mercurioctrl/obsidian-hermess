# Cache de competencia (BluPartPicker) — inventario

Cómo se cachea la data de competencia que muestra la grilla de [[modulo-precios|Precios]].

## Backend — cache en memoria (30 min, SWR)

`ms-metadata/core/controllers/competition/competition.py`

- Endpoint `POST /itemsCompetition` (`{items:[{itemId,sku}]}`) → `get_items_competition`.
- **Cache en memoria del proceso** (variable global `_catalog`), NO en DB ni Redis.
  `CACHE_TTL_SECONDS = 30*60`. Política **stale-while-revalidate**:
  1. 1er pedido (cache vacío) → bloquea y descarga todo el catálogo.
  2. < 30 min → sirve de memoria, instantáneo.
  3. > 30 min → sirve viejo y refresca en un daemon thread.
- Fuente: `https://partpicker.blustudioinc.com` (paginado 500, 8 workers). Dos
  catálogos: mayorista (USD s/IVA) y resellers (ARS).
- Matching: MPN/SKU exacto + `scrap_hg.search_keys` (palabra completa).
- **Implicancias**: reiniciar el backend vacía el cache (el 1ro paga ~30s);
  cada worker de uvicorn tiene su propio catálogo.

## Frontend — cache local (agregado 2026-06-13)

- Antes traía competencia en background en cada carga. Ahora **NO pega solo**:
  hidrata la grilla desde **localStorage** y solo refresca con botón.
- Clave por usuario: `itemsPricesCompetition:<userId>` =
  `{updatedAt, byId:{itemId:{wholesale,resellers}}}`.
- Botón **"Actualizar competencia"** (`fetchCompetition`) refresca TODO lo visible
  (cacheado o no, por si cambió), actualiza grilla + reescribe cache con timestamp.
  Guarda solo la mejor oferta por tipo y campos mínimos (price, source, updatedAt,
  tendencia, producto, urlFicha) para no reventar la cuota de localStorage.
- Indicador "Competencia: hace X" = cuándo refrescaste vos (≠ columna "Hace" de
  cada fila, que es la antigüedad del dato en partpicker).
- El **detalle** (modal `ModalCompetitionDetail`) sigue en vivo (`GET /itemsCompetition/{id}`), no se cachea.

## Ver también

- [[modulo-precios]] · [[arquitectura]] · [[contexto]] · [[inventario]]
- [[BluPartPicker]] — la API de competencia
