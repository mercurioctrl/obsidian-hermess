# API - Fix - Corrección: albclil faltante en ventas cobradas (caso DIAMOND)

**Proyecto:** [[pedidos|Pedidos]]
**Estado:** Corrección importante del análisis previo
**Fecha:** 2026-06-11
**Corrige:** [[API - Fix - Script de regularización stock doble-descuento|Script de regularización]] · [[API - Research - Causas del stockDelta distinto de cero|Causas del stockDelta]]

Una pista del usuario (serial `34F97379400841` → cliente DIAMOND SYSTEM, remito 00610352) destapó que **buena parte de la "pérdida de stock" no es pérdida: son ventas REALES cobradas a las que solo les falta la línea `albclil`.** Esto corrige la conclusión y el monto a regularizar.

---

## El caso testigo — remito 00610352 a DIAMOND SYSTEM (017404)

El 17/03/2025, además del doble-descuento en el remito `00610351`, hubo una **venta real** en el remito siguiente `00610352`:

| Pieza | Estado |
|---|---|
| Pedido `pedclit` 10396344 | ✅ existe, estado `s`, cliente DIAMOND |
| Línea `pedclil` | ✅ item 119699, **50 u** |
| Cabecera `albclit` 00610352 | ✅ existe |
| **Cuenta corriente** (`MC_CCORRIENTES_MOVIMIENTOS`, `REMITO_FP=00610352`) | ✅ **cobrado 2.269,23 USD**, `CC_ANULADO=NO` |
| Seriales | ✅ egresaron (entregados) |
| **Línea `albclil` del item** | ❌ **borrada — lo único que falta** |

La venta ocurrió y se cobró; solo desapareció la línea de detalle `albclil`. Causa: el borrado parcial de un `RemoveSaleService` **no transaccional** (que ya blindamos) borró la línea pero dejó cabecera + pedido + cobranza + serial.

Como la fórmula del `stockDelta` calcula `sales` desde `albclil`, **sub-cuenta las ventas** → reporta delta 70 cuando el stock real es 20:
```
Restaurando la línea: ventas 8930 → 8980 ; delta = 9000 − 8980 − 0 = 20 ✅ (= 20 seriales presentes)
```

---

## Verificación sistemática (los 138 ítems del race)

Se buscó el patrón en todos: líneas de pedido en estado `s` con remito emitido pero **sin** `albclil`, y se cruzó contra cuenta corriente.

- **2.136 líneas huérfanas** (vendido, remito emitido, sin `albclil`).
- **100 % con cargo en cuenta corriente** (`CC_ANULADO=NO`). **0 sin cargo.**

**Conclusión: NO hay fuga.** Todas las ventas con `albclil` faltante están cobradas.

---

## Re-verificación del monto — de 683 a 380

| Concepto | Unidades | Qué es / qué hacer |
|---|---:|---|
| Loss viejo (delta/kardex) | **683** | ❌ método incorrecto |
| **Stock REAL recuperable** (seriales presentes − sistema) | **~380** | ✅ regularizar stock |
| **Venta cobrada / `albclil` faltante** | **~303** | ⚠️ restaurar `albclil`, NO es stock |

El método correcto para el stock es el **registro de seriales** (`ST_DETALLE_STOCK`, sin egreso), no el delta:
```
recuperable = min( delta_positivo , max(0, seriales_presentes − stock_sistema) )
```
El `min` capa los seriales viejos inflados (egresos no registrados). Ej. item 7658: 1212 seriales pero delta 20 → recuperable 20.

Ejemplos del split (CSV `items_reverificado.csv`):
- `117542` SSD Netac: 75 → **75 recuperable** (todo en estante).
- `119699` Mouse: 70 → **20 recuperable + 50 vendido** (DIAMOND).
- `102048` Servicio transporte: 19 → **0** (servicio, excluido).

---

## Dos arreglos distintos (no mezclar)

1. **Stock recuperable (~380 u):** reponer a `nstock` con el script corregido `regularizar_doble_descuento.py` (ahora serial-based, da 379 en dry-run). Conviene conteo físico antes.
2. **Ventas con `albclil` faltante (~303 u):** **restaurar la línea `albclil`** desde el `pedclil`/`albclit` que sobreviven (la venta ya está cobrada). Es un arreglo documental; corrige el delta sin tocar stock. *(Pendiente: script de restauración de líneas.)*

## Ver también

- [[API - Fix - Corregir doble-descuento de stock por race en MakeSale|Fix del race (causa raíz)]]
- [[API - Fix - Script de regularización stock doble-descuento|Script de regularización (corregido)]]
- [[API - Research - Stock en estantería no reflejado en el sistema|Stock en estantería (seriales)]]
- [[relacion-tablas-ped-alb|pedclit / pedclil / albclit / albclil]]
