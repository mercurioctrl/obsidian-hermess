---
jira_key: "PED-355"
aliases: ["PED-355"]
summary: "API - Refactor - En el detalle de ordenes, mostrar dispoibilidad de los productos si recibe el parametro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-18 16:00"
updated: "2023-12-18 16:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-355"
---

# PED-355: API - Refactor - En el detalle de ordenes, mostrar dispoibilidad de los productos si recibe el parametro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-18 16:00 |
| Actualizado | 2023-12-18 16:39 |
| Etiquetas | ninguna |
| Jira | [PED-355](https://bluinc.atlassian.net/browse/PED-355) |

## Relaciones

- **Padre:** [[PED-354]] Descarga de pedidos

## Descripcion

```
GET {API_URL}/v1/orders/{}
```

Agregaremos el parámetro `showAvailable` para poder conocer el stock disponible a la hora de modificarlo
