---
jira_key: "NBWEB-584"
aliases: ["NBWEB-584"]
summary: "API - Feat - Promos especiales"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-19 12:57"
updated: "2023-09-26 13:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-584"
---

# NBWEB-584: API - Feat - Promos especiales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-19 12:57 |
| Actualizado | 2023-09-26 13:13 |
| Etiquetas | ninguna |
| Jira | [NBWEB-584](https://bluinc.atlassian.net/browse/NBWEB-584) |

## Relaciones

- **Padre:** [[NBWEB-495 - API - Features especiales|NBWEB-495]] API - Features especiales
- **Subtarea:** [[NBWEB-588 - APP - Feat - Promos especiales|NBWEB-588]] APP - Feat - Promos especiales
- **Subtarea:** [[NBWEB-589 - API - DATA - Marcar como promocionarles los que pasaron en la historia de MKT|NBWEB-589]] API - DATA - Marcar como promocionarles los que pasaron en la historia de MKT
- **blocks:** [[MKT-163 - NB_ FILTRO ESPECIAL PROMO PRECIOS ESPECIALES|MKT-163]] NB_ FILTRO ESPECIAL PROMO PRECIOS ESPECIALES

## Descripcion

Agregaremos una columna extra a la tabla `[NewBytes_DBF].[dbo].[articulo]` llamado `prom` (true/false)

Una vez realizado haremos un refactor del recurso de listar productos en la API de NB para poder filtrar y mostrar todos estos productos (solo ellos).

Este filtro puede combinarse con otros filtros de busqueda.
