# Módulo Precios — inventario

Sección del admin (`/itemsPrices`) dedicada a gestión de precios: costos,
utilidades, precios por lista y comparación contra la competencia.
Construida el 2026-06-11. Hermana de la pantalla de Stock — reutiliza
`GET /itemsStocks?controlPrices=1` y `PATCH /itemsPrice`.

## Edición bidireccional precio ⇄ utilidad

Fórmula base: `precio = NCOSTEPROM × (1 + Σ utilidades / 100)`.

| Precio | Utilidades que lo componen | Columna en `articulo` |
|--------|---------------------------|----------------------|
| UNIT | PL1 + PL2 | `npvp1` |
| MAY | MAY1 + MAY2 | `npvp5` |
| LO | LO1 + LO2 | `nplo` |
| ML | MAY1 + MAY2 + PML | `npvp3` (display: × cotización × (1+IVA), ARS) |
| PCAM | PCAM | `npvp6` |

- Editar una **utilidad** → recalcula su precio (flujo original).
- Editar un **precio** → deriva la utilidad total y ajusta **solo la primera**
  del par (PL1, MAY1, LO1, PML), dejando fija la segunda. Regla de negocio
  pedida explícitamente. Implementado en `update_item_price_by_target`
  (`prices.py`), que delega en `update_item_price` → hereda validación de
  utilidad mínima, `historial_precios` y recálculo.
- Costo editable solo con permiso `gerencia`.

## Código de colores (heredado del sistema legacy)

Cada precio comparte color con sus utilidades: 🟠 UNIT+PL1/PL2 · 🩷 MAY+MAY1/MAY2
· 🔵 LO+LO1/LO2 · 🟣 ML+PML. Memoria muscular de los operadores del sistema viejo.

## Competencia (BluPartPicker)

Dos bloques de columnas: **mayoristas** (Invid/Ceven/Stylus/Air, USD sin IVA,
con Δ% vs UNIT y semáforo) y **resellers** (37 tiendas PreciosGamer, ARS).
Cada precio mínimo muestra una flecha de **tendencia** (▲ subió / ▼ bajó,
tooltip con el precio anterior) que viene de partpicker con `tendencia=1`.

- Matching por unión de dos vías: SKU exacto (== `nro_parte`) y keywords de
  `scrap_hg.search_keys` matcheadas como **palabra completa** contra títulos
  (no LIKE: "5500" no debe matchear "5500GT").
- En partpicker el source `nb` es el catálogo propio: `codigo` == itemId,
  `nro_parte` == SKU. Esa igualdad habilita todo el cruce.
- Modal ⊕ por item: preview en vivo de keywords (≥3 chars, debounce 400ms,
  sin persistir), "Guardar y rematchear" (upsert a `scrap_hg` — la misma
  tabla que usa el scraper de hardgamers), lista completa de ofertas y
  historial de precios por fila (proxy de partpicker `/historia`).
- Cache backend: 2 catálogos en memoria, TTL 30 min, stale-while-revalidate,
  descarga paralela (~30s la primera vez, instantáneo después).

### Endpoints (ms-metadata)

- `POST /itemsCompetition` — bulk por `{itemId, sku}`, respuesta keyed por itemId
- `GET /itemsCompetition/{itemId}?sku&keys` — detalle; `keys` = preview sin guardar
- `PATCH /itemsCompetition/{itemId}/searchKeys` — upsert keywords
- `GET /itemsCompetitionHistory?source&codigo` — historial de un listing

## UI / tabla

- Columnas definidas en `store/itemsPrices.js` (`columnsConfig`), visibilidad
  toggleable (popover "Columnas") persistida en localStorage **por usuario**:
  `itemsPricesColumnsVisibility:<userId>`. SKU oculta por defecto (se muestra
  bajo el título). Título no ocultable.
- Título = link en pestaña nueva al item en Productos (deep-link por ID,
  sin filtros `noImage`/`stock` que lo ocultarían).
- Anclajes: título sticky por CSS (NUNCA `fixed:'left'` de antd) y headers
  fijos con `scroll.y` + `scroll.x` numérico. Ver [[contexto#Gotchas conocidos]].
- Fuentes de competencia siempre en MAYÚSCULAS.

## Ver también

- [[arquitectura]] · [[contexto]] · [[changelog]] · [[inventario]]
- [[BluPartPicker]] — la API que provee los precios de competencia
