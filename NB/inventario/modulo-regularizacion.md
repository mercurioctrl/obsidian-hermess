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
**documental**, que puede no coincidir con lo físico.

## Origen de los descuadres

1. **Race MakeSale (doble-descuento)** — ya con guard en pedidos (`90c0a1ce`). Genera
   filas duplicadas de descuento. La pestaña lista los afectados y descompone el delta.
2. **OC recibida pero nunca documentada** — la orden quedó en estado "P", la mercadería
   se serializó e ingresó pero el `albprol` nunca se generó → el grid cuenta la venta
   pero no la compra (delta negativo). Espejo-compra del caso `albclil` de ventas.
3. **Duplicados de SKU entre empresas** — el mismo producto cargado en cc4 y cc11
   (mismo `ID_PRODUCTO`): ingresos/seriales/reservas se cruzan inconsistentemente.

## Acciones (todas gateadas por permiso `gerencia`, transaccionales, idempotentes)

- **Acción 1 — `apply_stock_regularization`**: repone a **Control** (`nstock_ctrl`,
  cuarentena) los seriales físicamente presentes que el sistema no refleja
  (`recuperable = min(delta, presentes − stockSistema)`). Marcador en `registro_stock`.
- **Acción 2 — `apply_albclil_restoration`**: restaura la línea `albclil` de ventas
  ya cobradas que un RemoveSale no transaccional borró (reconstruye desde `pedclil`).
- **`apply_albprol_restoration`** (nuevo, 2026-06-23): restaura el `albprol` faltante
  de una **OC recibida sin documentar**, desde el `pedprol` sobreviviente. Es un **puro
  asiento, cost-neutral**: NO toca stock ni costo (verificado: sin triggers en
  albprol/albprot/articulo/stocks, `NCOSTEPROM` es columna almacenada, y el FOB
  mostrado usa el **último** albprol por fecha → un asiento backdated no lo cambia).
  Usa **una sola cabecera canónica** (la menor `nnumalb`; las otras son duplicadas del
  fallo), **maneja parciales** (inserta `faltante = pedido − ya documentado`),
  idempotente. Preview con **cruce de seriales** por ítem: `serialesOC`,
  `serialesPresentes`, `stockSistema`, `gapFisico`, `serialMatch`, `perfecto`.

## Cost-neutral: por qué insertar albprol no recalcula costo

El recálculo de `NCOSTEPROM`/FOB lo hace el **flujo de recepción** del backend, NO la
existencia de la fila `albprol`. Un INSERT crudo del asiento:
- No dispara nada (no hay triggers en esas tablas).
- `NCOSTEPROM` es columna almacenada → no se toca.
- El FOB mostrado = `albprol.nprediv` de la **última** línea por `albprot.dfecalb`
  → un asiento backdated no es el último. Ver [[contexto]] (FOB).

## Caso testigo: item 111454 / OC 11568 (cc4)

`PROCESADOR AMD (AM4) RYZEN 7 5700G`, delta **−412**. Causa: OC **11568** (14 líneas,
2470 u, estado "P") recibida y vendida pero sin `albprol`. **Aplicada en prod** la
restauración (14 líneas en cabecera 15844): 7 ítems quedaron perfectos (delta 0); el
resto expuso descuadres físicos/regularizaciones previas a ajustar aparte.

## cc11 no serializa (artefacto, no error)

El barrido de "OC recibida sin albprol" dio falsos positivos en cc11/cc9. Razón:
**cc11 prácticamente no usa el ledger de seriales** (16 de 602 artículos con seriales;
**955 seriales vs 107.058 u de albprol**). Su "albprol fantasma" es un **artefacto de
medición** (comparar albprol contra seriales que no genera), no mercadería mal ruteada
ni un error a revertir. Verificado en ambos sentidos: el albprol de cc11 son OCs
propias (no de cc4), y los seriales de cc11 no son items que le falten a cc4
(cc4 está balanceado; cc11 tiene 955 seriales vs un gap de cc4 de ~528k). Los deltas
raros de cc11 son descuadres de **columnas de stock**, no cruces con cc4. Hay que
mirarlos con lente de reconciliación de stock, NO restaurar/revertir albprol.

## Clasificación catálogo-wide de deltas (cc4)

Identidad exacta: `delta = INB − HELD − OUT`, con INB = ingreso_doc − seriales_creados,
HELD = stock_sistema − seriales_presentes, OUT = salida_doc − seriales_egresados. Cada delta
se descompone en 3 discrepancias contra el ledger de seriales (vale por la invariante
creados = presentes + egresados). Scan cc4: 1.365 items con delta ≠ 0. Buckets:

- **auto_stock (24)**: solo HELD (stock ≠ serials) → reconciliar a serial, **sin recuento**.
  Aplicados a Control (295 u, `registro_stock` marcador "Regularizacion stock recuperable
  (seriales presentes)").
- **recontar (74)**: ledger inconsistente (creados ≠ pres + egres) → **recuento físico**.
- **revisar_legacy / revisar_doc / no_serializado** (granel, −1,17M en pocos): otra lente.

Ver [[regularizacion-buckets]] + el CSV `regularizacion_buckets_cc4.csv`.

**Caveat: el cierre limpio por albprol (11568) es RARO.** "restaurar-albprol" solo aplica si
`pedprol > albprol` (OC con cantidad sin documentar). Si `pedprol ≤ albprol`, el gap son
seriales sin ningún documento (legacy / ingreso no trackeado), NO restaurable. Y los pocos con
OC sin documentar suelen tener delta positivo → restaurar **sobre-corrige** (como cc11). El
bucket "auto_con_doc" no se sostiene; solo `auto_stock` es auto-cerrable seguro.

## Pendientes

- 13164/13209/13171 fueron falsos positivos (cc11/cc9 sobre-documentados).
- Definir deduplicación de artículos cross-company (mismo SKU cc4↔cc11).
- Que el grid trate distinto a empresas no-serializadoras (cc11, parte de cc9).
- `apply_albprol_restoration` aún **no está wireada a endpoint** en `main.py`.

## Ver también

- [[inventario]] · [[arquitectura]] · [[contexto]] · [[memoria]] · [[changelog]]
- [[pedidos]] — el guard del race vive ahí
