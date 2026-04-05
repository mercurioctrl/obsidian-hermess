---
jira_key: "POS-323"
aliases: ["POS-323"]
summary: "APP - Informacion proveedor x RMA ID"
status: "Finalizada"
type: "Historia"
priority: "Low"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2024-12-20 16:36"
updated: "2025-01-27 17:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-323"
---

# POS-323: APP - Informacion proveedor x RMA ID

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Low |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2024-12-20 16:36 |
| Actualizado | 2025-01-27 17:26 |
| Etiquetas | ninguna |
| Jira | [POS-323](https://bluinc.atlassian.net/browse/POS-323) |

## Relaciones

- **relates to:** [[POS-322]] Feat : Agregar recurso en send to provider, para buscar x rma 

## Descripcion

La idea es agregar un botón en la pestaña de proveedores para facilitarle a dani la busqueda de postventas que tiene perdidas, dado que no es muy ductil con el tema de los filtrados etc. 



Se creo un recurso en el backend para esto



```
{{API_URL}}/v1/getProviderInfoByRma?rmaId=34767
```



Que devuelve 

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



Mi idea era simular esto:





[adjunto]
Pero en lo posible hacerlo lo mas APB posible..



Cuando lo veas, avisame y nos juntamos que te explico cuales son los campos importantes /  a resaltar y creaneamos que podemos mostrarle o no para que no se vuelva loco
