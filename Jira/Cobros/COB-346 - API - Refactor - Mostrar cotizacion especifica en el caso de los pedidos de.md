---
jira_key: "COB-346"
aliases: ["COB-346"]
summary: "API - Refactor - Mostrar cotizacion especifica en el caso de los pedidos de libre opcion"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-09 16:25"
updated: "2023-03-10 13:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-346"
---

# COB-346: API - Refactor - Mostrar cotizacion especifica en el caso de los pedidos de libre opcion

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-09 16:25 |
| Actualizado | 2023-03-10 13:00 |
| Etiquetas | ninguna |
| Jira | [COB-346](https://bluinc.atlassian.net/browse/COB-346) |

## Relaciones

- **Padre:** [[COB-41]] APP - Feat -  Listar cobrables

## Descripcion

En caso de estar visualizando un pedido de libre opcion usaremos la cotizacion que surge de

```
SELECT nvaldiv
  FROM [NewBytes_DBF].[dbo].[pedclit]
  where cnumped = '10283909'
```
