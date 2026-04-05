---
jira_key: "EXP-506"
aliases: ["EXP-506"]
summary: "API - Refactor - Des-alertar pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-30 08:08"
updated: "2025-07-31 10:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-506"
---

# EXP-506: API - Refactor - Des-alertar pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-30 08:08 |
| Actualizado | 2025-07-31 10:41 |
| Etiquetas | ninguna |
| Jira | [EXP-506](https://bluinc.atlassian.net/browse/EXP-506) |

## Relaciones

- **Padre:** [[EXP-169]] Feat - Alertar pedidos
- **has action item:** [[SNB-3284]] pedidos alertados

## Descripcion

Haremos un refactor en el recurso de alertar pedidos, para poder desalertarlos.

La idea es que al recibir la peticion, si esta alertado, se desalerte.

Y si esta sin alertar, se alerte, es decir se invierta el estado.

```
PATCH {API_URL}/v1/alertOrder/{pedidoAAlertar}
```
