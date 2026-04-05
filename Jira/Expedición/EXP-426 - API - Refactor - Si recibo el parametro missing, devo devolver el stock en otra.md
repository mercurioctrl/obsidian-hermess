---
jira_key: "EXP-426"
aliases: ["EXP-426"]
summary: "API - Refactor - Si recibo el parametro missing, devo devolver el stock en otra columna"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-05 09:50"
updated: "2024-08-08 03:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-426"
---

# EXP-426: API - Refactor - Si recibo el parametro missing, devo devolver el stock en otra columna

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-05 09:50 |
| Actualizado | 2024-08-08 03:00 |
| Etiquetas | ninguna |
| Jira | [EXP-426](https://bluinc.atlassian.net/browse/EXP-426) |

## Relaciones

- **Padre:** [[EXP-424]] Controles de stock al despachar

## Descripcion

Según la historia [link](https://lioteam.atlassian.net/browse/EXP-425)  si se recibe el parámetro `missing:true` en el recurso 

```
POST {API_URL}/v1/ordersRefund/{PEDIDO}
```

Entonces hago la devolución normalmente, pero el stock en lugar de agregarlo donde siempre (nstock o nstock_lo) lo voy a agregar en `[NewBytes_DBF].[dbo].[stocks].[nstock_ctrl]`

De esta forma evitamos que se agregue a stock y se vuelva a comprar algo que no esta fisicamente.
