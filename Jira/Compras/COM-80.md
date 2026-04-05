---
jira_key: "COM-80"
summary: "API - Feat - Agregar/Editar un producto a una orden de compra abierta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-04-04 06:37"
updated: "2024-06-14 14:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-80"
---

# COM-80: API - Feat - Agregar/Editar un producto a una orden de compra abierta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-04 06:37 |
| Actualizado | 2024-06-14 14:42 |
| Etiquetas | ninguna |
| Jira | [COM-80](https://bluinc.atlassian.net/browse/COM-80) |

## Descripción

Este recurso me permite tanto editar como agregar un item nuevo a mi orden de compra.

Básicamente al recibir el parámetro `id` en referencia al “id del item” entonces evalua si el mismo ya se encuentra dentro de la orden.

Si se encuentra dentro de la orden entonces hace un UPDATE de los parámetros presentes, si no se encuentra, hace un INSERT.

```
PATCH /v1/providerOrder/{prviderOrderId}
```

```
           {
                "id": 104829,
                "price": {
                    "value": 50,
                    "iva": 21,
                },
                "amount": 6,
                "position": "4823.69.00.200M",
            },
```

Este recurso solo puede ejecutarse mientras `[NewBytes_DBF].[dbo].[PedProT].cEstado = 'P'`
