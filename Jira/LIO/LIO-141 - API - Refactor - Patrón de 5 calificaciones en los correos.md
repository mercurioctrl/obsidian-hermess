---
jira_key: "LIO-141"
aliases: ["LIO-141"]
summary: "API - Refactor - Patrón de 5 calificaciones en los correos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-26 17:18"
updated: "2024-12-18 11:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-141"
---

# LIO-141: API - Refactor - Patrón de 5 calificaciones en los correos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-26 17:18 |
| Actualizado | 2024-12-18 11:21 |
| Etiquetas | ninguna |
| Jira | [LIO-141](https://bluinc.atlassian.net/browse/LIO-141) |

## Relaciones

- **Padre:** [[LIO-124]] Calificaciones
- **action item from:** [[LIO-143]] APP - Refactor - Preparar imágenes para 5 calificaciones  
- **has action item:** [[LIO-144]] APP - Refctor - Patron de 5 calificaciones al calificar 

## Descripcion

Una vez que ya tengamos los recursos  [link](https://lioteam.atlassian.net/browse/LIO-143)  nos encargaremos de agregar las faltantes en el correo de calificacion con su enlace correcto para cada tipo de calificación.

```
POST {{API_URL}}/v4/email/calification
```

[adjunto]
