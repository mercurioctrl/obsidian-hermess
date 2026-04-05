---
jira_key: "PED-940"
aliases: ["PED-940"]
summary: "API - Refactor - Filtros de búsqueda para cuentas corrientes (fecha y observaciones)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-01-30 16:29"
updated: "2025-02-03 17:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-940"
---

# PED-940: API - Refactor - Filtros de búsqueda para cuentas corrientes (fecha y observaciones)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-30 16:29 |
| Actualizado | 2025-02-03 17:57 |
| Etiquetas | ninguna |
| Jira | [PED-940](https://bluinc.atlassian.net/browse/PED-940) |

## Relaciones

- **Padre:** [[PED-54]] Cuenta corriente de clientes
- **has action item:** [[PED-941]] APP - Refactor - Filtros de búsqueda para cuentas corrientes (fecha y observaciones)

## Descripcion

Segun lo conversado y como ya hemos hablado en otro momento, se busca agilizar la navegacion por las cuentas corrientesd e clientes para facilitar el trabajo de la operación diaria

Para esto agregaremos los filtros de busqueda y fechas

```
GET {API_URL}/v1/currentAccount/{clientId}?search={terminosDeObservaciones}&between=01-05-2024_30-01-2025
```
