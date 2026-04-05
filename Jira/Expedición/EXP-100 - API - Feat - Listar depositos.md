---
jira_key: "EXP-100"
aliases: ["EXP-100"]
summary: "API - Feat - Listar depositos"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-12-14 10:11"
updated: "2023-06-28 13:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-100"
---

# EXP-100: API - Feat - Listar depositos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-14 10:11 |
| Actualizado | 2023-06-28 13:21 |
| Etiquetas | ninguna |
| Jira | [EXP-100](https://bluinc.atlassian.net/browse/EXP-100) |

## Relaciones

- **Padre:** [[EXP-1 - Base y Repositorios|EXP-1]] Base y Repositorios

## Descripcion

Los depósitos o `warehouse` son instancia de almacenaje de mercadería dentro del sistema. 

```
GET {API_URL}/v1/warehouse
```

```json
[
  {
    "id": 0,
    "description": "Supervisor ",
    "type": 0
  },
  {
    "warehouseId": 1,
    "description": "Expedicion",
    "type": 1
  },
  {
    "warehouseId": 2,
    "description": "Servicio Técnico",
    "type": 1
  },
  {
    "warehouseId": 3,
    "description": "Dario RMA Prov",
    "type": 1
  },
  {
    "warehouseId": 4,
    "description": "Armado PC",
    "type": 1
  },
  {
    "warehouseId": 5,
    "description": "Uso Interno",
    "type": 2
  },
  {
    "warehouseId": 6,
    "description": "Pérdida",
    "type": 2
  }
  ]
```

```
SELECT TOP (1000) [ID_DEPOSITO] 
      ,[DESCRIPCION_DEP] 
      ,[DEPOSITO_TIPO] 
  FROM [NEW_BYTES].[dbo].[ST_DEPOSITOS_SAF]
```
