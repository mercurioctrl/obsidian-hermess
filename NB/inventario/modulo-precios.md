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
  (`prices.py`), que delega en `update_item_price` → hereda la validación de
  utilidad mínima (hoy **no bloqueante**, ver abajo), `historial_precios` y recálculo.
- Costo editable solo con permiso `gerencia`.
- **Items sin fila en `ST_GANANCIA_ESTIPULADA_ARTICULOS`** (típicamente los más nuevos): `_update_gain_column` es **upsert** — inserta la fila sembrada si no existe. Antes el `UPDATE` puro afectaba 0 filas en silencio y la utilidad no persistía. La tabla no tiene PK; clave = `articulo.cRef` (nvarchar). Ver [[contexto#Gotchas conocidos]] y [[memoria]].

## Columnas de costo: FOB vs NCOSTEPROM

El grid muestra **dos** costos, que NO son lo mismo:

- **Costo (`NCOSTEPROM`)** — costo promedio almacenado en `articulo`; es la **base del cálculo de precios** (la fórmula de arriba).
- **FOB** — sale de `NewBytes_DBF.dbo.albprol.nprediv`, tomando la **última línea de albarán de proveedor** del artículo:
  `OUTER APPLY (SELECT TOP(1) albprol.nprediv FROM albprol JOIN albprot ON albprol.nnumalb = albprot.nnumalb WHERE albprol.cref = articulo.cref ORDER BY albprot.dfecalb DESC)`.
  Es el FOB del ingreso de compra más reciente. Subquery **idéntica** en `prices.py` (`_read_current_prices`) y `stocks.py` → FOB consistente entre Precios y Stock. Si el artículo no tiene líneas en `albprol`, devuelve NULL → `0.0`.
  *(Detalle relevante para [[modulo-regularizacion]]: restaurar un `albprol` backdated NO mueve el FOB mostrado, porque este usa el albarán más reciente por fecha.)*

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

## Búsqueda tolerante a paréntesis (2026-06-24)

La búsqueda por slug fallaba con títulos que tienen `()`/símbolos (ej. el slug
`procesador_intel_lga1700` no matcheaba "PROCESADOR INTEL (LGA1700)"): en `LIKE`
el `_` es comodín de 1 char y los paréntesis agregan caracteres. Se reemplaza `_`
y espacio por `%`. Aplicado en Precios, Stock y Productos (back `7534f92`/`0c0cfcf`).

## Utilidades negativas (2026-07-13)

Una utilidad puede ser **negativa**, y la utilidad **total** de un par también:

- `MAY1 = 10` + `MAY2 = -9` ⇒ utilidad MAY = **1%**.
- `LO1 = 5` + `LO2 = -10` ⇒ utilidad LO = **-5%** ⇒ el precio queda **por debajo del costo, a propósito**.

Aplica igual en la pestaña **Precios** y en el *ctrl precios* de la grilla de **Stock** (comparten `EditablePriceCell` y `PATCH /itemsPrice`).

- **Input**: `EditablePriceCell` tiene prop `allowNegative` (antes `:min="0"` fijo impedía tipear el menos). Activada en las 8 utilidades (PL, PLI, MAY1, MAY2, LO1, LO2, PML, PCAM). **Costo, precios y DT2/DT3 siguen `>= 0`**.
- **Utilidad mínima = aviso, no bloqueo**: `_validate_min_utility` sigue comparando la **suma del par** contra `minUtility` (`PV_PARAMETROS_VARIOS`), pero el `422 MIN_UTILITY_NOT_MET` ahora es **confirmable** (lleva `totalUtility` / `minUtility` / `confirmable`). El front muestra el modal y reenvía el mismo PATCH con **`force=true`** (`ItemPriceUpdateRequest.force`). Sin `force`, el comportamiento es el de siempre. Las excepciones previas (`minUtilityExclude=1`, familia 65) siguen sin preguntar nada.
- **Revert de la celda**: `EditablePriceCell` emite `{ value, done }`; `done(false)` (error o cancelación) devuelve la celda al valor original. Guard `pending` para no emitir dos veces con Enter (Enter + blur).
- **Recálculo masivo**: sin clamp a 0; los cambios bajo la mínima se confirman juntos en un único modal al final.
- Helper `app/utils/minUtility.js`: `minUtilityError()` / `confirmMinUtility()` / `minUtilityContent()`.

Ramas `feature/utilidad-negativa` (front `03f23d7`, back `aa13999`), pusheadas, PRs sin abrir.

## Ver también

- [[arquitectura]] · [[contexto]] · [[changelog]] · [[inventario]]
- [[modulo-regularizacion]] — comparte la grilla de Stock y el costo FOB
- [[BluPartPicker]] — la API que provee los precios de competencia
