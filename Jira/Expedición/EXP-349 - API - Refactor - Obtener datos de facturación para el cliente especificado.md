---
jira_key: "EXP-349"
aliases: ["EXP-349"]
summary: "API - Refactor - Obtener datos de facturación para el cliente especificado"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-07-25 12:35"
updated: "2023-07-26 11:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-349"
---

# EXP-349: API - Refactor - Obtener datos de facturación para el cliente especificado

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-25 12:35 |
| Actualizado | 2023-07-26 11:06 |
| Etiquetas | ninguna |
| Jira | [EXP-349](https://bluinc.atlassian.net/browse/EXP-349) |

## Relaciones

- **Padre:** [[EXP-119]] Feat - Acreditar un pedido parcial o totalmente

## Descripcion

Utilizando el recurso del servicio de comprobantes 

```
{API_URL}/v2/clientByCreateVoucher/023278?voucherDescription=CREDITO
```

Para servirle en la API de expedición evitando el loguea al front el valor necesario, para esto pasaremos el parámetro `voucherDescription` y  `clientId`

El recurso resulta en una copia del original, y por lo tanto tiene la misma morfología, de forma tal que desde el front solo enviando el concepto que queremos, obtenemos el `voucherType` 



URL EN EL SERVICIO DE EXPEDICION

```
{API_URL}/v2/voucherTypes?clientId=19690&search=credito
```

La otra posibilidad es abrir el recurso específicamente para entregar SOLO EL `voucherType` cuando no estas logueado. Esto no es peligroso porque el dato es abstracto y no entregaría informacion sensible de clientes.
