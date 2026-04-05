---
jira_key: "PED-499"
aliases: ["PED-499"]
summary: "APP - Feat - Agregar prametro para mostrar los acreditados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-01-18 08:38"
updated: "2024-01-26 03:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-499"
---

# PED-499: APP - Feat - Agregar prametro para mostrar los acreditados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-18 08:38 |
| Actualizado | 2024-01-26 03:18 |
| Etiquetas | ninguna |
| Jira | [PED-499](https://bluinc.atlassian.net/browse/PED-499) |

## Relaciones

- **Padre:** [[PED-497 - Ver orden de compra|PED-497]] Ver orden de compra
- **is blocked by:** [[PED-498 - API - Feat - Agregar parametro para mostrar los acreditados|PED-498]] API - Feat - Agregar parametro para mostrar los acreditados

## Descripcion

Agregaremos una columna extra al modal donde vemos los pedidos con la finalidad de mostrar la cantidad de acreditados de ese producto.

[adjunto]
Se busca un resultado similar a este que es mucho mas visual que el original,  lo que se intenta es dar cuenta de que crédito se realizo, usando el nuevo parámetro `refundAmount` y al iterar guardarnos aquellos que tengan algún crédito para repetir los cálculos mas abajo y ver de cuanto es el crédito por ese pedido.

Para eso usaremos las unidades `refundAmount` multipicando por precio y agregando ivas tal cual lo hacemos con un detalle de venta.

Al final, pondremos los totales.

[adjunto]
