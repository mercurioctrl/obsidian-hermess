---
jira_key: "PED-347"
aliases: ["PED-347"]
summary: "API - Refactor - Listar cliente -> Agregar filtros"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-18 09:02"
updated: "2024-01-26 04:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-347"
---

# PED-347: API - Refactor - Listar cliente -> Agregar filtros

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-18 09:02 |
| Actualizado | 2024-01-26 04:35 |
| Etiquetas | ninguna |
| Jira | [PED-347](https://bluinc.atlassian.net/browse/PED-347) |

## Relaciones

- **Padre:** [[PED-16]] Listar clientes
- **blocks:** [[PED-348]] APP - Refactor - Listar cliente -> Agregar filtros
- **is blocked by:** [[PED-358]] API - Listar cliente -> Agregar filtros - Incidencias varias

## Descripcion

Crearemos un recurso para traer los datos principales de los clientes, el mismo tendra el paginado tal como lo utilizamos siempre y mas adelante agregaremos filtros en otras historias

```
GET {API_URL}/v1/clients?sellerId=(vendedor)&provinceId={provincia}
```

```
[
    {
        "date": "2022-05-30 19:36:52",
        "ccodcli": "053669",
        "businessName": "Catriel Mercurio",
        "name": "Catriel Mercurio",
        "clientTaxNumber": "20000000002",
        "email": "defecto@nb.com.ar",
        "phone": "0000",
        "salespersonName": " ",
        "address": null,
        "id": 53669
        "sellerId": "Nombre vendedor" <--- nuevo parametro
        "provinceId": "Provincia"" <----- nuevo parametro
    },
    {
        "date": "2022-05-28 18:48:33",
        "ccodcli": "053392",
        "businessName": "Catriel Mercurio",
        "name": "Catriel Mercurio",
        "clientTaxNumber": "20000000002",
        "email": "defecto@nb.com.ar",
        "phone": "0000",
        "salespersonName": " ",
        "address": null,
        "id": 53392,
        "sellerId": "Nombre vendedor" <--- nuevo parametro
        "provinceId": "Provincia"" <----- nuevo parametro        
    }
]
```
