---
jira_key: "LIO-51"
aliases: ["LIO-51"]
summary: "API - PED - Refactor - Agregar filtro para ver cancelados / eliminados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-18 12:14"
updated: "2024-06-24 17:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-51"
---

# LIO-51: API - PED - Refactor - Agregar filtro para ver cancelados / eliminados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-18 12:14 |
| Actualizado | 2024-06-24 17:37 |
| Etiquetas | ninguna |
| Jira | [LIO-51](https://bluinc.atlassian.net/browse/LIO-51) |

## Relaciones

- **Padre:** [[LIO-28 - El sitio debe funcionar correctamente, sin puntos grises o cosas que no se|LIO-28]] El sitio debe funcionar correctamente, sin puntos grises o cosas que no se entienden
- **blocks:** [[LIO-52 - APP - PED - Refactor - Agregar filtro para vert cancelados eliminados|LIO-52]] APP - PED - Refactor - Agregar filtro para vert cancelados / eliminados

## Descripcion

Agregaremos un nuevo filtro para ver las ordenes de venta que nos permita visualizar SOLO aquellas ordenes que fueron canceladas/eliminadas, es decir donde `[NewBytes_DBF].[dbo].[pedclit].lanula = 1`

```
GET {API_URL}/v1/orders?&orderStatus=cancelled

```
