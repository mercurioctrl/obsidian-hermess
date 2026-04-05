---
jira_key: "POS-43"
summary: "API - Feat - Listar estados de salida"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-29 08:51"
updated: "2022-10-12 08:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-43"
---

# POS-43: API - Feat - Listar estados de salida

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-29 08:51 |
| Actualizado | 2022-10-12 08:50 |
| Etiquetas | ninguna |
| Jira | [POS-43](https://bluinc.atlassian.net/browse/POS-43) |

## Descripción

Este recurso lista los estados posibles de salida de un caso

```
GET {API_URL}/v1/outboundStatus
```

```
[
  {
    "id": 1,
    "description": "SIN ENTREGAR",
    "defaultOption": false
  },
  {
    "id": 2,
    "description": "PARCIALMENTE ENTREGADO",
    "defaultOption": false
  },
  {
    "id": 3,
    "description": "ENTREGADO",
    "defaultOption": false
  },
  {
    "id": 4,
    "description": "TODOS",
    "defaultOption": false
  },
  {
    "id": 5,
    "description": "PENDIENTES",
    "defaultOption": true
  }
]
```





```
SELECT TOP (1000) [IdEstadoEntregado]
      ,[Descripcion]
      ,[Predeterminado]
  FROM [NEW_BYTES].[dbo].[ST_RMAESTADOSENTREGADOS]
```
