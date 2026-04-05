---
jira_key: "COB-528"
aliases: ["COB-528"]
summary: "API - Refactor - El repositorio de medios de envio, debe mostrar todos los metodos que tengan una de las columnas activas en 1"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-19 15:20"
updated: "2024-07-21 23:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-528"
---

# COB-528: API - Refactor - El repositorio de medios de envio, debe mostrar todos los metodos que tengan una de las columnas activas en 1

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-19 15:20 |
| Actualizado | 2024-07-21 23:25 |
| Etiquetas | ninguna |
| Jira | [COB-528](https://bluinc.atlassian.net/browse/COB-528) |

## Relaciones

- **Padre:** [[COB-21]] Base del proyecto y formularios

## Descripcion

Modificaremos el repositorio 

```
GET /v1/shippingMethods
```

Deben mostrarse todos los que cumplen algunas de estas tres condiciones

`activo = 1 OR activo = 1 OR activo = 1`
