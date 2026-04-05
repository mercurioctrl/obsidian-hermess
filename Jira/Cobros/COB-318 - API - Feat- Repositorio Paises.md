---
jira_key: "COB-318"
aliases: ["COB-318"]
summary: "API - Feat- Repositorio Paises"
status: "Tareas por hacer"
type: "Tarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2023-01-30 09:32"
updated: "2023-01-30 09:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-318"
---

# COB-318: API - Feat- Repositorio Paises

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-30 09:32 |
| Actualizado | 2023-01-30 09:37 |
| Etiquetas | ninguna |
| Jira | [COB-318](https://bluinc.atlassian.net/browse/COB-318) |

## Relaciones

- **Padre:** [[COB-21 - Base del proyecto y formularios|COB-21]] Base del proyecto y formularios
- **blocks:** [[COB-316 - APP - Feat - Agregar proveedor|COB-316]] APP - Feat - Agregar proveedor

## Descripcion

Source

```
GET {{API_URL}}/v1/countries
```



Request

```json
[
  {
    "id": 2,
    "prefix": "ESPA      ",
    "description": "España                        ",
    "flag": "28        ",
    "default": null
  },
  {
    "id": 3,
    "prefix": "GBR       ",
    "description": "Gran Breta±a456               ",
    "flag": "34        ",
    "default": null
  },
  {
    "id": 4,
    "prefix": "EURO      ",
    "description": "Resto de Europa               ",
    "flag": "30        ",
    "default": null
  }
  ...
  ]
```

Data

```sql
SELECT
Id_Ciudad 
,Descripcion 
,CCODPOBL 
,Id_Provincia 
FROM [NewBytes_DBF].[dbo].[FP_Paises]
```
