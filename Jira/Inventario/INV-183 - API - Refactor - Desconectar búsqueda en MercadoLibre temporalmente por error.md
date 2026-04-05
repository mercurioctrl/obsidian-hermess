---
jira_key: "INV-183"
aliases: ["INV-183"]
summary: "API - Refactor - Desconectar búsqueda en MercadoLibre temporalmente por error con recurso de imágenes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-07 08:36"
updated: "2025-04-09 02:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-183"
---

# INV-183: API - Refactor - Desconectar búsqueda en MercadoLibre temporalmente por error con recurso de imágenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-07 08:36 |
| Actualizado | 2025-04-09 02:03 |
| Etiquetas | ninguna |
| Jira | [INV-183](https://bluinc.atlassian.net/browse/INV-183) |

## Relaciones

- **Padre:** [[INV-35 - Importadores Scrappers|INV-35]] Importadores/ Scrappers

## Descripcion

Actualmente, la integración con MercadoLibre está generando errores al intentar obtener imágenes desde el recurso: 

```
GET {API_URL}/getImages/string?title={titulo} 
```

Este recurso parece estar fallando o respondiendo incorrectamente, lo cual interrumpe el funcionamiento esperado. Mientras se investiga y se encuentra una solución definitiva, es necesario desconectar temporalmente la búsqueda en MercadoLibre para evitar errores en el sistema y mejorar la experiencia del usuario. 

**Notas técnicas (opcional): **Se recomienda agregar un flag o condición temporal para no perder la lógica ya implementada (SOLO SI ES POSIBLE)
