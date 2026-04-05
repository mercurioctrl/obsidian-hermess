---
jira_key: "COM-79"
aliases: ["COM-79"]
summary: "APP - Refactor - Agregar unidades ingresadas al detalle de la ordende compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-04-04 06:11"
updated: "2024-06-14 14:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-79"
---

# COM-79: APP - Refactor - Agregar unidades ingresadas al detalle de la ordende compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-04 06:11 |
| Actualizado | 2024-06-14 14:41 |
| Etiquetas | ninguna |
| Jira | [COM-79](https://bluinc.atlassian.net/browse/COM-79) |

## Relaciones

- **Padre:** [[COM-38]] Ver orden de compra
- **is blocked by:** [[COM-78]] API - Refactor - Agregar unidades ingresadas al detalle de la ordende compra

## Descripcion

Dado que debe ser posible ingresar a stock parcialmente mercadería lo que haremos sera agregar un parámetro para este fin. Para esto usaremos agregaremos una nueva columna junto a la columna “Cant.” llamada “ingresado”.

Obtendremos el parametro de [https://lioteam.atlassian.net/browse/COM-78](https://lioteam.atlassian.net/browse/COM-78)
