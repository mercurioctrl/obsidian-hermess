---
jira_key: "NBWEB-738"
summary: "API - Oportunidad de mejora - Validación de productos al procesar carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-05-22 17:47"
updated: "2024-05-27 20:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-738"
---

# NBWEB-738: API - Oportunidad de mejora - Validación de productos al procesar carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-22 17:47 |
| Actualizado | 2024-05-27 20:12 |
| Etiquetas | ninguna |
| Jira | [NBWEB-738](https://bluinc.atlassian.net/browse/NBWEB-738) |

## Descripción

Como propuesta de mejora validaremos que al intentar procesar un carrito de compras que no contenga artículos, el sistema no permita continuar con el proceso.

```
POST {{API_URL}}/v1/carrito/process
```

[attachment]
