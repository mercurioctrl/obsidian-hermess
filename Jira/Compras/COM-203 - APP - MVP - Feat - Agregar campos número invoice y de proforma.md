---
jira_key: "COM-203"
aliases: ["COM-203"]
summary: "APP - MVP - Feat - Agregar campos número invoice y de proforma"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2025-09-30 15:53"
updated: "2025-10-24 10:15"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-203"
---

# COM-203: APP - MVP - Feat - Agregar campos número invoice y de proforma

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2025-09-30 15:53 |
| Actualizado | 2025-10-24 10:15 |
| Etiquetas | MVPLaset |
| Jira | [COM-203](https://bluinc.atlassian.net/browse/COM-203) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra
- **action item from:** [[COM-204 - API - MVP - Feat - Agregar campos número invoice y de proforma|COM-204]] API - MVP - Feat - Agregar campos número invoice y de proforma

## Descripcion

[adjunto]
Se deben incorporar dos nuevos campos al modal de detalle de la orden de compra:

- **número de invoice** (`voucherNumber`) → corregir el voucher por nro de invoice para que ellas la tengan correctamente


- **Proforma** (`proformaInvoice`)



Ambos campos deben poder visualizarse si existen en la respuesta del backend (`GET /v1/providerOrder/{id}`) y ser editables para su actualización (`PATCH`).

**Cambios solicitados:**

- En el modal de orden de compra:

- Agregar un campo de texto para `voucherNumber`.


- Agregar un campo de texto para `proformaInvoice`.


- Ubicarlos visualmente cerca del bloque superior (donde figura el trackingnumber, fecha de arribo, etc), según criterio de diseño.




- Si los campos ya existen en la respuesta, deben precargarse con su valor.


- Al generar el ingreso (botón “Generar ingreso” u otra acción de confirmación), si se modificaron o completaron estos campos, deben enviarse en el `PATCH`.






Relacionada con tarea 7 [link](https://docs.google.com/spreadsheets/d/18TUSaVG3bY_lMLunZ3kDCRlLnKpQV-_BPfrtbL4pHNA/edit?gid=723483997#gid=723483997)
