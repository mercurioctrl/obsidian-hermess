---
jira_key: "PED-22"
aliases: ["PED-22"]
summary: "API - Repository - Localidades"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-08 08:52"
updated: "2023-08-08 15:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-22"
---

# PED-22: API - Repository - Localidades

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-08 08:52 |
| Actualizado | 2023-08-08 15:42 |
| Etiquetas | ninguna |
| Jira | [PED-22](https://bluinc.atlassian.net/browse/PED-22) |

## Relaciones

- **Padre:** [[PED-7 - Repositorios y base del proyecto|PED-7]] Repositorios y base del proyecto

## Descripcion

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
