# Módulo — Movimientos de stock (transferencias entre depósitos)

Documentado el **2026-09-15** leyendo el código (no hay cambios de esta sesión).

Hay **tres** mecanismos distintos para tocar stock desde la pestaña Stock, y conviene
no confundirlos:

| Mecanismo | Endpoint | Qué hace |
|-----------|----------|----------|
| **Transferencia entre depósitos** | `POST /stock-transfers` | Mueve `nstock` de un almacén a otro |
| **Mover entre columnas** | `moveStock` → `move_stock_between_columns` | Mueve entre buckets (General/Control/Oculto/D1…) **dentro del mismo depósito** |
| **Ajuste manual** | `POST /itemsStocks/{itemId}/manualAdjustments` | Pisa el valor de un bucket. Ver [[modulo-regularizacion]] |

## Transferencia entre depósitos — flujo completo

### Frontend

- Modal *"Mover stock a otro depósito"* en `pages/itemsStock.vue` (~línea 864); handler
  `moveStockWarehouse()` (~línea 1695).
- El selector de **origen** se arma desde `itemsStocksWarehouse`, o sea solo depósitos
  donde el artículo **ya tiene fila** de stock. El destino sale de `warehouses`
  (preselecciona el `Predeterminado` de la empresa, ver [[changelog#2026-08-26 — Feature APA/Soportes + depósito en Precios (filtro y predeterminado)|changelog]]).
- Payload: `{ fromWarehouseId, toWarehouseId, reason, items: [{ itemId, quantity }] }`
  (la API acepta **lote** de items, pero la UI manda siempre uno solo).
- `plugins/api.js` → `moveStockWarehouse()` → `POST stock-transfers`.

### Backend

`main.py:create_stock_transfer` → `core/controllers/stocks/stocks.py:transfer_stock_between_warehouses`.

Todo corre en **una transacción** (`autocommit = False`, un solo `commit()` al final;
cualquier excepción hace `rollback()` de todo el lote):

1. **Valida depósitos** contra `NewBytes_DBF.dbo.FP_Almacen`: que existan los dos y que
   compartan `companyCode` → si no, `400`. **No se puede transferir entre compañías.**
2. Por cada item:
   - Lee la fila origen de `NewBytes_DBF.dbo.stocks` con `WITH (UPDLOCK, ROWLOCK)`;
     si no existe → `404`.
   - Valida `nstock >= quantity` → si no, `409` informando el disponible.
   - `UPDATE stocks SET nstock = nstock - quantity` en origen.
   - Lee destino con el mismo lock: si existe, `nstock + quantity`; si **no existe, la
     crea** (`INSERT` de 18 columnas, busca `cRef` en `articulo`, usa el `CCODALM` del
     destino, `ID_TIPOSTOCK = 1` y el resto de los buckets en 0). Es el mismo `INSERT`
     que reusa el ajuste manual — ver [[memoria#Ajuste manual crea la fila de stock si no existe (2026-07-08)]].
   - Inserta **dos filas de auditoría** en `NB_WEB.dbo.registro_stock`:
     `cantidad = -quantity` con `query = "TRANSFER OUT to warehouse X | motivo"` y
     `cantidad = +quantity` con `"TRANSFER IN from warehouse Y | motivo"`. Ambas guardan
     `sAnterior`/`sPosterior`, snapshot de todos los buckets, `ID_ALMACEN`, `agente`
     (sale del `usuario` del JWT) y `justificacion`.
3. El `transferId` devuelto es el `SCOPE_IDENTITY()` del **primer** insert de auditoría
   (no hay tabla de cabecera de transferencia).

### Límites a tener en cuenta

- **Solo se mueve el bucket `nstock` (General).** `nstock_lo` (Oculto), `nstock_ctrl`
  (Control), `nstock_d1`, `nstock_postventa` y las reservas se leen para el snapshot de
  auditoría pero **no se transfieren**: si el stock está en Control u Oculto hay que
  pasarlo antes a General con "mover entre columnas". Ver [[regularizacion-buckets]].
- **No toca seriales**: la tabla de series no se actualiza con el nuevo depósito, así que
  tras una transferencia el serial sigue figurando en el almacén viejo. Ver [[modulo-seriales]].
- Validaciones Pydantic (`StockTransferRequest`, `core/models/models.py`): `quantity > 0`,
  `itemId > 0`, `reason` no vacío y `fromWarehouseId != toWarehouseId`.
- El N+1 de escritura (una conexión/statement por item) se dejó a propósito por ser
  transaccional — ver [[memoria#N+1 con dbconnection (backend) — clave]].
- El refresco de la grilla tras transferir se hace con update inmutable (spread), no
  mutando el state de Vuex — ver [[changelog#2026-08-21 — Fixes de la grilla de Stock: historial, mutaciones Vuex|changelog]].

## Ver también

- [[arquitectura]] · [[modulo-regularizacion]] · [[regularizacion-buckets]] · [[modulo-seriales]] · [[inventario]]
