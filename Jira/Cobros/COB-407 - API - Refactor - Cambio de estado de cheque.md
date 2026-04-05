---
jira_key: "COB-407"
aliases: ["COB-407"]
summary: "API - Refactor - Cambio de estado de cheque "
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-04-20 13:50"
updated: "2023-04-28 07:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-407"
---

# COB-407: API - Refactor - Cambio de estado de cheque 

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-20 13:50 |
| Actualizado | 2023-04-28 07:43 |
| Etiquetas | ninguna |
| Jira | [COB-407](https://bluinc.atlassian.net/browse/COB-407) |

## Relaciones

- **Padre:** [[COB-183]] Feat - Listar cheques
- **blocks:** [[COB-408]] APP - Refactor - Cambio de estado de cheque 

## Descripcion

Se debe crear un recurso para poder hacer el cambio de estado de un cheque o varios

```
PATCH {API_URL}/v1/checks/
```

```json
[
  {
  checkId: 2352,
  newStatus:3
  },
  {
  checkId: 2352,
  newStatus:3
  },
  {
  checkId: 2352,
  newStatus:3
  }
]
```

Se debe modificar la tabla `[NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOS]` tanto los valores `ID_ESTADOCHEQUE` como aquellos correspondientes a su estado legacy (los que están con string)

**Retorna según un caso de ejemplo:**

```
{
  "status": "success",
  "message": "Se modificaron algunos de los cheques"
  "data" : {
    "success":[3434,343,434,3434,3434]
    "rejected":[4234,4324,434]
  }
}
```
