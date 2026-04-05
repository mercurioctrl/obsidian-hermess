---
jira_key: "NBWEB-798"
summary: "API - Refactor - Agregar utilidad extra a finalPriceWithUtility por porducto y cliente (no al costo como hicimos antes, sino que a finalPriceWithUtility)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-31 12:56"
updated: "2024-08-02 01:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-798"
---

# NBWEB-798: API - Refactor - Agregar utilidad extra a finalPriceWithUtility por porducto y cliente (no al costo como hicimos antes, sino que a finalPriceWithUtility)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-31 12:56 |
| Actualizado | 2024-08-02 01:26 |
| Etiquetas | ninguna |
| Jira | [NBWEB-798](https://bluinc.atlassian.net/browse/NBWEB-798) |

## Descripción

Esta feature es muy parecida a la anterior, pero no trabaja sobre el costo del reseller, sino sobre su precio para sus clientes (finalPriceWithUtility)

Agregaremos la tabla `[NB_WEB].[dbo].[userItems]`

Crearemos una tabla con 4 columnas

- id (auto)


- clientId (int)


- itemId (int)


- utility


- Description



Se debe verificar que los cambios no generen retrasos a los recursos cuando listas todo el catalogo o muchos items
