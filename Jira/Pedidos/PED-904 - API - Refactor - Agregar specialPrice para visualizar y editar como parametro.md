---
jira_key: "PED-904"
aliases: ["PED-904"]
summary: "API - Refactor - Agregar specialPrice para visualizar y editar como parametro de los clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2024-12-18 17:10"
updated: "2024-12-20 03:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-904"
---

# PED-904: API - Refactor - Agregar specialPrice para visualizar y editar como parametro de los clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-18 17:10 |
| Actualizado | 2024-12-20 03:59 |
| Etiquetas | ninguna |
| Jira | [PED-904](https://bluinc.atlassian.net/browse/PED-904) |

## Relaciones

- **Padre:** [[PED-600 - EdicionAlta de cliente|PED-600]] Edicion/Alta de cliente
- **has action item:** [[PED-905 - APP - Refactor - Agregar utilidad extra o specialPrice al modal de parámetros|PED-905]] APP - Refactor - Agregar utilidad extra o "specialPrice" al modal de parámetros del cliente

## Descripcion

Agregaremos el parámetro `specialPrice` para ser leído 

```
GET {{API_URL}}/v1/clients/{clientId}
```

```
PATCH {{API_URL}}/v1/clients/{clientId}
```



**Carga útil:**

```
{
    "clientId": 26806,
    "email": "mercurio@nb.com.ar",
    "provinceId": 1,
    "localityId": 20891,
    "address": "Calle falsa 123",
    "cuil": "33567898",
    "clientName": "MERCURIO CATRIEL EDUARDO",
    "commercialName": "BSASPC",
    "postalCode": "1406",
    "telephone": "2343243223",
    "telephone2": "",
    "typeDocument": 4,
    "category": 5,
    "whaPhone": "549113051026",
    "companyCode": 5,
    "profile": 4,
    "currencyId": 1,
    "salespersonId": 12,
    "specialPrice": 50.00 << -- Se agrega tanto para leer como para editar
}
```
