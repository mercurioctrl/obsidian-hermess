---
jira_key: "EXP-123"
aliases: ["EXP-123"]
summary: "APP - Feat - Ver detalle para acreditar"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-12-22 09:38"
updated: "2022-12-27 13:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-123"
---

# EXP-123: APP - Feat - Ver detalle para acreditar

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-22 09:38 |
| Actualizado | 2022-12-27 13:27 |
| Etiquetas | ninguna |
| Jira | [EXP-123](https://bluinc.atlassian.net/browse/EXP-123) |

## Relaciones

- **Padre:** [[EXP-119 - Feat - Acreditar un pedido parcial o totalmente|EXP-119]] Feat - Acreditar un pedido parcial o totalmente
- **is blocked by:** [[EXP-124 - API - Feat - Ver detalle para acreditar|EXP-124]] API - Feat - Ver detalle para acreditar

## Descripcion

Se trata de un modal muy similar al siguiente

[adjunto]


donde Adicionalmente veremos la cantidad acreditada de ese item y podremos setear una cantidad que deseo acreditar de ese item

Para saber que se debe mostrar, consume el recurso [link](https://lioteam.atlassian.net/browse/EXP-124)

Al hacer click en el botón acreditar (una vez ingresadas las cantidades a acreditar, previa validar que `CantidadEnPedido` - `CantidadEnPedidoAcreditado` >= `LoQueQuieroAcreditar`) desplegaremos un área  o nuevo modal para ingresar los seriales que están dentro de las cosas que estoy devolviendo, de modo tal que en el back pueda operarlos para devolverlos a stock en [link](https://lioteam.atlassian.net/browse/EXP-124).

Una cosa mas:

Se debe incorporar la opción para seleccionar las cantidades máximas de todo para acreditar. Esta opción sirve para cuando la quieren acreditar completa y liberar todo por si el cliente finalmente no hace la compra, o cuando por alguna razón tienen que tirar todo para atrás. Si tenes dudas con esto preguntame.
