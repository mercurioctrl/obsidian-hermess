---
jira_key: "PED-1027"
aliases: ["PED-1027"]
summary: "API - Feat - Repositorio de motivo de ticket"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-27 08:41"
updated: "2025-07-08 10:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1027"
---

# PED-1027: API - Feat - Repositorio de motivo de ticket

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-27 08:41 |
| Actualizado | 2025-07-08 10:44 |
| Etiquetas | ninguna |
| Jira | [PED-1027](https://bluinc.atlassian.net/browse/PED-1027) |

## Relaciones

- **Padre:** [[PED-960 - Tickets de pedido|PED-960]] Tickets de pedido
- **has action item:** [[SNB-3151 - FILTRO DE TICKET|SNB-3151]] FILTRO DE TICKET
- **has action item:** [[PED-1030 - APP - Feat - Agregar selectores y cambio de motivo de ticket para un pedido ya|PED-1030]] APP - Feat - Agregar selectores y cambio de motivo de ticket para un pedido ya realizado

## Descripcion

Agregaremos un repositorio de motivos de ticket, filtrado por tipo de ticket al igual que lo hicimos en libre opcion para filtrado interno

```
GET {API_URL}/v1/ticket/issues/2
```

```
[
    {
        "id": 6,
        "description": "Con el pago"
    },
    {
        "id": 7,
        "description": "Con el env\u00edo"
    },
    {
        "id": 8,
        "description": "Con el vendedor"
    },
    {
        "id": 9,
        "description": "Con el producto"
    },
    {
        "id": 20,
        "description": "Con la factura"
    }
]
```
