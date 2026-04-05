---
jira_key: "PED-782"
aliases: ["PED-782"]
summary: "[deprecada] API - Refactor - Agregar utilidad extra a finalPriceWithUtility por porducto y cliente (no al costo como hicimos antes, sino que a finalPriceWithUtility)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-31 12:30"
updated: "2024-08-01 11:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-782"
---

# PED-782: [deprecada] API - Refactor - Agregar utilidad extra a finalPriceWithUtility por porducto y cliente (no al costo como hicimos antes, sino que a finalPriceWithUtility)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-31 12:30 |
| Actualizado | 2024-08-01 11:29 |
| Etiquetas | ninguna |
| Jira | [PED-782](https://bluinc.atlassian.net/browse/PED-782) |

## Relaciones

- **Padre:** [[PED-65 - Listado de productos|PED-65]] Listado de productos

## Descripcion

Esta feature es muy parecida a la anterior, pero no trabaja sobre el costo del reseller, sino sobre su precio para sus clientes (finalPriceWithUtility)

Agregaremos la tabla `[NB_WEB].[dbo].[userItems]`

Crearemos una tabla con 4 columnas

- id (auto)


- clientId (int)


- itemId (int)


- utility


- Description



Se debe verificar que los cambios no generen retrasos a los recursos cuando listas todo el catalogo o muchos items
