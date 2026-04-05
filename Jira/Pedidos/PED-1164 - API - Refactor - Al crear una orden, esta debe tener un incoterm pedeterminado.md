---
jira_key: "PED-1164"
aliases: ["PED-1164"]
summary: "API - Refactor - Al crear una orden, esta debe tener un incoterm pedeterminado "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-30 12:31"
updated: "2025-12-05 04:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1164"
---

# PED-1164: API - Refactor - Al crear una orden, esta debe tener un incoterm pedeterminado 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-30 12:31 |
| Actualizado | 2025-12-05 04:06 |
| Etiquetas | ninguna |
| Jira | [PED-1164](https://bluinc.atlassian.net/browse/PED-1164) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **action item from:** [[PED-1161 - API - MVP - Repositorio incoterms|PED-1161]] API - MVP - Repositorio incoterms

## Descripcion

Basándonos en un parámetro que agregaremos en `[NewBytes_DBF].[dbo].[FP_Empresas].defaultIncoterms` 

Refactorizaremos el recurso para crear ordenes de venta

```
POST {API_URL}/v1/orders
```

Para que según la `companyCode` con que se va a crear, tambien ponga el valor por default si es que existe en  `[NewBytes_DBF].[dbo].[FP_Empresas].defaultIncoterms` 

`[NewBytes_DBF].[dbo].[FP_Empresas].defaultIncoterms`  sera un valor entero según la tabla `[NewBytes_DBF].[dbo].[FP_Incoterms]`

Si esta en `null`, no lo guarda.
