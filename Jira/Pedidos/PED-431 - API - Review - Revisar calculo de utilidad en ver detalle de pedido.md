---
jira_key: "PED-431"
aliases: ["PED-431"]
summary: "API - Review - Revisar calculo de utilidad en \"ver detalle de pedido\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-03 10:07"
updated: "2024-01-06 15:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-431"
---

# PED-431: API - Review - Revisar calculo de utilidad en "ver detalle de pedido"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-03 10:07 |
| Actualizado | 2024-01-06 15:13 |
| Etiquetas | ninguna |
| Jira | [PED-431](https://bluinc.atlassian.net/browse/PED-431) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **is blocked by:** [[PED-393]] API - Feat - Ver detalle de orden de compra -> Agregar direccion al objeto de la orden

## Descripcion

Al inspeccionar el recurso

```
GET {API_URL}/v1/orders/{PEDIDO}
```

Se obtiene un parametro llamado `effectiveness`

Este parámetro representa la utilidad porcentual de un producto, pero me resulta raro que siempre que lo veo, esta por arriba de 100.

Sospecho que la formula se encuentra indicando por ejemplo 140% cuando en realidad se trata de un 40%

No se si me explico, pero si queres revisa la formula y lo charlamos
