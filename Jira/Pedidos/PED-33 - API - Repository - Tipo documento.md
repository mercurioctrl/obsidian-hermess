---
jira_key: "PED-33"
aliases: ["PED-33"]
summary: "API - Repository - Tipo documento"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-17 16:43"
updated: "2023-08-18 17:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-33"
---

# PED-33: API - Repository - Tipo documento

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-17 16:43 |
| Actualizado | 2023-08-18 17:04 |
| Etiquetas | ninguna |
| Jira | [PED-33](https://bluinc.atlassian.net/browse/PED-33) |

## Relaciones

- **Padre:** [[PED-7 - Repositorios y base del proyecto|PED-7]] Repositorios y base del proyecto

## Descripcion

```
GET {API_URL}/v1/taxDocuments
```

```
[
  {
    "code": 0,
    "description": "CI Policía Federal",
    "taxDocumentsId": 6
  },
  {
    "code": 80,
    "description": "CUIT",
    "taxDocumentsId": 1
  },
  {
    "code": 89,
    "description": "LE",
    "taxDocumentsId": 3
  },
  {
    "code": 90,
    "description": "LC",
    "taxDocumentsId": 2
  },
  {
    "code": 94,
    "description": "Pasaporte",
    "taxDocumentsId": 5
  },
  {
    "code": 96,
    "description": "DNI",
    "taxDocumentsId": 4
  }
]
```

```
SELECT TOP (1000) [ndocidenti] as code
      ,[Descripcion] as description
      ,[Id_TipoDocumentoInterno] as taxDocumentsId
  FROM [NewBytes_DBF].[dbo].[FP_DocumentosAFIP]
  WHERE Id_TipoDocumentoInterno is not null
```
