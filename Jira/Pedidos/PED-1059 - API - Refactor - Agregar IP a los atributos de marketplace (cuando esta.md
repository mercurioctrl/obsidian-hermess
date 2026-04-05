---
jira_key: "PED-1059"
aliases: ["PED-1059"]
summary: "API - Refactor - Agregar IP a los atributos de marketplace (cuando esta disponible)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-23 07:21"
updated: "2025-08-05 19:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1059"
---

# PED-1059: API - Refactor - Agregar IP a los atributos de marketplace (cuando esta disponible)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-23 07:21 |
| Actualizado | 2025-08-05 19:20 |
| Etiquetas | ninguna |
| Jira | [PED-1059](https://bluinc.atlassian.net/browse/PED-1059) |

## Relaciones

- **Padre:** [[PED-724 - Modal Venta Market Place LO|PED-724]] Modal "Venta Market Place LO"

## Descripcion

```
GET {API_URL}/v1/aboutMarketPlace/{branch-order}
```

```
{
    "success": true,
    "data": {
        "document": "44439904",
        "idLo": 741394,
        "creationDate": "22\/07\/2025",
        "currencyQuote": 1280,
        "resellerOrderId": 739419,
        "resellerDescription": "Gears Store",
        "resellerPhone": "3425949841",
        "order": "10420342",
        "cnumalb": null,
        "branch": null,
        "shippingAddressLo": "{\"Nombre del que recibe\":\"Roman Corales\",\"Direcci\\u00f3n\":\"Sarmiento 2810,  ,  CP: 3260, CONCEPCION DEL URUGUAY        , ENTRE RIOS\",\"C\\u00f3digo Postal\":\"3260\"}",
        "direccionEnvioLo": "Sarmiento 2810,  ,  CP: 3260, CONCEPCION DEL URUGUAY        , ENTRE RIOS",
        "shippingPostalCodeLo": "3260",
        "clientDescriptionLo": "Roman Corales",
        "clientEmailLo": "romancorales202@gmail.com",
        "clientPhoneLo": "3442672522",
        "deliveryNameLo": "OCA                                               ",
        "paymentMethodDescriptionLo": "Transferencia",
        "placeIdLo": 4885,
        "provinceIdLo": 5,
        "deliveryDescriptionLo": "A domicilio por OCA",
        "specialDiscountLo": 0,
        "shippingCost": 0,
        "interestRate": 0,
        "ipOrigin": "181.87.129.137", <--- SE AGREGA
        "items": [
            {
                "distributorId": 1,
                "detailIdLo": 779441,
                "productIdLo": 731007,
                "resellerOrderId": 739419,
                "priceLo": 59794,
                "discountLo": 0,
                "clientCostLo": 37.85,
                "utilityLo": 2,
                "iva": 21,
                "amountLo": 1,
                "descriptionLo": "FUENTE GAMER GIGABYTE 550W 80 PLUS SILVER ATX 3.0",
                "itemId": 119726,
                "refundLo": 0
            }
        ]
    }
}
```
