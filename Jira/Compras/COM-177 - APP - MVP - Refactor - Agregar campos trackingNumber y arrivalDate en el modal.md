---
jira_key: "COM-177"
aliases: ["COM-177"]
summary: "APP - MVP - Refactor - Agregar campos trackingNumber y arrivalDate en el modal de orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-29 14:11"
updated: "2025-05-13 14:40"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-177"
---

# COM-177: APP - MVP - Refactor - Agregar campos trackingNumber y arrivalDate en el modal de orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-29 14:11 |
| Actualizado | 2025-05-13 14:40 |
| Etiquetas | MVPLaset |
| Jira | [COM-177](https://bluinc.atlassian.net/browse/COM-177) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra
- **action item from:** [[COM-176 - API - MVP - Refactor - Agregar trackingNumber y arrivalDate en órdenes de compra|COM-176]] API - MVP - Refactor - Agregar trackingNumber y arrivalDate en órdenes de compra
- **is blocked by:** [[COM-185 - API - MVP - Feat - Recurso para modificar datos de cabecera en Provider Order|COM-185]] API - MVP - Feat - Recurso para modificar datos de cabecera en Provider Order 

## Descripcion

[adjunto]
Se deben incorporar dos nuevos campos al modal de detalle de la orden de compra:

- **Tracking number** (`trackingNumber`)


- **Fecha de arribo** (`arrivalDate`)



Ambos campos deben poder visualizarse si existen en la respuesta del backend (`GET /v1/providerOrder/{id}`) y ser editables para su actualización (`PATCH`).

**Cambios solicitados:**

- En el modal de orden de compra:

- Agregar un campo de texto para `trackingNumber`.


- Agregar un campo de tipo fecha/hora (`datetime-local`) para `arrivalDate`.


- Ubicarlos visualmente cerca del bloque superior (donde figura el comprador, proveedor, etc), según criterio de diseño.




- Si los campos ya existen en la respuesta, deben precargarse con su valor.


- Al generar el ingreso (botón “Generar ingreso” u otra acción de confirmación), si se modificaron o completaron estos campos, deben enviarse en el `PATCH`.
