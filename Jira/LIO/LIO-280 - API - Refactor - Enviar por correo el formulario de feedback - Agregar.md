---
jira_key: "LIO-280"
aliases: ["LIO-280"]
summary: "API - Refactor - Enviar por correo el formulario de feedback -> Agregar parámetro success al objeto de respuesta"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-03-18 16:19"
updated: "2025-03-19 12:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-280"
---

# LIO-280: API - Refactor - Enviar por correo el formulario de feedback -> Agregar parámetro success al objeto de respuesta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-03-18 16:19 |
| Actualizado | 2025-03-19 12:07 |
| Etiquetas | ninguna |
| Jira | [LIO-280](https://bluinc.atlassian.net/browse/LIO-280) |

## Relaciones

- **relates to:** [[LIO-272]] API - Refactor - Enviar por correo el formulario de feedback

## Descripcion

Debido a que el Front End espera el parámetro `success` para mostrar el éxito o fallo de la petición, realizaremos una refactorización para añadir este parámetro.

```
{{API_URL}}/v4/feedback
```

```
{
    "success": {true|false} <------------------- Se agrega    
    "message": "Feedback enviado correctamente"
}
```
