---
jira_key: "PED-388"
aliases: ["PED-388"]
summary: "API - Refactor - Listar clientes -> Agregar ultima compra tanto en fecha, como en cantidad de dias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-26 06:47"
updated: "2023-12-27 16:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-388"
---

# PED-388: API - Refactor - Listar clientes -> Agregar ultima compra tanto en fecha, como en cantidad de dias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-26 06:47 |
| Actualizado | 2023-12-27 16:58 |
| Etiquetas | ninguna |
| Jira | [PED-388](https://bluinc.atlassian.net/browse/PED-388) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **blocks:** [[PED-387 - APP - Refactor - Agregaremos informacion del cliente al listado|PED-387]] APP - Refactor - Agregaremos informacion del cliente al listado

## Descripcion

Refactorizaremos el recurso 

```
GET {API_URL}/v1/clients
```

Para poder devolver adicionalmente la fecha de ultima compra en formato “fecha” y  la cantidad de días, hasta el día actual.

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
        "id": 53669,
        "lasPurchase": "21/05/2023", <---- Fecha de ultima compra
        "sinceLastPurchase": 186 <--- Dias desde la ultima compra
    },
    ...
```
