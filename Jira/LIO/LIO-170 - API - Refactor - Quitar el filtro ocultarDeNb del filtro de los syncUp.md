---
jira_key: "LIO-170"
aliases: ["LIO-170"]
summary: "API - Refactor - Quitar el filtro \"ocultarDeNb\" del filtro de los syncUp"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-03 10:05"
updated: "2025-01-27 17:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-170"
---

# LIO-170: API - Refactor - Quitar el filtro "ocultarDeNb" del filtro de los syncUp

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-03 10:05 |
| Actualizado | 2025-01-27 17:31 |
| Etiquetas | ninguna |
| Jira | [LIO-170](https://bluinc.atlassian.net/browse/LIO-170) |

## Relaciones

- **Padre:** [[LIO-166]] Catalogos y sincronizaciones

## Descripcion

Se debe quitar el filtro `ocultarDeNb` ya que ahora solo se usara `ocultar_lo` para definir si se sincroniza o no de manera independiente…

```
PATCH {{API_URL}}/v4/syncUp/items
```

```
POST {{API_URL}}/v4/syncUp/items
```
