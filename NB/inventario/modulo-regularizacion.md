# Módulo Regularización de stock

Pestaña **Regularización** (`/regularizacion`) + controladores backend para corregir
descuadres de stock (delta del grid). Backend: `core/controllers/regularization/regularization.py`.
Frontend: pestaña + `components/Modal/RegularizationDetail.vue`.

## Qué es el "delta" del grid

El delta de la grilla de Stock es **pura aritmética de documentos**, NO de seriales
(`stocks.py:700`):

```
delta = inProviderInbound(albprol) − aftersalesCreditNote(RMA) + creditNoteReturn(albclil.ACREDITADO)
        − nstockHide − stock − stockLio − stockCtrl − stockLoQueue
        − salesReserved(albclil ntipoalb=1) − sales(albclil ntipoalb>1) + regularizacion_global
```

- **delta < 0** → vendiste/tenés más de lo que compraste (ingreso sub-documentado).
- **delta > 0** → compraste más de lo que tenés/vendiste (sobre-documentado o faltante físico).

El ledger de seriales (`ST_DETALLE_STOCK`) es la **verdad física** y cierra por
construcción (creados = presentes + egresados); el delta mide consistencia
**documental**, que puede no coincidir con lo físico. **Un item con `columnas_stock == seriales_presentes` está sano aunque su delta ≠ 0** (el residuo es ruido documental).

## Origen de los descuadres

1. **Race MakeSale (doble-descuento)** — ya con guard en pedidos (`90c0a1ce`). Genera
   filas duplicadas de descuento. La pestaña lista los afectados y descompone el delta.
2. **OC recibida pero nunca documentada** — la orden quedó en estado "P", la mercadería
   se serializó e ingresó pero el `albprol` nunca se generó → el grid cuenta la venta
   pero no la compra (delta negativo). Espejo-compra del caso `albclil` de ventas.
3. **Gap serial↔columnas** — seriales físicamente presentes que las columnas de stock no
   reflejan (descuadre interno). Delta positivo, **recuperable a Control**.
4. **Duplicados de SKU entre empresas** — el mismo producto cargado en cc4 y cc11
   (mismo `ID_PRODUCTO`): ingresos/seriales/reservas se cruzan inconsistentemente.
5. **Re-tagueo de era vieja** — `ID_COMPRA` de seriales y `albprot.nnumped` numerados
   distinto (pre-2022): el albprol existe pero "no matchea" por orden. Neto ≈ 0, NO restaurar.

## Acciones (todas gateadas por permiso `gerencia`, transaccionales, idempotentes)

- **Acción 1 — `apply_stock_regularization`**: repone a **Control** (`nstock_ctrl`,
  cuarentena) los seriales físicamente presentes que el sistema no refleja
  (`recuperable = min(delta, presentes − stockSistema)`), para items del universo del race.
- **Acción 2 — `apply_albclil_restoration`**: restaura la línea `albclil` de ventas
  ya cobradas que un RemoveSale no transaccional borró (reconstruye desde `pedclil`).
- **`apply_albprol_restoration`** (2026-06-23): restaura el `albprol` faltante
  de una **OC recibida sin documentar**, desde el `pedprol` sobreviviente. Es un **puro
  asiento, cost-neutral**: NO toca stock ni costo (verificado: sin triggers en
  albprol/albprot/articulo/stocks, `NCOSTEPROM` es columna almacenada, y el FOB
  mostrado usa el **último** albprol por fecha → un asiento backdated no lo cambia).
  Usa **una sola cabecera canónica**, **maneja parciales**, idempotente. Preview con
  **cruce de seriales** por ítem.
- **`apply_serial_gap_to_control`** (NUEVO 2026-06-25): cierra el delta+ residual
  reponiendo a **Control** el **gapFísico** = `presentes − columnas_stock` por depósito,
  **sin depender del universo del race** (sirve para la cola de albprol restaurado y
  cualquier item). Tope = delta canónico (no sobre-corrige), `COUNT(DISTINCT SERIAL)`,
  marcador `MARCADOR_SERIAL_GAP`, dry-run por defecto.

- **`apply_acreditado_correction`** (2026-06-26): corrige `albclil.ACREDITADO` cargado por
  encima de lo realmente acreditado por la NC real → quita el crédito fantasma que infla el
  delta+. Key = `IdDetalleRemito` (único por línea). Valor autoritativo en vivo desde la NC
  real (`FP_FactWebCli`, NTIPODOCU=2). NO toca la NC real ni AFIP. Aplicado en prod.

## Test de "gap limpio" (3 identidades del ledger)

Antes de reponer un delta+, verificar que el descuadre vive **solo en columnas** (los
presentes son estante real, no ventas sin egresar):

