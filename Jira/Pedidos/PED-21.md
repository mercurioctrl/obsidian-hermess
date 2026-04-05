---
jira_key: "PED-21"
summary: "API - Repository - Provincias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-08 08:51"
updated: "2023-08-08 15:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-21"
---

# PED-21: API - Repository - Provincias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-08 08:51 |
| Actualizado | 2023-08-08 15:37 |
| Etiquetas | ninguna |
| Jira | [PED-21](https://bluinc.atlassian.net/browse/PED-21) |

## Descripción

Source:

```
GET {{API_URL}}/v1/provinces
```

Return:

```json
  {
    "id": 4,
    "description": "CHUBUT                        ",
    "countryId": 7,
    "fiscalId": 17
  },
  {
    "id": 5,
    "description": "ENTRE RIOS                    ",
    "countryId": 7,
    "fiscalId": 5
  },
  {
    "id": 6,
    "description": "CORDOBA                       ",
    "countryId": 7,
    "fiscalId": 3
  },
```

Data:

```sql
SELECT [Id_Provincia] 
,[Descripcion] 
,[Id_Pais] 
,[ID_AFIP]  
FROM [NewBytes_DBF].[dbo].[FP_Provincias]
```
