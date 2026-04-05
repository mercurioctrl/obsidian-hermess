---
jira_key: "PEGA-125"
aliases: ["PEGA-125"]
summary: "API - Refactor - Dividir en 3 recursos el detalle del producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2024-09-25 15:14"
updated: "2024-10-01 17:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-125"
---

# PEGA-125: API - Refactor - Dividir en 3 recursos el detalle del producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2024-09-25 15:14 |
| Actualizado | 2024-10-01 17:08 |
| Etiquetas | ninguna |
| Jira | [PEGA-125](https://bluinc.atlassian.net/browse/PEGA-125) |

## Relaciones

- **Padre:** [[PEGA-7 - Feat - Detalle del producto (Ficha)|PEGA-7]] Feat - Detalle del producto (Ficha)
- **blocks:** [[PEGA-126 - APP - Refactor - Dividir en 3 recursos el detalle del producto|PEGA-126]] APP - Refactor - Dividir en 3 recursos el detalle del producto

## Descripcion

Ficha:
`GET itemDetail/${id}`

```
{
    "id": 34481,
    "resellerId": 1079,
    "resellerDescription": "Space",
    "brandId": 11656,
    "brandDescription": "Asus",
    "description": "WATER COOLER ASUS ROG STRIX LC II 280 ARGB",
    "currentPrice": 319994,
    "lastPrice": 1176600,
    "percentage": -72.8,
    "destinyUrl": "https://spacegamer.com.ar/314276-componentes-de-pc-asus-water-cooler-rog-strix-lc-ii-280-argb?utm_source=hardgamers&utm_medium=search%20engine ",
    "defaultImgUrl": "https://spacegamer.com.ar/img/Public/1058-producto-1019-producto-water-cooler-asus-rog-strix-lc-ii-280-argb-1-3108-293.jpg",
    
}
```


HIstograma de precios:
`GET itemDetail/${id}/histogram/prices?signature=ars,usdOfficial,ripte,usd` 

```
"histogram": {
        "date": [
            "28-05-24",
            "30-05-24",
            "31-05-24",
            "03-06-24",
            "05-06-24",
            "07-06-24",
            "10-06-24",
            "11-06-24",
            "12-06-24",
            "13-06-24",
            "14-06-24",
            "15-06-24",
            "21-06-24"
        ],
        "price": [
            1157520,
            1163880,
            1163880,
            1163880,
            1170240,
            1170240,
            1170240,
            1170240,
            1176600,
            1176600,
            1176600,
            1176600,
            319994
        ],
        "maxValue": 1235430,
        "minValue": 303994.3,
        "priceUsd": [
            980.95,
            969.9,
            973.96,
            965.88,
            959.21,
            947.56,
            936.19,
            925.09,
            937.53,
            968.4,
            941.28,
            888,
            251.96
        ],
        "maxValueDollar": 1030,
        "minValueDollar": 239.36,
        "priceUsdOfficial": [
            1319.86,
            1327.12,
            1327.12,
            1324.1,
            1329.82,
            1328.31,
            1325.3,
            1323.8,
            1331,
            1331,
            1331,
            1274.76,
            360.76
        ],
        "maxValueDollarOfficial": 1397.55,
        "minValueDollarOfficial": 342.72,
        "priceRipte": [
            4.26,
            4.29,
            4.29,
            4.29,
            4.31,
            4.31,
            4.31,
            4.31,
            4.33,
            4.33,
            4.33,
            4.33,
            1.18
        ],
        "maxValueRipte": 4.55,
        "minValueRipte": 1.12
    }
```


Histograma de cotizaciones:
`GET itemDetail/${id}/histogram/quotes`
