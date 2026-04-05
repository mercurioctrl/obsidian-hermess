---
jira_key: "NBWEB-196"
summary: "API - Listar localidades"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-20 12:56"
updated: "2023-01-30 09:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-196"
---

# NBWEB-196: API - Listar localidades

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-20 12:56 |
| Actualizado | 2023-01-30 09:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-196](https://bluinc.atlassian.net/browse/NBWEB-196) |

## Descripción

Source

```
GET {{API_URL}}/v1/places
```



Request

```json
[  {
    "id": 8,
    "description": "ABBOTT                        ",
    "alphaCode": "0005",
    "provinceId": 2
  },
  {
    "id": 9,
    "description": "ABBURRA                       ",
    "alphaCode": "0006",
    "provinceId": 6
  },
  {
    "id": 10,
    "description": "ABDON CASTRO TOLAY            ",
    "alphaCode": "0007",
    "provinceId": 15
  }]
```

Data

```sql
SELECT
Id_Ciudad 
,Descripcion 
,CCODPOBL 
,Id_Provincia 
FROM [NewBytes_DBF].[dbo].[FP_Ciudades]
```
