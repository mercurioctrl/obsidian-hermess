---
jira_key: "PED-796"
aliases: ["PED-796"]
summary: "API - Refactor - numero de operacion no debe ser obligatorio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-08-14 08:28"
updated: "2024-08-15 03:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-796"
---

# PED-796: API - Refactor - numero de operacion no debe ser obligatorio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-08-14 08:28 |
| Actualizado | 2024-08-15 03:48 |
| Etiquetas | ninguna |
| Jira | [PED-796](https://bluinc.atlassian.net/browse/PED-796) |

## Relaciones

- **Padre:** [[PED-729 - Comprobante de pago y autorizacion|PED-729]] Comprobante de pago y autorizacion

## Descripcion

Se debe quitar validación de campo(nroOperacion), pero si el campo es enviado se valida  si ya existe el numero de operacion en la bd.

PEDIDOS:

PATCH: URL/v1/paymentVoucher
