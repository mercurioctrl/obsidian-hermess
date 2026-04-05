---
jira_key: "INV-217"
aliases: ["INV-217"]
summary: "API - MVP - Feat - Mover stock entre columnas (conservando totales)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-20 09:39"
updated: "2025-12-05 03:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-217"
---

# INV-217: API - MVP - Feat - Mover stock entre columnas (conservando totales)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-20 09:39 |
| Actualizado | 2025-12-05 03:57 |
| Etiquetas | ninguna |
| Jira | [INV-217](https://bluinc.atlassian.net/browse/INV-217) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

Se implementará una **feature** para **mover stock** entre columnas de la tabla `[NewBytes_DBF].[dbo].[stocks]` para un determinado `itemId` (y su `warehouseStockId`), **garantizando la conservación del total**.
Columnas afectadas (origen/destino posibles):

- `nstock_ctrl`


- `nstock_lo`


- `nstock`


- `nstock_en_cola`


- `nstock_d1`



**Invariante:** la **suma** de estas cinco columnas debe ser **idéntica antes y después** del movimiento. Si el movimiento no mantiene esta invariante, **no se realiza**.

```
PATCH {API_URL}/itemsStocks/moves
```

```
{
  "itemId":323,
  "warehouseStockId": 3,              // ID del registro de stock en depósito (si corresponde a tu modelo)
  "from_column": "nstock_d1",                  // columna origen (enum)
  "to_column": "nstock_lo",                    // columna destino (enum)
  "amount": 5,                          // unidades a mover
  "reason": "Reubicación operativa"     // opcional: motivo/auditoría
}
```

### Reglas y validaciones

- **Existencia de registro**: debe existir una fila en `stocks` para `itemId` (y `warehouseStockId` cuando aplique). Si no: **404 Not Found**.


- **Campos válidos**:

- `from` y `to` deben estar en `{ nstock_ctrl, nstock_lo, nstock, nstock_en_cola, nstock_d1 }`.


- `from != to`. Si no: **422 Unprocessable Entity**.




- **Amount**: entero `> 0`. Si no: **422**.


- **Stock suficiente en origen**: el valor de `from` debe ser `>= amount`. Si no: **409 Conflict** (insuficiente).


- **Conservación de total**:

- Se calcula `total_before = nstock_ctrl + nstock_lo + nstock + nstock_en_cola + nstock_d1`.


- Se simula el movimiento: `from' = from - amount`, `to' = to + amount`, el resto igual.


- Se verifica `total_after == total_before`. Si no: **409 Conflict** (no conserva total) y no se aplica.




- **Concurrencia**: la operación debe ejecutarse dentro de **TRAN** y con **bloqueo de fila** (`UPDLOCK, ROWLOCK, HOLDLOCK`) para evitar colisiones.


- **Atomicidad**: ante cualquier error, **ROLLBACK** sin efectos parciales.


- **Auditoría**: registrar el movimiento (p.ej., en `[NB_WEB].[dbo].[registro_stock]`), incluyendo `itemId`, `warehouseStockId`, `from`, `to`, `amount`, snapshot antes/después y `reason`.



## Respuestas

- **201 Created**: movimiento aplicado; devolver resumen (valores antes/después de `from` y `to`, y `total` invariante).


- **404 Not Found**: no se encuentra el registro de stock.


- **422 Unprocessable Entity**: validaciones de campos y formato.


- **409 Conflict**: stock insuficiente o violación de invariante de suma.


- **500 Internal Server Error**: error inesperado (con rollback).



## Criterios de Aceptación

- ✅ El endpoint **no** permite `from == to`.


- ✅ `amount > 0` obligatorio.


- ✅ Retorna **404** si no existe fila de stock para `itemId` (y `warehouseStockId` si aplica).


- ✅ Retorna **409** si el **stock origen** es insuficiente.


- ✅ Retorna **409** si el movimiento **no conserva** el total.


- ✅ Aplica **TRAN** + **locks** de fila para evitar colisiones.


- ✅ Tras aplicar, la **suma** de las cinco columnas es exactamente la misma que antes.


- ✅ (Opcional) Se registra auditoría con `reason` y snapshot antes/después.
