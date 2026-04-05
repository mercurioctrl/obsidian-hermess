---
jira_key: "SNB-12"
aliases: ["SNB-12"]
summary: "Diferencia en la liquidación de remitos a clientes con condición de IVA IMPORT/EXPORT"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Lautaro Alejandro Soto"
created: "2021-09-22 09:46"
updated: "2021-09-29 16:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-12"
---

# SNB-12: Diferencia en la liquidación de remitos a clientes con condición de IVA IMPORT/EXPORT

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Lautaro Alejandro Soto |
| Creado | 2021-09-22 09:46 |
| Actualizado | 2021-09-29 16:57 |
| Etiquetas | ninguna |
| Jira | [SNB-12](https://bluinc.atlassian.net/browse/SNB-12) |

## Relaciones

*Sin relaciones*

## Descripcion

Los clientes con condición de IVA IMPORT/EXPORT abonan por el total que arroja el remito (sin IVA) pero al momento de liquidar el remito del pedido generado en el nuevo sistema, en el sector de facturación visualizan el total a abonar como el total del remito (el monto que abonó el cliente) + el IVA, por lo que se genera una diferencia como si el cliente hubiese abonado de menos y por ende facturación no autoriza el pago.

Adjunto imágenes a modo de ejemplo.
