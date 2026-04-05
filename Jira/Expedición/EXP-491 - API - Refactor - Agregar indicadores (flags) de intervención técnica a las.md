---
jira_key: "EXP-491"
aliases: ["EXP-491"]
summary: "API - Refactor - Agregar indicadores (flags) de intervención técnica a las órdenes de retiros"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-20 12:36"
updated: "2025-06-03 11:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-491"
---

# EXP-491: API - Refactor - Agregar indicadores (flags) de intervención técnica a las órdenes de retiros

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-20 12:36 |
| Actualizado | 2025-06-03 11:07 |
| Etiquetas | ninguna |
| Jira | [EXP-491](https://bluinc.atlassian.net/browse/EXP-491) |

## Relaciones

- **Padre:** [[EXP-439]] Despacho de retiros LibreOpcion
- **has action item:** [[SNB-2003]] Agregar opcion para armado de pc y actualizacion de firmware
- **has action item:** [[EXP-492]] APP - Feat - Agregar indicadores (flags) de intervención técnica a las órdenes de retiro
- **has action item:** [[POS-331]] API - Refactor - Agregar indicadores (flags) de intervención técnica a las órdenes dentro de postventa

## Descripcion

Asi como lo hicimos en [link](https://bluinc.atlassian.net/browse/PED-999)  agregaremos a una orden de retiro las flags de intervención técnica

```
GET {API_URL}/v1/pickUp
```

```
{
    "response": [
        {
            "date": "2025-05-20 12:24:05",
            "pedido": "X000200617916",
            "clientId": 33499,
            "clientName": "MEGATECNOLOGIA SOCIEDAD POR ACCIONES SIMPLIFICADAS",
            "sellerId": 8,
            "sellerName": "Altamiranda Andrea",
            "dispatch": "Retiro de cliente en Local",
            "statusId": 2,
            "statusDescription": "Autorizados. Pendiente a despachar",
            "order": "10408263",
            "branch": "0002",
            "cfactura": "A000600019511",
            "cnumalb": "00617916",
            "fullSerialized": false,
            "shippingLabel": null,
            "token": "8d8c5665eaff72bc61403bc55e16a0",
            "tokenFactura": null,
            "voucherId": "575879",
            "shippingStatus": null,
            "alert": true,
            "whoBuild": null,
            "whoAuthorized": null,
            "secretKey": true,
            "facturado": true,
            "thirdVoucher": 0,
            "idLo": 0,
            "authorizedDate": "2025-05-20 12:31:19.017",
            "companyCode": "5"
            "assemblePc": true, <-- SE AGREGA
            "updateBios": false, <-- SE AGREGA
            "installOS": true <-- SE AGREGA
        },
        {
            "date": "2025-05-15 10:11:45",
            "pedido": "X000200617315",
            "clientId": 87774,
```

Mantener la performance del recurso en los mismos valores para evitar demoras en un recurso que es muy utilizado
