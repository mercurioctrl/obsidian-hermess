---
jira_key: "PED-876"
aliases: ["PED-876"]
summary: "API - Refactor - Al hacer una orden de SUC3 esta debe solo mover el stock virtualmente como en los otros casos hasta el momento de generar el pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-20 15:20"
updated: "2024-11-25 01:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-876"
---

# PED-876: API - Refactor - Al hacer una orden de SUC3 esta debe solo mover el stock virtualmente como en los otros casos hasta el momento de generar el pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-20 15:20 |
| Actualizado | 2024-11-25 01:06 |
| Etiquetas | ninguna |
| Jira | [PED-876](https://bluinc.atlassian.net/browse/PED-876) |

## Relaciones

- **Padre:** [[PED-58]] Agregar / Editar Envío en las ordenes de compra
- **has action item:** [[SNB-2535]] no podemos generar pedido para uso internos

## Descripcion

Segun lo conversado por la llamada, hay un paso extra al agregar un item en **SUC0003 donde se altera la tabla stock, y esto no deberia suceder hasta el próximo paso (al generar pedido)**

```
PATCH {API_URL}/v1/orders/addItem
```
