---
jira_key: "INV-87"
summary: "API - Refactor - Marcar las descripciones cuando están asistidas por un humano"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-19 16:35"
updated: "2024-07-20 21:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-87"
---

# INV-87: API - Refactor - Marcar las descripciones cuando están asistidas por un humano

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-19 16:35 |
| Actualizado | 2024-07-20 21:33 |
| Etiquetas | ninguna |
| Jira | [INV-87](https://bluinc.atlassian.net/browse/INV-87) |

## Descripción

Al ejecutar el recurso [link](https://lioteam.atlassian.net/browse/INV-82)  (es decir al editar una descripcion), marcaremos esa descripcion como que fue asistida por un humano (por lo tanto ya no es automatica).

Para esto marcaremos la columna `[PRODUCTOS].[dbo].[iaDescriptions].copilot = true`
