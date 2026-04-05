---
jira_key: "PED-621"
aliases: ["PED-621"]
summary: "API - Obtener información de como se genero una orden en Marketplace (LO) - Sugerencias de mejora en el objeto"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-03-20 09:04"
updated: "2024-05-30 18:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-621"
---

# PED-621: API - Obtener información de como se genero una orden en Marketplace (LO) - Sugerencias de mejora en el objeto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-20 09:04 |
| Actualizado | 2024-05-30 18:20 |
| Etiquetas | ninguna |
| Jira | [PED-621](https://bluinc.atlassian.net/browse/PED-621) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **relates to:** [[PED-725]] API - Feat - Recurso para obtener la informacion completa tal como se genero en el market place (LO)

## Descripcion

Con base en el objeto de respuesta obtuve algunos  nombres de claves y valores de los que me gustaría sugerir un par de mejoras, adicional te dejo abajo el objeto de respuesta para más detalles.

- `clave actual` →   sugerencia clave y/o sugerencia en el valor



- `idResellerOrderId` → `resellerOrderId`


- `deliveryInfoLo` → Cuando no tenga envío devolver nulo y me parece que se repiten los datos


- `direccionEnvioLo` → `shippingAddressLo` y me parece que se repiten los datos


- `codigoPostalEnvioLo` → `shippingPostalCodeLo`


- `mailClientLo` → `clientEmailLo`


- `deliveryNameLo` → `deliveryDescriptionLo` y quitar espacios en el valor


- `paymentNameLo` → `paymentMethodDescriptionLo` y quitar espacios en el valor


- `intterestRate` → `interestRate`


- `idDistribuidora` → `distributorId`


- `detailIdLo` → `idLoDetail`


- `productoIDLo` → `productIdLo`


- `orderResellerID` → `resellerOrderId`


- `resellerName` → `resellerDescription`


- `clientNameLo` → `clientDescriptionLo` 


- `costoEnvio` → `shippingCost`





```
{
    "success": true,
    "data": {
        "document": "01234567",
        "idLo": 579705,
        "creationDate": "02/05/2024",
        "currencyQuote": 880,
        "idResellerOrderId": 570123,
        "resellerName": "Fullh4rd",
        "order": "10332782",
        "cnumalb": "00569134",
        "branch": "0002",
        "deliveryInfoLo":"{\"Nombre del que recibe\":\"Gprueba Guillermo\",\"Direcci\ón\":\"A la vuelta Cerca, 2 Departamento, Departamento CP: 1200, CABA, CABA\",\"C\ódigo Postal\":\"1200\"}",
        "direccionEnvioLo": "A la vuelta Cerca, 2 Departamento, Departamento CP: 1200, CABA, CABA",
        "codigoPostalEnvioLo": "1200",
        "clientNameLo": "Gprueba Guillermo",
        "mailClientLo": "gavila@nb.com.ar",
        "clientPhoneLo": "4426022591",
        "deliveryNameLo": "Entregar                                          ",
        "paymentNameLo": "Transferencia                                     ",
        "placeIdLo": 57,
        "provinceIdLo": 3,
        "deliveryDescriptionLo": "Entregar a domicilio",
        "specialDiscountLo": 0,
        "costoEnvio": 2802,
        "intterestRate": 0,
        "items": [
            {
                "idDistribuidora": 1,
                "detailIdLo": 588223,
                "productoIDLo": 685451,
                "orderResellerID": 570123,
                "priceLo": 16720,
                "discountLo": 0,
                "clientCostLo": 14.54,
                "utilityLo": 8,
                "iva": 21,
                "amountLo": 1,
                "descriptionLo": "ASPEN BALANZA DIGITAL PERSONAL B010",
                "itemId": 117345,
                "refundLo": 0
            }
        ]
    }
}
```
