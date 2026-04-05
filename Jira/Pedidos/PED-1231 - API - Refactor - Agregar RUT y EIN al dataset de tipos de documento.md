---
jira_key: "PED-1231"
aliases: ["PED-1231"]
summary: "API - Refactor - Agregar RUT y EIN al dataset de tipos de documento"
status: "Finalizada"
type: "Tarea"
priority: "Low"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-06 08:06"
updated: "2026-01-27 14:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1231"
---

# PED-1231: API - Refactor - Agregar RUT y EIN al dataset de tipos de documento

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-06 08:06 |
| Actualizado | 2026-01-27 14:16 |
| Etiquetas | ninguna |
| Jira | [PED-1231](https://bluinc.atlassian.net/browse/PED-1231) |

## Relaciones

- **Padre:** [[PED-15]] Clientes
- **has action item:** [[PED-1232]] APP - Refactor - Agregar validacion nueva para RUT y EIN (y otros)

## Descripcion

Agregaremos al repositorio `NewBytes_DBF.dbo.FP_DocumentosAFIP`

- RUT (Uruguay) ############


- RUT (Chile) ##.###.###-#


- EIN (Usa) ##-#######



Y agregaremos a `NewBytes_DBF.dbo.FP_DocumentosAFIP` un nuevo parámetro llamado `mask`

que contendrá cada formato según corresponda, ej: cuit ##-########-#

Adicionalmente refactorizaremos brevemente el recurso

```
GET {API_URL}/v1/taxDocuments
```

```
[
    {
        "code": 0,
        "description": "CI Polic\u00eda Federal",
        "taxDocumentId": 6,
        "mask": ""
    },
    {
        "code": 80,
        "description": "CUIT",
        "taxDocumentId": 1,
        "mask": "##-########-#"
    },
...
]
```

Dejar las query para correr en produccion

Se debe agregar el `Id_TipoDocumentoInterno` de los 3 casos nuevos para que aparezcan
