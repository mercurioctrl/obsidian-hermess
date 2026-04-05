---
jira_key: "NBWEB-644"
summary: "API - Feat - Mis Categorias -> Leer enlaces entre categorias del cliente y categorias de la api"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-13 21:56"
updated: "2024-03-18 13:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-644"
---

# NBWEB-644: API - Feat - Mis Categorias -> Leer enlaces entre categorias del cliente y categorias de la api

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-13 21:56 |
| Actualizado | 2024-03-18 13:39 |
| Etiquetas | ninguna |
| Jira | [NBWEB-644](https://bluinc.atlassian.net/browse/NBWEB-644) |

## Descripción

```
GET {API_URL}/v1/miCuenta/misCategorias
```

```
[{
categoryId: 5,
description: 'Mother Asus',
userId: 34343,
categoryUserId: 45455,
descriptionUser: 'Mother varias marcas',
utility: 2.5
},
{
categoryId: 5,
description: 'Mother Asus',
userId: 34343,
categoryUserId: 45455,
descriptionUser: 'Mother varias marcas',
utility: 2.5
},
{
categoryId: 5,
description: 'Mother Asus',
userId: 34343,
categoryUserId: 45455,
descriptionUser: 'Mother varias marcas',
utility: 2.5
}
]
```
