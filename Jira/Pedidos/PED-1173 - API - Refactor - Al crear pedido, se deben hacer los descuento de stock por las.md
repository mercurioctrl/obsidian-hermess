---
jira_key: "PED-1173"
aliases: ["PED-1173"]
summary: "API - Refactor - Al crear pedido, se deben hacer los descuento de stock por las partes que se encuentran dentro del kit"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-28 16:35"
updated: "2025-12-15 15:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1173"
---

# PED-1173: API - Refactor - Al crear pedido, se deben hacer los descuento de stock por las partes que se encuentran dentro del kit

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-28 16:35 |
| Actualizado | 2025-12-15 15:49 |
| Etiquetas | ninguna |
| Jira | [PED-1173](https://bluinc.atlassian.net/browse/PED-1173) |

## Relaciones

- **Padre:** [[PED-1170]] Kits

## Descripcion

Según lo conversado, necesitamos refactorizar el flujo para que, al ejecutar el recurso:

```
POST {API_URL}/v1/makeSale
```

el descuento de stock se aplique **ítem por ítem** y no al kit completo. En teoría esto ya debería ocurrir, ya que en el pedido nunca se registra el kit como tal, sino los ítems individuales asociados mediante **kitId**.

Como parte del refactor, debemos **propagar el kitId** a las tablas nuevas. Específicamente:

- `[NewBytes_DBF].[dbo].[albclil].kitId`


- `[NB_WEB].[dbo].[registro_stock].kitId`
