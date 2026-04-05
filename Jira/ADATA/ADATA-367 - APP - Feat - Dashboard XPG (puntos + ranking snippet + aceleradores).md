---
jira_key: "ADATA-367"
aliases: ["ADATA-367"]
summary: "APP - Feat - Dashboard XPG (puntos + ranking snippet + aceleradores)"
status: "Revisión"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:24"
updated: "2026-02-24 16:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-367"
---

# ADATA-367: APP - Feat - Dashboard XPG (puntos + ranking snippet + aceleradores)

| Campo | Valor |
|-------|-------|
| Estado | Revisión (En curso) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-19 11:24 |
| Actualizado | 2026-02-24 16:41 |
| Etiquetas | ninguna |
| Jira | [ADATA-367](https://bluinc.atlassian.net/browse/ADATA-367) |

## Relaciones

- **Padre:** [[ADATA-356]] XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)

## Descripcion

Dashboard según mockup XPG:

- Puntos totales


- Ranking snippet (anterior/yo/siguiente)


- Aceleradores activos (y accesos a próximos/expirados)


- Banner/área de contenido



Consume repos:

- datos usuario (/me)


- aceleradores (/accelerators?status=)


- ranking snippet (/ranking/snippet)



### Acceptance Criteria

| AC | Criterio |
| --- | --- |
| AC1 | Renderiza puntos totales y estado sin datos. |
| AC2 | Renderiza ranking snippet correctamente (máx 3 filas). |
| AC3 | Renderiza aceleradores con vigencia y multiplicador. |
