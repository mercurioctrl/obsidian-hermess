---
jira_key: "COB-296"
aliases: ["COB-296"]
summary: "API - Feat - Listar provincias y el total de retenciones"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-01-06 09:56"
updated: "2023-01-06 10:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-296"
---

# COB-296: API - Feat - Listar provincias y el total de retenciones

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-06 09:56 |
| Actualizado | 2023-01-06 10:29 |
| Etiquetas | ninguna |
| Jira | [COB-296](https://bluinc.atlassian.net/browse/COB-296) |

## Relaciones

- **Padre:** [[COB-294 - Feat - Listar provincias (Mas subtotales de retenciones)|COB-294]] Feat - Listar provincias (Mas subtotales de retenciones)
- **is blocked by:** [[COB-290 - API - Refactor - Cobrar con retencion|COB-290]] API - Refactor - Cobrar con retencion
- **blocks:** [[COB-297 - APP - Feat - Listar provincias y el total de retenciones|COB-297]] APP - Feat - Listar provincias y el total de retenciones

## Descripcion

Basándonos en el listado de provincias y en la tabla que contiene las retenciones aplicadas, se debe confeccionar un listado para poder mostrar el acceso al detalle de cada uno.

El mismo estará en una pestaña nueva y mostrara las siguientes columnas

- id provincia


- nombre provincia


- retenciones acumuladas (el subtotal)



Debe estar ordenado de mayor a menor subtotal y tendra un filtro para ver solo *con saldo de retenciones /sin saldo de retenciones*

```
GET {API_URL}/v1/retentionIibb
```

ver con  el tema de la tablita que agrego con las retenciones en si
