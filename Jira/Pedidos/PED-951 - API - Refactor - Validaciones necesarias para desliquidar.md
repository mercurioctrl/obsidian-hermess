---
jira_key: "PED-951"
aliases: ["PED-951"]
summary: "API - Refactor - Validaciones necesarias para desliquidar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-20 10:03"
updated: "2025-02-21 19:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-951"
---

# PED-951: API - Refactor - Validaciones necesarias para desliquidar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-20 10:03 |
| Actualizado | 2025-02-21 19:24 |
| Etiquetas | ninguna |
| Jira | [PED-951](https://bluinc.atlassian.net/browse/PED-951) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido
- **action item from:** [[PED-152 - API - Feat - Desliquidar pedido|PED-152]] API - Feat - Desliquidar pedido
- **has action item:** [[SNB-2785 - mejoras para el sistema|SNB-2785]] mejoras para el sistema

## Descripcion

A partir de un problema que hubo ([link](https://lioteam.atlassian.net/browse/SNB-2785) ) hice unas pruebas y note que al menos existe una validación que no se esta haciendo ya que probe desliquidar un pedido facturado, y me lo desliquido.

Esto no deberia suceder.

Se debe revisar y refactorizar para lograr que el recurso

```
PATCH {API_URL}/v1/openSale
```

Para que cuando `[NewBytes_DBF].[dbo].[albclit].lfacturado` esta marcado en `true` entonces no se puede hacer y se debe indicar esto mismo en un mensaje de salida.

Por otro lado, aprovecharemos para revisar que el pedido solo puede ser “desliquidado” si esta en uno de los siguientes `ID_STATUS` `IN (1,2)` y si no tiene ningún serial tomado.
