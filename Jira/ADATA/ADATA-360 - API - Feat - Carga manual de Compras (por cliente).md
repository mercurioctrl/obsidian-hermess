---
jira_key: "ADATA-360"
aliases: ["ADATA-360"]
summary: "API - Feat - Carga manual de Compras (por cliente)"
status: "Listo"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:18"
updated: "2026-02-23 12:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-360"
---

# ADATA-360: API - Feat - Carga manual de Compras (por cliente)

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
| Jira | [ADATA-360](https://bluinc.atlassian.net/browse/ADATA-360) |

## Relaciones

- **Padre:** [[ADATA-356 - XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)|ADATA-356]] XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)

## Descripcion

Permitir que un usuario cargue compras para uno de sus clientes asociados.
Reglas:

- No se puede cargar compra para un clientId que no pertenezca al user.


- Si viene precio y cantidad, se puede calcular montoTotal; si viene montoTotal directo, precio puede ser null.



Endpoints sugeridos

- `GET /clients` (solo los del usuario)


- `POST /purchases` (manual)



### Acceptance Criteria

| AC | Criterio |
| --- | --- |
| AC1 | Un user solo puede cargar compras para sus clientes. |
| AC2 | Se persiste fechaCarga automáticamente. |
| AC3 | Validaciones de campos requeridos y numéricos. |
