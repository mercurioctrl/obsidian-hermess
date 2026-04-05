---
jira_key: "NBWEB-195"
summary: "API - Listar Provincias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-20 12:55"
updated: "2022-06-26 21:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-195"
---

# NBWEB-195: API - Listar Provincias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-20 12:55 |
| Actualizado | 2022-06-26 21:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-195](https://bluinc.atlassian.net/browse/NBWEB-195) |

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
