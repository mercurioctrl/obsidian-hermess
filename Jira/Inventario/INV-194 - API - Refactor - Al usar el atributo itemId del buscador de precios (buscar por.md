---
jira_key: "INV-194"
aliases: ["INV-194"]
summary: "API - Refactor - Al usar el atributo itemId del buscador de precios (buscar por termino) se debe guardar el precio obtenido, si pudo hacerse con exito"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-15 14:52"
updated: "2025-07-28 10:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-194"
---

# INV-194: API - Refactor - Al usar el atributo itemId del buscador de precios (buscar por termino) se debe guardar el precio obtenido, si pudo hacerse con exito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-15 14:52 |
| Actualizado | 2025-07-28 10:31 |
| Etiquetas | ninguna |
| Jira | [INV-194](https://bluinc.atlassian.net/browse/INV-194) |

## Relaciones

- **Padre:** [[INV-35 - Importadores Scrappers|INV-35]] Importadores/ Scrappers

## Descripcion

Se guardara en la mista tabla de donde saco el “termino” de búsqueda `[NewBytes_DBF].[dbo].[scrap_hg]`

Específicamente en el parámetro para tal fin `[NewBytes_DBF].[dbo].[scrap_hg].precio_ml`  asi como tambien guardaremos `[NewBytes_DBF].[dbo].[scrap_hg].fecha_actualizacion_ml`
