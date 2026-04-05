---
jira_key: "PED-1034"
aliases: ["PED-1034"]
summary: "API - Refactor - Admitir multiples comprobantes en la misma carga y tambien en cargas posteriores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-07-01 14:03"
updated: "2025-07-14 10:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1034"
---

# PED-1034: API - Refactor - Admitir multiples comprobantes en la misma carga y tambien en cargas posteriores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-01 14:03 |
| Actualizado | 2025-07-14 10:32 |
| Etiquetas | ninguna |
| Jira | [PED-1034](https://bluinc.atlassian.net/browse/PED-1034) |

## Relaciones

- **Padre:** [[PED-761 - Comprobantes de pago|PED-761]] Comprobantes de pago
- **has action item:** [[SNB-2991 - Venta con mas de un cupon no autoriza|SNB-2991]] Venta con mas de un cupon no autoriza

## Descripcion

Al realizar una compra desde LO y cargar un comprobante, este se visualiza correctamente en la sección de pedidos, (una vez completada la sincronización.)

El problema se presenta cuando, desde pedidos, se intenta cargar un segundo comprobante: esto genera un error al realizar cargas múltiples.

El recurso `PATCH paymentVoucher` debería contemplar la posibilidad de carga múltiple, manteniendo los criterios de aceptación establecidos.

Entre estos criterios, es fundamental evitar que se cargue un comprobante con un número de operación que ya exista en otro pedido o que esté repetido.
