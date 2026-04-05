---
jira_key: "COB-122"
aliases: ["COB-122"]
summary: "APP - Feat - Contadores para burbujas de cantidad pendientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2022-09-28 15:21"
updated: "2022-10-27 08:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-122"
---

# COB-122: APP - Feat - Contadores para burbujas de cantidad pendientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2022-09-28 15:21 |
| Actualizado | 2022-10-27 08:12 |
| Etiquetas | ninguna |
| Jira | [COB-122](https://bluinc.atlassian.net/browse/COB-122) |

## Relaciones

- **Padre:** [[COB-44 - API - Feat - Contadores para burbujas de cantidad pendientes|COB-44]] API - Feat - Contadores para burbujas de cantidad pendientes

## Descripcion

Se trata de un recurso necesario para cargar las cantidades de elementos pendientes para cada pestaña.

Las pestañas son:

- Pases realizados (Los que aun no fueron aceptados por su contraparte)


- Pases recibidos (Pases de mercadería que aun están pendientes)


- Cobrables (Los elementos cobrables que aun no fueron cobrados)



```
GET {API_URL}/v1/pendings
```

```
{
  "sentPasses":3,
  "receivedPasses":5,
  "tradables":4,
}

```
