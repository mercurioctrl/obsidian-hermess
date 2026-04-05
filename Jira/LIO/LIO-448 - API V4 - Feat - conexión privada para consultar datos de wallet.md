---
jira_key: "LIO-448"
aliases: ["LIO-448"]
summary: "API V4 - Feat - conexión privada para consultar datos de wallet"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-09-10 12:35"
updated: "2025-09-23 10:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-448"
---

# LIO-448: API V4 - Feat - conexión privada para consultar datos de wallet

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-09-10 12:35 |
| Actualizado | 2025-09-23 10:44 |
| Etiquetas | ninguna |
| Jira | [LIO-448](https://bluinc.atlassian.net/browse/LIO-448) |

## Relaciones

- **Padre:** [[LIO-231]] Billetera

## Descripcion

Se debe implementar un recurso que permita la comunicación eficiente de forma privada entre microservicios, en este caso para obtener el balance de una wallet mediante id de cliente pasando por header `X-Private-Key` la clave quer permite el acceso.



- Variable en el .env : permite la conexión privada con la API de wallet.



`PRIVATE_CONNECTION_WALLET=123` → el valor aquie es el que se espera para permitir el acceso al recurso.



```
GET /v4/wallet/balance/274942'
--header 'X-Private-Key: 123' --> token 
```
