---
jira_key: "PED-178"
aliases: ["PED-178"]
summary: "API - Repository - Estados de pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-27 12:01"
updated: "2023-10-31 17:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-178"
---

# PED-178: API - Repository - Estados de pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-27 12:01 |
| Actualizado | 2023-10-31 17:21 |
| Etiquetas | ninguna |
| Jira | [PED-178](https://bluinc.atlassian.net/browse/PED-178) |

## Relaciones

- **Padre:** [[PED-7 - Repositorios y base del proyecto|PED-7]] Repositorios y base del proyecto
- **blocks:** [[PED-185 - APP - Feat - Filtros de ordenes - Filtrar por estado de pedido|PED-185]] APP - Feat - Filtros de ordenes -> Filtrar por estado de pedido

## Descripcion

```
GET {API_URL}/v1/orderStatus
```

```
[
  {
    "id": 1,
    "description": "Pendientes a Autorizar"
  },
  {
    "id": 2,
    "description": "Autorizados. Pendiente a despachar"
  },
  {
    "id": 4,
    "description": "Armado Finalizado"
  }
]
```

Tabla `[NEW_BYTES].[dbo].[MS_STATUS_REMITO]`
