---
jira_key: "COB-261"
aliases: ["COB-261"]
summary: "API - Refactor - Realizar cobro, agregar nuevos parámetros de cotización"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-12-15 15:23"
updated: "2022-12-16 17:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-261"
---

# COB-261: API - Refactor - Realizar cobro, agregar nuevos parámetros de cotización

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-15 15:23 |
| Actualizado | 2022-12-16 17:53 |
| Etiquetas | ninguna |
| Jira | [COB-261](https://bluinc.atlassian.net/browse/COB-261) |

## Relaciones

- **Padre:** [[COB-115 - Feat - Realizar un cobro|COB-115]] Feat - Realizar un cobro

## Descripcion

Segun el refactor  [link](https://lioteam.atlassian.net/browse/COB-257) que se esta preparando, ahora tomaremos la cotización para cada medio de pago, directamente del objeto.

En caso de no existir, sea por el motivo que sea tomaremos la del pedido (tener en cuanta que en realidad por ahora siempre es la del pedido salvo en cheques, pero lo dejamos preparado para que sea mas versátil de esta manera). 

```
[{
"clientId":4543, 
"pedido": 'X000234234324', //opcional
"finalAmount": 1214,
"comment":"Algun comentario opcional"
  "payments":[
 {
   "paymentMethodsId": 1,
   "amountPaid": "300",
   "quote": 165.45 <--Nuvo parametro
 },
 {
  "paymentMethodsId": 2,
   "amountPaid": "5000",
   "quote": 165.45 <--Nuvo parametro
 },
 {
  "paymentMethodsId": 3,
   "amountPaid": "150",
   "quote": 155.45 <--Nuvo parametro
 },
 {
 "paymentMethodsId": 4,
   "amountPaid": "50000",
   "quote": 175.45 <--Nuvo parametro
 }
]
}]
```
