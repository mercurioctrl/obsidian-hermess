---
jira_key: "ADATA-363"
summary: "API - Feat - Ranking snippet (anterior/yo/siguiente) + Ranking Admin completo"
status: "Listo"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:20"
updated: "2026-02-23 12:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-363"
---

# ADATA-363: API - Feat - Ranking snippet (anterior/yo/siguiente) + Ranking Admin completo

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-19 11:20 |
| Actualizado | 2026-02-23 12:40 |
| Etiquetas | ninguna |
| Jira | [ADATA-363](https://bluinc.atlassian.net/browse/ADATA-363) |

## Descripción

Ranking se calcula sumando puntos finales de todas las compras de todos los clientes del usuario.

- Endpoint **usuario**: devolver solo 3 filas máximo: anterior, yo, siguiente.


- Endpoint **admin**: ranking completo paginado.



Endpoints sugeridos

- `GET /ranking/snippet`


- `GET /admin/ranking?page=&limit=`



### Acceptance Criteria

AC

Criterio

AC1

Ranking suma compras de todos los clientes del user.

AC2

Snippet no expone ranking completo ni parámetros de paginación.

AC3

Admin ranking devuelve listado completo paginado.
