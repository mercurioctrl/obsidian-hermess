---
jira_key: "POS-3"
aliases: ["POS-3"]
summary: "API - Feat - Listar pre ingresos"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-13 14:25"
updated: "2022-10-04 09:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-3"
---

# POS-3: API - Feat - Listar pre ingresos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-13 14:25 |
| Actualizado | 2022-10-04 09:39 |
| Etiquetas | ninguna |
| Jira | [POS-3](https://bluinc.atlassian.net/browse/POS-3) |

## Relaciones

- **Padre:** [[POS-18 - Pre-Ingresos|POS-18]] Pre-Ingresos
- **Subtarea:** [[POS-38 - API - Feat - Filtros|POS-38]] API - Feat - Filtros
- **Subtarea:** [[POS-39 - API - Refactor - Agregar parametro para mostrar si ya fue procesado|POS-39]] API - Refactor -  Agregar parametro para mostrar si ya fue procesado
- **Subtarea:** [[POS-41 - API - Feat - Agregar paginado|POS-41]] API - Feat - Agregar paginado
- **Subtarea:** [[POS-74 - Revisar Filtro de pre ingreso|POS-74]] Revisar Filtro de pre ingreso
- **blocks:** [[POS-34 - APP - Feat - Listar pre ingresos|POS-34]] APP - Feat - Listar pre ingresos

## Descripcion

Se trata del recurso basico  que permite listar las postventas propiamente dichas, una vez que se pasaron desde el preingreso, o bien se crearon directamente.

```
GET {API_URL}/v1/preAftersales
```

Retorna

```json
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

 Se deben utilizar principalmente las tablas 

`ST_RMACABECERA` y `ST_RMADETALLE`

pero puede haber mas, en ese caso podemos verlo.
