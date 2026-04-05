---
jira_key: "POS-36"
summary: "API - Feat - Ver detalle de pre ingreso"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-26 08:58"
updated: "2022-10-14 09:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-36"
---

# POS-36: API - Feat - Ver detalle de pre ingreso

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-26 08:58 |
| Actualizado | 2022-10-14 09:34 |
| Etiquetas | ninguna |
| Jira | [POS-36](https://bluinc.atlassian.net/browse/POS-36) |

## Descripción

Se trata del recurso encargado de mostrar los detalles de un pre ingreso.

```
GET {API_URL}/v1/preAftersales/{preAftersalesId}
```

Retorna

```
[ 
  {
    "productDescription": "TECLADO DUCKY TKL",
    "invoiceNumber": "A0020000432",
    "quantity": 1,
    "failType": 1,
    "failTypeDescription": "Daño fisico",
    "serialNumber":"WQEQWEWQE",
    "productId": 34234,
    "contactNumber": "1243141242",
    "date": "2022-06-26T21:24:44.65",
    "clientId": "019227",
    "clientName": "Bartolomeo J simpson",
    "userId": 7463,
    "userName": "bart"
  },
    {
    "productDescription": "TECLADO DUCKY TKL",
    "invoiceNumber": "A0020000432",
    "quantity": 1,
    "failType": 1,
    "failTypeDescription": "Daño fisico",
    "serialNumber":"WQEQWEWQE",
    "productId": 34234,
    "contactNumber": "1243141242",
    "date": "2022-06-26T21:24:44.65",
    "clientId": "019227",
    "clientName": "Bartolomeo J simpson",
    "userId": 7463,
    "userName": "bart"
  },
]
```

Es el mismo objeto que las cabeceras, pero se agrega el serial y esta desagrupado.
