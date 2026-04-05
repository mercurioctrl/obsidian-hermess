---
jira_key: "COB-290"
aliases: ["COB-290"]
summary: "API - Refactor - Cobrar con retencion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-01-05 09:43"
updated: "2023-01-23 18:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-290"
---

# COB-290: API - Refactor - Cobrar con retencion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-05 09:43 |
| Actualizado | 2023-01-23 18:38 |
| Etiquetas | ninguna |
| Jira | [COB-290](https://bluinc.atlassian.net/browse/COB-290) |

## Relaciones

- **Padre:** [[COB-115]] Feat - Realizar un cobro
- **relates to:** [[COB-291]] API - Feat - Listar provincias (para retención)
- **blocks:** [[COB-296]] API - Feat - Listar provincias y el total de retenciones

## Descripcion

Agregaremos un nuevo tipo de cobro llamado “Retencion IIBB”. El mismo es como un pago comun. El tipo de pago mas parecido a este es el pago bancario, solo que en lugar de un banco se utiliza una caja por cada provincia.

¿que quiere decir esto?

Por ejemplo, puede pasar que un cliente viene y me paga:

a) $1000 (pesos) con retenciones de Ciudad de Buenos Aires

b) $1500 (pesos) con retenciones de Santa Fe

c) $400 (pesos) con retenciones de Cordoba.

d) $1000 (pesos) en efectivo.

De esta forma acreditaremos $3900 en la cuenta del cliente en concepto por el pago de pedido. (Como siempre hacemos con el monto total del pedido y el excedente en una linea aparte).

El pago (d) que es en pesos, como siempre ira a la caja que esta realizando el cobro.

Mientras que los pagos (a), (b), (c) se imputaran en una especie de cuenta (parecido a banco) para cada provincia.

Las provincias llegaran agregadas al objeto de cobro, así como lo hace el pago de una transferencia bancaria

```
[{
"clientId":4543, 
"pedido": 'X000234234324', //opcional
"finalAmount": 1214,
"comment":"Algun comentario opcional"
  "payments":[
 {
   "paymentMethodsId": {idNuevoParaElNuevoMetododePago},
   "amountPaid": "1000"
   "provinceId": 2,
 },
 {
   "paymentMethodsId": {idNuevoParaElNuevoMetododePago},
   "amountPaid": "1500"
   "provinceId": 4,
 },
 {
   "paymentMethodsId": {idNuevoParaElNuevoMetododePago},
   "amountPaid": "400"
   "provinceId": 12,
 },
 {
 "paymentMethodsId": 2,
   "amountPaid": "1000",
 }
]
}]

```



Es probable que debamos agregar una tabla nueva del tipo `NEW_BYTES.dbo.retentionIIBB` en donde iremos cargando las distintas recepciones para poder leerla.

Las columnas que puede tener son:

- id (auto)


- provinceId


- amountPaid


- date


- userId (u otro dato para ver quien la cobro)


- datos extra que se usan en el cobro por banco para ver si pertenece a un pedido o algo
