---
jira_key: "LIO-83"
aliases: ["LIO-83"]
summary: "APP - Revisar errores que suceden respecto a carrito express o carrito normal al abandonar alguno de ellos y querer procesar una nueva compra"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2024-08-07 17:06"
updated: "2024-08-26 00:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-83"
---

# LIO-83: APP - Revisar errores que suceden respecto a carrito express o carrito normal al abandonar alguno de ellos y querer procesar una nueva compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2024-08-07 17:06 |
| Actualizado | 2024-08-26 00:03 |
| Etiquetas | ninguna |
| Jira | [LIO-83](https://bluinc.atlassian.net/browse/LIO-83) |

## Relaciones

- **is blocked by:** [[SNB-2190]] cliente no puede finalizar pedido

## Descripcion

Casos:
1- si estoy realizando una compra→ debo preguntar sobre el stock de carrito express solo si estoy en carrito express si no no
controlar-disponibilidad (mando false en caso q sea carrito normal)
se manda uno true y uno false ahi hay algo raro
2 - si tengo un carrito 3 items, luego voy a producto X y le doy comprar ahora me abre carrito express llegar al paso 3 del checkout cierro (pagina), si luego voy a carrito y quiero procesar mis 3 items aparece lo que quedo en el express
