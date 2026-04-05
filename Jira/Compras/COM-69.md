---
jira_key: "COM-69"
summary: "API - Refactor - Agregar a el objeto del detalle de la orden la posicion arancelaria y sus impuestos "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-03-08 08:20"
updated: "2024-03-25 02:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-69"
---

# COM-69: API - Refactor - Agregar a el objeto del detalle de la orden la posicion arancelaria y sus impuestos 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-08 08:20 |
| Actualizado | 2024-03-25 02:49 |
| Etiquetas | ninguna |
| Jira | [COM-69](https://bluinc.atlassian.net/browse/COM-69) |

## Descripción

Agregaremos en el recurso 

```
GET {API_URL}/v1/providerOrder/338834
```

Dentro del array `items` un parametro para la posicion arancelaria y a su vez todos los valores referidos a los impuestos ligados a esa posicion arancelaria. Cuando no estan, se devuelve cero.

```
{
    "providerOrder": "338834",
    "providerName": "OLMEDO GUSTAVO JAVIER",
    "providerId": 36839,
    "observation": null,
    "status": "P",
    "voucherPurchseId": null,
    "buyer": "Albarracin",
    "buyerId": "30",
    "currencyQuote": 850,
    "items": [
        {
            "title": "MOTHER ASROCK (LGA1700) H610M-HDV",
            "sku": "MB-H610M-HDV",
            "id": 117720,
            "price": {
                "value": 124.3928,
                "iva": 10.5,
                "finalPrice": 137.45404399999998
            },
            "warranty": "36 meses",
            "amount": 1
        },
        {
            "title": "DISCO SSD PATRIOT BURST ELITE SOLID 120 GB SATA3 PE000775",
            "sku": "PBE120GS25SSDR",
            "id": 109489,
            "price": {
                "value": 22.12688,
                "iva": 10.5,
                "finalPrice": 24.4502024,
            },
            "warranty": "12 meses",
            "amount": 1
        }
    ]
}
```

Consulta orientadora (cualquier cosa me preguntas)

```
SELECT 
pedprol.cref,
pedprol.cdetalle,
ncanped,
nprediv,
ndto,
ivaCompra,
... (info extra en la tabla articulos)
FROM NewBytes_DBF.dbo.pedprol
LEFT JOIN NewBytes_DBF.dbo.articulo ON pedprol.cRef = articulo.cref
WHERE nnumped =10830
```
