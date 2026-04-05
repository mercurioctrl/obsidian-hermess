---
jira_key: "EXP-438"
aliases: ["EXP-438"]
summary: "Despacho envios LIbreOpcion"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-30 14:31"
updated: "2024-09-04 02:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-438"
---

# EXP-438: Despacho envios LIbreOpcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-30 14:31 |
| Actualizado | 2024-09-04 02:39 |
| Etiquetas | ninguna |
| Jira | [EXP-438](https://bluinc.atlassian.net/browse/EXP-438) |

## Relaciones

- **Padre:** [[EXP-6 - Despacho de envios|EXP-6]] Despacho de envios
- **Subtarea:** [[EXP-441 - APP - Refactor - Agregar el numero de Libre Opcion como en pedidos|EXP-441]] APP - Refactor - Agregar el numero de Libre Opcion como en pedidos
- **blocks:** [[EXP-441 - APP - Refactor - Agregar el numero de Libre Opcion como en pedidos|EXP-441]] APP - Refactor - Agregar el numero de Libre Opcion como en pedidos

## Descripcion

Refactorizaremos el recurso para que resuelva en la búsqueda si se escribe directamente el numero de libre opción.

Adicionalemente tambien lo agregaremos como dato al objeto para poder mostrar.

```
GET {API_URL}/v1/shipments
```

```
{
    "response": [
        {
            "date": "2024-08-30 12:01:39",
            "pedido": "X000200591645",
            "idLo": 659782, <<<--- SE AGREGA NUEVO
            "clientId": 43778,
            "clientName": "RUIZ PABLO EXEQUIEL",
            "sellerId": 30,
            "sellerName": "Albarracin Julian",
            "paymentMethod": "Dep\u00f3sito en Banco",
            "dispatch": "OCA PickUp",
            "statusId": 2,
            "statusDescription": "Autorizados. Pendiente a despachar",
            "order": "10367882",
            "branch": "0002",
            "cfactura": null,
            "cnumalb": "00591674",
            "fullSerialized": false,
            "currierId": 4041,
            "currierName": "OCA                                               ",
            "placeId": 13685,
            "placeName": "MENDOZA",
            "provinceId": 12,
            "provinceName": "MENDOZA",
            "zipCode": 5500,
            "shippingLabel": false,
            "token": null,
            "alert": false,
            "idDirCliNbWeb": 19758,
            "paymentMethodId": 3,
            "whoBuild": null,
            "whoAuthorized": null,
            "secretKey": true,
            "facturado": false,
            "joinShipping": false,
            "dropShipping": false,
            "shippingStatus": null,
            "voucherId": null,
            "thirdVoucher": "0"
        },
```
