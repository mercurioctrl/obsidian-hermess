---
jira_key: "COB-94"
aliases: ["COB-94"]
summary: "API - Feat - Listar condiciones fiscales"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-06 10:05"
updated: "2022-10-13 09:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-94"
---

# COB-94: API - Feat - Listar condiciones fiscales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-06 10:05 |
| Actualizado | 2022-10-13 09:01 |
| Etiquetas | ninguna |
| Jira | [COB-94](https://bluinc.atlassian.net/browse/COB-94) |

## Relaciones

- **Padre:** [[COB-21 - Base del proyecto y formularios|COB-21]] Base del proyecto y formularios
- **blocks:** [[COB-93 - API - Feat - Filtrar lista clientes|COB-93]] API - Feat - Filtrar lista clientes

## Descripcion

```
GET {API_URL}/v1/fiscalConditions
```

```
[
  {
    "id": 1,
    "description": "Responsable Inscripto"
  },
  {
    "id": 2,
    "description": "Responsable NO Inscripto"
  },
  {
    "id": 3,
    "description": "Consumidor Final"
  },
  {
    "id": 4,
    "description": "Exento / No Gravado"
  },
  {
    "id": 5,
    "description": "Import / Export"
  },
  {
    "id": 6,
    "description": "Responsable Monotributo"
  },
  {
    "id": 7,
    "description": "No Categorizado"
  }
]
```

```
SELECT TOP (1000) [NIVA]
      ,[Descripcion]
      ,[OBS]
      ,[Predeterminado]
  FROM [NewBytes_DBF].[dbo].[FP_CategoriasIVA]
```
