---
jira_key: "PED-46"
aliases: ["PED-46"]
summary: "APP - Feat - Filtros de ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-24 08:44"
updated: "2023-10-04 14:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-46"
---

# PED-46: APP - Feat - Filtros de ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-24 08:44 |
| Actualizado | 2023-10-04 14:32 |
| Etiquetas | ninguna |
| Jira | [PED-46](https://bluinc.atlassian.net/browse/PED-46) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra

## Descripcion

Haremos algunos filtros para poder operar con el listado de ordenes de compra teniendo en cuenta que solo operaremos aquellos del ultimo año, a menos que se especifique al menos una fecha.

Para esto nos basaremos en 

[link](https://lioteam.atlassian.net/browse/PED-36) 

¿como se utiliza?

```
GET {API_URL}/v1/orders?search={order|branch|clientId|clientDescription|cnumalb|voucher}&paymentMethod={paymentMethodId}&deliveyMethod={deliveyMethodId}
```

de tal forma de poder recibir los siguientes filtros que proviene de la caja de búsqueda.

También necesitaremos agregar dos selectores para los repositorios [link](https://lioteam.atlassian.net/browse/PED-38)  y [link](https://lioteam.atlassian.net/browse/PED-37)

Filtros:

- Por numero de orden (order)


- Por sucursal (branch)


- Por numero de cliente  (clientId)


- Por nombre de cliente {clientDescription}


- Por numero de pedido (cnumalb)


- Por factura (vocher)


- Por metodo de pago (paymentMethod) (Viene de un repositorio)


- Por metodo de envío/retiro (deliveyMethodId) (Viene de un repositorio)


- Por Agente de ventas
