---
jira_key: "PED-67"
aliases: ["PED-67"]
summary: "API - Repository - Categorias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-09-12 09:44"
updated: "2023-09-12 13:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-67"
---

# PED-67: API - Repository - Categorias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-12 09:44 |
| Actualizado | 2023-09-12 13:03 |
| Etiquetas | ninguna |
| Jira | [PED-67](https://bluinc.atlassian.net/browse/PED-67) |

## Relaciones

- **Padre:** [[PED-7]] Repositorios y base del proyecto
- **blocks:** [[PED-69]] API - Feat - Listar productos -> Filtros

## Descripcion

Según el recurso utilizado en la API debemos armar 

```
GET {API_URL}/v1/categories
```

```json
[
    {
        "description": "ACCESORIOS",
        "id": "20",
        "initialB": "5",
        "initialC": "20"
    },
    {
        "description": "AURICULARES",
        "id": "28",
        "initialB": "5",
        "initialC": "10"
    },
    {
        "description": "CAMARAS IP",
        "id": "44",
        "initialB": "5",
        "initialC": "10"
    }
  ...
]
```

```sql
SELECT  * FROM [NewBytes_DBF].[dbo].[familias] ORDER BY cnomfam ASC
```
