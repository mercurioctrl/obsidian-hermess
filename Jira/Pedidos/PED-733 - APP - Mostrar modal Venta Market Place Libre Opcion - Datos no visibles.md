---
jira_key: "PED-733"
aliases: ["PED-733"]
summary: "APP - Mostrar modal \"Venta Market Place: Libre Opcion\" - Datos no visibles"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-05-31 16:43"
updated: "2024-06-04 15:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-733"
---

# PED-733: APP - Mostrar modal "Venta Market Place: Libre Opcion" - Datos no visibles

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-31 16:43 |
| Actualizado | 2024-06-04 15:07 |
| Etiquetas | ninguna |
| Jira | [PED-733](https://bluinc.atlassian.net/browse/PED-733) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **blocks:** [[PED-726]] APP - Feat - Mostrar modal "Venta Market Place: Libre Opcion"

## Descripcion

Basándome en la imagen muestra que se compartió en la historia principal tengo un par de observaciones. 

1. No se visualizan los siguientes parámetros:

- `placeIdLo`


- `shippingCost`


- `interestRate`


- `detailIdLo`



[adjunto]
```
curl 'https://gamma.api.orders.lio.red/v1/aboutMarketPlace/0002-10332824' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTcxODU3NDYsImF1ZCI6IjRlNTM0ZGUxMWUwMDcxNjAyNzg2MWY3OWU3NzAzMzEyODlkMzkzOTkiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxNzE4MjE0NiwibmJmIjoxNzE3MTgyMTQ2fQ._gqdbp5vdxVnKv8gQ-DnxlLcmMtdS4q495n0AXtvpTo' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0' \
  -H 'sec-ch-ua: "Chromium";v="124", "Opera";v="110", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

```
{
    "success": true,
    "data": {
        "document": "01234567",
        "idLo": 580711,
        "creationDate": "28\/05\/2024",
        "currencyQuote": 880,
        "resellerOrderId": 571129,
        "resellerDescription": "Rm Insumos",
        "order": "10332824",
        "cnumalb": "00569153",
        "branch": "0002",
        "shippingAddressLo": "{\"Nombre del que recibe\":\"Gprueba Guillermo\",\"Direcci\\u00f3n\":\"\",\"C\\u00f3digo Postal\":\"\"}",
        "direccionEnvioLo": "",
        "shippingPostalCodeLo": "",
        "clientDescriptionLo": "Gprueba Guillermo",
        "clientEmailLo": "gavila@nb.com.ar",
        "clientPhoneLo": "4426022591",
        "deliveryNameLo": null,
        "paymentMethodDescriptionLo": "Efectivo",
        "placeIdLo": 57,
        "provinceIdLo": 3,
        "deliveryDescriptionLo": "Retiro",
        "specialDiscountLo": 0,
        "shippingCost": 0,
        "interestRate": 0,
        "items": [
            {
                "distributorId": 1,
                "detailIdLo": 589230,
                "productIdLo": 247762,
                "resellerOrderId": 571129,
                "priceLo": 87204,
                "discountLo": 0,
                "clientCostLo": 76,
                "utilityLo": 18,
                "iva": 10.5,
                "amountLo": 1,
                "descriptionLo": "GABINETE SFX RACKEABLE A4U450 SERVER SERVIDORES",
                "itemId": 101006,
                "refundLo": 0
            }
        ]
    }
```



3. No se visualiza el precio con descuento

4. ¿Crees que podamos hacer algo con estos espacios vacíos para cuando la orden no tenga medio de envío?

[adjunto]
