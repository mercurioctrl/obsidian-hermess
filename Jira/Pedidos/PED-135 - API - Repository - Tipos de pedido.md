---
jira_key: "PED-135"
aliases: ["PED-135"]
summary: "API - Repository - Tipos de pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-10 09:13"
updated: "2023-10-10 10:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-135"
---

# PED-135: API - Repository - Tipos de pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-10 09:13 |
| Actualizado | 2023-10-10 10:43 |
| Etiquetas | ninguna |
| Jira | [PED-135](https://bluinc.atlassian.net/browse/PED-135) |

## Relaciones

- **Padre:** [[PED-7]] Repositorios y base del proyecto
- **blocks:** [[PED-136]] APP - Feat - Filtros de ordenes -> Filtrar por tipo de orden

## Descripcion

Necesitamos hacer 2 cosas

1 - Obtener los tipos de ordenes disponibles para poder filtrarlas (evitar nulos y vacios)

2 - Agregar una columna nueva, de ids numéricos llamada `orderTypeId` para poder filtrar de manera mas ágil. En principio la agregaremos y luego con una tarea completaremos las “orders” que no lo tienen, ademas de refactorizar los sistemas que usen esto.

```
GET {API_URL}/v1/orderTypes
```

```
SELECT cobserv, orderTypeId
FROM [NewBytes_DBF].[dbo].[pedclit]
GROUP BY cobserv
```

Devuelve

```
[
  {
    "description": "DESCARGADO",
    "id": 1
  },
  {
    "description": "INTERNO",
    "id": 2
  },
  {
    "description": "PEDIDO APP ANDROID",
    "id": 3
  },
  {
    "description": "PEDIDO DE INTERNET  ",
    "id": 4
  },
  {
    "description": "PEDIDO LIBRE OPCION",
    "id": 5
  },
  {
    "description": "PRESUPUESTO",
    "id": 6
  }
]
```
