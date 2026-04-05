---
jira_key: "NBWEB-796"
summary: "EXTENSION - Refactor - Dejar expuesto el endpoint que vamos a golpear para actualizar los productos de nuestro lado al cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-07-31 12:11"
updated: "2024-08-15 16:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-796"
---

# NBWEB-796: EXTENSION - Refactor - Dejar expuesto el endpoint que vamos a golpear para actualizar los productos de nuestro lado al cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-31 12:11 |
| Actualizado | 2024-08-15 16:05 |
| Etiquetas | ninguna |
| Jira | [NBWEB-796](https://bluinc.atlassian.net/browse/NBWEB-796) |

## Descripción

Dejar expuesto el endpoint que vamos a golpear para actualizar los productos de nuestro lado al cliente.

Se debe dejar una regla interna que no actualice si ya lo hizo en los ultimos 5 minutos (Esto es para que no existan abusos sobre el recurso) basándonos en la fecha de actualización guardada del lado del cliente.
