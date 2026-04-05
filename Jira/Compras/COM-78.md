---
jira_key: "COM-78"
summary: "API - Refactor - Agregar unidades ingresadas al detalle de la ordende compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-04-04 06:07"
updated: "2024-04-21 19:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-78"
---

# COM-78: API - Refactor - Agregar unidades ingresadas al detalle de la ordende compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-04 06:07 |
| Actualizado | 2024-04-21 19:39 |
| Etiquetas | ninguna |
| Jira | [COM-78](https://bluinc.atlassian.net/browse/COM-78) |

## Descripción

Dado que debe ser posible ingresar a stock parcialmente mercadería lo que haremos sera agregar un parámetro para este fin. Para esto usaremos `[NewBytes_DBF].[dbo].[pedprol].nCanEnt`

```
GET {API_URL}/v1/providerOrder/338834

```

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
            "amount": 2,
            "amountEntered":1 <-- NUEVO PARAMETRO
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
            "amount": 2,
            "amountEntered": 0 <-- NUEVO PARAMETRO
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
ncanent,
nprediv,
ndto,
ivaCompra,
... (info extra en la tabla articulos)
FROM NewBytes_DBF.dbo.pedprol
LEFT JOIN NewBytes_DBF.dbo.articulo ON pedprol.cRef = articulo.cref
WHERE nnumped =10830
```
