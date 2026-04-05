---
jira_key: "PED-36"
aliases: ["PED-36"]
summary: "API - Feat - Filtros de ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-20 21:16"
updated: "2024-07-17 18:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-36"
---

# PED-36: API - Feat - Filtros de ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-20 21:16 |
| Actualizado | 2024-07-17 18:12 |
| Etiquetas | ninguna |
| Jira | [PED-36](https://bluinc.atlassian.net/browse/PED-36) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **relates to:** [[PED-773 - API - Refactor - Filtros de ordenes - Filtrar por medio de pago - Pago diferido|PED-773]] API - Refactor - Filtros de ordenes -> Filtrar por medio de pago - Pago diferido

## Descripcion

Refactorizaremos el recurso 

```
GET {API_URL}/v1/orders?search={order|branch|clientId|clientDescription|cnumalb|voucher}&paymentMethod={paymentMethodId}&deliveyMethod={deliveyMethodId}
```

de tal forma de poder recibir los siguientes filtros

- Por numero de orden (order)


- Por sucursal (branch)


- Por numero de cliente  (clientId)


- Por nombre de cliente {clientDescription}


- Por numero de pedido (cnumalb)


- Por factura (vocher)


- Por metodo de pago (paymentMethod) (Viene de un repositorio)


- Por metodo de envío/retiro (deliveyMethodId) (Viene de un repositorio)
