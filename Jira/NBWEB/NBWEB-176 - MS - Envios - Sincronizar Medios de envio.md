---
jira_key: "NBWEB-176"
aliases: ["NBWEB-176"]
summary: "MS - Envios - Sincronizar Medios de envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-12 16:18"
updated: "2022-06-26 20:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-176"
---

# NBWEB-176: MS - Envios - Sincronizar Medios de envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-12 16:18 |
| Actualizado | 2022-06-26 20:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-176](https://bluinc.atlassian.net/browse/NBWEB-176) |

## Relaciones

- **Padre:** [[NBWEB-76]] API - Implementar MS envios

## Descripcion

Se trata de un recurso que al ser solicitado por alguien que tenga el role de administrador, debe actualizar los campos de la base de datos en `db_mariadb.service-envios-api-rest-db.mediosenvio` desde `db.LO.dbo.mediosEnvio`

```
GET {{API_URL}}/sync-up/shippingMethods
```

Se deben agregar aquellos que faltan, y actualizar los existentes.

Como algo extra podríamos actualizar una fechad e actualizan en la tabla remota
