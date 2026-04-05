---
jira_key: "PED-826"
aliases: ["PED-826"]
summary: "API - Refactor - Agregar al repositorio de productos, aquellos productos que tienen stock en postventa y cuanto stock tiene de manera correspondiente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-19 09:25"
updated: "2024-09-25 01:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-826"
---

# PED-826: API - Refactor - Agregar al repositorio de productos, aquellos productos que tienen stock en postventa y cuanto stock tiene de manera correspondiente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-19 09:25 |
| Actualizado | 2024-09-25 01:30 |
| Etiquetas | ninguna |
| Jira | [PED-826](https://bluinc.atlassian.net/browse/PED-826) |

## Relaciones

- **Padre:** [[PED-65]] Listado de productos
- **blocks:** [[PED-827]] APP - Refactor - Agregar stock de postventa
- **relates to:** [[PED-830]] API - Agregar articulo a orden - Stock de postventa no coincidente al agregar articulo 

## Descripcion

Como parte de los refactor que estuvimos hablando para lograr que armen el envío de postventa necesitamos tener un parámetro mas para el stock de postventa.

Agregaremos una NUEVO PARAMETRO llamado `stockAfterSale` que proviene de `[NewBytes_DBF].[dbo].[stocks].nstock_postventa`

```
GET {API_URL}/v1/items
```

```
{
    "response": [
        {
            "title": "MINI PC GIGABYTE BRIX [[BSRE-1505]] (AMD Ryzen 1505G)",
            "sku": "GB-BSRE-1505",
            "id": 116741,
            "category": "COMPUTADORAS",
            "categoryId": 31,
            "brand": "GIGABYTE",
            "brandId": 4,
            "mainImage": "https:\/\/static.nb.com.ar\/img\/cc931534c55dd0fe2ee6a3fa0aa4378f.jpeg",
            "brandImage": "https:\/\/static.nb.com.ar\/img\/f2aae2c829b051430eb6a039ad6bc7ae.jpg",
            "price": {
                "value": 375.3055,
                "iva": 10.5,
                "finalPrice": 414.7125775,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 554.0555,
                    "B": 543.5284455000001,
                    "C": 536.325724,
                    "D": 375.3055
                },
                "savedPriceList": "D",
                "currencyQuote": 982,
                "effectiveness": 15.480000000000004,
                "profit": 0
            },
            "warranty": "36 meses",
            "stock": 66,
            "stockLio": 0,
            "stockInOrders": 10,
            "availableStock": 56,
            "stockInMyOrder": 0,
            "stockAfterSale": 1, <<- NUEVO PARAMETRO
            "companyCode": 4
        },
        {
            "title": "OUTLET AMD ATHLON 5150 1.6 GHBOX",
            "sku": "O5150AMD",
            "id": 5199,
            "category": "OUTLET",
            "categoryId": 8,
            "brand": "AMD",
            "brandId": 43,
            "mainImage": "https:\/\/static.nb.com.ar\/img\/e51b37755db5fc014e72b5648cf38535.jpeg",
            "brandImage": "https:\/\/static.nb.com.ar\/img\/266f407b98b3c0721710b6c651d4108f.jpg",
            "price": {
                "value": 42.89957,
                "iva": 10.5,
                "finalPrice": 47.40402485,
                "percepcion": null,
                "letra": "D",
                "priceList": {
                    "A": 67.27884,
                    "B": 66.00054204,
                    "C": 65.12591712,
                    "D": 42.89957
                },
                "savedPriceList": "D",
                "currencyQuote": 982,
                "effectiveness": -12.019999999999996,
                "profit": 0
            },
            "warranty": "3 meses",
            "stock": 1,
            "stockLio": 0,
            "stockInOrders": 0,
            "availableStock": 1,
            "stockInMyOrder": 0,
            "stockAfterSale": 1, <<- NUEVO PARAMETRO
            "companyCode": 4
        },
        {
            "title": "PROCESADOR AMD (AM4) ATHLON 3000G",
            "sku": "YD3000C6FHSBX",
            "id": 118820,
            "category": "PROCESADORES",
            "categoryId": 3,
            "brand": "AMD",
            "brandId": 43,
            "mainImage": "https:\/\/static.nb.com.ar\/img\/847e39f4c80c83af68d18c34c2cdf672.jpg",
            "brandImage": "https:\/\/static.nb.com.ar\/img\/266f407b98b3c0721710b6c651d4108f.jpg",
            "price": {
                "value": 55.23683,
                "iva": 10.5,
                "finalPrice": 61.036697149999995,
                "percepcion": null,
```
