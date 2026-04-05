---
jira_key: "COM-197"
aliases: ["COM-197"]
summary: "API - Refactor - MVP - Agregar pre filtrado por empresa para cuando se busca un producto para ingresar en orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-25 10:20"
updated: "2025-10-01 10:47"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-197"
---

# COM-197: API - Refactor - MVP - Agregar pre filtrado por empresa para cuando se busca un producto para ingresar en orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-25 10:20 |
| Actualizado | 2025-10-01 10:47 |
| Etiquetas | MVPLaset |
| Jira | [COM-197](https://bluinc.atlassian.net/browse/COM-197) |

## Relaciones

- **Padre:** [[COM-77]] Editar orden de compra
- **has action item:** [[COM-199]] APP - Refactor - MVP - Agregar pre filtrado por empresa para cuando se busca un producto para ingresar en orden de compra

## Descripcion

La idea es que al buscar en el seleccionador para agregar productos, ya tengan pre filtrados los productos para la empresa a la que pertenecen

```
GET /v1/items?search=AMD&companyCode={companyCode}
```

El repositorio usara este parámetro para filtrar `[NewBytes_DBF].[dbo].[articulo].companyCode`

Cuando sea `companyCode=NULL`  entonces muestro todos, sin filtrar por este parámetro

[adjunto]
