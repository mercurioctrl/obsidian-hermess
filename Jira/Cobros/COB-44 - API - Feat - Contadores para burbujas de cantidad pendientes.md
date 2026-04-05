---
jira_key: "COB-44"
aliases: ["COB-44"]
summary: "API - Feat - Contadores para burbujas de cantidad pendientes"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2022-08-04 11:19"
updated: "2023-01-18 17:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-44"
---

# COB-44: API - Feat - Contadores para burbujas de cantidad pendientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-04 11:19 |
| Actualizado | 2023-01-18 17:14 |
| Etiquetas | ninguna |
| Jira | [COB-44](https://bluinc.atlassian.net/browse/COB-44) |

## Relaciones

- **Padre:** [[COB-21]] Base del proyecto y formularios
- **Subtarea:** [[COB-122]] APP - Feat - Contadores para burbujas de cantidad pendientes
- **Subtarea:** [[COB-167]] API - Review - Solo mostrar los pases que son de la caja logueada
- **Subtarea:** [[COB-194]] API - Review - La burbuja de pases, debe mostrar solo los pases recibido pendientes para esa cuenta.
- **Subtarea:** [[COB-372]] API - Refactor - Agregar cobros pendientes "pendingTradables"
- **Subtarea:** [[COB-373]] APP - Refactor - Agregar cobros pendientes "pendingTradables"

## Descripcion

Estas burbujas buscan dar cuenta del la cantidad de pendientes que hay en cada uno de las pestañas a ser procesadas. Son tareas que es necesario hacer para remover de la lista y dejar en cero el numero de pendiente de cada pestaña.

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



- Al ingresar a cada pestaña en la aplicación la cantidad que debo ver inicialmente, es la que se indica en la burbuja de la pestaña.
