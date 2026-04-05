---
jira_key: "COB-98"
aliases: ["COB-98"]
summary: "API - Feat - Editar comentario en movimiento de caja"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-14 09:41"
updated: "2022-10-25 09:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-98"
---

# COB-98: API - Feat - Editar comentario en movimiento de caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-14 09:41 |
| Actualizado | 2022-10-25 09:02 |
| Etiquetas | ninguna |
| Jira | [COB-98](https://bluinc.atlassian.net/browse/COB-98) |

## Relaciones

- **Padre:** [[COB-3]] API - Feat - Listar movimiento por caja
- **blocks:** [[COB-99]] APP - Feat - Editar comentario en movimiento de caja

## Descripcion

Se trata de la opción para editar el comentario, o bien agregarlo (siempre existe en realidad pero esta vació)

```
PATCH {API_URL}/v1/box/{idMovimiento}
```

```
{
  comment: 'Se envia comentario de prueba'
}
```
