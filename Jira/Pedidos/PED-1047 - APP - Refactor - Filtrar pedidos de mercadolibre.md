---
jira_key: "PED-1047"
aliases: ["PED-1047"]
summary: "APP - Refactor - Filtrar pedidos de mercadolibre"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-07-13 20:27"
updated: "2025-07-15 10:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1047"
---

# PED-1047: APP - Refactor - Filtrar pedidos de mercadolibre

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-13 20:27 |
| Actualizado | 2025-07-15 10:30 |
| Etiquetas | ninguna |
| Jira | [PED-1047](https://bluinc.atlassian.net/browse/PED-1047) |

## Relaciones

- **Padre:** [[PED-915]] MercadoLibre
- **action item from:** [[PED-1044]] API - Refactor - Filtro MLA y atributos extra para el repositorio de pedidos

## Descripcion

Agregaremos una opción extra llamada “Mercadolibre” dentro del filtro de tipo de ordenes, pero que no funciona con el tipo sino que al seleccionarla usaremos el filtro `GET {API_URL}/v1/orders?ml=true` realizado en la historia [link](https://bluinc.atlassian.net/browse/PED-1044) 

[adjunto]
