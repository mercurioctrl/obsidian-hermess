---
jira_key: "PED-900"
aliases: ["PED-900"]
summary: "API - Refactor - Agregar parametro \"companyCode\" al repositorio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-12 12:42"
updated: "2024-12-13 07:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-900"
---

# PED-900: API - Refactor - Agregar parametro "companyCode" al repositorio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-12 12:42 |
| Actualizado | 2024-12-13 07:34 |
| Etiquetas | ninguna |
| Jira | [PED-900](https://bluinc.atlassian.net/browse/PED-900) |

## Relaciones

- **Padre:** [[PED-201]] Solicitudes de Alta

## Descripcion

```
GET {API_URL}/v1/clientsRequests?currentPage=1&full=true
```

```
[
    {
        "requestId": 58045,
        "username": "komoxo5579",
        "email": "komoxo5579@lofiey.com",
        "emailConfirmed": false,
        "socialReason": "Yajafo7798",
        "fantasyName": "Yajafo7798",
        "dni": 44567897,
        "name": "Fgdgdfg",
        "cuit": "33456789",
        "telephone": "",
        "cellPhone": "",
        "secondaryEmail": "",
        "companyWebsite": "",
        "howYouKnowUs": "",
        "date": "2024-12-11 17:31:14",
        "provinceId": "1",
        "taxType": 7,
        "zipCode": "2345",
        "whaPhone": "",
        "address": "yajafo7798",
        "dniOcuit": 4,
        "localityId": "20891",
        "companyCode": 4 <<- ESTE SE AGREGA
    },
    {
        "requestId": 58044,
        "username": "nebaw85674",
        "email": "nebaw85674@pokeline.co


```
