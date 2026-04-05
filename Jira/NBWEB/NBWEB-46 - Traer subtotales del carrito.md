---
jira_key: "NBWEB-46"
aliases: ["NBWEB-46"]
summary: "Traer subtotales del carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-21 12:00"
updated: "2022-03-28 12:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-46"
---

# NBWEB-46: Traer subtotales del carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-21 12:00 |
| Actualizado | 2022-03-28 12:37 |
| Etiquetas | ninguna |
| Jira | [NBWEB-46](https://bluinc.atlassian.net/browse/NBWEB-46) |

## Relaciones

- **Padre:** [[NBWEB-1 - API - Carrito de compras|NBWEB-1]] API - Carrito de compras

## Descripcion

```
GET {{API_URL}}/v1/carrito/subtotales
```

Este recurso debe traer la informacion sobre los subtotales del carrito.

Debe retornar un objeto con los siguientes parámetros

```javascript
{
  cartId:3334,
  cartName:"Nuevo Carrito Alfabis",
  cotizacion:104.5,
  subtotalDollar:4324.56,
  subtotalDollarFinal:5232.72,
  subtotalPesosAr:454078.8,
  subtotalPesosArFinal:549434.38
}
```

¿como se obtiene la cotización?

Para obtener la cotización es posible hacer,  queda a criterio del desarrollador como obtener este valor y de que forma almacenarlo. 

```
SELECT 
COTIZACION    
FROM [NB_WEB].[dbo].[MS_COTIZACIONES]
WHERE IDFORMAPAGO = 1
```
