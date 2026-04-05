---
jira_key: "PED-1089"
aliases: ["PED-1089"]
summary: "API - Feat - Recurso de eficiencia logística por CP y transportista"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-08-22 18:04"
updated: "2025-08-29 10:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1089"
---

# PED-1089: API - Feat - Recurso de eficiencia logística por CP y transportista

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-08-22 18:04 |
| Actualizado | 2025-08-29 10:21 |
| Etiquetas | ninguna |
| Jira | [PED-1089](https://bluinc.atlassian.net/browse/PED-1089) |

## Relaciones

- **Padre:** [[PED-1068]] Periodos logisticos
- **has action item:** [[PED-1091]] APP - Feat - Eficiencia logística por zona

## Descripcion

Se implementará un recurso que permita la visualización clara de qué transportista resulta más eficiente según la provincia, mostrando los códigos postales en los que se hayan realizado envíos.

El objetivo es que el sistema muestre de forma sencilla cuál es el transportista más eficiente en cada zona, tomando como referencia:

- La **cantidad de pedidos enviados**.


- El **tiempo promedio de entrega**.



De esta manera, se contará con una herramienta que facilite el análisis y comparación del desempeño logístico por provincia y código postal.


```
GET /v1/statistics/logisticPerformance/heatmap
```

Ejemplos de fitlrado.

```
GET /statistics/logisticPerformance/heatmap?provinceId=7&minDeliveries=10&carrierId=4065
```

response:

```json
{
    "data": [
        {
            "postalCode": 3220,
            "province": "Corrientes",
            "carriers": [
                {
                    "name": "OCA",
                    "time": null,
                    "deliveries": null
                },
                {
                    "name": "Andreani",
                    "time": 4.9,
                    "deliveries": 25
                },
                {
                    "name": "Entregar",
                    "time": null,
                    "deliveries": null
                }
            ],
            "bestOption": {
                "name": "Andreani",
                "time": 4.9
            }
        },
        {
            "postalCode": 3400,
            "province": "Corrientes",
            "carriers": [
                {
                    "name": "OCA",
                    "time": null,
                    "deliveries": null
                },
                {
                    "name": "Andreani",
                    "time": 6.1,
                    "deliveries": 27
                },
                {
                    "name": "Entregar",
                    "time": null,
                    "deliveries": null
                }
            ],
            "bestOption": {
                "name": "Andreani",
                "time": 6.1
            }
        },
        {
            "postalCode": 3450,
            "province": "Corrientes",
            "carriers": [
                {
                    "name": "OCA",
                    "time": null,
                    "deliveries": null
                },
                {
                    "name": "Andreani",
                    "time": 6,
                    "deliveries": 33
                },
                {
                    "name": "Entregar",
                    "time": null,
                    "deliveries": null
                }
            ],
            "bestOption": {
                "name": "Andreani",
                "time": 6
            }
        }
    ],
    "pagination": {
        "total": 3,
        "current": 1,
        "pageSize": 15
    }
}
```



Esta imagen es un ejemplo para reforzar la idea, no es necesario que deba ser asi.

[adjunto]
