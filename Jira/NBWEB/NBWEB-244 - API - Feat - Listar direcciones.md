---
jira_key: "NBWEB-244"
aliases: ["NBWEB-244"]
summary: "API - Feat - Listar direcciones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-08 14:45"
updated: "2023-03-06 10:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-244"
---

# NBWEB-244: API - Feat - Listar direcciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-08 14:45 |
| Actualizado | 2023-03-06 10:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-244](https://bluinc.atlassian.net/browse/NBWEB-244) |

## Relaciones

- **Padre:** [[NBWEB-2 - API - Mi cuenta|NBWEB-2]] API - Mi cuenta
- **blocks:** [[NBWEB-285 - APP - Feat - Mi cuenta - Listar direcciones|NBWEB-285]] APP - Feat - Mi cuenta - Listar direcciones

## Descripcion

```
GET {{API_URL}}/v1/miCuenta/shippingAddress
```

```json
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
