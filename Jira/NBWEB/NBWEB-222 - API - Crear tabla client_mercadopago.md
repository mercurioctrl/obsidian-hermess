---
jira_key: "NBWEB-222"
aliases: ["NBWEB-222"]
summary: "API -  Crear tabla client_mercadopago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-06-03 16:13"
updated: "2022-06-26 21:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-222"
---

# NBWEB-222: API -  Crear tabla client_mercadopago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-03 16:13 |
| Actualizado | 2022-06-26 21:08 |
| Etiquetas | ninguna |
| Jira | [NBWEB-222](https://bluinc.atlassian.net/browse/NBWEB-222) |

## Relaciones

- **Padre:** [[NBWEB-77]] Implementar Pagos

## Descripcion

Crea la tabla necesaria para almacenar los correos con los que se creara el cliente en mercadopago para recuperar sus datos

```
NB_WEB.dbo.client_mercadopago
```

La misma contara con las siguientes columnas mínimas

- id (autonumerico)


- mpId  


- mpEmail


- clientId
