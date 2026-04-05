---
jira_key: "NBWEB-285"
summary: "APP - Feat - Mi cuenta - Listar direcciones"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-06-26 20:31"
updated: "2022-07-01 17:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-285"
---

# NBWEB-285: APP - Feat - Mi cuenta - Listar direcciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-26 20:31 |
| Actualizado | 2022-07-01 17:41 |
| Etiquetas | ninguna |
| Jira | [NBWEB-285](https://bluinc.atlassian.net/browse/NBWEB-285) |

## Descripción

Se trata de la sección donde se administran las direcciones de entrega.

Pueden hacerse altas bajas y modificaciones.

```
GET {{API_URL}}/v1/miCuenta/shippingAddress

[
    {
    "direccion": "alguna de prueba 124",
        "telefono": "1530510267",
        "placeId": 1,
        "provinceId": 4,
        "codigoPostal": "1407",
        "predeterminado": true,
        
    },
    {
        "direccion": "Direccion de prueba 234",
        "telefono": "1540329485",
   "placeId": 1,
        "provinceId": 4,
        "codigoPostal": "5000",
        "IdDirCli": "19140",
        "predeterminado": null
    },
    {
        "direccion": "Direccion de pruba",
        "telefono": "423434",
        "localidad": "MAR DEL PLATA                 ",
        "provincia": "BUENOS AIRES ( BS. AS )       ",
        "codigoPostal": "4324",
        "IdDirCli": "19149",
        "predeterminado": "29626"
    }
]
```
