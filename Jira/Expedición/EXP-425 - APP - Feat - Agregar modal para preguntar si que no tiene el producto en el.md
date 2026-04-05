---
jira_key: "EXP-425"
aliases: ["EXP-425"]
summary: "APP - Feat - Agregar modal para preguntar si que no tiene el producto en el inventario"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-08-05 09:42"
updated: "2024-08-08 03:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-425"
---

# EXP-425: APP - Feat - Agregar modal para preguntar si que no tiene el producto en el inventario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-05 09:42 |
| Actualizado | 2024-08-08 03:00 |
| Etiquetas | ninguna |
| Jira | [EXP-425](https://bluinc.atlassian.net/browse/EXP-425) |

## Relaciones

- **Padre:** [[EXP-424]] Controles de stock al despachar

## Descripcion

Cuando estamos haciendo una Devolucion en una de estas dos pantallas

[adjunto]
[adjunto]
Debo mostrar un cartel con dos opciones con la leyenda:

“Estas realizando la devolución porque no contas con la mercadria físicamente? 
Si presionas “Si” se enviara el stock a control en lugar de ponerse nuevamente a la venta. Si presionas “NO” volverá a stock.

SI | NO 

En el caso de que sea SI  agregaremos al recurso `missing:true` para que el back sepa que debe devolver el stock en otra columna.

```
POST {API_URL}/v1/ordersRefund/{PEDIDO}
```

```
{
"voucherTypeId":"2",
"clientId":19227,
"pedido":"X000200583945",
"autorizaUser":"FE5BA42E32632445",
"missing": true/false,
"trade":[
  {
    "units":1,
    "price":141.80505,
    "ivaTax":21,
    "internalId":109609
    }
]
}
```
