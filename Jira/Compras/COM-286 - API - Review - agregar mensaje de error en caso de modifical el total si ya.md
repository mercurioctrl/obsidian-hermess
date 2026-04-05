---
jira_key: "COM-286"
aliases: ["COM-286"]
summary: "API - Review -  agregar mensaje de error en caso de modifical el total si ya fueron escaneados los serials desde EXP"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2026-03-04 08:57"
updated: "2026-03-05 15:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-286"
---

# COM-286: API - Review -  agregar mensaje de error en caso de modifical el total si ya fueron escaneados los serials desde EXP

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2026-03-04 08:57 |
| Actualizado | 2026-03-05 15:12 |
| Etiquetas | ninguna |
| Jira | [COM-286](https://bluinc.atlassian.net/browse/COM-286) |

## Relaciones

- **Padre:** [[COM-8 - Ordenes de compra|COM-8]] Ordenes de compra
- **action item from:** [[COM-287 - APP - Review - Mantener cantidades y mostrar mensaje caso de error al editar|COM-287]] APP - Review - Mantener cantidades y mostrar mensaje caso de error  al editar total

## Descripcion

```
PATCH https://gamma.api.purchases.lio.red/v1/providerOrder/13249
```

payload

```
{
    "id": 123904,
    "amount": 30,
    "price": {
        "value": 0,
        "iva": 0
    },
    "position": null
}

```

si amount es menor que los serials ya tomados desde expedicion en ingresos, se debe retornar un mensaje de error algo como:
Libera serials desde Expedicion para poder modificar el total de esta orden
