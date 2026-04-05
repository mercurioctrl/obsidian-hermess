---
jira_key: "PED-471"
aliases: ["PED-471"]
summary: "API - Refactor - Generar reporte de stock y ventas por producto -> Columnas disponibles"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-11 10:12"
updated: "2024-01-17 02:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-471"
---

# PED-471: API - Refactor - Generar reporte de stock y ventas por producto -> Columnas disponibles

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-11 10:12 |
| Actualizado | 2024-01-17 02:06 |
| Etiquetas | ninguna |
| Jira | [PED-471](https://bluinc.atlassian.net/browse/PED-471) |

## Relaciones

- **Padre:** [[PED-213]] Reportes de ventas

## Descripcion

Hay una diferencia de como debe mostrarse la cantidad en el parámetro `DISPONIBLE`, para poder establecer un ejemplo usaremos una consulta en **produccion** para el producto `111453 - PROCESADOR AMD (AM4) RYZEN 5 5600G`

Al obtener el archivo vemos lo siguiente

[adjunto]
Vemos el parámetro `DISPONIBLE` en 3015

Sin embargo el reporte viejo arroja lo siguiente

[adjunto]
Entonces el dato sale de aca:

`(NSTOCK - nstock_reserva_pedidos) `segun la tabla stocks
