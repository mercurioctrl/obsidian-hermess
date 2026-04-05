---
jira_key: "NBWEB-651"
aliases: ["NBWEB-651"]
summary: "API - Feat - Al procesar un carrito que tiene utilidad por categoría, la guardaremos para no perder el dato si esta cambia"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-18 13:54"
updated: "2024-03-25 01:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-651"
---

# NBWEB-651: API - Feat - Al procesar un carrito que tiene utilidad por categoría, la guardaremos para no perder el dato si esta cambia

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-18 13:54 |
| Actualizado | 2024-03-25 01:07 |
| Etiquetas | ninguna |
| Jira | [NBWEB-651](https://bluinc.atlassian.net/browse/NBWEB-651) |

## Relaciones

- **Padre:** [[NBWEB-641 - Listas de precio|NBWEB-641]] Listas de precio
- **is blocked by:** [[NBWEB-666 - API - Agregar precio con utilidad final - No se visualiza el articulo|NBWEB-666]] API - Agregar precio con utilidad final - No se visualiza el articulo 

## Descripcion

Para que el dato nunca se pierda y podamos utilizarlo para obtener informacion de como se realizo la venta lo guardaremos en la tabla


`[NewBytes_DBF].[dbo].[pedclil].userUtility`
