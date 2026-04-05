---
jira_key: "SNB-2749"
aliases: ["SNB-2749"]
summary: "En gamma, al realizar el SyncUp da un error en un parametro, pero en produ anda perfecto."
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-28 09:48"
updated: "2025-01-28 10:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-2749"
---

# SNB-2749: En gamma, al realizar el SyncUp da un error en un parametro, pero en produ anda perfecto.

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-28 09:48 |
| Actualizado | 2025-01-28 10:14 |
| Etiquetas | ninguna |
| Jira | [SNB-2749](https://bluinc.atlassian.net/browse/SNB-2749) |

## Relaciones

*Sin relaciones*

## Descripcion

Estaría bueno revisarlo para ver que no estemos llevando diferencias entre ambas instancias

```
curl --location --request PATCH 'https://gamma.api4.libreopcion.com/v4/syncUp/items' \
--header 'Content-Type: application/json' \
--data '[
    "price",
    "freeShipping",
    "instantFlash",
    "discount",
    "sellerName",
    "sellerId",
    "description",
    "image",
    "keywords",
    "brandId"
]'
```
