---
jira_key: "NBWEB-552"
aliases: ["NBWEB-552"]
summary: "API - Refactor - Precio especial desde costo (Cambio de sucursal)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-07 11:21"
updated: "2023-07-03 05:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-552"
---

# NBWEB-552: API - Refactor - Precio especial desde costo (Cambio de sucursal)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-07 11:21 |
| Actualizado | 2023-07-03 05:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-552](https://bluinc.atlassian.net/browse/NBWEB-552) |

## Relaciones

- **Padre:** [[NBWEB-544]] Refactor - Precios especiales por cliente y para marketplace
- **blocks:** [[SNB-783]] Integracion - Producteca

## Descripcion

Se deben marcar para ingresar en Sucursal 10, aquellos que trabajen con la modalidad `specialPriceFromCost`

Es decir que en vez de crear una orden se debe guardar en `NewBytes_DBF.dbo.pedclit.cnumsuc` `y NewBytes_DBF.dbo.pedclit.ID_Sucursal`  como '0010' y 10 respectivamente.

```
{API_URL}/v1/carrito/process
```
