---
jira_key: "LIO-38"
summary: "API - Feat - Recurso de consulta en AFIP por cuit"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-11 11:40"
updated: "2025-07-17 10:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-38"
---

# LIO-38: API - Feat - Recurso de consulta en AFIP por cuit

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-11 11:40 |
| Actualizado | 2025-07-17 10:37 |
| Etiquetas | ninguna |
| Jira | [LIO-38](https://bluinc.atlassian.net/browse/LIO-38) |

## Descripción

Utilizando el servicio de comprobantes, se debe proveer un recurso 

```
GET {{API_URL}}/auth/taxRegister
```

```
{
    "clientName": "NB DISTRIBUIDORA MAYORISTA S R L",
    "commercialName": "NB DISTRIBUIDORA MAYORISTA S R L",
    "countryId": 7,
    "cityCode": "A860",
    "taxId": 30709246638,
    "contactName": "NB DISTRIBUIDORA MAYORISTA S R L",
    "invoiceSeries": null,
    "addressDirection": null,
    "email": null,
    "provinceId": 1,
    "provinceName": "CAPITAL FEDERAL ( CAP. FED. )",
    "cityId": 10863,
    "clientCity": "LA PLATA",
    "clientCityAfip": "",
    "postalCodeId": null,
    "clientAddress": "JUJUY AV. 1039",
    "postalCode": "1229",
    "niva": 1,
    "typeDocument": 1
}
```
