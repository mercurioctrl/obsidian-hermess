---
jira_key: "PED-498"
aliases: ["PED-498"]
summary: "API - Feat - Agregar parametro para mostrar los acreditados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-18 08:31"
updated: "2024-01-25 16:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-498"
---

# PED-498: API - Feat - Agregar parametro para mostrar los acreditados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-18 08:31 |
| Actualizado | 2024-01-25 16:38 |
| Etiquetas | ninguna |
| Jira | [PED-498](https://bluinc.atlassian.net/browse/PED-498) |

## Relaciones

- **Padre:** [[PED-497 - Ver orden de compra|PED-497]] Ver orden de compra
- **blocks:** [[PED-499 - APP - Feat - Agregar prametro para mostrar los acreditados|PED-499]] APP - Feat - Agregar prametro para mostrar los acreditados

## Descripcion

Agregaremos un parámetro en el recurso que muestra el detalle de un producto ([link](https://lioteam.atlassian.net/browse/PED-82) ) para saber que items tiene acreditado el mismo.

```
GET {API_URL}/v1/orders/{branch-order}
```

Devuelve

```json
{
"agentDescription": "Andrea Altamiranda",
"agentId": 45,
"createdBy": "Andrea Altamiranda",
"albNumber": "10328179",
"invoiceBranch": "0003",
  "invoiceNumber": "00005433",
  "invoiceType": "B",
  "voucherId": 510381,
  "voucherUrl": "https:\/\/omega.comprobantes.lio.red\/voucher\/F\/510381\/6af1b94f4d21a2738ca76c44391d56?show=1"
"items": 
    [
        {
            "orderId": "10281918",
            "branch": "0002",
            "clientId": "019227",
            "description": "ACCESORIOS PHILIPS HUE CABLE 2M RGB LIGHTSTRIP PLUS V4",
            "itemId": "113234",
            "amount": "1.000",
            "refundAmount": "0",  <------- NUEVO PARAEMTRO
            "status": "P",
            "value": "56.79523",
            "iva": "21.00",
            "price": {
                "value": 56.79523,
                "iva": 21,
                "finalPrice": 68.7222283
            }
        },
        {
            "orderId": "10281918",
            "branch": "0002",
            "clientId": "019227",
            "description": "ACCESORIOS GENERICO CABLE MONITOR VGA",
            "itemId": "111770",
            "amount": "1.000",
            "refundAmount": "0",  <------- NUEVO PARAEMTRO
            "status": "P",
            "value": "18.72000",
            "iva": "21.00",
            "price": {
                "value": 18.72,
                "iva": 21,
                "finalPrice": 22.6512
            }
        },
        {
            "orderId": "10281918",
            "branch": "0002",
            "clientId": "019227",
            "description": "SSD SATA 480GB 2.5 PNY",
            "itemId": "109455",
            "amount": "1.000",
            "refundAmount": "1",  <------- NUEVO PARAEMTRO
            "status": "P",
            "value": "74.36000",
            "iva": "21.00",
            "price": {
                "value": 74.36,
                "iva": 21,
                "finalPrice": 89.9756
            }
        }
    ]
}
```

El parámetro en cuestión, solo estará disponible cuando esta enlazada la tabla `[NewBytes_DBF].[dbo].[albclit]` y `[NewBytes_DBF].[dbo].[albclil]` y si no esta disponible devuelve cero.

El dato se obtiene de `[NewBytes_DBF].[dbo].[albclil].[ACREDITADO]`
