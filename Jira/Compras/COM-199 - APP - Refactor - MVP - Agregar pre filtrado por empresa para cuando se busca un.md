---
jira_key: "COM-199"
aliases: ["COM-199"]
summary: "APP - Refactor - MVP - Agregar pre filtrado por empresa para cuando se busca un producto para ingresar en orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-09-29 13:14"
updated: "2025-10-08 10:48"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-199"
---

# COM-199: APP - Refactor - MVP - Agregar pre filtrado por empresa para cuando se busca un producto para ingresar en orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-29 13:14 |
| Actualizado | 2025-10-08 10:48 |
| Etiquetas | MVPLaset |
| Jira | [COM-199](https://bluinc.atlassian.net/browse/COM-199) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra
- **action item from:** [[COM-197 - API - Refactor - MVP - Agregar pre filtrado por empresa para cuando se busca un|COM-197]] API - Refactor - MVP - Agregar pre filtrado por empresa para cuando se busca un producto para ingresar en orden de compra

## Descripcion

La idea es que al buscar en el seleccionador para agregar productos, ya tengan pre filtrados los productos para la empresa a la que pertenecen, para esto, tomaremos de el objeto user el parámetro companyCode

Para esto agregaremos el filtro al llamar al repositorio

```
GET /v1/items?search=AMD&companyCode={companyCode}
```

[adjunto]
