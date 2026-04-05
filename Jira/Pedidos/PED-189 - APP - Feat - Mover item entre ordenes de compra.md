---
jira_key: "PED-189"
aliases: ["PED-189"]
summary: "APP - Feat - Mover item entre ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-10-30 09:38"
updated: "2023-11-08 07:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-189"
---

# PED-189: APP - Feat - Mover item entre ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-30 09:38 |
| Actualizado | 2023-11-08 07:00 |
| Etiquetas | ninguna |
| Jira | [PED-189](https://bluinc.atlassian.net/browse/PED-189) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **is blocked by:** [[PED-221 - APP - Mover item entre ordenes de compra - Incidencias varias|PED-221]] APP - Mover item entre ordenes de compra - Incidencias varias

## Descripcion

Esta funcionalidad permite trasladar ítems directamente de una orden de compra a otra. Esta acción es útil en casos donde la mercadería requerida para un pedido específico se encuentra ya asignada a otra orden y no está disponible libremente en el inventario. Al permitir esta transferencia directa, se evita el proceso de descarga y carga en la nueva orden, reduciendo el riesgo de que otro vendedor tome el ítem en ese lapso a cero y mejorando la experiencia.

Lo que sigue a continuación es una descripción de la feature actual, pero podemos ver alternativas en el caso de que se ocurran mejores formas de disponer los elementos.

### ¿Como funciona?

Agregaremos un checkbox a cada uno de los items de pedido (solo cuando esta pendiente, sin pedido)

[adjunto]
De clickear en uno o mas de ellos, resaltaremos la linea y permitiremos enviar una cantidad de ese item a una orden de destino.

Al seleccionar uno  o mas items, aparecerán dos botones accionables, uno para hacer el envío a una orden determinada y otro para crear una nueva orden y enviarlo a ella.

(ver sistema beta)

[adjunto]
Para el caso utilizaremos la siguiente feature [link](https://lioteam.atlassian.net/browse/PED-188)
