---
jira_key: "PED-536"
aliases: ["PED-536"]
summary: "API - Listar ordenes de compra -> Código postal vacío "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-02-06 20:04"
updated: "2024-03-10 21:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-536"
---

# PED-536: API - Listar ordenes de compra -> Código postal vacío 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-06 20:04 |
| Actualizado | 2024-03-10 21:49 |
| Etiquetas | ninguna |
| Jira | [PED-536](https://bluinc.atlassian.net/browse/PED-536) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **relates to:** [[PED-581]] APP - Cambiar el selector de cotizar envío por la favorita si no existe envío - Detalles al abrir el modal de cotización de envío

## Descripcion

Al listar la orden `10332494`, se observa que el código postal está vacío. 

[adjunto]
Sin embargo, al verificar esta orden en la base de datos, se puede ver que tiene una dirección asociada que incluye el código postal. 

[adjunto]


Dato extra:
Es posible que este problema esté relacionado con la forma en que se establece la relación entre las direcciones de los clientes y las órdenes.

[adjunto]
