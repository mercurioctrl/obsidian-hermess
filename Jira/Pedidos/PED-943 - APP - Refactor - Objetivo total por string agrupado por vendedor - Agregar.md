---
jira_key: "PED-943"
aliases: ["PED-943"]
summary: "APP - Refactor - Objetivo total por string agrupado por vendedor -> Agregar \"monto por unidad vendida\" y parámetro \"mostrar\""
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-02-04 10:24"
updated: "2025-02-05 17:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-943"
---

# PED-943: APP - Refactor - Objetivo total por string agrupado por vendedor -> Agregar "monto por unidad vendida" y parámetro "mostrar"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-04 10:24 |
| Actualizado | 2025-02-05 17:17 |
| Etiquetas | ninguna |
| Jira | [PED-943](https://bluinc.atlassian.net/browse/PED-943) |

## Relaciones

- **Padre:** [[PED-299]] Objetivos y Desafios
- **action item from:** [[PED-942]] API - Refactor - Objetivo total por string agrupado por vendedor -> Agregar "monto por unidad vendida" y parámetro "mostrar"
- **has action item:** [[MKT-245]] NB_ INCENTIVO FUERZA DE VENTAS
- **has action item:** [[PED-944]] API - Refactor - Objetivo total por string agrupado por vendedor -> Visibilizar para poder mostrar cuando aun no hicieron ventas

## Descripcion

## Agregaremos 2 nuevas columnas

- una que contenga el valor `unitsSold`.


- Una columna para mostrar cuanto van ganando por unidad vendida, que solo esta cuando tengo el parámetro `paymentPerUnit` y surge de la multiplicación `paymentPerUnit` x `unitsSold`



[adjunto]
Adicionalmente empezaremos a enviar el recurso con el filtro `show=1` y por ahora no enviaremos mas el `goalId` de la siguiente manera:

```
GET {{API_URL}}/v1/objectives/TotalSaleBymatch?show=1
```

El resto del esquema funciona igual que antes. Tener en cuenta que ahora, es posible que en algunas acciones no venga mas el `targetAmount` porque tal vez el objetivo este fijado por cantidad de unidades.
