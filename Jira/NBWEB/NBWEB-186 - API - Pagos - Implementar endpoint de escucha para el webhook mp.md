---
jira_key: "NBWEB-186"
aliases: ["NBWEB-186"]
summary: "API - Pagos - Implementar endpoint de escucha para el webhook mp"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-13 10:54"
updated: "2022-11-09 11:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-186"
---

# NBWEB-186: API - Pagos - Implementar endpoint de escucha para el webhook mp

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-13 10:54 |
| Actualizado | 2022-11-09 11:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-186](https://bluinc.atlassian.net/browse/NBWEB-186) |

## Relaciones

- **Padre:** [[NBWEB-77 - Implementar Pagos|NBWEB-77]] Implementar Pagos
- **blocks:** [[NBWEB-189 - API - Pagos - Guardar historial de cobros y sus estados confirmados o rechazados|NBWEB-189]] API - Pagos - Guardar historial de cobros y sus estados confirmados o rechazados

## Descripcion

Se debe guardar en una tabla asociada el cliente y numero de orden

Tablas

```
------------------------------
response_mercadopago
------------------------------
id
client_num
order
status
status_detail
date_approved
payment_method_id
payment_type_id
error_message
```

```
------------------------------
notification_mercadopago
------------------------------
id
id_webhook
live_mode
type
date_created
application_id
user_id_mercadopago
version
api_version
action
data
attempts
request
```
