---
jira_key: "POS-94"
aliases: ["POS-94"]
summary: "API - Dataset - Crear estructura de datos refactorizada para sistema de pases"
status: "Gamma"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2022-08-30 15:56"
updated: "2022-09-28 22:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-94"
---

# POS-94: API - Dataset - Crear estructura de datos refactorizada para sistema de pases

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-30 15:56 |
| Actualizado | 2022-09-28 22:26 |
| Etiquetas | ninguna |
| Jira | [POS-94](https://bluinc.atlassian.net/browse/POS-94) |

## Relaciones

- **Padre:** [[POS-23 - Pases de mercaderia|POS-23]] Pases de mercaderia

## Descripcion

Segun lo conversado se crearan las siguientes tablas a criterio de eze

pasesCabecera => id,datetime,userId, status (*), idOrigin, idDestiny

[14:47](https://liosistemas.slack.com/archives/D037A2S4JC9/p1661881641916849)

acá con el campo status, tengo una duda, si dejamos status ( pendiente, aceptado , anulado ? ) o si ponemos cambio_aceptado como está hoy día

[14:47](https://liosistemas.slack.com/archives/D037A2S4JC9/p1661881659419739)

obviamente haria q sea statusId y lo realcionamos con otra tabla

[14:48](https://liosistemas.slack.com/archives/D037A2S4JC9/p1661881703202109)

y para el detalle tengo => id,itemId, itemDescription,serial, headerId
