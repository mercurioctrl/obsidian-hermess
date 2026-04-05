---
jira_key: "EXP-260"
aliases: ["EXP-260"]
summary: "APP - Feat - Marcar pedido como entregado mediante tarjeta de autorizacion"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-03-28 08:47"
updated: "2023-03-29 14:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-260"
---

# EXP-260: APP - Feat - Marcar pedido como entregado mediante tarjeta de autorizacion

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-28 08:47 |
| Actualizado | 2023-03-29 14:10 |
| Etiquetas | ninguna |
| Jira | [EXP-260](https://bluinc.atlassian.net/browse/EXP-260) |

## Relaciones

- **Padre:** [[EXP-258 - Feat - Autorizar Entrega mediante tarjeta de autorizacion|EXP-258]] Feat - Autorizar Entrega mediante tarjeta de autorizacion
- **is blocked by:** [[EXP-259 - API - Feat - Marcar pedido como entregado mediante tarjeta de autorizacion|EXP-259]] API - Feat - Marcar pedido como entregado mediante tarjeta de autorizacion

## Descripcion

Este recurso sirve para que (desde el mostrador) se marque el momento y la persona que esta “entregando” la mercaderia en manos del cliente o el transportista.

Es diferente a “Despachar” que es la acción inmediatamente anterior y que indica que el pedido fue armado por el deposito.

En el siguiente modal:

[adjunto]
- Cambiaremos la leyenda “Despachar” por “Finalizar Pedido”


- Una vez “Despachado” o “Finalizado el pedido”, el botón se dejara de mostrar y mostraremos uno nuevo con la leyenda “Entregar”, este recurso nos pedirá una tarjeta de autorización y ejecutara el recurso [https://lioteam.atlassian.net/browse/EXP-259](https://lioteam.atlassian.net/browse/EXP-259)



Por esta razon, **solo pueden marcarse como entregados aquellos pedidos que estén en STATUS 4 o 3**

Ejecutaremos el recurso

```
PATCH {API_URL}/v1/orders/{pedido}/hand
```

```
{
    autorizaUser: {token}
}
```

Al ejecutar el recurso marca en el estado del remito en `[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS]` en `ID_STATUS` = 13
