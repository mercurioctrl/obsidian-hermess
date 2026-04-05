---
jira_key: "EXP-328"
aliases: ["EXP-328"]
summary: "API - Feat - Descargar planilla de retiro de currier"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-30 09:26"
updated: "2023-07-04 09:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-328"
---

# EXP-328: API - Feat - Descargar planilla de retiro de currier

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-30 09:26 |
| Actualizado | 2023-07-04 09:33 |
| Etiquetas | ninguna |
| Jira | [EXP-328](https://bluinc.atlassian.net/browse/EXP-328) |

## Relaciones

- **Padre:** [[EXP-325]] Feat - Pestaña seguimiento

## Descripcion

Este recurso se trata sobre descargar una planilla con el siguiente formato (similar) al que adicionalmente agregaría el nombre del currier en el titulo como “ENTREGA DE CORRESPONDENCIA ANDREANI”.

[adjunto]
```
POST {API_URL}/v1/downloadDropTrackingOrders/{DropTrackingOrdersId}
```

Este recurso debe crear un archivo del lado del servidor y facilitar un enlace par su  descarga como hacemos en otros casos.

Es importante destacar que el listado es agrupado por bulto y no por pedido, como se viene haciendo anteriormente.
