---
jira_key: "PED-1135"
aliases: ["PED-1135"]
summary: "API - Refactor MVP - EN addItem cuando tiene el permiso useStockIncoming agregar la cantidad que ingresa al stock disponible para permitir reservar el stock también. (Recordar contabilizar como una reserva en la tabla de stocks)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-10-03 14:26"
updated: "2025-10-27 10:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1135"
---

# PED-1135: API - Refactor MVP - EN addItem cuando tiene el permiso useStockIncoming agregar la cantidad que ingresa al stock disponible para permitir reservar el stock también. (Recordar contabilizar como una reserva en la tabla de stocks)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-03 14:26 |
| Actualizado | 2025-10-27 10:47 |
| Etiquetas | ninguna |
| Jira | [PED-1135](https://bluinc.atlassian.net/browse/PED-1135) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra

## Descripcion

Existe un caso de uso (pre - venta) donde un vendedor quiere usar stock de mercadería que aun no esta en la empresa ni en ningún deposito, para esto introducimos el permiso o feature flag `useStockIncoming` en el usuario.

Lo que haremos es que al hacer nuestro control al momento de meter un item en la orden de compra (por ejemplo nstock - nstoc_reservas_pedidos >= cantidad) agregaremos sumando los que están ingresando solo si tengo el permiso `useStockIncoming` sumaremos `stockIncoming` como un stock mas, lo que me permitira tomarme “a cuenta” cierta cantidad para meterla en una orden

```
PATCH /v1/orders/addItem
```

```
{
"order":"10425817",
"branch":"0002",
"itemId":119554,
"amount":1,
"stockWarehouseId": 3
}
```

Importante `stockIncoming` cuenta como reserva para todos, mas alla de que solo pueden usarlo quiene tengan la feature flag `useStockIncoming` por esto, es correcto que afecte el update del metodo `updateReserveStock` aunque sea contra intuitivo
