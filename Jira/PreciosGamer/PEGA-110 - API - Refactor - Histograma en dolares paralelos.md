---
jira_key: "PEGA-110"
aliases: ["PEGA-110"]
summary: "API - Refactor - Histograma en dolares paralelos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-12 09:36"
updated: "2024-09-20 06:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-110"
---

# PEGA-110: API - Refactor - Histograma en dolares paralelos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-12 09:36 |
| Actualizado | 2024-09-20 06:23 |
| Etiquetas | ninguna |
| Jira | [PEGA-110](https://bluinc.atlassian.net/browse/PEGA-110) |

## Relaciones

- **Padre:** [[PEGA-7 - Feat - Detalle del producto (Ficha)|PEGA-7]] Feat - Detalle del producto (Ficha)
- **blocks:** [[PEGA-117 - APP - Refactor - Hisotograma de dolar oficial paralelo|PEGA-117]] APP - Refactor - Hisotograma de dolar oficial / paralelo 

## Descripcion

Agregaremos al histograma la posibilidad de medir cada momento al dolar paralelo de ese momento

```
GET {API_URL}/v1/itemDetail/{itemId}
```

```
{
    "id": 19605,
    "resellerId": 1093,
    "resellerDescription": "Mercado libre",
    "brandId": 11756,
    "brandDescription": "Noga",
    "description": "Reloj Inteligente Smartwatch Noga Sw04 Presion Ip67 Unisex Color De La Malla Verde",
    "currentPrice": 11999,
    "lastPrice": 12490,
    "percentage": -3.93,
    "destinyUrl": "https:\/\/articulo.mercadolibre.com.ar\/MLA-1651033318-reloj-inteligente-smartwatch-noga-sw04-presion-ip67-unisex-color-de-la-malla-verde-_JM",
    "defaultImgUrl": "http:\/\/http2.mlstatic.com\/D_779705-MLU74974702912_032024-F.jpg",
    "histogram": {
        "date": [
            "12-08-24",
            "13-08-24",
            "19-08-24",
            "20-08-24"
        ],
        "price": [
            12490,
            12490,
            12490,
            12490,
        ],
        "priceUsd": [
            124.90,
            124.90,
            124.90,
            124.90,
        ],        
        "maxValue": 13114.5,
        "minValue": 9962.706999999999
    }
}
```
