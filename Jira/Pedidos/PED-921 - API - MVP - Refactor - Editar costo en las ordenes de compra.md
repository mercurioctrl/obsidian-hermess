---
jira_key: "PED-921"
aliases: ["PED-921"]
summary: "API - MVP - Refactor - Editar costo en las ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-30 07:42"
updated: "2025-04-29 12:26"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/PED-921"
---

# PED-921: API - MVP - Refactor - Editar costo en las ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-30 07:42 |
| Actualizado | 2025-04-29 12:26 |
| Etiquetas | MVPLaset |
| Jira | [PED-921](https://bluinc.atlassian.net/browse/PED-921) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **has action item:** [[PED-922 - API - Refactor - Agregar en el caso que corresponda el costForSale al generar|PED-922]] API - Refactor - Agregar en el caso que corresponda el costForSale al generar un pedido
- **blocks:** [[PED-925 - APP - MVP - Refactor - Guardar costo para el item de una orden|PED-925]] APP - MVP - Refactor - Guardar costo para el item de una orden

## Descripcion

Haremos un refactor que nos permita editar (solo para quien tiene el permiso `editCostForSale`) el costo de un producto para un pedido especifico. Para esto usaremos el mismo recurso que utilizamos para editar precios por ejemplo.

```
PATCH {API_URL}/v1/orders/addItem
```

```
{
"order":"10384169",
"branch":"0002",
"itemId":116741,
"amount":1,
"selectedPrice":540.36894861
"costForSale": 500.00 <--- SI ESTA EL PARAMETRO Y TIENE PERMISO, SE GUARDA
}
```

**¿Donde lo guardaremos?**

Para esto seguiremos el mismo esquema para toda la informacion relevante del contenido de un pedido y lo guardaremos en nuestra cadena de consecuentes `Orden -> Pedido -> Liquidación` 

`[NewBytes_DBF].[dbo].[pedclil].costForSale`
