---
jira_key: "COB-55"
aliases: ["COB-55"]
summary: "API - Feat - Listar estados cobrarbles"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-11 13:16"
updated: "2022-10-13 09:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-55"
---

# COB-55: API - Feat - Listar estados cobrarbles

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-11 13:16 |
| Actualizado | 2022-10-13 09:01 |
| Etiquetas | ninguna |
| Jira | [COB-55](https://bluinc.atlassian.net/browse/COB-55) |

## Relaciones

- **Padre:** [[COB-21]] Base del proyecto y formularios
- **blocks:** [[COB-41]] APP - Feat -  Listar cobrables

## Descripcion

```
GET {{API_URL}}/v1/tradableStatus
```

```
[
  {
    "id": 1,
    "description": "Pendientes a Autorizar"
  },
  {
    "id": 2,
    "description": "Autorizados. Pendiente a despachar"
  },
  {
    "id": 4,
    "description": "Finalizado"
  },
  {
    "id": 3,
    "description": "Despachado, Pendiente a Cobrar"
  },
  {
    "id": 9,
    "description": "A Facturar Sin Autorizar"
  },
  {
    "id": 11,
    "description": "Serializado"
  },
  {
    "id": 10,
    "description": "Parcialmente Serializado"
  },
  {
    "id": 12,
    "description": "Facturado Por No Autorizado"
  }
]
```

```
SELECT [ID_STATUS]
      ,[DESCRIPCION]
  FROM [NEW_BYTES].[dbo].[MS_STATUS_REMITO]
```
