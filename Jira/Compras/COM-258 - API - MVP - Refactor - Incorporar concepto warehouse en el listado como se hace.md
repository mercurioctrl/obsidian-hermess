---
jira_key: "COM-258"
aliases: ["COM-258"]
summary: "API - MVP - Refactor - Incorporar concepto warehouse en el listado como se hace en ordenes de compra incluyendo el filtrado del mismo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-12-11 18:03"
updated: "2025-12-16 14:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-258"
---

# COM-258: API - MVP - Refactor - Incorporar concepto warehouse en el listado como se hace en ordenes de compra incluyendo el filtrado del mismo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-12-11 18:03 |
| Actualizado | 2025-12-16 14:50 |
| Etiquetas | ninguna |
| Jira | [COM-258](https://bluinc.atlassian.net/browse/COM-258) |

## Relaciones

- **Padre:** [[COM-12]] Listar ingresos (despachos de compra)
- **has action item:** [[COM-259]] APP - MVP - Refactor - Incorporar concepto warehouse en el listado como se hace en ordenes de compra incluyendo el filtrado del mismo

## Descripcion

Se debe refactorizar el siguente recurso mostrando el deposito asignado en la orden.

```
GET /v1/providerOrder?warehouse=DE1
```



Se debe agregar los campos `warehouse` y `warehouseDescription` permitiendo posteriormente realizar filtros reutilizando estos campos.

```
GET /v1/providerOrderInbound?warehouse=DE1
```

```
{
    "response": [
        {
            "id": 0,
            "providerOrder": 12719,
            "providerId": "002198",
            "providerName": "TRADER MOTOR - PARISI FERNANDEZ EMMANUEL",
            "dispatchName": "",
            "userId": "59",
            "updated": 0,
            "dispatchDate": "2025-12-09 09:04:09.183",
            "numPed": 12719,
            "fullSerialized": false,
            "total": 65,
            "totalFinal": 71.825,
            "iva": 0,
            "companyCode": 4,
            "providerOrderInboundId": 16257,
            "warehousesId": 1,
            "warehouse": "DE1",---> NUEVO
            "warehouseDescription": "DEPOSITO 1" ---> NUEVO
        },
        ...
],
"pagination": {
    "total": 46,
    "limit": 15,
    "offset": 0
}
```

}
