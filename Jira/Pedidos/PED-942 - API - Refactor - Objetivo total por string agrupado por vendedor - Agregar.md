---
jira_key: "PED-942"
aliases: ["PED-942"]
summary: "API - Refactor - Objetivo total por string agrupado por vendedor -> Agregar \"monto por unidad vendida\" y parámetro \"mostrar\""
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-04 10:02"
updated: "2025-02-05 17:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-942"
---

# PED-942: API - Refactor - Objetivo total por string agrupado por vendedor -> Agregar "monto por unidad vendida" y parámetro "mostrar"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-04 10:02 |
| Actualizado | 2025-02-05 17:35 |
| Etiquetas | ninguna |
| Jira | [PED-942](https://bluinc.atlassian.net/browse/PED-942) |

## Relaciones

- **Padre:** [[PED-299]] Objetivos y Desafios
- **relates to:** [[PED-897]] API - Feat - Objetivo total por string agrupado por vendedor
- **has action item:** [[PED-943]] APP - Refactor - Objetivo total por string agrupado por vendedor -> Agregar "monto por unidad vendida" y parámetro "mostrar"
- **has action item:** [[MKT-245]] NB_ INCENTIVO FUERZA DE VENTAS

## Descripcion

Refactorizaremos el recurso de “totales por match” para poder hacerlo flexible para abarcar tambien este tipo de acciones dentro del mismo criterio: [link](https://lioteam.atlassian.net/browse/MKT-245) 

```
GET {{API_URL}}/v1/objectives/TotalSaleBymatch?goalId={goalId}&show={show}
```

Para esto haremos lo siguientes.

## Nuevos parámetros en la tabla `[NewBytes_DBF].[dbo].[dynamicGoalsSellers]`

- `Show`(0|1) - Agregaremos el parámetro para decidir cuando mostrar y no la acción (si bien podríamos tomar la fecha, a veces queresa dejar un tiempo como finalizo la actividad)


- `paymentPerUnit`(float | NULL) - Representa que monto se paga por unidad vendida, puede ser NULL o no depende si la acción contempla este tipo de pago.



## Refactor del recurso

Agregaremos a la query la capacidad de contar cuantas unidades que “matchearon” tenemos vendidas

```
...
    , DGS.startDate
    , DGS.endDate
    , DGS.rewardDescription
    , DGS.paymentPerUnit
    , COUNT(PD.ncanped) as unitsSold <<--- SE AGREGA
FROM [NewBytes_DBF].[dbo].[pedclil] PD
LEFT JOIN NewBytes_DBF.dbo.articulo A
    ON A.ID_ARTICULO = PD.ID_Articulo
LEFT JOIN NewBytes_DBF.dbo.pedclit PC
    ON PC.cnumped = PD.cnumped
        AND PC.cnumsuc = PD.cnumsuc
...        
```

##  ¿Como quedaría nuestro objeto?

```
[
    {
        "sellerId": 8,
        "sellerDescription": "Altamiranda Andrea",
        "amount": 48537.48428,
        "targetAmount": 16000,
        "goalId": 1,
        "keywords": "PATRIOT",
        "startDate": "2024-12-10 00:00:00",
        "endDate": "2024-12-20 23:59:00",
        "rewardDescription": "Gana u$s100 al cumplir tu objetivo.",
        "unitsSold": 45,
        "paymentPerUnit": 10.00,
    },
    {
        "sellerId": 30,
        "sellerDescription": "Albarracin Julian",
        "amount": 15441.77237,
        "targetAmount": 8000,
        "goalId": 1,
        "keywords": "PATRIOT",
        "startDate": "2024-12-10 00:00:00",
        "endDate": "2024-12-20 23:59:00",
        "rewardDescription": "Gana u$s100 al cumplir tu objetivo.",
        "unitsSold": 15,
        "paymentPerUnit": 10.00,
    },

...
```
