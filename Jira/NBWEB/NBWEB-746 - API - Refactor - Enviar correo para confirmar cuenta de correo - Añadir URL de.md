---
jira_key: "NBWEB-746"
aliases: ["NBWEB-746"]
summary: "API - Refactor - Enviar correo para confirmar cuenta de correo - Añadir URL de pruebas"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-06-10 17:43"
updated: "2024-06-11 16:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-746"
---

# NBWEB-746: API - Refactor - Enviar correo para confirmar cuenta de correo - Añadir URL de pruebas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-10 17:43 |
| Actualizado | 2024-06-11 16:11 |
| Etiquetas | ninguna |
| Jira | [NBWEB-746](https://bluinc.atlassian.net/browse/NBWEB-746) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **relates to:** [[NBWEB-132]] Enviar correo para confirmar cuenta de correo

## Descripcion

Realizaremos un refactor para que cuando un cliente se registre en el sitio de pruebas, los enlaces para la confirmación de correo también sean para el ambiente de pruebas.

```
PUT {{API_URL}}/v1/registrationRequest
```

[adjunto]
