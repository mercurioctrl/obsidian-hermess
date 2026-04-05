---
jira_key: "COM-165"
aliases: ["COM-165"]
summary: "API - Feat - Agregar cotizacion y cotizacion fiscal"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-01-20 07:56"
updated: "2025-01-24 16:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-165"
---

# COM-165: API - Feat - Agregar cotizacion y cotizacion fiscal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-20 07:56 |
| Actualizado | 2025-01-24 16:39 |
| Etiquetas | ninguna |
| Jira | [COM-165](https://bluinc.atlassian.net/browse/COM-165) |

## Relaciones

- **Padre:** [[COM-77]] Editar orden de compra
- **has action item:** [[COM-166]] APP - Feat - Agregar cotizacion y cotizacion fiscal

## Descripcion

```
GET {API_URL}/v1/providerOrder/{providerOrdeId}
```

```
{
    "response": {
        "orderNumber": 11455,
        "providerId": "001978",
        "providerName": "AEA APARATOS ELECTRONICOS AUTOMATICOS",
        "observation": "",
        "status": "P",
        "voucherPurchaseId": "",
        "buyerName": "Carou Agustin",
        "buyerId": 67,
        "currencyQuote": 1, <-- SE AGREGA
        "currencyFiscalQuote": 1, <-- SE AGREGA
        "distributeTaxes": [],
        "items": [
            {
                "id": 119854,
                "title": "SELECTOR A PALANCA 7000N",
                "sku": "5200050",
                "price": {
                    "value": 6580.449,
                    "iva": 21,
                    "finalPrice": 7962.34329
                },
                "warranty": "12 meses",
                "amount": 10,
                "position": null,
                "taxPosition": null,
                "amountEntered": "10.000"
            }
        ]
    }
}
```

```
PATCH {API_URL}/v1/providerOrder/{providerOrdeId}
```

```
{
  "id":119854,
  "currencyFiscalQuote":10,
  "currencyQuote": 6580.44
}
```



## Parametros en la tabal que afectaremos

```
  [NewBytes_DBF].[dbo].[PedProT].nvaldiv_FISCAL

  [NewBytes_DBF].[dbo].[PedProT].nValDiv
```





Actualizado 21/01/25:

Al crear una orde se debe incializar los valores de 

`[PedProT].nvaldiv_FISCAL`

`[PedProT].nValDiv`

Se debe implementar el recurso PATCH /providerOrder/{orderId}/head

El cual permitira extender a proximos ajustes que relacionados a la cabecera de la orden. como

```
"currencyFiscalQuote":10,
"currencyQuote": 6580.44
```
