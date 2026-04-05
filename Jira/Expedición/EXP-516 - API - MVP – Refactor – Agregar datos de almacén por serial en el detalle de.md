---
jira_key: "EXP-516"
aliases: ["EXP-516"]
summary: "API - MVP – Refactor – Agregar datos de almacén por serial en el detalle de serial de un item, dentro de una orden "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-09 09:04"
updated: "2025-11-12 10:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-516"
---

# EXP-516: API - MVP – Refactor – Agregar datos de almacén por serial en el detalle de serial de un item, dentro de una orden 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-09 09:04 |
| Actualizado | 2025-11-12 10:37 |
| Etiquetas | ninguna |
| Jira | [EXP-516](https://bluinc.atlassian.net/browse/EXP-516) |

## Relaciones

- **Padre:** [[EXP-512 - Almacenes multiples|EXP-512]] Almacenes multiples

## Descripcion

```
GET /v1/orders/{pedido}/serials/{itemId}?stockWarehouseId={stockWarehouseId}
```

El endpoint actual devuelve los seriales de un ítem dentro de un pedido. Se requiere **agregar la información de almacén por cada serial**:

- `stockWarehouseId`


- `stockWarehouseCode`


- `stockWarehouseDescription`



Para soportarlo, se incorporará `stockWarehouseId` en `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]` (inicializado en 2 para todo) y se crearán **índices** que mejoren la performance de las búsquedas por pedido/ítem/serial/almacén.



Se agrega el filtro `stockWarehouseId` para poder filtrar si quisiéramos ese ítem solo para el almacén puntual, sino traigo cualquiera que este dentro del pedido sea del almacén que sea

```
{
    "title": "AURICULAR GENIUS HS-05A",
    "id": 4999,
    "sku": "31710011100",
    "mainImage": "20eba63183490636ed457e03b307a1d7.jpg",
    "serial": [
        {
            "serial": "VW205A802711",
            "admissionDate": "30\/05\/2025 17:37",
            "dispatchDate": "30\/05\/2025 17:38",
            "stockWarehouseId": 2, <--
            "stockWarehouseDescription": "SAFcom", <--
            "stockWarehouseCode": "SAF" <--
        },
        {
            "serial": "VW205A802719",
            "admissionDate": "30\/05\/2025 17:37",
            "dispatchDate": "30\/05\/2025 17:38",
            "stockWarehouseId": 2, <--
            "stockWarehouseDescription": "SAFcom", <--
            "stockWarehouseCode": "SAF" <--            
        },
        {
 ...
    ]
}
```

Se crean índices sugeridos si no existían, y **no** se degradan tiempos de respuesta del endpoint.
