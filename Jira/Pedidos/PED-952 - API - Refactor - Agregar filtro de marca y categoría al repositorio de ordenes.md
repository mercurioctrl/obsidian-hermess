---
jira_key: "PED-952"
aliases: ["PED-952"]
summary: "API - Refactor - Agregar filtro de marca y categoría al repositorio de ordenes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-21 09:26"
updated: "2025-02-21 21:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-952"
---

# PED-952: API - Refactor - Agregar filtro de marca y categoría al repositorio de ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-21 09:26 |
| Actualizado | 2025-02-21 21:01 |
| Etiquetas | ninguna |
| Jira | [PED-952](https://bluinc.atlassian.net/browse/PED-952) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **has action item:** [[PED-953]] APP - Refactor - Agregar filtro de marca y categoría al repositorio de ordenes

## Descripcion

Agregaremos los filtros de marca y categoría para poder filtrar en el repositorio aquellas ordenes que tienen productos reactivos a la marca y/o categoría filtrada en su contenido.

```
GET {API_URL}/v1/orders?categoryId={categoryId}&brandId={brandId}
```

Como se suele hacer,  se debe cuidar la performance de modo tal que el recurso tarde o lo mismo con los filtros, como minimo que sin los filtros funcione exactamente igual en tiempos
