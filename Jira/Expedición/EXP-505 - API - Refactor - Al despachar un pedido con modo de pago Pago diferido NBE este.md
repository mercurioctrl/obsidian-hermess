---
jira_key: "EXP-505"
aliases: ["EXP-505"]
summary: "API - Refactor - Al despachar un pedido con modo de pago \"Pago diferido NBE\" este pasa a Pendiente a Cobrar"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-07-28 14:15"
updated: "2025-08-06 10:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-505"
---

# EXP-505: API - Refactor - Al despachar un pedido con modo de pago "Pago diferido NBE" este pasa a Pendiente a Cobrar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-28 14:15 |
| Actualizado | 2025-08-06 10:25 |
| Etiquetas | ninguna |
| Jira | [EXP-505](https://bluinc.atlassian.net/browse/EXP-505) |

## Relaciones

- **Padre:** [[EXP-7 - Despacho de retiros|EXP-7]] Despacho de retiros

## Descripcion

Según lo conversado, refactorizaremos el recurso para despachar pedidos, de modo tal que nuestro nuevo medio de envío “Pago diferido NBE” pase los pedidos a “Despachado, pendiente a cobrar” siempre y cuando sea “Pago diferido NBE”

```
PATCH {API_URL}/v1/orders/{pedido}/dispatch
```





Se requiere inicializar las siguientes variables de entorno.

```sql
# Medios de Pago table: new_bytes.dbo.ms_formaspago_remitos_vendedores
MOTORCYCLE_PAYMENT=2
VAN_PAYMENT=4
DEFERRED_PAYMENT=16
DEFERRED_NBE_PAYMENT=19
```
