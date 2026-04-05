---
jira_key: "LIO-230"
aliases: ["LIO-230"]
summary: "API - Mover recurso \"vendedor\" de Legacy y V4 - Error de tipeo al filtrar por vendedor"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-02-21 15:47"
updated: "2025-03-06 10:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-230"
---

# LIO-230: API - Mover recurso "vendedor" de Legacy y V4 - Error de tipeo al filtrar por vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-02-21 15:47 |
| Actualizado | 2025-03-06 10:41 |
| Etiquetas | ninguna |
| Jira | [LIO-230](https://bluinc.atlassian.net/browse/LIO-230) |

## Relaciones

- **Padre:** [[LIO-212]] Perfil de vendedor
- **action item from:** [[LIO-213]] API - Feat - Mover recurso "vendedor" de Legacy y V4

## Descripcion

Por alguna razón al filtrar por el vendedor `135266` me aparece el siguiente error:

```
GET {{API_URL}}/v4/seller/{vendedor}
```

[adjunto]
Al filtrar por otro vendedor no aparece el error

[adjunto]
[adjunto]
