---
jira_key: "PED-1303"
aliases: ["PED-1303"]
summary: "API - Refactor Clientes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2026-02-04 12:39"
updated: "2026-02-13 11:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1303"
---

# PED-1303: API - Refactor Clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2026-02-04 12:39 |
| Actualizado | 2026-02-13 11:00 |
| Etiquetas | ninguna |
| Jira | [PED-1303](https://bluinc.atlassian.net/browse/PED-1303) |

## Relaciones

- **Padre:** [[PED-15]] Clientes
- **has action item:** [[PED-1304]] APP - Refactor - Editar Clientes, cambios en casos internacionales

## Descripcion

Se agregar el countryId a el get , patch y post . de clientes



```powershell
curl --location 'https://gamma.api.orders.lio.red/v1/clients' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data-raw '{
    "cuil": "23-37892693-1",
    "clientName": "Emanuel Ferreyra dev-local",
    "commercialName": "Emanuel Ferreyra dev-local",
    "provinceId": 2,
    "localityId": 4,
    "address": "ANDRES FERREYRA 2685",
    "postalCode": 1678,
    "category": 6,
    "typeDocument": 1,
    "telephone": "2235181916",
    "telephone2": "2235171718",
    "email": "test@gmail.com",
    "whaPhone" : 1164331855,
    "countryId" : 4
}'
```




```powershell
curl --location --request PATCH 'https://gamma.api.orders.lio.red/v1/clients/90713' \
--header 'Content-Type: application/json' \
--data-raw '{"cuil":"40495867","clientName":"Eduardo","commercialName":"Eduardo quinteros","typeDocument":4,"category":7,"address":"Av. Jujuy 1039","postalCode":"2034","telephone":"01148576653","telephone2":"01137465757","whaPhone":"5491139485763","email":"equinteros^@nb.com.ar","clientId":90713,"companyCode":4,"profile":1,"currencyId":1,"salespersonId":12,"specialPrice":0,"paymentTerms":0,"voucherCompanyCode":4, "countryId" : 4}'
```
