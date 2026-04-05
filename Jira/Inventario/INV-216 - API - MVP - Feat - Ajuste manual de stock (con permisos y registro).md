---
jira_key: "INV-216"
aliases: ["INV-216"]
summary: "API - MVP - Feat - Ajuste manual de stock (con permisos y registro)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-20 08:39"
updated: "2025-12-05 03:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-216"
---

# INV-216: API - MVP - Feat - Ajuste manual de stock (con permisos y registro)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-20 08:39 |
| Actualizado | 2025-12-05 03:47 |
| Etiquetas | ninguna |
| Jira | [INV-216](https://bluinc.atlassian.net/browse/INV-216) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **has action item:** [[INV-235 - APP - Feat - Ajuste manual de stock|INV-235]] APP - Feat - Ajuste manual de stock 

## Descripcion

Se implementará una **feature** para ajustar manualmente el stock operativo de un ítem.
El ajuste **solo** podrá ejecutarlo un usuario que tenga el permiso `regularizacion = 1` en `[NB_WEB].[dbo].[permisos_agente]`.
Si el usuario **no** posee dicho permiso, el endpoint deberá responder con el error HTTP correspondiente indicando que no tiene permisos

```
POST {API_URL}/itemsStocks/{itemId}/manualAdjustments
```

```
{
  "amount": 5,
  "reason": "Ajuste por conteo físico",
  "warehouseStockId" : 2
}
```

- `itemId` (path): identificador del ítem a ajustar.


- `amount` (body): **valor objetivo** al que se quiere llevar `nstock_d1` (no es el delta).


- `reason` (body): comentario del ajuste; se persistirá en `registro_stock.query`.



**RTA**:

```
{
  "updated": true,
  "itemId": 101537,
  "previous": 5,
  "current": 7,
  "delta": 2,
  "reason": "Ajuste por conteo físico",
}
```

> Nota: El **delta** aplicado será `amount - nstock_d1_actual`.
Ej.: Si `nstock_d1 = 5` y llega `amount = 7` ⇒ **delta = +2**.


## Reglas y validaciones

- **Permisos**: verificar que el agente autenticado tenga `regularizacion = 1` en `[NB_WEB].[dbo].[permisos_agente]`.

- Si no cumple: **403 Forbidden** con mensaje “No tiene permisos para regularizar stock.”




- **Existencia de ítem**: si `itemId` no existe: **404 Not Found**.


- **amount**:

- Debe ser un entero `>= 0`. Si no: **422 Unprocessable Entity**.




- **No-Op**: si `amount` es igual al valor actual de `nstock_d1`, responder **200 OK** con `{ "updated": false, "message": "Sin cambios" }` y **no** registrar movimiento.


- **Concurrencia**: el ajuste debe realizarse dentro de una **transacción** y con **lock** de fila para evitar colisiones.


- **Registro histórico**: todo ajuste que cambie el valor debe crear un registro en `[NB_WEB].[dbo].[registro_stock]`.


- **Atomicidad**: ante cualquier error, **ROLLBACK** sin efectos parciales.


- **Auditoría**: incluir `agente` (usuario ejecutor) y marcas antes/después del stock.



## Comportamiento de stock

- Campo afectado: `dbo.Stocks.nstock_d1`.


- Se calcula `@Delta = @AmountObjetivo - @nstock_d1_actual` y se aplica:



```
UPDATE dbo.Stocks
   SET nstock_d1 = @AmountObjetivo
 WHERE ItemId = @ItemId;
```

- El **registro histórico** guardará:

- `sAnterior = @nstock_d1_actual`


- `sPosterior = @AmountObjetivo`


- `cantidad = @Delta` (lo efectivamente agregado/restado)


- `query = @Reason`


- Además tomará **los valores actuales** (luego del UPDATE o antes, ver “Timing” abajo) de:

- `nstock_postventa`


- `nstock_lo_reserva_pedidos`


- `nstock_reserva_pedidos`


- `nstock_d1`


- `nstock_en_cola`


- `nstock`


- `nstock_lo`


- `nstock_ctrl`







### Timing recomendado para el snapshot

- Guardar `sAnterior` antes del UPDATE.


- Ejecutar el UPDATE a `nstock_d1 = @AmountObjetivo`.


- Leer nuevamente los campos y **persistir en registro_stock el estado posterior** (incluyendo `nstock_d1` ya actualizado).
Así el registro refleja claramente “antes/después”.



## Respuestas

- **201 Created** (cuando hubo cambio): retorna el resumen del ajuste y el id del registro creado.


- **200 OK** (sin cambios).


- **403 Forbidden** (sin permiso).


- **404 Not Found** (ítem no existe).


- **422 Unprocessable Entity** (validaciones).


- **409 Conflict** (si se detecta alguna condición de negocio que impida el ajuste).


- **500** (error inesperado, con rollback).
