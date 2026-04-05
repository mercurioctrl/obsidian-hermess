---
jira_key: "EXP-259"
aliases: ["EXP-259"]
summary: "API - Feat - Marcar pedido como entregado mediante tarjeta de autorizacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-28 08:47"
updated: "2023-04-17 09:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-259"
---

# EXP-259: API - Feat - Marcar pedido como entregado mediante tarjeta de autorizacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-28 08:47 |
| Actualizado | 2023-04-17 09:40 |
| Etiquetas | ninguna |
| Jira | [EXP-259](https://bluinc.atlassian.net/browse/EXP-259) |

## Relaciones

- **Padre:** [[EXP-258 - Feat - Autorizar Entrega mediante tarjeta de autorizacion|EXP-258]] Feat - Autorizar Entrega mediante tarjeta de autorizacion
- **blocks:** [[EXP-260 - APP - Feat - Marcar pedido como entregado mediante tarjeta de autorizacion|EXP-260]] APP - Feat - Marcar pedido como entregado mediante tarjeta de autorizacion

## Descripcion

Este recurso sirve para que (desde el mostrador) se marque el momento y la persona que esta “entregando” la mercaderia en manos del cliente o el transportista.

Es diferente a “Despachar” que es la acción inmediatamente anterior y que indica que el pedido fue armado por el deposito.

Por esta razon, **solo pueden marcarse como entregados aquellos pedidos que estén en ID_STATUS 4 o 3** según la tabla `[NEW_BYTES].[dbo].[MS_STATUS_REMITO]`

```
PATCH {API_URL}/v1/orders/{pedido}/hand
```

```
{
    autorizaUser: {token}
}
```

Al ejecutar el recurso marca en el estado del remito en `[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS]` en `ID_STATUS` = 13

*Si es 3 (Despachado, Pendiente a Cobrar), debe pasar a 14 (Entregado, Pendiente a cobrar)

Importante: Esta feature, lleva token de autorización (con tarjeta), aunque en principio no sera oblgitario.
