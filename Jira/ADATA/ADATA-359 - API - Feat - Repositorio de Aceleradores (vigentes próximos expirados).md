---
jira_key: "ADATA-359"
aliases: ["ADATA-359"]
summary: "API - Feat - Repositorio de Aceleradores (vigentes / próximos / expirados)"
status: "Listo"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:18"
updated: "2026-02-23 12:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-359"
---

# ADATA-359: API - Feat - Repositorio de Aceleradores (vigentes / próximos / expirados)

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-19 11:18 |
| Actualizado | 2026-02-23 12:40 |
| Etiquetas | ninguna |
| Jira | [ADATA-359](https://bluinc.atlassian.net/browse/ADATA-359) |

## Relaciones

- **Padre:** [[ADATA-356 - XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)|ADATA-356]] XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)

## Descripcion

Implementar repositorio/listado de aceleradores con filtros por estado:

- **vigentes**: hoy entre fechaInicial y fechaFinal


- **próximos**: fechaInicial > hoy


- **expirados**: fechaFinal < hoy



Endpoints sugeridos

- `GET /accelerators?status=active|upcoming|expired`


- (Admin) `POST/PUT/DELETE /admin/accelerators`



### Acceptance Criteria

| AC | Criterio |
| --- | --- |
| AC1 | Endpoint devuelve aceleradores filtrados correctamente por estado. |
| AC2 | Aceleradores incluyen multiplicador y fechas en la respuesta. |
| AC3 | (Admin) CRUD aceleradores disponible y validado. |
