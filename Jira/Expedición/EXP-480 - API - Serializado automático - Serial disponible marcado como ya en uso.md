---
jira_key: "EXP-480"
aliases: ["EXP-480"]
summary: "API - Serializado automático - Serial disponible marcado como ya en uso"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-02-18 22:44"
updated: "2025-03-28 12:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-480"
---

# EXP-480: API - Serializado automático - Serial disponible marcado como ya en uso

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-02-18 22:44 |
| Actualizado | 2025-03-28 12:58 |
| Etiquetas | ninguna |
| Jira | [EXP-480](https://bluinc.atlassian.net/browse/EXP-480) |

## Relaciones

- **Padre:** [[EXP-1 - Base y Repositorios|EXP-1]] Base y Repositorios
- **action item from:** [[EXP-185 - API - Feat - Serializado automatico|EXP-185]] API - Feat - Serializado automatico

## Descripcion

Al intentar utilizar el recurso de serializado automático me retorna el mensaje de que el serial ya se encuentra en uso, sin embargo, al momento de cargar el serial dentro del artículo en específico si me permite hacerlo.

```
POST {API_URL}/v1/orders/{remito}/serials
```

```
POST {API_URL}/v1/orders/{remito}/serials/{id de articulo}
```

[adjunto]
[adjunto]
