---
jira_key: "PED-115"
aliases: ["PED-115"]
summary: "API - Refactor - Ver detalle de una orden de compra -> Mostrar nombre de currier segun pedclil"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-03 09:37"
updated: "2023-10-03 09:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-115"
---

# PED-115: API - Refactor - Ver detalle de una orden de compra -> Mostrar nombre de currier segun pedclil

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-03 09:37 |
| Actualizado | 2023-10-03 09:48 |
| Etiquetas | ninguna |
| Jira | [PED-115](https://bluinc.atlassian.net/browse/PED-115) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra

## Descripcion

En los casos donde se incorpora un envío, y se agrega el item “Servicio de envío”  en `[NewBytes_DBF].[dbo].[pedclil]` se hace con el nombre del currier. Pero al ver el pedido no se ve correctamente.

Ver siguiente ejemplo:

```
SELECT *
  FROM [NewBytes_DBF].[dbo].[pedclil]
  WHERE cnumped = '10314720'
```
