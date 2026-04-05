---
jira_key: "ADATA-368"
aliases: ["ADATA-368"]
summary: "APP - Feat - Carga de compras manual (XPG)"
status: "Revisión"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:25"
updated: "2026-02-25 18:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-368"
---

# ADATA-368: APP - Feat - Carga de compras manual (XPG)

| Campo | Valor |
|-------|-------|
| Estado | Revisión (En curso) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-19 11:25 |
| Actualizado | 2026-02-25 18:14 |
| Etiquetas | ninguna |
| Jira | [ADATA-368](https://bluinc.atlassian.net/browse/ADATA-368) |

## Relaciones

- **Padre:** [[ADATA-356 - XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)|ADATA-356]] XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)

## Descripcion

Pantalla para cargar compras manualmente:

- seleccionar cliente (si user tiene más de 1)


- sku (opcional)


- nombreProducto


- cantidad


- precio (opcional)


- montoTotal


- facturaCompra (opcional)


- fechaCompra (opcional)



### Acceptance Criteria

| AC | Criterio |
| --- | --- |
| AC1 | Carga manual crea compra y actualiza puntos/ranking al volver. |
| AC2 | Validaciones frontend evitan quantity/montoTotal inválidos. |
| AC3 | Maneja errores por permisos (cliente no pertenece). |
