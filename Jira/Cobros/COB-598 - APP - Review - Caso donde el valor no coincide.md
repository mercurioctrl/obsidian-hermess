---
jira_key: "COB-598"
aliases: ["COB-598"]
summary: "APP - Review - Caso donde el valor no coincide"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-26 17:12"
updated: "2026-01-09 13:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-598"
---

# COB-598: APP - Review - Caso donde el valor no coincide

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-26 17:12 |
| Actualizado | 2026-01-09 13:56 |
| Etiquetas | ninguna |
| Jira | [COB-598](https://bluinc.atlassian.net/browse/COB-598) |

## Relaciones

- **Padre:** [[COB-573 - Clientes|COB-573]] Clientes

## Descripcion

Revisando algunas features encontre en GAMMA algo que me llamo la atencion, en este caso por ejemplo el disponible es igual al limite de credito, y teoricamente este deberia ser el limite de credito menos  el balance o ultimo subtotal

[adjunto]
---

Según lo conversado y el refactor realizado en la historia [link](https://bluinc.atlassian.net/browse/COB-601)  agregaremos un nuevo parámetro llamado `currentBalance` para desambiguar la informacion y que estén parámetros por separado
