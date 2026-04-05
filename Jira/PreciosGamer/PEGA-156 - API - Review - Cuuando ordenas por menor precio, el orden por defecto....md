---
jira_key: "PEGA-156"
aliases: ["PEGA-156"]
summary: "API - Review - Cuuando ordenas por menor precio, el orden por defecto... muestra resutlados limitados para algunas busquedas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-10 13:36"
updated: "2024-12-27 05:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-156"
---

# PEGA-156: API - Review - Cuuando ordenas por menor precio, el orden por defecto... muestra resutlados limitados para algunas busquedas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-10 13:36 |
| Actualizado | 2024-12-27 05:02 |
| Etiquetas | ninguna |
| Jira | [PEGA-156](https://bluinc.atlassian.net/browse/PEGA-156) |

## Relaciones

- **Padre:** [[PEGA-6]] Feat - Listar productos

## Descripcion

Limitado

[https://api.preciosgamer.com/v1/items?search=mother&offset=0&order=asc_price](https://api.preciosgamer.com/v1/items?search=mother&offset=0&order=asc_price&)

No limitado

[https://api.preciosgamer.com/v1/items?search=mother&offset=0](https://api.preciosgamer.com/v1/items?search=mother&offset=0)



Por alguna razón da resultados diferentes, sin ordenar parece ser correcto, pero claro esta desordenado
