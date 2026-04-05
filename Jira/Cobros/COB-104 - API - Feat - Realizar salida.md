---
jira_key: "COB-104"
aliases: ["COB-104"]
summary: "API - Feat - Realizar salida"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-15 09:55"
updated: "2022-12-05 14:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-104"
---

# COB-104: API - Feat - Realizar salida

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-15 09:55 |
| Actualizado | 2022-12-05 14:29 |
| Etiquetas | ninguna |
| Jira | [COB-104](https://bluinc.atlassian.net/browse/COB-104) |

## Relaciones

- **Padre:** [[COB-101 - Feat - Realizar salida de caja|COB-101]] Feat - Realizar salida de caja
- **is blocked by:** [[COB-102 - APP - Feat - Modal Salida|COB-102]] APP - Feat - Modal Salida
- **blocks:** [[COB-246 - API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un|COB-246]] API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un "pago de factura" o "pago proveedor"

## Descripcion

Se trata del procesamiento de la salida que se genera en el formulario [link](https://lioteam.atlassian.net/browse/COB-102) , la cual pude ser un movimiento (objeto) o varios dentro de un array y debe procesarse en bloque

```
POST {URL_API}/v1/cashOut
```

```
[
{
  ammount: 250.33,
  paymentMethodId:2,
  outputConceptId: 2,
  reference: "Este es un texto de referencia.",
  currencyQuote: 140.5
},
{
  ammount: 250.33,
  paymentMethodId:2,
  outputConceptId: 2,
  reference: "Este es un texto de referencia.",
  currencyQuote: 140.5
},
{
  ammount: 250.33,
  paymentMethodId:2,
  outputConceptId: 2,
  reference: "Este es un texto de referencia.",
  currencyQuote: 140.5
}
]
```
