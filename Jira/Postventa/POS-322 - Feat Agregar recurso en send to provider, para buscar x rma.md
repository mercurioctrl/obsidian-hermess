---
jira_key: "POS-322"
aliases: ["POS-322"]
summary: "Feat : Agregar recurso en send to provider, para buscar x rma "
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2024-12-20 14:36"
updated: "2025-01-27 17:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-322"
---

# POS-322: Feat : Agregar recurso en send to provider, para buscar x rma 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2024-12-20 14:36 |
| Actualizado | 2025-01-27 17:26 |
| Etiquetas | ninguna |
| Jira | [POS-322](https://bluinc.atlassian.net/browse/POS-322) |

## Relaciones

- **relates to:** [[POS-323]] APP - Informacion proveedor x RMA ID

## Descripcion

```
{{API_URL}}/v1/getProviderInfoByRma?rmaId=34767
```





```
{
    "itemId": "102289",
    "description": "DISCO SSD GIGABYTE 240 GB",
    "serial": "SN224208937160",
    "brandId": "4",
    "brandDescription": "GIGABYTE                                          ",
    "afterSaleId": "34767",
    "afterSaleDetailId": "58565",
    "afterSaleInboundDate": "2024-04-30 09:53:49.987",
    "providerId": "88",
    "providerDescription": "New Bytes INC                      ",
    "categoryId": "56",
    "categoryDescription": "DISCOS SSD",
    "statusId": "3",
    "statusDescription": "Acreditar",
    "warehouseId": "2",
    "warehouseDescription": "Servicio Técnico",
    "isRecovery": "1",
    "sended": "0",
    "providerOrderRma": null
}
```
