---
jira_key: "NBWEB-63"
summary: "Mas Vendidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-03-29 18:06"
updated: "2022-06-25 17:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-63"
---

# NBWEB-63: Mas Vendidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-29 18:06 |
| Actualizado | 2022-06-25 17:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-63](https://bluinc.atlassian.net/browse/NBWEB-63) |

## Descripción

```
GET {{API_URL}}/v1/?mas_vendidos=1
```



Retorna:



```json
[
    {
        "title": "MINI PC GIGABYTE BAREBONE H310M STX",
        "sku": "GA-H310MSTX-HD3-CM",
        "id": 103615,
        "category": "COMPUTADORAS",
        "categoryId": 31,
        "brand": "GIGABYTE",
        "brandId": 4,
        "imagenPrincipal": "GIGABYTE.jpg",
        "initialB": 0,
        "initialC": 0,
        "stock": "Alto",
        "price": {
            "value": 213.79914,
            "iva": 10.5,
            "finalPrice": 236.2480497
        }
    },
    {
        "title": "MINI PC GIGABYTE BAREBONE H110M STX",
        "sku": "GA-H110MSTX-HD3-ZK",
        "id": 101161,
        "category": "COMPUTADORAS",
        "categoryId": 31,
        "brand": "GIGABYTE",
        "brandId": 4,
        "imagenPrincipal": "GIGABYTE.jpg",
        "initialB": 0,
        "initialC": 0,
        "stock": "Alto",
        "price": {
            "value": 164.5239024,
            "iva": 10.5,
            "finalPrice": 181.798912152
        }
    },
    {
        "title": "MONITOR BENQ LED 22 L GW2283 BLACK",
        "sku": "9H.LHLLA.TBL",
        "id": 109164,
        "category": "MONITORES",
        "categoryId": 7,
        "brand": "BENQ",
        "brandId": 40,
        "imagenPrincipal": "BenQ.jpg",
        "initialB": 3,
        "initialC": 5,
        "stock": "Sin stock",
        "price": {
            "value": 153.95690394,
            "iva": 21,
            "finalPrice": 186.28785376739998
        }
    },
    {
        "title": "MONITOR BENQ LED 22 GW2283 BLACK",
        "sku": "9H.LHLLA.TBR",
        "id": 104917,
        "category": "MONITORES",
        "categoryId": 7,
        "brand": "BENQ",
        "brandId": 40,
        "imagenPrincipal": "BenQ.jpg",
        "initialB": 3,
        "initialC": 5,
        "stock": "Sin stock",
        "price": {
            "value": 153.95633496000002,
            "iva": 21,
            "finalPrice": 186.28716530160003
        }
    },
    {
        "title": "MONITOR BENQ LED 22 GW2280 HDMI BLACK",
        "sku": "9H.LH4LA.TBL",
        "id": 103132,
        "category": "MONITORES",
        "categoryId": 7,
        "brand": "BENQ",
        "brandId": 40,
        "imagenPrincipal": "BenQ.jpg",
        "initialB": 3,
        "initialC": 5,
        "stock": "Sin stock",
        "price": {
            "value": 143.313309,
            "iva": 21,
            "finalPrice": 173.40910389
        }
    },
    {
        "title": "OUTLET MONITOR BENQ LED 22 GW2280 HDMI BLACK",
        "sku": "O9H.LH4LA.TBR",
        "id": 108624,
        "category": "MONITORES",
        "categoryId": 7,
        "brand": "BENQ",
        "brandId": 40,
        "imagenPrincipal": "BenQ.jpg",
        "initialB": 3,
        "initialC": 5,
        "stock": "Sin stock",
        "price": {
            "value": 114.444441,
            "iva": 21,
            "finalPrice": 138.47777360999999
        }
    },
    {
        "title": "DISCO HDD WD S 1 TB S-ATA3 BLUE",
        "sku": "WD10EZEX",
        "id": 3574,
        "category": "DISCOS HDD",
        "categoryId": 2,
        "brand": "WD",
        "brandId": 62,
        "imagenPrincipal": "WDIGITAL.jpg",
        "initialB": 3,
        "initialC": 5,
        "stock": "Sin stock",
        "price": {
            "value": 57.89396025,
            "iva": 10.5,
            "finalPrice": 63.97282607625
        }
    },
    {
        "title": "DISCO HDD WD S 1 TB S-ATA3 RECERTIFIED",
        "sku": "WD10EZEX-R",
        "id": 102306,
        "category": "DISCOS HDD",
        "categoryId": 2,
        "brand": "WD",
        "brandId": 62,
        "imagenPrincipal": "WDIGITAL.jpg",
        "initialB": 3,
        "initialC": 5,
        "stock": "Sin stock",
        "price": {
            "value": 48.05891532,
            "iva": 10.5,
            "finalPrice": 53.105101428599994
        }
    },
    {
        "title": "OUTLET DISCO HDD WD 1 TB S-ATA3 RECERTIFIED",
        "sku": "OWD10EZEX-R",
        "id": 108633,
        "category": "DISCOS HDD",
        "categoryId": 2,
        "brand": "WD",
        "brandId": 62,
        "imagenPrincipal": "WDIGITAL.jpg",
        "initialB": 3,
        "initialC": 5,
        "stock": "Sin stock",
        "price": {
            "value": 40.5796536,
            "iva": 10.5,
            "finalPrice": 44.840517228
        }
    },
    {
        "title": "OUTLET DISCO HDD WD S 1 TB S-ATA3 BLUE",
        "sku": "OWD10EZEX",
        "id": 108632,
        "category": "DISCOS HDD",
        "categoryId": 2,
        "brand": "WD",
        "brandId": 62,
        "imagenPrincipal": "WDIGITAL.jpg",
        "initialB": 3,
        "initialC": 5,
        "stock": "Sin stock",
        "price": {
            "value": 32.6414016,
            "iva": 10.5,
            "finalPrice": 36.068748768
        }
    }
]
```
