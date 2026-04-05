---
jira_key: "NBWEB-156"
aliases: ["NBWEB-156"]
summary: "APP - CMS - Categorias"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-04-29 17:12"
updated: "2022-07-21 10:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-156"
---

# NBWEB-156: APP - CMS - Categorias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-29 17:12 |
| Actualizado | 2022-07-21 10:43 |
| Etiquetas | ninguna |
| Jira | [NBWEB-156](https://bluinc.atlassian.net/browse/NBWEB-156) |

## Relaciones

- **Padre:** [[NBWEB-54]] Content Manager
- **Subtarea:** [[NBWEB-563]] Visualización de stock activo por categoría
- **Subtarea:** [[NBWEB-565]] Validación al editar una categoría
- **relates to:** [[NBWEB-158]] API - CMS - Categories

## Descripcion

Se deben listar las categorias para poder mostrarlas en el CMS y así poder editarlas posteriormente.

- Podrá editarse el nombre


- Si se muestra o no en el sitio. 


- los campos initialB y initialC, que son de tipo numero entero.



Todos los recursos de CMA estan detras de un token del CMS, no mezclar con el de usuarios del sitio.

```
GET {{API_URL}}/v1/cms/Categories
```

Retorna

```
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
