---
jira_key: "POS-287"
aliases: ["POS-287"]
summary: "APP - Listar pedidos - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-02-27 14:51"
updated: "2024-03-02 18:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-287"
---

# POS-287: APP - Listar pedidos - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-27 14:51 |
| Actualizado | 2024-03-02 18:26 |
| Etiquetas | ninguna |
| Jira | [POS-287](https://bluinc.atlassian.net/browse/POS-287) |

## Relaciones

- **Padre:** [[POS-280 - Pedidos|POS-280]] Pedidos
- **blocks:** [[POS-283 - APP - Feat - Listar pedidos|POS-283]] APP - Feat - Listar pedidos
- **relates to:** [[POS-286 - API - Listar pedidos - Observaciones del objeto respuesta|POS-286]] API - Listar pedidos - Observaciones del objeto respuesta

## Descripcion

1. El parámetro `total` es el total en dólares, no el total en pesos, por lo que debería de tomar el parámetro en pesos. Entiendo que este parámetro no viene en el objeto de respuesta, se levantó la incidencia para esta y demás correcciones, la dejo añadida en la sección de incidencias vinculadas.

[adjunto]
2. Al eliminar la búsqueda (x) por fecha o por texto, no se actualiza automáticamente el listado

[adjunto]

3. Aunque el número de elementos por página sea 50, solo se muestran 10 inicialmente. Los restantes están disponibles, pero solo se visualizan tras seleccionar la opción manualmente.

[adjunto]
