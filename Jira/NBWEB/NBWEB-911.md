---
jira_key: "NBWEB-911"
summary: "API - Refactor - Agregar InternalTax al listado general"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-04 17:22"
updated: "2024-11-06 02:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-911"
---

# NBWEB-911: API - Refactor - Agregar InternalTax al listado general

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-04 17:22 |
| Actualizado | 2024-11-06 02:12 |
| Etiquetas | ninguna |
| Jira | [NBWEB-911](https://bluinc.atlassian.net/browse/NBWEB-911) |

## Descripción

```
GET {API_URL}/v1
```

```
[
    {
        "title": "PROCESADOR INTEL (1151) CORE I3 9300 3.7 GHZ",
        "sku": "BX80684I39300",
        "id": 109749,
        "category": "PROCESADORES",
        "categoryId": 3,
        "brand": "INTEL",
        "brandId": 39,
        "mainImage": "https:\/\/static.nb.com.ar\/i\/nb_PROCESADOR-INTEL-(1151)-CORE-I3-9300-3.7-GHZ_ver_fe18c2cafa3c0ad7a6d5d87a18b83961.jpeg",
        "mainImageExp": "https:\/\/static.nb.com.ar\/i\/nb_PROCESADOR-INTEL-(1151)-CORE-I3-9300-3.7-GHZ_export_fe18c2cafa3c0ad7a6d5d87a18b83961.jpeg",
        "brandImage": "https:\/\/static.nb.com.ar\/img\/6d79b2f278033128dd6ec7f481332a46.png",
        "initialB": 5,
        "initialC": 10,
        "stock": "Sin stock",
        "amountInCart": 0,
        "amountStock": 0,
        "categoryIdUser": null,
        "categoryDescriptionUser": null,
        "utility": null,
        "highAverage": 70,
        "widthAverage": 70,
        "lengthAverage": 50,
        "weightAverage": 500,
        "titleUser": null,
        "price": {
            "value": 311.32951,
            "iva": 10.5,
            "internalTax": 23.34, <- NUEVO PARAMETRO
            "finalPrice": 344.01910855000006, <- INCLUIR EN EL TOTAL
            "percepcion": null,
            "finalPriceWithUtility": 344.01911,
            "ncostoextra": 0
        },
        "warranty": "36 meses",
        "cotizacion": 1013
    },
    {
        "title": "PROCESADOR INTEL (1151) CORE I7 9700 3.0 GHZ",
        "sku": "BX80684I79700",
        "id": 109574,
        
        ...
```
