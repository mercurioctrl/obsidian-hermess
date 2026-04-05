---
jira_key: "LIO-127"
aliases: ["LIO-127"]
summary: "APP - Research - Modelar el siguiente recurso con (solo) los requisitos necesarios para mostrar la ficha de vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-11-08 13:35"
updated: "2024-11-19 18:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-127"
---

# LIO-127: APP - Research - Modelar el siguiente recurso con (solo) los requisitos necesarios para mostrar la ficha de vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-08 13:35 |
| Actualizado | 2024-11-19 18:35 |
| Etiquetas | ninguna |
| Jira | [LIO-127](https://bluinc.atlassian.net/browse/LIO-127) |

## Relaciones

- **Padre:** [[LIO-124 - Calificaciones|LIO-124]] Calificaciones
- **has action item:** [[LIO-129 - API - Feat - Recurso ficha de vendedor|LIO-129]] API - Feat - Recurso "ficha de vendedor"

## Descripcion

En la migracion de legacy a v4 buscamos hacer recursos que son mas especificos y pequeños.

Por eso me gustaria que revises el recurso

```
GET https://api.libreopcion.com.ar/vendedores/ficha/447
```

Que se utiliza en [link](https://libreopcion.com.ar/venta/reputacion/gears-store-V447)  la ficha de los vendedores, para traer solo aquello que se utiliza verdaderamente. Con esa informacion, eze podra construir el recurso adecuado en la api nueva.

[adjunto]
