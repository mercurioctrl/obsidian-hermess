---
jira_key: "NBWEB-414"
aliases: ["NBWEB-414"]
summary: "DB - Refactor - Se debe agregar un token que cambie periodicamente y se guarde para el usuarios"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2022-07-19 08:18"
updated: "2022-11-25 10:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-414"
---

# NBWEB-414: DB - Refactor - Se debe agregar un token que cambie periodicamente y se guarde para el usuarios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-19 08:18 |
| Actualizado | 2022-11-25 10:23 |
| Etiquetas | ninguna |
| Jira | [NBWEB-414](https://bluinc.atlassian.net/browse/NBWEB-414) |

## Relaciones

- **causes:** [[NBWEB-413]] API - Refactor - Mi cuenta - Mis comprobantes

## Descripcion

Se deben crear y completar las columnas softToken y hardToken.

**softToken**: Es un token temporal, que se regenera cada 24hs y que siempre debe estar disponible para los ususarios.

**hardToken**: Es un token que se genera y cambia, solo a demanda del ususario. Puede o no estar.
