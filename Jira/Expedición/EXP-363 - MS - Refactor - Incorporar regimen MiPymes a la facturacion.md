---
jira_key: "EXP-363"
aliases: ["EXP-363"]
summary: "MS - Refactor - Incorporar regimen MiPymes a la facturacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-25 15:32"
updated: "2023-08-31 09:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-363"
---

# EXP-363: MS - Refactor - Incorporar regimen MiPymes a la facturacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-25 15:32 |
| Actualizado | 2023-08-31 09:01 |
| Etiquetas | ninguna |
| Jira | [EXP-363](https://bluinc.atlassian.net/browse/EXP-363) |

## Relaciones

- **Padre:** [[EXP-355]] Emision de facturas
- **blocks:** [[SNB-1141]] facturacion 

## Descripcion

Existe un régimen especial de facturación (factura,débito y crédito) que es  para Pequeñas y Medianas Empresas (MiPyMEs) emitir facturas de crédito electrónicas a grandes empresas, las cuales pueden ser descontadas en el mercado financiero para obtener liquidez. 

Estas facturas tienen un plazo de pago establecido y, si la gran empresa no paga en ese plazo, la MiPyME puede cobrarla en el mercado secundario. Es una herramienta que busca mejorar el financiamiento y la liquidez de las MiPyMEs en Argentina.

Este régimen solo se aplica a muy pocos clientes.

Un caso es OVERDRIVE S.A (9657) 

Ver ejemplo de comprobante realizado:

[link](https://omega.comprobantes.lio.red/voucher/F/512979/bd54e08567cc4d03b4ee4a7c69f7c7?show=1) 

Hasta donde yo conozco, solo podes saber si el cliente y operación deben ser bajo ese régimen una vez que lo intentaste hacer con la logica normal, por ejemplo a un “Responsable inscrito” una Factura A.

Si justo es MyPyme entonces devolverá “1 - No es un comprobante valido bajo el Régimen de la Ley n\u00b0 27.440” y es ahi, donde debemos intentarlo del otro modo.

Uno podría pensar que debe marcar el cliente, para en el futuro componer el “Request” para este régimen particular, pero la realidad es que eso no sirve porque esa condición o cambia de un momento a otro o bien, el total del comprobante puede afectar si cae o no dentro del régimen.

Por tanto lo mejor es siempre esperar que nos dice el endpoint.
