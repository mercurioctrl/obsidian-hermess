---
jira_key: "EXP-459"
aliases: ["EXP-459"]
summary: "APP - Refactor - Modificaremos la funcionalidad del modal para generar un envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-11-04 09:36"
updated: "2024-11-20 22:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-459"
---

# EXP-459: APP - Refactor - Modificaremos la funcionalidad del modal para generar un envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-04 09:36 |
| Actualizado | 2024-11-20 22:39 |
| Etiquetas | ninguna |
| Jira | [EXP-459](https://bluinc.atlassian.net/browse/EXP-459) |

## Relaciones

- **Padre:** [[EXP-13]] Feat - Etiquetas y seguimiento
- **action item from:** [[EXP-457]] API - Feat - Agregar un recurso para traer informacion completa y complementaria de lo referido al envio (para evaluar datos de cotizacion y posteriormente de armado)
- **is duplicated by:** [[EXP-460]] APP- Refactor en el modal de crear etiqueta

## Descripcion

Basándonos en lo realizado en el recurso [link](https://lioteam.atlassian.net/browse/EXP-457) 

Incluiremos informacion que permita discernir de que forma fue “cotizado” el envío por parte del sistema: Es decir, cuantos bultos y de que tamaño el sistema dedujo que tenia el paquete.

El objetivo en este paso, es que el “operario” que prepara el paquete pueda entender de que forma fue formulado por el sistema y así intentar acercarse lo mas posible o bien rechazar el armado como si hubiese estado mal cotizado.

Usaremos cualquier estrategia visual y de ux que nos permita dejar clara cualquier diferencia en contra.

Es decir que si por ejemplo el sistema armo 2 bultos y la persona ingresa 3 bultos, por ahí podemos marcar en amarillo el input y poner alguna leyenda de que están armando el paquete distinto a como lo formulo el sistema.

[adjunto]
