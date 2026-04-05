---
jira_key: "PED-954"
aliases: ["PED-954"]
summary: "API - Refactor - Validacion de permisos para desliquidar pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-02-24 12:15"
updated: "2025-02-24 15:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-954"
---

# PED-954: API - Refactor - Validacion de permisos para desliquidar pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-02-24 12:15 |
| Actualizado | 2025-02-24 15:30 |
| Etiquetas | ninguna |
| Jira | [PED-954](https://bluinc.atlassian.net/browse/PED-954) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido

## Descripcion

Este recurso es utilizado para desliquidar un pedido.                             



```
PATCH {{API_URL}}/v1/openSale
```



```
    Route::patch('openSale', [LiquidateController::class, 'openSale']);
```



Se debe agregar validacion de permiso tomado de la tabla 

`NB_WEB.dbo.permisos_agente`el campo `desliquidar` el cual debe estar en 1 para poder permitir la acción.
