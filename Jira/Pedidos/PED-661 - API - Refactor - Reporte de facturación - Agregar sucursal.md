---
jira_key: "PED-661"
aliases: ["PED-661"]
summary: "API - Refactor - Reporte de facturación -> Agregar sucursal "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-04-09 19:46"
updated: "2024-04-19 00:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-661"
---

# PED-661: API - Refactor - Reporte de facturación -> Agregar sucursal 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-09 19:46 |
| Actualizado | 2024-04-19 00:28 |
| Etiquetas | ninguna |
| Jira | [PED-661](https://bluinc.atlassian.net/browse/PED-661) |

## Relaciones

- **Padre:** [[PED-213 - Reportes de ventas|PED-213]] Reportes de ventas
- **relates to:** [[SNB-1674 - REPORTE DE MEJORAS EN REPORTES DE FACTURACIÓN|SNB-1674]] REPORTE DE MEJORAS EN REPORTES DE FACTURACIÓN

## Descripcion

Realizaremos una refactorización al reporte de facturación para que ahora sea posible visualizar la sucursal del remito. Si la sucursal no viene como parámetro, el reporte contendrá todas las sucursales. Si mal no recuerdo, Catri hizo la sugerencia de que esta columna apareciera junto con la de remito.

```
GET {{API_URL}}/v1/reports/billingreport
```



Esta refactorización surge debido a que se han recibido un par de reportes mencionando que no aparecen pedidos con una u otra sucursal.
