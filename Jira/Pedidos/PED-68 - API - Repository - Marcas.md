---
jira_key: "PED-68"
aliases: ["PED-68"]
summary: "API - Repository - Marcas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-09-12 09:46"
updated: "2023-09-12 13:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-68"
---

# PED-68: API - Repository - Marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-12 09:46 |
| Actualizado | 2023-09-12 13:03 |
| Etiquetas | ninguna |
| Jira | [PED-68](https://bluinc.atlassian.net/browse/PED-68) |

## Relaciones

- **Padre:** [[PED-7]] Repositorios y base del proyecto
- **blocks:** [[PED-69]] API - Feat - Listar productos -> Filtros

## Descripcion

```
GET {API_URL}/v1/brands
```

```
[
    {
        "description": "ACER",
        "id": "42"
    },
    {
        "description": "ADATA",
        "id": "91"
    },
    {
        "description": "ALCATEL",
        "id": "223"
    }
...
]
```

```
SELECT  *   FROM [NB_WEB].[dbo].[marcas] ORDER BY [referencia] ASC
```
