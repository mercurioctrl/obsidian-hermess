---
jira_key: "LIO-265"
aliases: ["LIO-265"]
summary: "APP - Refactor - Accionable feedback en el menu horizontal"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-03-11 13:33"
updated: "2025-03-19 16:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-265"
---

# LIO-265: APP - Refactor - Accionable feedback en el menu horizontal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-11 13:33 |
| Actualizado | 2025-03-19 16:50 |
| Etiquetas | ninguna |
| Jira | [LIO-265](https://bluinc.atlassian.net/browse/LIO-265) |

## Relaciones

- **Padre:** [[LIO-1]] Experiencia del Usuario (UX)
- **has action item:** [[LIO-272]] API - Refactor - Enviar por correo el formulario de feedback

## Descripcion

Según lo conversado, agregaremos una nueva opción en el menú horizontal que permitirá a los usuarios proporcionar feedback de manera rápida y sencilla.

[adjunto]
**Detalles de Implementación:**

- Se añadirá un botón en el menú horizontal que, al hacer clic, desplegará un modal.


- El modal incluirá:

- Un campo de texto para que el usuario ingrese su feedback.


- Un sistema de calificación con un rating de 1 a 5.




- Al enviar, se consumirá el recurso  para almacenar la información.


- Se mostrará una notificación de éxito o error según la respuesta de la API.



```
POST {API_V4}/feedback
```

```
{
  "userId": 12345, //si existe
  "rating": 4,
  "feedback": "La experiencia de uso es buena, pero podría mejorar la velocidad de carga.",
}

```

Respuesta

```
{
  "success": true,
  "message": "Feedback enviado correctamente.",
  "feedbackId": 98765
}

```
