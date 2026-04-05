---
jira_key: "PED-188"
aliases: ["PED-188"]
summary: "API - Feat - Mover item entre ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-10-30 09:38"
updated: "2023-11-08 06:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-188"
---

# PED-188: API - Feat - Mover item entre ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-30 09:38 |
| Actualizado | 2023-11-08 06:58 |
| Etiquetas | ninguna |
| Jira | [PED-188](https://bluinc.atlassian.net/browse/PED-188) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **is blocked by:** [[PED-227 - API - Mover item entre ordenes de compra - Incidencias varias|PED-227]] API - Mover item entre ordenes de compra - Incidencias varias

## Descripcion

**Funcionalidad de Transferencia de Ítems entre Órdenes de Compra**

Esta funcionalidad permite trasladar ítems directamente de una orden de compra a otra. Esta acción es útil en casos donde la mercadería requerida para un pedido específico se encuentra ya asignada a otra orden y no está disponible libremente en el inventario. Al permitir esta transferencia directa, se evita el proceso de descarga y carga en la nueva orden, reduciendo el riesgo de que otro vendedor tome el ítem en ese lapso a cero y mejorando la experiencia.

**Condiciones para la Transferencia**

- Solo es posible realizar la transferencia cuando ambas órdenes de compra tienen el estado `cestado='P'`.



**Criterios de Aceptación**

- Es necesario proporcionar la cantidad, ítem, sucursal (branch) y número de orden tanto de la orden de origen como de la orden de destino.


- Antes de realizar la transferencia, se debe confirmar que la cantidad en la orden de origen es suficiente para completar la transferencia


- El precio del ítem en la orden receptora será siempre el correspondiente al cliente receptor.



```
PATCH {API_URL}/v1/order/moveItem
```

```
[
    {
        "senderOrder": "0002",
        "senderBranch": "10328550",
        "recipientOrder": "0002",
        "recipientBranch": "10328551",
        "items": [
                    {
                      "amount": "9.000", <-- esta es la cantidad que quiero que el pedido tenga
                      "itemId": 12434
                    },
                    {
                      "amount": "2.000", <-- esta es la cantidad que quiero que el pedido tenga
                      "itemId": 15134
                    }
    }
]
```

Se recomienda poner updates en lugar de deletes
