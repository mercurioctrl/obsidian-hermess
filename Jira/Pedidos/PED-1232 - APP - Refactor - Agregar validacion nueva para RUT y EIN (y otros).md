---
jira_key: "PED-1232"
aliases: ["PED-1232"]
summary: "APP - Refactor - Agregar validacion nueva para RUT y EIN (y otros)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-06 08:18"
updated: "2026-01-13 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1232"
---

# PED-1232: APP - Refactor - Agregar validacion nueva para RUT y EIN (y otros)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-06 08:18 |
| Actualizado | 2026-01-13 10:42 |
| Etiquetas | ninguna |
| Jira | [PED-1232](https://bluinc.atlassian.net/browse/PED-1232) |

## Relaciones

- **Padre:** [[PED-15]] Clientes
- **action item from:** [[PED-1231]] API - Refactor - Agregar RUT y EIN al dataset de tipos de documento

## Descripcion

En el alta (y edición) de cliente, el front debe validar el **formato** del documento fiscal usando una **máscara dinámica** provista por el back en

```
GET /v1/taxDocuments
```

Esto evita hardcodear formatos por país/tipo y permite agregar nuevos documentos sin cambios de

## Contexto funcional

Backend incorporará en `NewBytes_DBF.dbo.FP_DocumentosAFIP` un nuevo campo `mask` con el patrón de formato del documento (ej: CUIT `##-########-#`).
El recurso se refactoriza y ahora devuelve, por cada tipo de documento, su máscara:

`GET {API_URL}/v1/taxDocuments`

```
[
  {
    "code": 0,
    "description": "CI Policía Federal",
    "taxDocumentId": 6,
    "mask": ""
  },
  {
    "code": 80,
    "description": "CUIT",
    "taxDocumentId": 1,
    "mask": "##-########-#"
  }
]

```

Se agregan 3 tipos nuevos en `FP_DocumentosAFIP`:

- **RUT (Uruguay):** `############`


- **RUT (Chile):** `##.###.###-#`


- **EIN (USA):** `##-#######`
