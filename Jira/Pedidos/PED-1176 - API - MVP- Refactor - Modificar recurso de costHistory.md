---
jira_key: "PED-1176"
aliases: ["PED-1176"]
summary: "API - MVP- Refactor - Modificar recurso de costHistory"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-12-09 15:12"
updated: "2025-12-10 15:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1176"
---

# PED-1176: API - MVP- Refactor - Modificar recurso de costHistory

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-12-09 15:12 |
| Actualizado | 2025-12-10 15:22 |
| Etiquetas | ninguna |
| Jira | [PED-1176](https://bluinc.atlassian.net/browse/PED-1176) |

## Relaciones

- **Padre:** [[PED-1115 - API - MVP - Mejora - Agregar al selector de costo el país (ISO 3166-1 alfa-3)y|PED-1115]] API - MVP - Mejora - Agregar al selector de costo el país (ISO 3166-1 alfa-3)y depósito
- **has action item:** [[PED-1123 - APP - MVP - Refactor - agregar otra opción en el selector de costo para|PED-1123]] APP - MVP - Refactor - agregar otra opción  en el selector de costo para promediar desde 2 “órdenes distintas” teniendo como campos cantidad y costo
- **is duplicated by:** [[PED-1177 - Deprecada - API - Refactor - Agregar al repositorio costHistory la información|PED-1177]] Deprecada - API - Refactor - Agregar al repositorio costHistory la información de "cantidad" para esa compra

## Descripcion

Dado que es necesario según algunos casos mostrar origen de la orden de compra y depósito/alamacen así como el proveedor donde esta la mercadería para que se asocien visualmente al costo elegido, es necesario mostrar el origen tanto del depósito como del proveedor



Ademas es necesario agregar el availableStock de cada uno, esto es la cantidad que se compro en cada compra, para posteriormente que el front pueda hacer promedios entre las cantidades.

Modificar el obj del siguiente recurso:

```
GET {API_URL}/v1/items/118151/costHistory
```

```
[
    {
        "cost": 600,
        "currencyQuote": 1085,
        "invoiceDate": "2025-03-31 15:16:58",
        "provider":{
          "cnompro": "RMA",
          "countryId": 2, 
          "countryDescription": "España", 
          "countryCode": "Es" 
        }
        "warehouse":{
          "warehouseId": 1, 
          "warehouseName": "DEPOSITO 1" 
          "warehouseCode": "DE1", 
          "countryId": 2,
          "countryDescription": "España", 
          "countryCode": "Es" 
        },
        "availableStock":7 // NUEVO PARAMETRO
    },
    
  ...
]
```
