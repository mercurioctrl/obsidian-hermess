---
jira_key: "POS-173"
aliases: ["POS-173"]
summary: "Despachar una postventa"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2022-10-05 13:38"
updated: "2022-10-18 14:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-173"
---

# POS-173: Despachar una postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2022-10-05 13:38 |
| Actualizado | 2022-10-18 14:21 |
| Etiquetas | ninguna |
| Jira | [POS-173](https://bluinc.atlassian.net/browse/POS-173) |

## Relaciones

*Sin relaciones*

## Descripcion

Se trata del recurso para despachar una orden una vez finalizada

```
{{API_URL}}/v1/afterSales/{aftersaleid}/finalized/dispatch
```

```
{
    "secretKey": "mar",
    "receiverName": "Ezequiel Manzano",//opcional (si no mandar vacio)
    "receiverDni": 39626870 //opcional (si no mandar vacio)
}
```



Esto cambiaria el estado a despachado por lo tanto se debe acutalizar la fila en el listado.
