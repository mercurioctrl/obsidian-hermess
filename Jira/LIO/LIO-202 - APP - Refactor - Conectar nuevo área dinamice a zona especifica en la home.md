---
jira_key: "LIO-202"
aliases: ["LIO-202"]
summary: "APP - Refactor  - Conectar nuevo  área dinamice a zona especifica en la home (precios relampago fondo y onomatopeya)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-02-01 20:45"
updated: "2025-02-05 20:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-202"
---

# LIO-202: APP - Refactor  - Conectar nuevo  área dinamice a zona especifica en la home (precios relampago fondo y onomatopeya)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-01 20:45 |
| Actualizado | 2025-02-05 20:29 |
| Etiquetas | ninguna |
| Jira | [LIO-202](https://bluinc.atlassian.net/browse/LIO-202) |

## Relaciones

- **Padre:** [[LIO-105 - Home|LIO-105]] Home

## Descripcion

Leeremos de forma dinámica los recursos para construir el área de precios flash



[adjunto]
Para esto usaremos el nuevo area (6dinamica)

```
GET {API_CMS}/v1/cms/banner/5
```

Tomaremos la primera imagen que viene para e fondo, y la segunda para la onomatopeya

[adjunto]
