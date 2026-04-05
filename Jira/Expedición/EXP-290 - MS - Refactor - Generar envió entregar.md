---
jira_key: "EXP-290"
aliases: ["EXP-290"]
summary: "MS - Refactor - Generar envió entregar"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-05-22 09:10"
updated: "2023-05-23 13:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-290"
---

# EXP-290: MS - Refactor - Generar envió entregar

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-22 09:10 |
| Actualizado | 2023-05-23 13:05 |
| Etiquetas | ninguna |
| Jira | [EXP-290](https://bluinc.atlassian.net/browse/EXP-290) |

## Relaciones

- **Padre:** [[EXP-289 - Refactor Entregar|EXP-289]] Refactor Entregar

## Descripcion

Haremos un refactor del recurso

```
POST {{API_URL}}/addTrackingOrder/nb
```

```
{
    "branch": "0002",
    "order": "10290322",
    "packageGroup": 1,
    "assignValue": false
}
```

Para incorporar envíos que tienen como `medioDeEnvioId` de Entregar
