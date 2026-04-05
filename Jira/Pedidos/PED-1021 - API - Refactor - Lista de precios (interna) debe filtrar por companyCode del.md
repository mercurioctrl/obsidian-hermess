---
jira_key: "PED-1021"
aliases: ["PED-1021"]
summary: "API - Refactor - Lista de precios (interna) debe filtrar por companyCode del cliente, si no esta el cliente del usuario que la pida"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-13 14:23"
updated: "2025-07-03 10:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1021"
---

# PED-1021: API - Refactor - Lista de precios (interna) debe filtrar por companyCode del cliente, si no esta el cliente del usuario que la pida

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-13 14:23 |
| Actualizado | 2025-07-03 10:46 |
| Etiquetas | ninguna |
| Jira | [PED-1021](https://bluinc.atlassian.net/browse/PED-1021) |

## Relaciones

- **Padre:** [[PED-191]] Descargar Listado de precios
- **has action item:** [[SNB-3166]] EXCEL LISTA DE PRECIOS

## Descripcion

Siguiendo lo mencionado en [link](https://bluinc.atlassian.net/jira/servicedesk/projects/SNB/queues/custom/63/[[SNB-3166]]) 

Modificaremos el recurso 

```
GET {API_URL}/v1/download/priceList?clientId={clientId}&type=xlsx|txt
```

Lo que haremos es aplicar el filtro según el cliente en principio

Cuando `[NewBytes_DBF].[dbo].[clientes].companyCode` no es NULL, solo mostraremos los productos que coinciden en `[NewBytes_DBF].[dbo].[articulo].companyCode` para la misma empresa.

En el caso de que `[NewBytes_DBF].[dbo].[clientes].companyCode` si sea NULL, miraremos el `companyCode`del usuario esta presente y lo haremos matchear con `[NewBytes_DBF].[dbo].[clientes].companyCode`.

Si el usuario tambien tiene `companyCode` NULL, entonces mostraremos todo.
