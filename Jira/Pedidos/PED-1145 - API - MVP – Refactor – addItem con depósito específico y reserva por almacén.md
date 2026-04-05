---
jira_key: "PED-1145"
aliases: ["PED-1145"]
summary: "API - MVP – Refactor – addItem con depósito específico y reserva por almacén"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-07 09:10"
updated: "2025-10-28 10:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1145"
---

# PED-1145: API - MVP – Refactor – addItem con depósito específico y reserva por almacén

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-07 09:10 |
| Actualizado | 2025-10-28 10:50 |
| Etiquetas | ninguna |
| Jira | [PED-1145](https://bluinc.atlassian.net/browse/PED-1145) |

## Relaciones

- **Padre:** [[PED-1107 - Almacenes Multiples|PED-1107]] Almacenes Multiples
- **has action item:** [[PED-1146 - APP - MVP – Refactor – addItem con depósito específico|PED-1146]] APP - MVP – Refactor – addItem con depósito específico
- **action item from:** [[PED-1146 - APP - MVP – Refactor – addItem con depósito específico|PED-1146]] APP - MVP – Refactor – addItem con depósito específico

## Descripcion

Refactorizar el endpoint 

```
PATCH /v1/orders/addItem
```

```
{
  "order": "10425810",
  "branch": "0002",
  "itemId": 119555,
  "amount": 1,
  "stockWarehouseId": 3
}
```

para **exigir** `stockWarehouseId` en el payload y validar/reservar stock **por almacén**. 

Si el depósito seleccionado no posee stock suficiente para la cantidad solicitada, debe responder un error informando las unidades disponibles en ese depósito. 

Se permite que el mismo ítem se agregue en **múltiples llamadas** usando distintos depósitos para alcanzar la cantidad total deseada, pero **nunca** superar el stock del depósito elegido en cada llamada. 

Además, refactorizar `updateReserveStock` para operar **fila a fila por almacén** sobre `[NewBytes_DBF].[dbo].[stocks].nstock_reserva_pedidos`.

## Contexto y objetivos

- Hoy el recurso agrega ítems sin especificar el depósito y/o reserva stock a nivel global del artículo.


- Necesitamos controlar de **qué almacén** se descontará la reserva, validando contra el disponible de ese almacén:
`stockDisponible = nstock - nstock_reserva_pedidos` (de la **misma** fila `stocks` del depósito).


- Debe actualizarse la **reserva por almacén** (no global) para evitar sobreventa y permitir picking correcto.



## Alcance (In Scope)

- **Endpoint existente:** `PATCH /v1/orders/addItem` (mismo path / versión).


- **Payload:** agregar `stockWarehouseId` (requerido).


- **Validación de stock por almacén** previo a insertar el ítem en la orden.


- **Reserva de stock por almacén** (incrementar `nstock_reserva_pedidos` en la fila de `stocks` correspondiente).


- **Errores detallados** cuando no alcance el stock del almacén seleccionado.


- **Refactor de **`updateReserveStock` para trabajar por almacén (no global).


- **Mantener compatibilidad funcional** con el resto del flujo de órdenes.



## Criterios de aceptación (QA)

- Si el stock **alcanza**, la API devuelve el objeto del item como sucede ahora:

```
{
  "msg": "Item agregado correctamente",
  "success": true,
  "item": {
    "id": 119566,
    "title": "...",
    "sku": "...",
    ...
    "stockWarehouseId": 2,
    "stockWarehouseDescription": "SAFcom",
    "availableStock": 58
  }
}

```

➜ El ítem se agrega correctamente y se descuenta del depósito indicado.


- Si el stock **no alcanza**, devuelve:

```
{
  "errors": {
    "status": 500,
    "title": "No hay stock suficiente para el articulo, quedan 59 unidades ",
    "file": "...",
    "line": 316
  }
}

```

➜ No se reserva ni se agrega el ítem.


- `stockWarehouseId` es obligatorio y debe corresponder a un depósito válido.


- Se puede agregar el mismo producto desde **diferentes depósitos** (en llamadas separadas) para la misma orden.


- Si se pide más cantidad de la disponible en el depósito, responde con el error 500 anterior.


- Las operaciones son **atómicas**: si algo falla, no se actualiza la reserva.


- Si se procesa correctamente, y se toma el stock, se altera `[NewBytes_DBF].[dbo].[stocks].nstock_reserva_pedidos` para la fila del deposito especifico
