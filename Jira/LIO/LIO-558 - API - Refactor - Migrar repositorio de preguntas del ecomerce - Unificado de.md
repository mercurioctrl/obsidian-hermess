---
jira_key: "LIO-558"
aliases: ["LIO-558"]
summary: "API - Refactor - Migrar repositorio de preguntas del ecomerce -> Unificado de imagen"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Guillermo Avila"
created: "2026-02-25 14:35"
updated: "2026-02-26 17:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-558"
---

# LIO-558: API - Refactor - Migrar repositorio de preguntas del ecomerce -> Unificado de imagen

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Guillermo Avila |
| Creado | 2026-02-25 14:35 |
| Actualizado | 2026-02-26 17:38 |
| Etiquetas | ninguna |
| Jira | [LIO-558](https://bluinc.atlassian.net/browse/LIO-558) |

## Relaciones

- **Padre:** [[LIO-537 - Migración de repositorios previa deprecación de la api legacy|LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **clones:** [[LIO-544 - API - Feat - Migrar repositorio de preguntas del ecomerce|LIO-544]] API - Feat - Migrar repositorio de preguntas del ecomerce

## Descripcion

Noté que la imagen en v4 viene el enlace completo, sin embargo, en legacy solamente el nombre.

Revisar e implementar si es necesario.



```
GET /productos/ficha/{id}/preguntas-respuestas
```

[adjunto]
[adjunto]
