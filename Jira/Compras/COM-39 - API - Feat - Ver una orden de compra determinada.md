---
jira_key: "COM-39"
aliases: ["COM-39"]
summary: "API - Feat - Ver una orden de compra determinada"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-16 14:32"
updated: "2025-11-20 14:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-39"
---

# COM-39: API - Feat - Ver una orden de compra determinada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-16 14:32 |
| Actualizado | 2025-11-20 14:56 |
| Etiquetas | ninguna |
| Jira | [COM-39](https://bluinc.atlassian.net/browse/COM-39) |

## Relaciones

- **Padre:** [[COM-38 - Ver orden de compra|COM-38]] Ver orden de compra
- **relates to:** [[COM-252 - API -MVP - Refactor - Detalle de la orden - Agregar costo promedio ponderado|COM-252]] API -MVP - Refactor - Detalle de la orden -> Agregar costo promedio ponderado

## Descripcion

Crearemos el recurso encargado de listar el detalle de un orden de compra

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
