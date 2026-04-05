---
jira_key: "COB-551"
aliases: ["COB-551"]
summary: "APP - Refactor - Filtros de búsqueda para cuentas corrientes (fecha y observaciones)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-01-30 17:36"
updated: "2025-02-04 17:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-551"
---

# COB-551: APP - Refactor - Filtros de búsqueda para cuentas corrientes (fecha y observaciones)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-30 17:36 |
| Actualizado | 2025-02-04 17:29 |
| Etiquetas | ninguna |
| Jira | [COB-551](https://bluinc.atlassian.net/browse/COB-551) |

## Relaciones

- **Padre:** [[COB-20 - Cuentas Corrientes|COB-20]] Cuentas Corrientes
- **action item from:** [[COB-550 - API - Refactor - Filtros de búsqueda para cuentas corrientes (fecha y|COB-550]] API - Refactor - Filtros de búsqueda para cuentas corrientes (fecha y observaciones)

## Descripcion

Según lo conversado y como ya hemos hablado en otro momento, se busca agilizar la navegacion por las cuentas corrientesd e clientes para facilitar el trabajo de la operación diaria

Para esto agregaremos los filtros de busqueda y fechas

```
GET {API_URL}/v1/currentAccount/{clientId}?search={terminosDeObservaciones}&between=01-05-2024_30-01-2025
```



[adjunto]
