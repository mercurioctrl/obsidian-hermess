---
jira_key: "PED-17"
aliases: ["PED-17"]
summary: "API - Feat - Listar clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-08 08:01"
updated: "2023-08-08 16:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-17"
---

# PED-17: API - Feat - Listar clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-08 08:01 |
| Actualizado | 2023-08-08 16:54 |
| Etiquetas | ninguna |
| Jira | [PED-17](https://bluinc.atlassian.net/browse/PED-17) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes

## Descripcion

Crearemos un recurso para traer los datos principales de los clientes, el mismo tendra el paginado tal como lo utilizamos siempre y mas adelante agregaremos filtros en otras historias

```
GET {API_URL}/v1/clients
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
        "id": 53392
    }
]
```

Repositorios útiles

```
SELECT
    ccodcli,
    cnomcli,
    cnomcom,
    cdircli,
    CONVERT(VARCHAR, FECHA_ALTA, 20) AS FECHA_ALTA,
    ID_CLIENTE,
    cdnicif,
    email,
    ctfo1cli,
    ctfo2cli,
    cnbrage,
    capeage
FROM 
    NewBytes_DBF.dbo.clientes
LEFT JOIN 
    NewBytes_DBF.dbo.agentes 
    ON clientes.ccodage = agentes.ccodage
ORDER BY 
    ID_CLIENTE DESC;
```

Es importante que este recurso sea rapido < 2s
