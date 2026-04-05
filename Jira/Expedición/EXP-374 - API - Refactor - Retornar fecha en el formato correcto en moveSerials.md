---
jira_key: "EXP-374"
aliases: ["EXP-374"]
summary: "API - Refactor - Retornar fecha en el formato correcto en moveSerials"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2023-10-17 11:41"
updated: "2023-10-17 16:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-374"
---

# EXP-374: API - Refactor - Retornar fecha en el formato correcto en moveSerials

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2023-10-17 11:41 |
| Actualizado | 2023-10-17 16:15 |
| Etiquetas | ninguna |
| Jira | [EXP-374](https://bluinc.atlassian.net/browse/EXP-374) |

## Relaciones

- **Padre:** [[EXP-346 - APP - Mover seriales - Incidencias varias|EXP-346]] APP - Mover seriales - Incidencias varias

## Descripcion

Ej:
[http://gamma.api.warehouse.lio.red/v1/moveSerials?itemsPerPage=15&currentPage=1&search=117511000048](http://gamma.api.warehouse.lio.red/v1/moveSerials?itemsPerPage=15&currentPage=1&search=117511000048)

```
{
    "serial": "117511000048",
    "FECHA_INGRESO": "20230331.0", <-- Este es el que hay que corregir
    "providerOrder": null,
    "productId": "117511",
    "productName": "TECLADO GAMER RAZER ORNATA V3 X",
    "previousProviderOrder": "10135"
}
```
