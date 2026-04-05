---
jira_key: "PED-38"
summary: "API - Repository - Medio de envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-20 21:29"
updated: "2023-08-22 11:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-38"
---

# PED-38: API - Repository - Medio de envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-20 21:29 |
| Actualizado | 2023-08-22 11:06 |
| Etiquetas | ninguna |
| Jira | [PED-38](https://bluinc.atlassian.net/browse/PED-38) |

## Descripción

```
GET {{API_URL}}/v1/shippingMethods
```

```
[
  {
    "show": 1,
    "code": "01",
    "description": "Retiro de cliente en Local    ",
    "taxCategory": 1.0,
    "id": 1,
    "shippingMethodId": null
  },
  {
    "show": 0,
    "code": "07",
    "description": "Cargas Terrestes y Aereas     ",
    "taxCategory": 1.0,
    "id": 7,
    "shippingMethodId": null
  },
  {
    "show": 0,
    "code": "08",
    "description": "Cruz del Sur                  ",
    "taxCategory": 1.0,
    "id": 8,
    "shippingMethodId": null
  },
```

```
SELECT TOP (1000) 
    [sitio] as show,
    [ccodtrans] as code,
    [cnomtrans] as 'description',
    [ncategiva] as taxCategory,
    [ID_TRANSPORTISTA] as transporterId,
    [medioEnvioId] as shippingMethodId
FROM [NewBytes_DBF].[dbo].[transpor]

```
