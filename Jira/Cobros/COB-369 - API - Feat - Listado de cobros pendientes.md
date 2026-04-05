---
jira_key: "COB-369"
aliases: ["COB-369"]
summary: "API - Feat - Listado de cobros pendientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-20 08:51"
updated: "2023-04-10 16:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-369"
---

# COB-369: API - Feat - Listado de cobros pendientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-20 08:51 |
| Actualizado | 2023-04-10 16:38 |
| Etiquetas | ninguna |
| Jira | [COB-369](https://bluinc.atlassian.net/browse/COB-369) |

## Relaciones

- **Padre:** [[COB-357]] Feat - Listar Despachados, pendientes a cobrar
- **blocks:** [[COB-370]] APP - Feat - Listado de cobros pendientes

## Descripcion

Este repositorio es casi igual a [link](https://lioteam.atlassian.net/browse/COB-41) solo que tiene filtrado para mostrar solo los “Despachados, pendientes de cobro” y se agrega quien es el “transportista”, en el caso de que exista. No todos los que estén en este estado van a tener transportista asociado, ya que agregaremos un nuevo medio de pago llamado “pago diferido” y estos tambien aparecerán aca. Pero los que lo tienen debemos mostrarlos.

```
{API_URL}/v1/pendingCharges
```

```
[
  {
    "fecha": "2022-07-31 19:05:15",
    "shipper": "Juan Carlols",
    "shipperId": 12,
    "pedido": "X001000020625",
    "clientName": "MUGELLO SRL",
    "sellerName": "Altamiranda                    Dario",
    "total": 173314502210.0,
    "taxes": 0.0,
    "totalFinal": 173314502210.0,
    "currencyQuote": 138.0,
    "currencyQuoteDay": 138.0,
    "status": 3.0,
    "paymentMethod": "Efectivo Camioneta",
    "estado": "Finalizado",
    "dispatch": "Envio Camioneta               ",
    "settlement": 4,
    "order": "10287149",
    "orderBrunch": "0010",
    "brunch": "0010",
    "clientId": 33181,
    "invoice": null,
    "albId": "00020625",
    "invoiceId": null,
    "taxesAmount": 0.0
  },
  {
    "fecha": "2022-07-29 17:39:04",
    "shipper": "Juan Carlols",
    "shipperId": 12,
    "pedido": "X001000020624",
    "clientName": "BLANCO INSUA GALO                  ",
    "sellerName": "Blanco Insua    Galo",
    "total": 51400000.0,
    "taxes": 0.0,
    "totalFinal": 51400000.0,
    "currencyQuote": 138.0,
    "currencyQuoteDay": 138.0,
    "status": 3.0,
    "paymentMethod": "Efectivo Caja",
    "estado": "Despachado, Pendiente a Cobrar",
    "dispatch": "Retiro de cliente en Local    ",
    "settlement": 3,
    "order": "10287114",
    "orderBrunch": "0010",
    "brunch": "0010",
    "clientId": 16718,
    "invoice": null,
    "albId": "00020624",
    "invoiceId": null,
    "taxesAmount": 0.0
  }
  ...
  ]
```

Adicionalmente agregaremos el filtro “`shipperId`" para poder filtrar por transportista.
