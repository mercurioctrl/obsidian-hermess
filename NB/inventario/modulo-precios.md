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
- **Items sin fila en `ST_GANANCIA_ESTIPULADA_ARTICULOS`** (típicamente los más nuevos): `_update_gain_column` es **upsert** — inserta la fila sembrada si no existe. Antes el `UPDATE` puro afectaba 0 filas en silencio y la utilidad no persistía. La tabla no tiene PK; clave = `articulo.cRef` (nvarchar). Ver [[contexto#Gotchas conocidos]] y [[memoria]].

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

## Mejoras 2026-06-13 (rama catri-fine-tuning)

- **Columnas fijas**: ahora son `Sel | ID | SKU | Título` con offsets izquierdos
  calculados en el getter `columns` vía `customCell`/`customHeaderCell` (left
  inline) — soporta cualquier offset y se reacomoda al ocultar columnas. El `#id`
  pasó a columna **ID** propia; el subtítulo bajo el título muestra solo el SKU.
- **Stock**: columna `stockTotal` (= nstock+nstock_ctrl+nstock_d1+nstock_lo) y
  filtro **Con stock / Sin stock / Todos** (default Con stock). Backend filtra con
  `(ISNULL(nstock)+...)>0`; el default lo inyecta `plugins/api.js`
  (`stock` ausente→1, `"all"`→sin filtro).
- **Fechas**: columnas Últ. ingreso / Últ. venta desde `articulo.ULTIMO_INGRESO`
  y `ULTIMA_VENTA` (datetime) en `get_items_prices`. (`ULTIMA_COMPRA` no existe en
  `articulo` — solo en `clientes`; usar `ULTIMO_INGRESO`.)
- **Orden**: todas las columnas ordenables asc/desc (client-side, página cargada;
  `COLUMN_SORTERS` en el store con accessors por tipo).
- **Recalcular masivo**: checkbox por fila + "todos" en cabecera; modal con un input
  por utilidad (PL1,PL2,MAY1,MAY2,LO1,LO2). 0=no toca esa columna, valor=suma esos
  puntos a TODAS las filas seleccionadas; secuencial con barra de progreso (reusa
  `PATCH /itemsPrice` por celda).
- **Paginación "Todo"** (sentinel 1.000.000) y tamaño de página persistido en
  `itemsPricesPageSize:<userId>` (pisa el `itemsPerPage` del link del tab).
- **Export**: CSV (es-AR, separador `;`, BOM) y Excel `.xlsx` (lib `xlsx`/SheetJS,
  import dinámico). Exporta columnas visibles + filas cargadas.
- **Cache local de competencia**: ver [[competencia-partpicker-cache]] / [[contexto]].
  Hidrata de `itemsPricesCompetition:<userId>`, refresca con botón.
- **Densidad** ~21px/fila y **altura dinámica** (`updateTableBodyHeight` mide
  `.ant-table-body`, no estima header).

## Mejoras 2026-06-15 (rama catri-fine-tuning)

- **Columna fija Compra-Gamer** (Resellers): siempre muestra ese reseller aunque
  no sea el más barato. Backend agrega `compragamer` por item (mejor oferta de
  `preciosgamer_compra-gamer`). Ver [[competencia-partpicker-cache]].
- **Modal competencia**: columnas **SKU** (`codigo`) y **Part #** (`nroParte`).
- **Título en una sola línea** (ellipsis); hover sobre el título agranda la fila y
  lo muestra completo (funciona porque es UNA tabla con sticky CSS, no el overlay
  de Ant). SKU sacado de abajo del título → **columna SKU visible por defecto**.
- **Performance** (la grilla pasó de ~5s a ~1,5s):
  - Backend: `get_items_prices_grid` (query liviana, sin las subqueries pesadas de
    Stock) + `get_items_prices_grid_count` (`COUNT(DISTINCT)`), enrutadas con
    `pricesView=1` y corridas **en paralelo** (`ThreadPoolExecutor`).
  - `get_items_stocks` (Stock) **intacto** — el flag `pricesView` solo lo usa Precios.
  - **Celdas editables lazy** (`EditablePriceCell`): texto por defecto, el input de
    Ant se monta solo al click. Evita montar miles de inputs. *UX:* click para
    editar; sin tab entre celdas.
  - `prewarm_catalog` al startup del backend (competencia lista, sin esperar 30s).
- **Fix** checkbox "seleccionar todos" en cabecera: Ant solo aplica `slots.title`
  si `column.title === undefined`; `title:""` lo bloqueaba. Ver [[contexto#Gotchas conocidos]].

## Ver también

- [[arquitectura]] · [[contexto]] · [[changelog]] · [[inventario]]
- [[BluPartPicker]] — la API que provee los precios de competencia
