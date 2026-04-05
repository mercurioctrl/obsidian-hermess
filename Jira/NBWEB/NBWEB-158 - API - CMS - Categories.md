---
jira_key: "NBWEB-158"
aliases: ["NBWEB-158"]
summary: "API - CMS - Categories"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-29 17:14"
updated: "2022-08-05 10:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-158"
---

# NBWEB-158: API - CMS - Categories

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-29 17:14 |
| Actualizado | 2022-08-05 10:48 |
| Etiquetas | ninguna |
| Jira | [NBWEB-158](https://bluinc.atlassian.net/browse/NBWEB-158) |

## Relaciones

- **Padre:** [[NBWEB-54 - Content Manager|NBWEB-54]] Content Manager
- **Subtarea:** [[NBWEB-562 - Al ocultar una categoría ocultar productos vinculados|NBWEB-562]] Al ocultar una categoría ocultar productos vinculados
- **Subtarea:** [[NBWEB-564 - Añadir stock activo por categoría|NBWEB-564]] Añadir stock activo por categoría
- **relates to:** [[NBWEB-156 - APP - CMS - Categorias|NBWEB-156]] APP - CMS - Categorias
- **blocks:** [[NBWEB-440 - Problema al guardar los limites en las categorias del CMS|NBWEB-440]] Problema al guardar los limites en las categorias del CMS

## Descripcion

Se deben listar las categorias para poder mostrarlas en el cms y asi poder editarlas posteriormente.

Todos los recursos de CMA estan detras de un token del CMS, no mezclar con el de usuarios del sitio.

```
GET {{API_URL}}/v1/cms/Categories
```

Retorna 



```json
[
    {
        "description": "Monitores",
        "id": "161",
        "show": 1,
        "initialB": 3,
        "initialc": 4
    },
    {
        "description": "Procesadores",
        "id": "42",
        "show": 1,
        "initialB": 3,
        "initialc": 4
    }
    ]
```
