---
jira_key: "COM-205"
aliases: ["COM-205"]
summary: "API - MVP - Feat - Agregar columna con el último precio de venta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-09-30 16:14"
updated: "2025-10-17 10:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-205"
---

# COM-205: API - MVP - Feat - Agregar columna con el último precio de venta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-09-30 16:14 |
| Actualizado | 2025-10-17 10:45 |
| Etiquetas | ninguna |
| Jira | [COM-205](https://bluinc.atlassian.net/browse/COM-205) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra
- **has action item:** [[COM-206 - APP - MVP - Feat - Agregar columna con el último precio de venta|COM-206]] APP - MVP - Feat - Agregar columna con el último precio de venta

## Descripcion

Al consultar un orden de compra, la API debe incluir en cada ítem un nuevo campo `lastCostForSale` que muestre el **último precio de venta** registrado para ese artículo (según pedidos “de venta” de cliente **liquidados**), tomando el valor más reciente por fecha de remito.



```
GET {API_URL}/v1/providerOrder/12259
```

Agregar nuevo campo  `lastCostForSale`  dentro de los items para dar información sobre el último precio de venta de ese item

## Alcance (Scope)

- Agregar el campo `lastCostForSale` dentro de cada objeto en `items[]` del endpoint.


- El valor proviene de la tabla de remitos de cliente, seleccionando el **último** (`ORDER BY albclit.dfecalb DESC`) **precio unitario** (`albclil.npreunit`) de remitos con **estado liquidado** (`albclit.ID_ESTADOREMITOCLI >= 2`), filtrando por el `ID_ARTICULO` del ítem.


- Si no existe historial de ventas para ese artículo, devolver `null`.



### Query orientativa no optimizada

```
SELECT TOP(1) albclit.dfecalb, albclit.ID_ESTADOREMITOCLI, albclil.npreunit
  FROM [NewBytes_DBF].[dbo].[articulo]
  LEFT JOIN NewBytes_DBF.dbo.albclil on albclil.ID_Articulo = articulo.ID_ARTICULO
  LEFT JOIN NewBytes_DBF.dbo.albclit ON albclit.ID_NROREMCLI_ENC = albclil.ID_NROREMCLI_ENC
WHERE articulo.ID_ARTICULO = ?  AND ID_ESTADOREMITOCLI>=2
ORDER BY dfecalb DESC
```

Es decir que tomaremos el ultimo `albclil.npreunit`, el mas nuevo (`ORDER BY dfecalb DESC`) de los que ya fueron liquidados (`ID_ESTADOREMITOCLI>=2`)

```
{
    "orderNumber": 12259,
    "trackingNumber": null,
    "arrivalDate": null,
    "providerId": "002320",
    "providerName": "MSI COMPUTER CORP.",
    "observation": "",
    "status": "P",
    "voucherPurchaseId": "",
    "countryId": 7,
    "countryName": "Argentina",
    "buyerName": "Obari Anabel",
    "buyerId": 72,
    "currencyQuote": 1310,
    "currencyFiscalQuote": 0,
    "distributeTaxes": [],
    "items": [
        {
            "id": 123834,
            "title": "ana usada",
            "sku": "ana usada",
            "price": {
                "value": 0,
                "iva": 0,
                "finalPrice": 0
            },
            lastCostForSale:0 // <---- NUEVO
            "warranty": "0 meses",
            "amount": 1,
            "position": null,
            "taxPosition": null,
            "amountEntered": ".000"
        }
    ]
}
```

[adjunto]
## Criterios de aceptación (QA)

- **CA1 – Presencia de campo:** Cada objeto de `items[]` incluye el campo `lastCostForSale`.


- **CA2 – Valor correcto:** Para un artículo con ventas previas, `lastCostForSale` coincide exactamente con el `albclil.npreunit` del remito más reciente por `albclit.dfecalb` con `ID_ESTADOREMITOCLI >= 2`.


- **CA3 – Sin historial:** Si no hay ventas previas para el `ID_ARTICULO`, `lastCostForSale` es `null`.


- **CA4 – Integridad de respuesta:** No se alteran otros campos del contrato actual; no cambia la paginación ni la performance del endpoint más allá de lo razonable (ver CA8).


- **CA5 – Errores:** Ante error en la subconsulta de último precio, la respuesta del endpoint no se rompe: el ítem correspondiente devuelve `lastCostForSale: null` y se loguea el evento.


- **CA6 – Performance:** Se debe mantener la performance de modo tal que el dato debe traerse casi sin afectar el rendimiento. Para que el recurso sea util mantendremos una regla de que como maximo, un pedido con 10 itemas, debe tardar 1 segundo o menos




Corresponde a la tarea 12 de [link](https://docs.google.com/spreadsheets/d/18TUSaVG3bY_lMLunZ3kDCRlLnKpQV-_BPfrtbL4pHNA/edit?usp=sharing)
