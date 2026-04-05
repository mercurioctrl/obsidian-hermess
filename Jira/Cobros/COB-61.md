---
jira_key: "COB-61"
summary: "API - Feat - Anular un movimiento"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-18 10:27"
updated: "2022-10-20 17:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-61"
---

# COB-61: API - Feat - Anular un movimiento

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-18 10:27 |
| Actualizado | 2022-10-20 17:08 |
| Etiquetas | ninguna |
| Jira | [COB-61](https://bluinc.atlassian.net/browse/COB-61) |

## Descripción

Básicamente se busca poder anular un movimiento determinado. 

A menos que se tenga un permiso explicito, un usuario solo puede eliminar un movimiento realizado por el mismo dentro del mismo dia.

```
PATCH {API_RUL}/v1/currentAccount/{currentAccointId}
```

Esta recurso marca como anulada la operación.

Es importante que el registro quede guardado, para poder listar posteriormente las anulaciones.

Para esto solo marcaremos en la misma tabla que el movimiento esta anulado (creo que el campo existe y se llama anulado)
