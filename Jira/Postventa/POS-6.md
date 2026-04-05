---
jira_key: "POS-6"
summary: "API - Feat - Obtener tipos de fallo"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-14 09:41"
updated: "2022-10-12 08:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-6"
---

# POS-6: API - Feat - Obtener tipos de fallo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-14 09:41 |
| Actualizado | 2022-10-12 08:50 |
| Etiquetas | ninguna |
| Jira | [POS-6](https://bluinc.atlassian.net/browse/POS-6) |

## Descripción

```
GET {API_URL}/v1/postSaleFailTypes
```

```json
[
  {
    "id": 1,
    "description": "Daño fisico",
    "requiredImg": "1"
  },
  {
    "id": 2,
    "description": "No enciende",
    "requiredImg": "0"
  },
  {
    "id": 3,
    "description": "No da imagen",
    "requiredImg": "0"
  },
  {
    "id": 4,
    "description": "No detecta",
    "requiredImg": "0"
  }
]
```

```
SELECT TOP (1000) [id]
      ,[description]
      ,[requiredImg]
  FROM [NB_WEB].[dbo].[postventaFailTypes]
```
