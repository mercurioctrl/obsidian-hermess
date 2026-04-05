---
jira_key: "EXP-103"
aliases: ["EXP-103"]
summary: "API - Feat - obtener etiqueta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-16 13:56"
updated: "2023-05-29 06:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-103"
---

# EXP-103: API - Feat - obtener etiqueta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-16 13:56 |
| Actualizado | 2023-05-29 06:34 |
| Etiquetas | ninguna |
| Jira | [EXP-103](https://bluinc.atlassian.net/browse/EXP-103) |

## Relaciones

- **Padre:** [[EXP-13]] Feat - Etiquetas y seguimiento

## Descripcion

Lo que hace este recurso es traer el código ZPL para poder imprimir la etiqueta directamente

```
GET {{API_URL}}/v1/orders/zpl/{trackingNumber}
```
