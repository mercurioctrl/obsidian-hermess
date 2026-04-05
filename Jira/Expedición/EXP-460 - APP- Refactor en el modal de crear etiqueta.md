---
jira_key: "EXP-460"
aliases: ["EXP-460"]
summary: "APP- Refactor en el modal de crear etiqueta"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2024-11-04 10:31"
updated: "2024-11-08 10:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-460"
---

# EXP-460: APP- Refactor en el modal de crear etiqueta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2024-11-04 10:31 |
| Actualizado | 2024-11-08 10:40 |
| Etiquetas | ninguna |
| Jira | [EXP-460](https://bluinc.atlassian.net/browse/EXP-460) |

## Relaciones

- **Padre:** [[EXP-6]] Despacho de envios
- **Subtarea:** [[EXP-469]] APP - Refactor - Habilitar para que "Andreani" y "Oca" tambien muestren la comparativa como lo hace entregar
- **duplicates:** [[EXP-459]] APP - Refactor - Modificaremos la funcionalidad del modal para generar un envio

## Descripcion

Al crear una etiqueta debe aparecer la info precargada de cuantos bultos fueron cotizados de X tamaño y X precio
si se modifica la cantidad de Bultos, se debe realizar una peticion para obetener el nuevo precio de cotizacion y si supera el min o max posible (30%) dependiendo de esto se habilita o no el boton para generar la etiqueta

```java
GET {API_URL}/v1/shipments/getDetails
```
