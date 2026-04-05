---
jira_key: "LIO-47"
aliases: ["LIO-47"]
summary: "APP - Refactor - Crear formularios de registro especifico para empresas e individuos - Añadir razón social al registrar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-06-14 15:15"
updated: "2025-01-22 12:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-47"
---

# LIO-47: APP - Refactor - Crear formularios de registro especifico para empresas e individuos - Añadir razón social al registrar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-14 15:15 |
| Actualizado | 2025-01-22 12:47 |
| Etiquetas | ninguna |
| Jira | [LIO-47](https://bluinc.atlassian.net/browse/LIO-47) |

## Relaciones

- **Padre:** [[LIO-11 - Proceso de registro sencillo para los vendedoresCompradores|LIO-11]] Proceso de registro sencillo para los vendedores/Compradores
- **relates to:** [[LIO-46 - API - Refactor - Crear formularios de registro especifico para empresas e|LIO-46]] API - Refactor - Crear formularios de registro especifico para empresas e individuos - Añadir razón social
- **has action item:** [[LIO-178 - API - Refactor - Devolver un mensaje concreto cuando el recurso de padron, no|LIO-178]] API - Refactor - Devolver un mensaje concreto cuando el recurso de padron, no encuentra el "cuit" buscado

## Descripcion

Realizaremos un refactor para que al enviar la petición de registro, se añada a la carga útil la razón social `commercialName` que se obtiene del objeto de respuesta `taxRegister`, adicional a esto para el parámetro que enviamos `fullName` lo tomaremos el `clientName`.



```
{{API_URL}}/v4/auth/taxRegister
```

```
{{API_URL}}/v4/auth/register
```

[adjunto]
```
{
    "clientName": "ANCHOVERRI PONCE NICOLAS RODRIGO",
    "commercialName": "ANCHOVERRI PONCE NICOLAS RODRIGO",
    "countryId": 7,
    "cityCode": "1449",
    "taxId": 20331854493,
    "contactName": "ANCHOVERRI PONCE NICOLAS RODRIGO",
    "invoiceSeries": null,
    "addressDirection": null,
    "email": null,
    "provinceId": 2,
    "provinceName": "BUENOS AIRES ( BS. AS )",
    "cityId": 1452,
    "clientCity": "BANFIELD",
    "clientCityAfip": "LOMAS DE ZAMORA",
    "postalCodeId": null,
    "clientAddress": "ALSINA 1977",
    "postalCode": "1832",
    "niva": 1,
    "typeDocument": 1
}
```

```
{
    "document": 
    "fullName": <----------------------- Se obtiene de clientName
    "businessName" <-------------------- Se obtiene de commercialName 
    "email": 
    "password": 
}
```
