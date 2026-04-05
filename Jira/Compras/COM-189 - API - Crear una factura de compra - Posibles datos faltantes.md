---
jira_key: "COM-189"
aliases: ["COM-189"]
summary: "API - Crear una factura de compra -> Posibles datos faltantes"
status: "En curso"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-06-01 23:40"
updated: "2025-06-02 16:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-189"
---

# COM-189: API - Crear una factura de compra -> Posibles datos faltantes

| Campo | Valor |
|-------|-------|
| Estado | En curso (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-06-01 23:40 |
| Actualizado | 2025-06-02 16:43 |
| Etiquetas | ninguna |
| Jira | [COM-189](https://bluinc.atlassian.net/browse/COM-189) |

## Relaciones

- **relates to:** [[COM-175 - API - Feat - Crear una factura de compra|COM-175]] API - Feat - Crear una factura de compra

## Descripcion

Al momento de enviar la siguiente carga útil no logro visualizar algunos de los siguientes datos:

```
{
   "providerId": "001922",
   "voucherNumber": "0000123456999",
   "accountingDate": "2025-06-01",
   "deposito": "DEP001",
   "paymentMethodId": 3,
   "currencyPrefix": "USD",
   "paymentBranch": "SUC001",
   "type": 1,
   "currencyAmount": 928,
   "fob": 1600.50,
   "providerOrder": 11234,
   "tariffTax": [
      {
         "id": 66,
         "acronym": "RT",
         "description": "RETENCIONES",
         "rate": 101,
         "taxBase": 1
      },
      {
         "id": 67,
         "acronym": "GN",
         "description": "GANANCIAS",
         "rate": 102,
         "taxBase": 2
      },
      {
         "id": 72,
         "acronym": "IVA",
         "description": "IVA ADICIONAL ALICUOTA REDUCIDA",
         "rate": 103,
         "taxBase": 3
      }
   ],
   "items": [
      {
         "id": 109594,
         "title": "TECLADO GAMER EVGA Z15 SP RGB CLICKY BRONZE",
         "sku": "822-W1-15SP",
         "price": {
            "value": 51,
            "iva": 20.5,
            "finalPrice": 100.25
         },
         "warranty": "12 meses",
         "amount": 5,
         "position": "8528.49.90.000U",
         "taxPosition": {
            "aec": 20,
            "dii": 21,
            "iibb": 2.5,
            "iva": 21,
            "ganancias": 6,
            "te": 3,
            "die": 20,
            "ivaAd": 0
         },
         "amountEntered": 5
      }
   ]
}
```

[adjunto]
- Es correcto que guardemos el `SKU` en la columna `CREF`? Ya que en otras tablas hemos utilizado esta columna para el identificador de articulo.


- Se inserto otro articulo el cual no agregue a la carga útil.



[adjunto]


- Se visualizan más impuestos que los agregados en la carga útil.


- No logro visualizar los valores de `rate` ni `taxBase`.



[adjunto]
