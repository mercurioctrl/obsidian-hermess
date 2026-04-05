---
jira_key: "POS-28"
aliases: ["POS-28"]
summary: "API - Feat - Listar Depositos"
status: "CodeReview"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-21 08:59"
updated: "2023-04-20 14:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-28"
---

# POS-28: API - Feat - Listar Depositos

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-21 08:59 |
| Actualizado | 2023-04-20 14:02 |
| Etiquetas | ninguna |
| Jira | [POS-28](https://bluinc.atlassian.net/browse/POS-28) |

## Relaciones

- **Padre:** [[POS-23]] Pases de mercaderia

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
