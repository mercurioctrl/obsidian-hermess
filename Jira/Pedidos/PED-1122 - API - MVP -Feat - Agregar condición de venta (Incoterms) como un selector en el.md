---
jira_key: "PED-1122"
aliases: ["PED-1122"]
summary: "API - MVP -Feat - Agregar condición de venta (Incoterms) como un selector en el detalle de la orden"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-09-29 10:01"
updated: "2025-11-10 10:02"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/PED-1122"
---

# PED-1122: API - MVP -Feat - Agregar condición de venta (Incoterms) como un selector en el detalle de la orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-09-29 10:01 |
| Actualizado | 2025-11-10 10:02 |
| Etiquetas | MVPLaset |
| Jira | [PED-1122](https://bluinc.atlassian.net/browse/PED-1122) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **has action item:** [[PED-1121 - APP - MVP -Feat - Agregar condición de venta (Incoterms) como un selector en el|PED-1121]] APP - MVP -Feat - Agregar condición de venta (Incoterms) como un selector en el detalle de la orden
- **action item from:** [[PED-1120 - API - MVP - Feat - Agregar adenda en el detalle del pedido (por default con los|PED-1120]] API - MVP - Feat - Agregar adenda en el detalle del pedido (por default con los datos bancarios de Laset)
- **action item from:** [[PED-1161 - API - MVP - Repositorio incoterms|PED-1161]] API - MVP - Repositorio incoterms

## Descripcion

-Opciones de Incoterm

FCA (ponerlo como predeterminado)

CIF

FOB

EXW

CFR

CIP

CPT



Estas opciones puedo dejarlas hardcodeadas en el front o puede ser un repo como prefieras catri
esta tarea debe contemplar el repo y que se pueda editar la orden para agregar / editar / leer el incoterm del detalle de una orden
 

Recordar que esto es parte de la Adenda ( es la condición de venta)
puede editarse aparte con:

---

Usando el repositorio `[NewBytes_DBF].[dbo].[FP_Incoterms]` utilizaremos la logica para guardarle el incoterm al pedido dentro de `[NewBytes_DBF].[dbo].[pedclit].incotermId`

Se deben crear los indices adecuados para que la incorporación del repositorio en el de ordenes sea sin perdida de performance

```
PATCH /v1/orders/{branch}-{order}
```

```
{
    "incotermId": 1
}
```

También modificaremos en GET para poder obtenerlo

```
{
    "date": "2025-10-15 11:08:49",
    "makeSaleDate": null,
    "orderNumber": "10425820",
    "branchNumber": "0002",
    "incotermId": 1, <--- SE AGREGA
    "incotermCode": "CFR", <--- SE AGREGA
    "albnumNumber": null,
    "realAlbumNumber": null,
    "clientEmail": null,
    "clientName": "MASTER COMPUTERS SAS",
    "clientId": 92236,
    "userId": 0,
    "observation": null,
    "status": "P",
    "invoice": null,
    "token": null,
    "voucherId": null,
    "seller": "Anabel",
    "sellerId": "72",
    "sellerCreator": "Anabel Obari",
    "sellerIdCreator": "72",
    "items": [
```
