---
jira_key: "COM-191"
aliases: ["COM-191"]
summary: "APP -MVP - Refactor - Elegir si altera o no el costo promedio del item para cada item"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-06-11 08:48"
updated: "2025-10-07 10:41"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/COM-191"
---

# COM-191: APP -MVP - Refactor - Elegir si altera o no el costo promedio del item para cada item

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-11 08:48 |
| Actualizado | 2025-10-07 10:41 |
| Etiquetas | esperandoDependencia |
| Jira | [COM-191](https://bluinc.atlassian.net/browse/COM-191) |

## Relaciones

- **Padre:** [[COM-109 - Generar INGRESO o pedido (a partir de una orden de compra)|COM-109]] Generar INGRESO o pedido (a partir de una orden de compra)
- **is blocked by:** [[COM-190 - API -MVP - Refactor - Elegir si altera o no el costo promedio del item para|COM-190]] API -MVP - Refactor - Elegir si altera o no el costo promedio del item para cada item

## Descripcion

A veces sucede que al ingresar un item dentro del inventario este item ya existe e ingreso a un precio determinado anteriormente e ingresa a un nuevo precio en la orden de compra actual. Para poder unificar el costo que tiene el product se usa una **técnica de valuación de inventario** que consiste en calcular el valor de los productos en stock usando un **promedio ponderado** de los costos históricos de adquisición.

Teniendo en cuenta:

- Cuántas unidades tenías y a qué costo las compraste.


- Cuántas unidades nuevas entran y a qué precio.



El resultado es un nuevo valor promedio que se aplica al item asimilando la nueva cantidad según la siguiente formula

```
Costo Promedio Ponderado = [(Stock anterior x Costo anterior) + (Ingreso nuevo x Precio nuevo)] \ Stock Actual
```


Para esto agregaremos una nueva columna, que esta marcada por defecto para promediar costo con la cual enviaremos el parametro `updateAverageCost` para cada item en `true/false` según corresponda

[adjunto]
Adicionalmente agregaremos un  para explicar la columna, que cuando esta marcado ejecutara un promedio en caso de que exista stock actualmente del producto.



```
POST /v1/makeProviderOrderInbound
```

```
{
  "orderNumber": 11257,
  "trackingNumber": null,
  "arrivalDate": null,
  "providerId": "001150",
  "providerName": "LASET S.A.",
  "observation": "",
  "status": "P",
  "voucherPurchaseId": "",
  "buyerName": "Web Sistema",
  "buyerId": 12,
  "currencyQuote": 927,
  "currencyFiscalQuote": 1,
  "distributeTaxes": [],
  "items": [
    {
      "id": 118847,
      "title": "AMD COOLER P/ PROCESADOR ATHLON/SEMPRON AM1",
      "sku": "COOLAMDAM1ATH/SEM",
      "price": { "value": "2", "iva": 10.5 },
      "warranty": "12 meses",
      "amount": 1,
      "position": null,
      "taxPosition": null,
      "amountEntered": null,
      "totalItemTax": 0,
      "partial": 1,
      "updateAverageCost": true <-- Se agrega enviado por el front
    },
    {
      "id": 116751,
      "title": "MSI NOTEBOOK CROSSHAIR 15 R6E B12UEZ (I7 + 16GB + 1TB + 3060)",
      "sku": "9S7-158362-636",
      "price": { "value": "3", "iva": 10.5 },
      "warranty": "12 meses",
      "amount": 1,
      "position": null,
      "taxPosition": null,
      "amountEntered": null,
      "totalItemTax": 0,
      "partial": 1,
      "updateAverageCost": true <-- Se agrega enviado por el front      
    }
  ]
}
```