1. **compra**: `albprol == filas_serial_totales`
2. **egreso**: `egresados == ventas(ntipoalb>1) + RMA(accion2) − notasCrédito(ACREDITADO)`
   — **incluir SIEMPRE las NC**: una devolución re-ingresa el serial (egreso→NULL).
3. **estante**: `presentes == albprol − ventas − rma + notasCrédito`
4. y `delta == presentes − columnas`

Si los 4 cierran → seguro reponer a Control. **Contar presentes con `COUNT(DISTINCT SERIAL)`**:
los items legacy (≤2022) tienen filas duplicadas/blank del mismo serial presentes que
inflan `COUNT(*)` (genera gap fantasma).

## Cost-neutral: por qué insertar albprol no recalcula costo

El recálculo de `NCOSTEPROM`/FOB lo hace el **flujo de recepción** del backend, NO la
existencia de la fila `albprol`. Un INSERT crudo del asiento no dispara nada (sin
triggers), `NCOSTEPROM` es columna almacenada, y el FOB usa el **último** albprol por
`albprot.dfecalb` → un asiento backdated no es el último. Ver [[contexto]] (FOB).

## Caso 111454 / OC 11568 (cc4) — CERRADO

`PROCESADOR AMD (AM4) RYZEN 7 5700G`. La OC **11568** (14 líneas, 2470 u, estado "P")
fue recibida y vendida sin `albprol`; se restauró en cabecera 15844. **Cola resuelta
(2026-06-25)**: los 5 items con resto positivo se cerraron con `apply_serial_gap_to_control`
(Catriel 7463): 4 limpios a 0 (64 u); **111454** repuso 19 físicos (→69) y, tras corregir
una **NC de 2022 con error de carga** (`ACREDITADO 100→10`, 90 u fantasma), quedó en **−21**.

**El −21 NO es albprol restaurable** (hallazgo clave): el cruce serial(`ID_COMPRA`)↔albprol
(`albprot.nnumped`) **por orden** muestra que el albprol ya existe, solo mal numerado en
la era vieja — 4.277 u de seriales en órdenes sin albprol espejadas por 4.705 de albprol
en órdenes sin seriales → neto **+17**. Restaurar duplicaría. La "reg +983" de notas
viejas **no existía** (eran movimientos `nstock→nstock_d1`). Item **sano**: `columnas==presentes==977`.

**Regla**: detectar albprol-faltante-real = gap **por orden** con `pedprol` vivo (OC 11568),
NO el neto agregado del artículo.

## Barrido "gap limpio" cc4 (2026-06-25, aplicado en prod)

De **2.751** items cc4 con delta>0, solo **150** pasan el test de 3 identidades. Aplicados
con `apply_serial_gap_to_control` (Catriel 7463): **143 cerraron a delta 0**, 355 u a
Control, **0 negativos** (sin sobre-corrección). 7 residuos legacy (101484, 6816, 6814...)
con filas de serial duplicadas/blank presentes — la función (DISTINCT) repuso solo el real.
Los **2.601 restantes** son causas documentales/re-tagueo (no tocar). Junto con los 24
`auto_stock` y los 5 de la cola OC 11568: **170 items** con stock vendible realineado a la
verdad física de seriales. Scripts: `sweep_gap_limpio_cc4.py` + `run_sweep_gap_limpio.py`.

## cc11 no serializa (artefacto, no error)

El barrido de "OC recibida sin albprol" dio falsos positivos en cc11/cc9. Razón:
**cc11 prácticamente no usa el ledger de seriales** (16 de 602 artículos con seriales;
**955 seriales vs 107.058 u de albprol**). Su "albprol fantasma" es un **artefacto de
medición**, no mercadería mal ruteada ni un error a revertir. Los deltas raros de cc11
son descuadres de **columnas de stock**, no cruces con cc4. Hay que mirarlos con lente de
reconciliación de stock, NO restaurar/revertir albprol.

## Clasificación catálogo-wide de deltas (cc4)

Identidad exacta: `delta = INB − HELD − OUT`. Scan cc4: 1.365 items con delta ≠ 0 (snapshot
2026-06-23; el universo delta>0 da 2.751). Buckets:

- **auto_stock (24)**: solo HELD (stock ≠ serials) → reconciliar a serial, **sin recuento**.
  Aplicados a Control (295 u).
- **recontar (74)**: ledger inconsistente (creados ≠ pres + egres) → **recuento físico**.
- **revisar_legacy / revisar_doc / no_serializado** (granel, −1,17M en pocos): otra lente.

Ver [[regularizacion-buckets]] + el CSV `regularizacion_buckets_cc4.csv`.

**Caveat: el cierre limpio por albprol (11568) es RARO** y "restaurar-albprol" solo aplica
con `pedprol > albprol` por orden; el bucket "auto_con_doc" no se sostiene.

