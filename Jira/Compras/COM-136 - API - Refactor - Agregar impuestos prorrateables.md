---
jira_key: "COM-136"
aliases: ["COM-136"]
summary: "API - Refactor - Agregar impuestos prorrateables"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-08-08 09:42"
updated: "2024-09-04 11:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-136"
---

# COM-136: API - Refactor - Agregar impuestos prorrateables

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-08 09:42 |
| Actualizado | 2024-09-04 11:15 |
| Etiquetas | ninguna |
| Jira | [COM-136](https://bluinc.atlassian.net/browse/COM-136) |

## Relaciones

- **Padre:** [[COM-38]] Ver orden de compra

## Descripcion

Le agregaremos al objeto providerOrder un nuevo objeto que tiene su propoa tabla llamado `distributeTaxes`. Se trata de un objeto par albergar los impuestos prorratebles

```

  
  {
    "response": {
        "orderNumber": 11202,
        "providerId": "000982",
        "providerName": "Vilus Technology Co Ltd",
        "observation": "",
        "status": "P",
        "voucherPurchaseId": "",
        "buyerName": "Web Sistema",
        "buyerId": 12,
        "currencyQuote": 927,
        "distributeTaxes": [  <<<<<-----------------NUEVO
              {
              "acronym": "DDI",
              "description": "Derechos de importancion",
              "rate": 100.0,
              "taxBase": 895.18,
              "id": 2
              },
            {
              "acronym": "IB",
              "description": "Percepcion ingresos brutos",
              "rate": 6.0,
              "taxBase": 12525.34,
              "id": 1
              },              
          ],
        "items": [
            {
                "id": 6877,
                "title": "ACCESORIOS SENTEY CAJA DE TECLADO [[GS-1501]]",
                "sku": "",
                "price": {
                    "value": 0,
                    "iva": 21,
                    "finalPrice": 0
                },
                "warranty": "12 meses",
                "amount": 10,
                "position": "8471.60.52.000H",
                "taxPosition": {
                    "aec": 10,
                    "die": 17,
                    "iibb": 11,
                    "iva": 12,
                    "ivaAd": 13,
                    "ganancias": 14,
                    "te": 15,
                    "dii": 16
                },
                "amountEntered": null,
                "partialIncome": 0
            }
        ]
    }
}
```

```
GET {API_URL}/v1/providerOrder/{providerOrderId}
```

La tabla que crearemos es `[NewBytes_DBF].[dbo].[pedproi]` para continuar la misma lógica.

RECOMENDADO ver esta tabla que contiene algo muy similar pero para las facturas de compra (un paso posterior que seguro despues lo terminamos empalmando como  paso final para este) `[NewBytes_DBF].[dbo].[FACPROI]`
