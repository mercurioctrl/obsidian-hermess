---
jira_key: "PED-447"
aliases: ["PED-447"]
summary: "APP - Feat - Unir pedido a otro envío (pedido)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-01-05 13:44"
updated: "2024-01-11 19:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-447"
---

# PED-447: APP - Feat - Unir pedido a otro envío (pedido)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-05 13:44 |
| Actualizado | 2024-01-11 19:27 |
| Etiquetas | ninguna |
| Jira | [PED-447](https://bluinc.atlassian.net/browse/PED-447) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido
- **is blocked by:** [[PED-444 - API - Feat - Unir pedido a otro envio|PED-444]] API - Feat - Unir pedido a otro envio 

## Descripcion

Agregaremos en el modal de liquidación un accionable que diga “Agregar a otro envío”



Este, a su vez abrirá un modal donde podemos seleccionar otro pedido del mismo cliente y una vez realizado, ejecutaremos el recurso 

[link](https://lioteam.atlassian.net/browse/PED-444) 

```
POST {{API_URL}}/v1/orders/joinShipping
```

```
{
  host: 'X001000021834',
  guest: 'X001000021832'
}
```

En donde `host`, es el pedido que acabamos de seleccionar y `guest` el pedido que estoy liquidando
