---
jira_key: "PED-1003"
aliases: ["PED-1003"]
summary: "API - MVP - Feat - Precios de venta anteriores para un cliente y producto predeterminados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-13 09:29"
updated: "2025-06-02 01:25"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/PED-1003"
---

# PED-1003: API - MVP - Feat - Precios de venta anteriores para un cliente y producto predeterminados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-13 09:29 |
| Actualizado | 2025-06-02 01:25 |
| Etiquetas | MVPLaset |
| Jira | [PED-1003](https://bluinc.atlassian.net/browse/PED-1003) |

## Relaciones

- **Padre:** [[PED-497 - Ver orden de compra|PED-497]] Ver orden de compra
- **has action item:** [[PED-1004 - APP - MVP - Feat - Precios de venta anteriores para un cliente y producto|PED-1004]] APP - MVP - Feat - Precios de venta anteriores para un cliente y producto especifico
- **relates to:** [[PED-1010 - API - MVP - Precios de venta anteriores para un cliente y producto|PED-1010]] API - MVP - Precios de venta anteriores para un cliente y producto predeterminados - Sugerencia de mejora en el orden

## Descripcion

Crearemos un repositorio para obtener el historial de precios de un producto (itemId) específico comprado por el cliente de una determinada orden (orderId). Este historial permitirá visualizar en qué fechas y a qué precios (sin IVA y en dólares) se le vendió ese ítem al mismo cliente.

```
/v1/orders/{branch-order}/items/{itemId}/price-history
```

```
[
  {
    "date": "2024-05-01T10:30:00Z",
    "order": "0002",
    "branch": "10405608",
    "price": 45999.99
  },
  {
    "date": "2024-04-20T08:15:00Z",
    "order": "0002",
    "branch": "10405608",
    "price": 49999.00 // es el precio sin iva en dolares
  }
]

```

**Notas técnicas:**

- El historial se obtiene filtrando por el `cliente` de la orden y el `itemId` en pedidos anteriores.


- Los precios deben estar expresados **sin IVA y en dólares**.


- Ordenar por fecha descendente (`ORDER BY date DESC`).



**Criterios de aceptación:**

- El endpoint responde correctamente con una lista de precios anteriores para el cliente de la orden especificada.


- Solo se incluyen órdenes anteriores al `order`-`branch` actual.


- La información de fecha, precio, orden y sucursal es precisa.


- Se validan los parámetros requeridos (`order-branch`, `itemId`).


- En caso de no haber historial, devuelve `200 OK` con una lista vacía.
