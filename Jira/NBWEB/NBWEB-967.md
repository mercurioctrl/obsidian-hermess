---
jira_key: "NBWEB-967"
summary: "APP - Refactor - Agregar parametro \"solo disponibles\" al repositorio \"ultimos ingresos\" cuando lo mostramos en en la home par evitar mostrar productos sin stock"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-28 08:16"
updated: "2025-05-07 11:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-967"
---

# NBWEB-967: APP - Refactor - Agregar parametro "solo disponibles" al repositorio "ultimos ingresos" cuando lo mostramos en en la home par evitar mostrar productos sin stock

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-28 08:16 |
| Actualizado | 2025-05-07 11:05 |
| Etiquetas | ninguna |
| Jira | [NBWEB-967](https://bluinc.atlassian.net/browse/NBWEB-967) |

## Descripción

APP - Refactor - Agregar parametro "solo disponibles" al repositorio "ultimos ingresos" cuando lo mostramos en en la home par evitar mostrar productos sin stock

Cambiaremos

```
GET {API_URL}/v1/?ultimos_ingresos=1
```

por

```
GET {API_URL}/v1/?ultimos_ingresos=1&available_stock=1
```
