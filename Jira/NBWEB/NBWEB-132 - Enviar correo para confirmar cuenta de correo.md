---
jira_key: "NBWEB-132"
aliases: ["NBWEB-132"]
summary: "Enviar correo para confirmar cuenta de correo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-22 15:11"
updated: "2024-06-10 17:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-132"
---

# NBWEB-132: Enviar correo para confirmar cuenta de correo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-22 15:11 |
| Actualizado | 2024-06-10 17:43 |
| Etiquetas | ninguna |
| Jira | [NBWEB-132](https://bluinc.atlassian.net/browse/NBWEB-132) |

## Relaciones

- **Padre:** [[NBWEB-130]] API - Registro y alta de cliente
- **relates to:** [[NBWEB-746]] API - Refactor - Enviar correo para confirmar cuenta de correo - Añadir URL de pruebas

## Descripcion

Se debe enviar un correo con un token para confirmar que al aspirante tiene acceso al correo

En el correo se envía un token, similar a la historia [link](https://lioteam.atlassian.net/browse/NBWEB-124) 

De coincidir el token, se marca la columna [NB_WEB].[dbo].[usuarios_nb].correoConfirmado
