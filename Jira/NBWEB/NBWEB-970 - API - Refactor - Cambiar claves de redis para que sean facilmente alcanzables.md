---
jira_key: "NBWEB-970"
aliases: ["NBWEB-970"]
summary: "API - Refactor - Cambiar claves de redis para que sean facilmente alcanzables por usuario"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-27 17:21"
updated: "2025-06-12 09:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-970"
---

# NBWEB-970: API - Refactor - Cambiar claves de redis para que sean facilmente alcanzables por usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-27 17:21 |
| Actualizado | 2025-06-12 09:49 |
| Etiquetas | ninguna |
| Jira | [NBWEB-970](https://bluinc.atlassian.net/browse/NBWEB-970) |

## Relaciones

- **Padre:** [[NBWEB-957]] Redis
- **has action item:** [[SNB-2998]] Conector NB - Se muestran artículos de categorías ocultas por el cliente

## Descripcion

Cambiar todas las claves de redis que son afectadas según el usuario para que todas finalicen con “:{idCliente}” de forma tal que sean facilmente alcanzables para hacer un flush en casos como el  de [link](https://bluinc.atlassian.net/browse/NBWEB-971)
