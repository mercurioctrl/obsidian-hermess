---
jira_key: "EXP-431"
aliases: ["EXP-431"]
summary: "API -  Aceptar pase de postventa - expedicion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2024-08-19 15:36"
updated: "2024-08-29 03:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-431"
---

# EXP-431: API -  Aceptar pase de postventa - expedicion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2024-08-19 15:36 |
| Actualizado | 2024-08-29 03:19 |
| Etiquetas | ninguna |
| Jira | [EXP-431](https://bluinc.atlassian.net/browse/EXP-431) |

## Relaciones

- **Padre:** [[EXP-430 - Refactorizar pases|EXP-430]] Refactorizar pases
- **relates to:** [[EXP-434 - API - Aceptar pase de postventa - Sugerencia de mejora al ingresar serial|EXP-434]] API - Aceptar pase de postventa - Sugerencia de mejora al ingresar serial invalido

## Descripcion

Al aceptar un pase de postventa a expedicion se debe:

- Mover el stock de pventa a expedicion


- Verificar que el serial pistoleteado coincide con el serial en el pase


- Registrar el log de stock


- Cambiar el estado del pase a finalizado
