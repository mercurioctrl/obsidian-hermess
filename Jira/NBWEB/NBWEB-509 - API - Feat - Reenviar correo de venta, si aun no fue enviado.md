---
jira_key: "NBWEB-509"
aliases: ["NBWEB-509"]
summary: "API - Feat - Reenviar correo de venta, si aun no fue enviado"
status: "Code Review"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-12 08:21"
updated: "2022-12-12 10:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-509"
---

# NBWEB-509: API - Feat - Reenviar correo de venta, si aun no fue enviado

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-12 08:21 |
| Actualizado | 2022-12-12 10:13 |
| Etiquetas | ninguna |
| Jira | [NBWEB-509](https://bluinc.atlassian.net/browse/NBWEB-509) |

## Relaciones

- **Padre:** [[NBWEB-498 - Oportunidades de mejora|NBWEB-498]] Oportunidades de mejora

## Descripcion

Se debe crear un recurso `GET` para poder enviar el correo que reciben los clientes al realizar una orden del sitio (incluida palabra clave si es retiro).

El recurso recibe los parámetros: `order` y `branch` y se utilizara para conectarlo a otras aplicaciones que les permiten a los vendedores realizar pedidos.

Este correo solo puede ser enviado si aun no fue enviado nunca, por lo cual es conveniente empezar a registrar cuando se envía en alguna columna.
