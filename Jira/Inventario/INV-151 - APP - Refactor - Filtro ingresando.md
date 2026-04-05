---
jira_key: "INV-151"
aliases: ["INV-151"]
summary: "APP - Refactor - Filtro \"ingresando\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-10-09 08:51"
updated: "2024-10-10 10:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-151"
---

# INV-151: APP - Refactor - Filtro "ingresando"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-09 08:51 |
| Actualizado | 2024-10-10 10:35 |
| Etiquetas | ninguna |
| Jira | [INV-151](https://bluinc.atlassian.net/browse/INV-151) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **action item from:** [[INV-150]] API - Refactor - Filtro "ingresando"

## Descripcion

[adjunto]
Agregaremos un filtro que se al activarlo, solo envía ese filtro y no envía ninguno de los otros como el de empresa, stock, etc

```
GET {api_url}/items?arrivals=1
```
