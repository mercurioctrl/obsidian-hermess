---
jira_key: "INV-221"
aliases: ["INV-221"]
summary: "[DEPRECADA] API - MVP - Feat - Mover stock entre stocks del mismo item"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-31 09:06"
updated: "2025-10-31 10:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-221"
---

# INV-221: [DEPRECADA] API - MVP - Feat - Mover stock entre stocks del mismo item

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-31 09:06 |
| Actualizado | 2025-10-31 10:52 |
| Etiquetas | ninguna |
| Jira | [INV-221](https://bluinc.atlassian.net/browse/INV-221) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

Implementar un recurso que mueva cantidad entre las columnas (buckets) del **mismo** `itemId` y `warehouseId` en `[NewBytes_DBF].[dbo].[stocks]`, dejando auditoría en `[NB_WEB].[dbo].[registro_stock]`.
Buckets involucrados:

- `[nstock_lo]`


- `[nstock]`


- `[nstock_en_cola]`


- `[nstock_d1]`


- `[nstock_reserva_pedidos]`


- `[nstock_lo_reserva_pedidos]`


- `[nstock_postventa]`



El movimiento **no agrega ni quita unidades totales**: solo las mueve.
Debe ser **atómico**, **a prueba de colisiones** y **auditable**.

```
PATCH {API_URL}/v1/stockBucketTransfers
```

**Payload**

```
{
  "itemId": 123836,
  "warehouseId": 2,
  "fromBucket": "nstock",
  "toBucket": "nstock_d1",
  "quantity": 5,
  "reason": "Movimiento entre stocks",
}
```

**Responde**

```
{
  "success": true,
  "message": "Stock bucket transfer completed",
  "data": {
    "itemId": 123836,
    "warehouseId": 2,
    "fromBucket": "nstock",
    "toBucket": "nstock_d1",
    "quantity": 5,
  }
}

```

**Si falla**

```
{
  "success": false,
  "message": "Stock total en nstock_d1 no alcanza para realizar el movimiento. Se aborta.",
  "data": {
    "itemId": 123836,
    "warehouseId": 2
  }
}
```

## Reglas, Validaciones e Invariantes

- `quantity > 0`.


- `fromBucket != toBucket`.


- Buckets válidos únicamente del set listado.


- Debe existir fila en `[stocks]` para (`itemId`, `warehouseId`) y pertenecer al mismo `companyCode`.


- `fromBucket_value >= quantity` (no permitir negativos).


- **Concurrencia**: una única `UPDATE` atómica sobre la fila con `WITH (ROWLOCK, UPDLOCK, HOLDLOCK)` en transacción.


- **Invariante de conservación** (**obligatorio**):
Sea

```
total = nstock_lo + nstock + nstock_en_cola + nstock_d1
      + nstock_reserva_pedidos + nstock_lo_reserva_pedidos + nstock_postventa

```

→ Debe cumplirse **total_before == total_after**.
Si no, **ROLLBACK** y error.



## Auditoría en `[NB_WEB].[dbo].[registro_stock]`

Una inserciones por operación (a diferencia de entre depositos):

Ejemplo de un movimiento

- **ORIGEN**



- `warehouseId`, `itemId`, `stockBucket = fromBucket`, `cantidad = -quantity`


- `sAnterior` (bucket origen antes), `sPosterior` (después)


- `justificacion = reason | Reasignación buckets`


- Snapshot completo de todos los buckets **después** (y si el modelo lo permite, guardar también el “before”)



## Criterios de aceptación

- Mueve stock entre dos buckets válidos del mismo `itemId` y `warehouseId`.


- `fromBucket_value >= quantity`; nunca quedan bucket negativos.


- **Una única **`UPDATE`** atómica** con locks (`ROWLOCK, UPDLOCK, HOLDLOCK`) en transacción.


- **Conservación total**: `total_before == total_after` (si no, rollback y error).


- **Sin lost updates** (colisiones evitadas por locks + condición de suficiencia).


- Una entradas en `registro_stock` (salida negativa en `fromBucket`, entrada positiva en `toBucket`), con `sAnterior/sPosterior` y snapshot completo.


- Respuestas estándar (`success`, `message`, `data`) incluyendo `totals.before/after`.


- Errores claros: bucket inválido, stock insuficiente, suma inconsistente, fila inexistente.
