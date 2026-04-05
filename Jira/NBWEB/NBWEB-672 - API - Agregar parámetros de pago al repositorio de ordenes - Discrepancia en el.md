---
jira_key: "NBWEB-672"
aliases: ["NBWEB-672"]
summary: "API - Agregar parámetros de pago al repositorio de ordenes - Discrepancia en el tipo de pago"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-03-25 13:22"
updated: "2024-04-09 01:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-672"
---

# NBWEB-672: API - Agregar parámetros de pago al repositorio de ordenes - Discrepancia en el tipo de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-25 13:22 |
| Actualizado | 2024-04-09 01:36 |
| Etiquetas | ninguna |
| Jira | [NBWEB-672](https://bluinc.atlassian.net/browse/NBWEB-672) |

## Relaciones

- **Padre:** [[NBWEB-498]] Oportunidades de mejora
- **relates to:** [[NBWEB-663]] API - Refactor - Agregar parametros para comprobantes de pago al repositorio de ordenes

## Descripcion

Siguiendo el mismo enfoque utilizado en el sistema de Pedidos para la lista de órdenes, primero seleccionaremos el medio de pago de `MS_VENTAS_REMITOS.ID_FORMA`. Si no está disponible, lo tomaremos de `pedclit.ID_FORMADEPAGO` como último recurso. De esta forma se asegura que el objeto tenga el tipo de pago actualizado.

[adjunto]
[adjunto]
