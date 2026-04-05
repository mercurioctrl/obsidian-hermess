---
jira_key: "PED-292"
aliases: ["PED-292"]
summary: "API - Feat - Obtener subtotales de comisiones agrupados por listas de precios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-01 10:11"
updated: "2023-12-11 07:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-292"
---

# PED-292: API - Feat - Obtener subtotales de comisiones agrupados por listas de precios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-01 10:11 |
| Actualizado | 2023-12-11 07:25 |
| Etiquetas | ninguna |
| Jira | [PED-292](https://bluinc.atlassian.net/browse/PED-292) |

## Relaciones

- **Padre:** [[PED-242]] Pestaña Estadisticas
- **blocks:** [[PED-293]] APP - Feat - Mostrar lista de comisiones (Agrupado por letra) y un grafico de torta que las represente

## Descripcion

Basándonos en los mismos repositorios de informacion que utilizamos en [link](https://lioteam.atlassian.net/browse/PED-175) 

Crearemos un recurso que nos sirva para obtener las comisiones de un vendedor determinado, pero segmentadas por lista de precio.

```
GET {API_URL}/statistics/groupedCommision?clientId={clientId}&sellerId{sellerId}&dateInterval={intervalo de fechas}&brandId={marca}&categoryId={categoria}
```

Retornaremos entonces el siguiente objeto

```
{
    "applied_filters": {
        "clientId": null,
        "sellerId": null,
        "between": "2-10-2023_1-11-2023",
        "category": null,
        "period": "0 Mes"
    },
    "commisions":[
    "A": {
        "subtotal": 632,
        "count": 13769
    },
   "B": {
        "subtotal": 632,
        "count": 13769
    },
    "C": {
        "subtotal": 632,
        "count": 13769
    },
    "D": {
        "subtotal": 632,
        "count": 13769
    },
    "E": {
        "subtotal": 632,
        "count": 13769
    }, 
    ]
}
```
