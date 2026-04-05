---
jira_key: "COB-419"
aliases: ["COB-419"]
summary: "API - Feat - Cambio de estado -> Finalizado"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-04-27 09:54"
updated: "2023-04-28 07:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-419"
---

# COB-419: API - Feat - Cambio de estado -> Finalizado

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-27 09:54 |
| Actualizado | 2023-04-28 07:44 |
| Etiquetas | ninguna |
| Jira | [COB-419](https://bluinc.atlassian.net/browse/COB-419) |

## Relaciones

- **Padre:** [[COB-183 - Feat - Listar cheques|COB-183]] Feat - Listar cheques

## Descripcion

Este cambio se da cuando el banco informa que el chque fue finalizado

Refactorizaremos el recurso 

```
PATCH {API_URL}/v1/checks/
```

```
[

   {

      "checkId":328542,

      "newStatus":4,

   },

   {

      "checkId":328541,

      "newStatus":4,

   }

]
```

Puede venir desde los estados

- Depositados


- A terceros


- Vendidos
