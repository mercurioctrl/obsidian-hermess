---
jira_key: "PED-60"
aliases: ["PED-60"]
summary: "APP - Feat - Cotizar envío a una orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-09-11 09:47"
updated: "2023-09-18 10:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-60"
---

# PED-60: APP - Feat - Cotizar envío a una orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-11 09:47 |
| Actualizado | 2023-09-18 10:16 |
| Etiquetas | ninguna |
| Jira | [PED-60](https://bluinc.atlassian.net/browse/PED-60) |

## Relaciones

- **Padre:** [[PED-58 - Agregar Editar Envío en las ordenes de compra|PED-58]] Agregar / Editar Envío en las ordenes de compra

## Descripcion

Agregaremos una opción, mediante un accionable en el contexto de los pedidos.

Lo que haremos es usar el retorno que nos entrega [link](https://lioteam.atlassian.net/browse/PED-59)  para mostrar una las opciones disponibles para agregar un envío. 

Un ejemplo similar que se utilizaba en la empresa hasta hace poco seria el siguiente.

[adjunto]
Esto solo se puede hacer cuando el pedido se encuentra “pendiente”  osea `pedclit.cestado = "P"`
