---
jira_key: "PED-938"
aliases: ["PED-938"]
summary: "API - Refactor - Permitir busqueda por nro de seguimiento en ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-01-27 14:52"
updated: "2025-01-28 03:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-938"
---

# PED-938: API - Refactor - Permitir busqueda por nro de seguimiento en ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-01-27 14:52 |
| Actualizado | 2025-01-28 03:35 |
| Etiquetas | ninguna |
| Jira | [PED-938](https://bluinc.atlassian.net/browse/PED-938) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **action item from:** [[SNB-2748]] Búsqueda por Guías de correo

## Descripcion

Se debe poder buscar por numero de seguimiento otorgado por transportista.



GET /v1/orders?currentPage=1&search=360002470181520

parametro de busqueda: **search=360002470181520**
