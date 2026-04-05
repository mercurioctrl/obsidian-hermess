---
jira_key: "PED-63"
summary: "API - Feat - Agregar Client"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2023-09-11 15:22"
updated: "2024-04-05 05:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-63"
---

# PED-63: API - Feat - Agregar Client

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2023-09-11 15:22 |
| Actualizado | 2024-04-05 05:02 |
| Etiquetas | ninguna |
| Jira | [PED-63](https://bluinc.atlassian.net/browse/PED-63) |

## Descripción

Endpoint.

```
POST {API_URL}/v1/clients
```

Payload a enviar.

```
{
    "cuil": "20131313390",
    "nombre": "COLONEL CLAUDIO LIVIO",
    "razonSocial": "",
    "provincia": "",
    "location": "",
    "localityId": 3681,
    "address": "ANDRES FERREYRA 2685",
    "postalCode": 1678,
    "category": 3,
    "typeDocument": 1,
    "telephone": "2235678123",
    "telephone2": "223434545",
    "email": "test@gmail.com",
    "commercialName": "COLONEL CLAUDIO LIVIO",
    "provinceId": 2,
    "localidad": "CASEROS (PDO. 3 DE FEBRERO)"
}
```

- Se encarga de agregar un client nuevo y en el mismo paso agregar una direccion en DirCli.
