---
jira_key: "POS-79"
aliases: ["POS-79"]
summary: "API - Refactor - Si ya pase un pre-ingreso, no me debe permitir volver a pasarlo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-23 16:03"
updated: "2022-10-04 09:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-79"
---

# POS-79: API - Refactor - Si ya pase un pre-ingreso, no me debe permitir volver a pasarlo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-23 16:03 |
| Actualizado | 2022-10-04 09:31 |
| Etiquetas | ninguna |
| Jira | [POS-79](https://bluinc.atlassian.net/browse/POS-79) |

## Relaciones

- **Padre:** [[POS-5 - API - Feat - Enviar correo con el preingreso de postventa|POS-5]] API - Feat - Enviar correo con el preingreso de postventa

## Descripcion

En este caso, debo devolver el error y el mensaje correspondiente y no hacer nada.

Ver ejemplo del pre ingreso 35 en desarrollo, que fue pasado a ingreso 4 veces.

[adjunto]
