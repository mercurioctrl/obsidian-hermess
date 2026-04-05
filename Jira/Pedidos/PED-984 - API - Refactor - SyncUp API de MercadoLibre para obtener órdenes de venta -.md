---
jira_key: "PED-984"
aliases: ["PED-984"]
summary: "API - Refactor - SyncUp API de MercadoLibre para obtener órdenes de venta -> Mensaje de éxito al no completarse la sincronización"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-04-08 09:36"
updated: "2025-04-14 10:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-984"
---

# PED-984: API - Refactor - SyncUp API de MercadoLibre para obtener órdenes de venta -> Mensaje de éxito al no completarse la sincronización

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-04-08 09:36 |
| Actualizado | 2025-04-14 10:49 |
| Etiquetas | ninguna |
| Jira | [PED-984](https://bluinc.atlassian.net/browse/PED-984) |

## Relaciones

- **Padre:** [[PED-915]] MercadoLibre
- **relates to:** [[PED-969]] API - Feat - SyncUp API de MercadoLibre para obtener órdenes de venta

## Descripcion

Vamos a refactorizar el recurso que obtiene las órdenes de Mercado Libre, de modo que, si el proceso falla por cualquier motivo, se devuelva un mensaje explicativo indicando la causa del error.

```
{{API_URL}}/v1/syncUp/mercadolibreOrders
```

Te presento un caso en el que me aparece la respuesta “Sync Up realizado correctamente.“ Sin embargo, el token estaba expirado

[adjunto]
[adjunto]
