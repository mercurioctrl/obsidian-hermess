---
jira_key: "PED-897"
aliases: ["PED-897"]
summary: "API - Feat - Objetivo total por string agrupado por vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-11 14:22"
updated: "2025-02-04 10:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-897"
---

# PED-897: API - Feat - Objetivo total por string agrupado por vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-11 14:22 |
| Actualizado | 2025-02-04 10:03 |
| Etiquetas | ninguna |
| Jira | [PED-897](https://bluinc.atlassian.net/browse/PED-897) |

## Relaciones

- **Padre:** [[PED-299 - Objetivos y Desafios|PED-299]] Objetivos y Desafios
- **has action item:** [[PED-898 - APP - Feat - Objetivo por sting agrupado por vendedor|PED-898]] APP - Feat - Objetivo por sting agrupado por vendedor
- **has action item:** [[MKT-240 - NB_ PATRIOT INCENTIVO|MKT-240]] NB_ PATRIOT INCENTIVO
- **relates to:** [[PED-942 - API - Refactor - Objetivo total por string agrupado por vendedor - Agregar|PED-942]] API - Refactor - Objetivo total por string agrupado por vendedor -> Agregar "monto por unidad vendida" y parámetro "mostrar"

## Descripcion

Crearemos un recurso que nos permita crear objetivos mas dinamicos a partir de un match o coincidencia y una tabla suplementaria llamada 
`NewBytes_DBF.dbo.dynamicGoalsSellers`

**Con las siguientes columnas:**

- id


- sellerId


- targetAmount


- keywords


- startDate


- endDate


- goalId



```
GET {{API_URL}}/v1/objectives/TotalSaleBymatch?goalId=3
```

```sql
SELECT V.ID_VENDEDOR, capeage, cnbrage, SUM (PD.npreunit*PD.ncanped) AS TOTAL
  FROM [NewBytes_DBF].[dbo].[pedclil] PD
  LEFT JOIN NewBytes_DBF.dbo.articulo A ON A.ID_ARTICULO = PD.ID_Articulo
  LEFT JOIN NewBytes_DBF.dbo.pedclit PC ON PC.cnumped = PD.cnumped AND PC.cnumsuc = PD.cnumsuc
  LEFT JOIN NewBytes_DBF.dbo.agentes V ON V.ID_VENDEDOR = PC.ID_VENDEDOR 
WHERE A.cDetalle like '%PATRIOT%' {keyword} 
AND PC.dfecped BETWEEN '10-12-2024 00:00' {start} AND '20-12-2024 23:59' {enddate}
GROUP BY V.ID_VENDEDOR, capeage, cnbrage
ORDER BY SUM (PD.npreunit*PD.ncanped) DESC
```

Retorno

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
"amount": 5000.65
}
...
]
```
