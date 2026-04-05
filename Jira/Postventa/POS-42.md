---
jira_key: "POS-42"
summary: "API - Feat - Listar estados de testeo"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-29 08:42"
updated: "2022-10-12 08:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-42"
---

# POS-42: API - Feat - Listar estados de testeo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-29 08:42 |
| Actualizado | 2022-10-12 08:50 |
| Etiquetas | ninguna |
| Jira | [POS-42](https://bluinc.atlassian.net/browse/POS-42) |

## Descripción

Son los estados posibles que pueden asignarse al momento de testear

```
GET {API_URL}/v1/testSatuts
```

```
[
  {
    "id": 1,
    "description": "REVISADO",
    "defaultOption": false
  },
  {
    "id": 2,
    "description": "SIN REVISAR",
    "defaultOption": false
  },
  {
    "id": 3,
    "description": "PARCIALMENTE REVISADO",
    "defaultOption": false
  },
  {
    "id": 4,
    "description": "TODOS",
    "defaultOption": true
  }
]
```



```
SELECT TOP (1000) [Id_Estado]
      ,[Descripcion]
      ,[Predetermminado]
  FROM [NEW_BYTES].[dbo].[ST_RMAESTADOSREVISADO]
```
