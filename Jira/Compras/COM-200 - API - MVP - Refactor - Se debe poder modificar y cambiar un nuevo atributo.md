---
jira_key: "COM-200"
aliases: ["COM-200"]
summary: "API - MVP - Refactor - Se debe poder modificar y cambiar un nuevo atributo warehousesId asociado a las ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-30 11:37"
updated: "2025-11-14 14:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-200"
---

# COM-200: API - MVP - Refactor - Se debe poder modificar y cambiar un nuevo atributo warehousesId asociado a las ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-30 11:37 |
| Actualizado | 2025-11-14 14:45 |
| Etiquetas | ninguna |
| Jira | [COM-200](https://bluinc.atlassian.net/browse/COM-200) |

## Relaciones

- **Padre:** [[COM-38]] Ver orden de compra
- **has action item:** [[COM-201]] APP - MVP - Refactor - Se debe poder modificar y cambiar un nuevo atributo warehousesId asociado a las ordenes
- **blocks:** [[PED-1115]] API - MVP - Mejora - Agregar al selector de costo el país (ISO 3166-1 alfa-3)y depósito
- **relates to:** [[COM-227]] API - MVP - Review - Al editar una orden no guarda el depósito cuando lo seleccionas y después volves a abrirlo  (da success pero al cerrar y abrir no aparece)

## Descripcion

Agregaremos el parámetro `warehousesId` al detalle de las ordenes para leerlo y para editarlo (si no esta, viene en `null`)

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
        "countryId": 1 
        "warehousesId": 2 <<-- SE AGREGA EL PARAMETRO EN EL GET
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
  "warehousesId": 2 <<-- SE AGREGA EN EL PATCH PARA PODER EDITARSE mientras la orden este en status" <> "s", 
}
```

```
{
  "success": true,                    // true o false
  "message": "Se guardo el deposito",     // Descripción opcional
  "data": {}                          // Objeto con datos devueltos o null
}
```

Se debe agrega un nuevo campo a la tabla `PedProT`

```
ALTER TABLE  NewBytes_DBF.dbo.PedProT
ADD warehousesId INT NULL;
```
