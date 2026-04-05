---
jira_key: "PED-275"
aliases: ["PED-275"]
summary: "API - Refactor - Al crear o editar usuario hay error con la provinciay localidad"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2023-11-22 10:47"
updated: "2023-11-28 17:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-275"
---

# PED-275: API - Refactor - Al crear o editar usuario hay error con la provinciay localidad

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2023-11-22 10:47 |
| Actualizado | 2023-11-28 17:19 |
| Etiquetas | ninguna |
| Jira | [PED-275](https://bluinc.atlassian.net/browse/PED-275) |

## Relaciones

*Sin relaciones*

## Descripcion

### Al crear POST


{{API_URL}}/v1/clients
se envia `provinceId` y `localityId` y guarda sin devolver algun error

Ej: 

```json
...
"provinceId": 1,
"localityId": 20891,
```



### Al editar el cliente PATCH 


[https://gamma.api.orders.lio.red/v1/clients/78109](https://gamma.api.orders.lio.red/v1/clients/78109)


```json
 {
    "clientCode": "078109",
    "taxIdentificationNumber": "30232323",
    "clientName": "Ezequiel",
    "commercialName": "Ezetest0101",
    "provinceId": 1,
    "cityCode": 20891,
    "clientAddress": "234rasfcsfe wswefsdf sd",
    "postalCode": 4534,
    "taxId": 2,
    "identityDocument": 1,
    "whaPhone": "1152323232",
    "phone1": "01111111111",
    "phone2": "",
    "email": "asd1231969623@gmail.com"
}
```



### **Al obtener los datos del nuevo cliente GET**

### [https://gamma.api.orders.lio.red/v1/clients/78109](https://gamma.api.orders.lio.red/v1/clients/78109)
**Despues de crear**


`provinceId -> codigo de provincia.  -> Devuelve 0`
`cityCode   -> codigo de localidad -> Devuelve 0`

**Despues de editar**

`provinceId -> codigo de provincia.  -> Devuelve 0`

`cityCode   -> codigo de localidad -> Devuelve 2089 Devuelve otro id se guardo el 20891`

```
{
    "clientCode": "078109",
    "clientName": "Ezequiel",
    "commercialName": "Ezetest0101",
    "clientAddress": "234rasfcsfe wswefsdf sd",
    "clientCity": "",
    "cityCode": 0,
    "postalCode": 4534,
    "phone1": "01111111111",
    "phone2": "",
    "fax": "",
    "taxId": 2,
    "contactName": "",
   ...
   
    "addressDirection": "",
    "email": "asd1231969623@gmail.com",
    "password": "",
    "birthCountry": "",
    "bankCountry": "",
    ...
    "taxIdentificationNumber": "30232323",
    "insuredLimit": "",
    "taxCode": "",
    ...
    "advanceAccount": "",
    "withholdingTax": "",
    "identityDocument": "1",
    ...
    "website": 0,
    "clientId": 78109,
    "postalCodeId": "",
    "countryId": 0,
    "cityId": 0,
    "provinceId": 0,
    "clientGroupId": 0,
    ...
    "registrationDate": "2023-11-22 09:14:15",
    "paymentMethodCode": "",
    "verified": 0,
    "web": "---",
    ...
    "profile": 1,
    "perception": "",
    "perceptionExpiry": "",
    "companyCode": 4,
    "belongsCompany": "",
    "excludePerception": "0",
    "specialPrice": "",
    "clientLo": "",
    "specialPriceFromCost": "",
    "productecaId": "",
    "whaPhone": "1152323232",
    "groupar": ""
}
```
