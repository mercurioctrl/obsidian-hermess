---
jira_key: "PED-32"
summary: "API - Repository - Condiciones fiscales"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-17 16:43"
updated: "2023-08-18 17:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-32"
---

# PED-32: API - Repository - Condiciones fiscales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-17 16:43 |
| Actualizado | 2023-08-18 17:22 |
| Etiquetas | ninguna |
| Jira | [PED-32](https://bluinc.atlassian.net/browse/PED-32) |

## Descripción

```
GET {API_URL}/v1/taxType
```

```
[
  {
    "id": 1,
    "description": "Responsable Inscripto",
    "default": 1,
    "cSerie": "A"
  },
  {
    "id": 2,
    "description": "Responsable NO Inscripto",
    "default": null,
    "cSerie": "B"
  },
  {
    "id": 3,
    "description": "Consumidor Final",
    "default": null,
    "cSerie": "B"
  },
  {
    "id": 4,
    "description": "Exento / No Gravado",
    "default": null,
    "cSerie": "B"
  },
  {
    "id": 5,
    "description": "Import / Export",
    "default": null,
    "cSerie": "E"
  },
  {
    "id": 6,
    "description": "Responsable Monotributo",
    "default": null,
    "cSerie": "B"
  },
  {
    "id": 7,
    "description": "No Categorizado",
    "default": null,
    "cSerie": "B"
  }
]
```

```
SELECT [NIVA] as id
      ,[Descripcion] as 'description'
      ,[Predeterminado] as 'default'
      ,[cSeriePredefinida] as cSerie
  FROM [NewBytes_DBF].[dbo].[FP_CategoriasIVA]
```
