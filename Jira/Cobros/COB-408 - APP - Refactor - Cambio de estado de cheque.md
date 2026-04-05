---
jira_key: "COB-408"
aliases: ["COB-408"]
summary: "APP - Refactor - Cambio de estado de cheque "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-04-20 13:50"
updated: "2023-04-28 07:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-408"
---

# COB-408: APP - Refactor - Cambio de estado de cheque 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-20 13:50 |
| Actualizado | 2023-04-28 07:43 |
| Etiquetas | ninguna |
| Jira | [COB-408](https://bluinc.atlassian.net/browse/COB-408) |

## Relaciones

- **Padre:** [[COB-183]] Feat - Listar cheques
- **is blocked by:** [[COB-407]] API - Refactor - Cambio de estado de cheque 

## Descripcion

Utilizaremos el recurso

```
PATCH {API_URL}/v1/checks/
```

Para construir una carga útil que nos permita alterar el estado, de uno o mas cheques mediante el selector izquierdo del listado.

Se debe agregar un accionable (o boton derecho, como prefieras) al seleccionar uno o mas cheques y levantar un modal que contendrá un selector con el repositorio 

```
{{API_URL}}/v1/checkStatus
```

Y los cheques que intentaran ser modificados.

Construiremos un una carga útil con la siguiente forma

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
