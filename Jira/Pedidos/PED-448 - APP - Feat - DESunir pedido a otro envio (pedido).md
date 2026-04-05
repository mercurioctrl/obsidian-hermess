---
jira_key: "PED-448"
aliases: ["PED-448"]
summary: "APP - Feat - DESunir pedido a otro envio (pedido)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-05 14:18"
updated: "2024-01-09 18:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-448"
---

# PED-448: APP - Feat - DESunir pedido a otro envio (pedido)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-05 14:18 |
| Actualizado | 2024-01-09 18:15 |
| Etiquetas | ninguna |
| Jira | [PED-448](https://bluinc.atlassian.net/browse/PED-448) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido
- **blocks:** [[PED-455 - APP - Feat - Desunir pedido de otro envio ()|PED-455]] APP - Feat - Desunir pedido de otro envio ()

## Descripcion

Crearemos el recurso para “desvincular” un pedido determinado de un host.

Esto se puede hacer si el pedido se encuentra en la tabla y ambos pedidos están en uno de los siguientes estados

- Pendiante a autorizar


- Armado finalizado


- serializado


- parcialmente serialziado


- Autorizado pendiente a despachar



```
DELETE {{API_URL}}/v1/orders/joinShipping
```

```
{
  host: 'X001000021834',
  guest: 'X001000021832'
}
```
