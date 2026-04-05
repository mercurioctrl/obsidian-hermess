---
jira_key: "PED-1028"
aliases: ["PED-1028"]
summary: "API - Feat - Repositorio de tipos de ticket"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-27 08:41"
updated: "2025-07-08 10:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1028"
---

# PED-1028: API - Feat - Repositorio de tipos de ticket

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-27 08:41 |
| Actualizado | 2025-07-08 10:45 |
| Etiquetas | ninguna |
| Jira | [PED-1028](https://bluinc.atlassian.net/browse/PED-1028) |

## Relaciones

- **Padre:** [[PED-960]] Tickets de pedido
- **has action item:** [[SNB-3151]] FILTRO DE TICKET
- **has action item:** [[PED-1030]] APP - Feat - Agregar selectores y cambio de motivo de ticket para un pedido ya realizado

## Descripcion

Agregaremos un repositorio de tipos de ticket igual que realizamos en libre opcion para filtrado interno de pedidos

```
GET {API_URL}/v4/ticket/types
```

```
[
    {
        "id": 1,
        "description": "Quiero Cancelar la compra"
    },
    {
        "id": 2,
        "description": "Tengo un problema"
    },
    {
        "id": 3,
        "description": "Quiero cancelar la venta"
    },
    {
        "id": 4,
        "description": "Solicito asistecia de Libre Opci\u00f3n en el chat de la compra"
    },
    {
        "id": 5,
        "description": "Solicito asistecia de Libre Opci\u00f3n en el chat de la venta"
    },
    {
        "id": 6,
        "description": "Quiero devolver el producto"
    },
    {
        "id": 7,
        "description": "Importaci\u00f3n de productos"
    }
]
```