## Corrección de ACREDITADO fantasma (NC real en FP_FactWebCli)

`albclil.ACREDITADO` (cantidad acreditada de una línea de venta) entra en el delta con
signo **+**. Hay un patrón de **error de carga**: líneas con `ACREDITADO > ncanent`
(imposible: no se acredita más de lo vendido en la línea) → inflan el delta+ con crédito
fantasma. En cc4: **88 líneas / 81 items / 772 u**, concentradas en ~30 NC viejas (2021-22);
3 NC explican 574 u (`X000200538000`=385, `X000200545212`=149, `X000200532935`=40).

**Fuente autoritativa de la NC real**: `NewBytes_DBF.dbo.FP_FactWebCliEncabezado` +
`FP_FactWebCliDetalle`, vinculadas a `albclit` por **`ID_NROREMCLI_ENC`**; **`NTIPODOCU=2`
= Nota de Crédito** (`LANULADA` bit). Cantidad real acreditada por artículo =
`SUM(FP_FactWebCliDetalle.NCANENT)` de las NC del remito. (El archivo `MS_NOTASCREDITO_*`
termina abril-2021 y NO sirve.)

**Aplicado en prod (2026-06-26, Catriel)**: 88 líneas corregidas, **772 u** de crédito
fantasma removido, 0 imposibles restantes en cc4, traza en `registro_stock`. 65 a su NC real,
23 capeadas a `ncanent`.

**CAVEAT (landmine)**: el alcance seguro es SOLO `ACREDITADO > ncanent`. NO usar
`ACREDITADO > nc_real`: el enlace FP_FactWebCli es **incompleto** (la mayoría de los
`ACREDITADO>0` no encuentran su NC; con esa condición el dry-run explotó a 2.615 líneas /
9.105 u). "Sin NC ⇒ corregir a 0" es FALSO en general → regla segura: **NC real si existe,
si no cap a `ncanent` (nunca 0)**. Bajar ACREDITADO empuja algunos deltas a negativo (benigno).
Es fix del campo denormalizado del lado stock, no contable.

## Ajuste manual de nstock_d1 (manualAdjustments)

`POST /itemsStocks/{itemId}/manualAdjustments` → `manual_adjust_item_stock` (`stocks.py`).
Ajuste directo del campo `nstock_d1` de un artículo, gateado por permiso `regularizacion = 1`
(en `NB_WEB.dbo.permisos_agente`), transaccional con `UPDLOCK/ROWLOCK`, no-op si
`amount == nstock_d1` actual, y traza en `NB_WEB.dbo.registro_stock` (`justificacion = reason`).
El body `warehouseStockId` mapea directo a `ID_ALMACEN`. Función hermana:
`alter_stock_d1` (mismo patrón, permiso `alterStock`).

**Crea la fila si no existe (2026-07-08)**: antes devolvía `404 "Item no encontrado"` cuando el
artículo no tenía fila en `stocks` para ese `ID_ALMACEN` (mensaje engañoso: faltaba la fila de
stock, no el artículo). Ahora, si `(ID_ARTICULO, ID_ALMACEN)` no existe, la crea con todo en 0
(mismo `INSERT` de 18 columnas que la transferencia entre almacenes `stocks.py:2100` / alta de
producto / kits) y el ajuste sigue normal (`previous=0 → current=amount`). **Guards**: solo crea
si el artículo existe en `articulo` y el almacén en `FP_Almacen` (si no, 404); creación concurrente
manejada (`IntegrityError` → re-SELECT). Rama `feature/manual-adjust-crea-stock-inexistente`
(`1b24882`, **PR sin abrir**). `alter_stock_d1` **no** se tocó (mismo patrón de 404 pendiente).

## Pendientes

- Ninguna acción de regularización está **wireada a endpoint** en `main.py` (todas vía scripts ad-hoc).
- El enlace NC real (FP_FactWebCli) es **incompleto** para el caso general de ACREDITADO — solo los `>ncanent` son corregibles con confianza.
- `apply_albprol_restoration` y `apply_serial_gap_to_control` también sin endpoint
  en `main.py` (se operan vía scripts ad-hoc).
- 7 residuos legacy del barrido (duplicados de serial en el ledger) — limpieza opcional.
- Re-clasificar bucket `auto_con_doc` con el filtro `pedprol > albprol` (por orden).
- 74 items para **recuento físico** (ledger inconsistente).
- Definir deduplicación de artículos cross-company (mismo SKU cc4↔cc11) y que el grid
  trate distinto a empresas no-serializadoras.

## Ver también

- [[inventario]] · [[arquitectura]] · [[contexto]] · [[memoria]] · [[changelog]] · [[regularizacion-buckets]]
- [[pedidos]] — el guard del race vive ahí
