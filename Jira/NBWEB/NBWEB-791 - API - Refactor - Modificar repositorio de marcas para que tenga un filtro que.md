---
jira_key: "NBWEB-791"
aliases: ["NBWEB-791"]
summary: "API - Refactor - Modificar repositorio de marcas para que tenga un filtro que solo muestre aquellas que tienen items en stock"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-26 11:00"
updated: "2024-07-30 12:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-791"
---

# NBWEB-791: API - Refactor - Modificar repositorio de marcas para que tenga un filtro que solo muestre aquellas que tienen items en stock

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-26 11:00 |
| Actualizado | 2024-07-30 12:48 |
| Etiquetas | ninguna |
| Jira | [NBWEB-791](https://bluinc.atlassian.net/browse/NBWEB-791) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web
- **blocks:** [[NBWEB-782 - APP - Feat - Rediseño de menu de productos|NBWEB-782]] APP - Feat - Rediseño de menu de productos

## Descripcion

```
GET {{API_URL}}/v1/brands?onlyInStock=true
```

Es muy importante que este recurso funcione lo mas rápido posible con el filtro y sin el filtro que funcione como ahora, es decir no agregue procesamiento la existencia del mismo cuando no se usa
