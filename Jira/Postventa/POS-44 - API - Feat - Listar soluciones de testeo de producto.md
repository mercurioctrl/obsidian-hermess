---
jira_key: "POS-44"
aliases: ["POS-44"]
summary: "API - Feat - Listar soluciones de testeo de producto"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-29 09:06"
updated: "2022-10-12 08:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-44"
---

# POS-44: API - Feat - Listar soluciones de testeo de producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-29 09:06 |
| Actualizado | 2022-10-12 08:50 |
| Etiquetas | ninguna |
| Jira | [POS-44](https://bluinc.atlassian.net/browse/POS-44) |

## Relaciones

- **Padre:** [[POS-12]] Bases del proyecto y formularios
- **blocks:** [[POS-35]] APP - Feat - Listar ingresos de postventa

## Descripcion

```
GET {API_URL}/v1/testProductStatus
```

```
[
  {
    "id": 1,
    "description": "Espera",
    "defaultOption": false
  },
  {
    "id": 2,
    "description": "Cambio",
    "defaultOption": false
  },
  {
    "id": 3,
    "description": "Acreditar",
    "defaultOption": false
  },
  {
    "id": 4,
    "description": "No Fallo",
    "defaultOption": false
  },
  {
    "id": 5,
    "description": "Fuera de Garantía",
    "defaultOption": false
  },
  {
    "id": 6,
    "description": "Reparado",
    "defaultOption": false
  },
  {
    "id": 0,
    "description": "A Revisar",
    "defaultOption": false
  },
  {
    "id": 7,
    "description": "Entregado",
    "defaultOption": false
  },
  {
    "id": 99,
    "description": "TODOS",
    "defaultOption": true
  }
]
```

```
SELECT TOP (1000) [ID_RMAPRODUCTOS] as id
      ,[DESCRIPCION] as description
      ,[PREDETERMINADO] as defaultOption
  FROM [NEW_BYTES].[dbo].[ST_RMAESTADOS_PRODUCTOS]
```
