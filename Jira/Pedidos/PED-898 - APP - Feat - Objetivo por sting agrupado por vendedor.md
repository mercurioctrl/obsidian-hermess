---
jira_key: "PED-898"
aliases: ["PED-898"]
summary: "APP - Feat - Objetivo por sting agrupado por vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-12-11 14:56"
updated: "2024-12-26 12:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-898"
---

# PED-898: APP - Feat - Objetivo por sting agrupado por vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-11 14:56 |
| Actualizado | 2024-12-26 12:49 |
| Etiquetas | ninguna |
| Jira | [PED-898](https://bluinc.atlassian.net/browse/PED-898) |

## Relaciones

- **Padre:** [[PED-299 - Objetivos y Desafios|PED-299]] Objetivos y Desafios
- **action item from:** [[PED-897 - API - Feat - Objetivo total por string agrupado por vendedor|PED-897]] API - Feat - Objetivo total por string agrupado por vendedor
- **has action item:** [[MKT-240 - NB_ PATRIOT INCENTIVO|MKT-240]] NB_ PATRIOT INCENTIVO

## Descripcion

Crearemos una tabla similar a esta 

[adjunto]
Donde recibimos el objeto de la dependencia [link](https://lioteam.atlassian.net/browse/PED-897) 

Similar a 

```
[
{
"sellerId":15,
"sellerDescription":'Andrea Altamiranda',
"keywords":"Patriot"
"startDate":"11-18-24 00:00",
"endDate":"11-29-24 23:59",
"targetAmount": 8000.00
"amount": 3000.45
},
{
"sellerId":18,
"sellerDescription":'Norberto Napolitano',
"keywords":"Patriot"
"startDate":"11-18-24 00:00",
"endDate":"11-29-24 23:59",
"targetAmount": 12000.00
"amount": 1000.65
}
...
]
```

Pero solo mostraremos una tabla del siguiente tipo

| **Ranking** | **Vendedor** | **Monto Objetivo** | **Monto alcanzado** | **Campaña** | **Vigencia** |
| --- | --- | --- | --- | --- | --- |
| 1 | 15 - Andrea Altamiranda | 8000 | 3000.45 | Patriot | `11-18-24 - 11-29-24 23:59` |
| 2 | 18 - Norberto Napolitano | 12000 | 1000.65 | Patriot | `11-18-24 - 11-29-24 23:59` |

Cuando Monto Alcanzado es >= a Monto Objetivo, ponemos la coronita

Al agregar esta tabla, ocultaremos 


[adjunto]
