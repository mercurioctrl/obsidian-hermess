---
jira_key: "INV-295"
aliases: ["INV-295"]
summary: "API - Review - En el historial de stock no se visualizan los movimientos que se producen al eliminar un pedido"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-21 18:33"
updated: "2025-12-26 15:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-295"
---

# INV-295: API - Review - En el historial de stock no se visualizan los movimientos que se producen al eliminar un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-21 18:33 |
| Actualizado | 2025-12-26 15:38 |
| Etiquetas | ninguna |
| Jira | [INV-295](https://bluinc.atlassian.net/browse/INV-295) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

Luego de hacer algunas pruebas de generar/eliminar un pedido pude observar que el recurso solo muestra los registros de cuando se crea, pero no los de su eliminación.

Por ejemplo en el item 

```
SELECT * FROM NB_WEB.dbo.registro_stock WHERE codigo = 119480
ORDER BY fecha desc
```

podemos ver que existen ambos movimientos

[adjunto]
Sin embargo al visualizar el registro vemos solo aquellos generados por `makeSaleService`

```
GET {API_URL}/stock-history?itemId=119480&warehouseId=2&between=21-11-2025_21-12-2025&currentPage=1&itemsPerPage=100
```

```
{
    "success": true,
    "data": [
        {
            "itemId": "119480",
            "warehouseId": 2,
            "date": "2025-12-21T18:17:35.563000-03:00",
            "document": "R-0002-00629055",
            "agent": "master",
            "source": "Generar Pedido | MakeSaleService.php",
            "quantity": -4,
            "stockPrev": 157,
            "stockPost": 153,
            "bucketsPrev": {
                "nstock_lo": 0,
                "nstock": 157,
                "nstock_en_cola": 0,
                "nstock_d1": 0,
                "nstock_reserva_pedidos": 4,
                "nstock_lo_reserva_pedidos": 0,
                "nstock_postventa": 0
            },
            "extraInfo": {
                "warehouseName": "SAFcom",
                "details": "190.189.118.96Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.3637b8b2542d52"
            }
        },
        {
            "itemId": "119480",
            "warehouseId": 2,
            "date": "2025-12-21T18:16:41.317000-03:00",
            "document": "R-0002-00629055",
            "agent": "master",
            "source": "Generar Pedido | MakeSaleService.php",
            "quantity": -4,
            "stockPrev": 157,
            "stockPost": 153,
            "bucketsPrev": {
                "nstock_lo": 0,
                "nstock": 157,
                "nstock_en_cola": 0,
                "nstock_d1": 0,
                "nstock_reserva_pedidos": 4,
                "nstock_lo_reserva_pedidos": 0,
                "nstock_postventa": 0
            },
            "extraInfo": {
                "warehouseName": "SAFcom",
                "details": "190.189.118.96Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.3637b8b2542d52"
            }
        }
    ],
    "pagination": {
        "total": 0,
        "currentPage": 1,
        "itemsPerPage": 100,
        "totalPages": 0
    }
}
```
