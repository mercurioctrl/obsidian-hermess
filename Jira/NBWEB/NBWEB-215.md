---
jira_key: "NBWEB-215"
summary: "APP - Paginas de destino para los pagos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-05-31 17:22"
updated: "2022-06-26 21:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-215"
---

# NBWEB-215: APP - Paginas de destino para los pagos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-31 17:22 |
| Actualizado | 2022-06-26 21:08 |
| Etiquetas | ninguna |
| Jira | [NBWEB-215](https://bluinc.atlassian.net/browse/NBWEB-215) |

## Descripción

Se deben genera las distintas paginas de destinos para que aterricen los resultados de los pagos.

No todos los pagos las usa, pero algunos tipo de pago (como el dinero en cuenta) si las necesitan.



```
{{APP_URL}}/pagos/success
```

```
{{APP_URL}}/pagos/failure
```

```
{{APP_URL}}/pagos/pending
```

Cuando el sitio retorne, volverá con algunas variables

`collection_id=1248492302&collection_status=approved&payment_id=1248492302&status=approved&external_reference=null&payment_type=credit_card&merchant_order_id=4866216069&preference_id=1128749028-14eb71d6-300c-4c31-a0b8-58d249634c98&site_id=MLA&processing_mode=aggregator&merchant_account_id=null`

De esos parámetros que llegan, se deben enviar a 



```
POST {{API_URL}}/webhook/{{MERCADOPAGO_URL_WEBHOOK}}
```

Los parametros:

- status


- status_detail


- payment_id



*`MERCADOPAGO_URL_WEBHOOK` se define en el .env y es un valor del tipo “`2a6afa6c45caf845c5cb0ff4d8b4870caa8716e648d5fc467cc13d3beb1b5902”`
