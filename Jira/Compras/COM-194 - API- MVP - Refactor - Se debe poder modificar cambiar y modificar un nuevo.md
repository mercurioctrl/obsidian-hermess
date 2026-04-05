---
jira_key: "COM-194"
aliases: ["COM-194"]
summary: "API- MVP  - Refactor - Se debe poder modificar cambiar y modificar un nuevo atributo countryId asosiado a las ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Low"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-08-04 15:57"
updated: "2025-09-30 10:17"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-194"
---

# COM-194: API- MVP  - Refactor - Se debe poder modificar cambiar y modificar un nuevo atributo countryId asosiado a las ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Low |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-04 15:57 |
| Actualizado | 2025-09-30 10:17 |
| Etiquetas | MVPLaset |
| Jira | [COM-194](https://bluinc.atlassian.net/browse/COM-194) |

## Relaciones

- **Padre:** [[COM-77]] Editar orden de compra
- **has action item:** [[COM-195]] APP- MVP  - Refactor - Se debe poder modificar cambiar y modificar un nuevo atributo countryId asociado a las ordenes

## Descripcion

Agregaremos el parámetro `countryId` al detalle de las ordenes para leerlo y para editarlo (si no esta, viene en `null`)

```
GET {API_URL}/v1/providerOrder/{providerOrderId}
```

```
{
    "response": {
        "orderNumber": 11266,
        "trackingNumber": null,
        "arrivalDate": null,
        "providerId": "001926",
        "providerName": "MSI",
        "observation": "",
        "status": "s",
        "countryId": 1 <<-- SE AGREGA EL PARAMETRO EN EL GET
        "voucherPurchaseId": "",
        "buyerName": "Huang Natalia",
        "buyerId": 67,
        "currencyQuote": 927,
        "currencyFiscalQuote": 1,
        "distributeTaxes": [],
        "items": [
            {
                "id": 118764,
                "title": "MSI NOTEBOOK KATANA 15 [[B12VFK-1463]] (I7 + 16GB + 1TB + 4060)",
                "sku": "9S7-158571-1463",

...
```

```
PATCH {API_URL}/v1/providerOrder/{purchaseOrderId}/head
```

```
{
  "countryId": 1 <<-- SE AGREGA EN EL PATCH PARA PODER EDITARSE mientras la orden este en status" <> "s", 
}
```



Se debe agrega un nuevo campo a la tabla `PedProT`

```
ALTER TABLE  NewBytes_DBF.dbo.PedProT
ADD countryId INT NULL;
```
