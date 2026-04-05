---
jira_key: "NBWEB-97"
aliases: ["NBWEB-97"]
summary: "Mi cuenta - Paginaciones"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-06 10:06"
updated: "2022-06-26 21:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-97"
---

# NBWEB-97: Mi cuenta - Paginaciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-06 10:06 |
| Actualizado | 2022-06-26 21:09 |
| Etiquetas | ninguna |
| Jira | [NBWEB-97](https://bluinc.atlassian.net/browse/NBWEB-97) |

## Relaciones

*Sin relaciones*

## Descripcion

Todos los recursos de lista de mi cuenta tienen que poder paginarse pasando los parametros LIMIT Y OFFSET.

Ejemplo : 

```
GET {{API_URL}}/v1/miCuenta/pedidos?limit=20&offset=100
```

En el caso de que se use el recurso de forma natural sin los parámetros

```
GET {{API_URL}}/v1/miCuenta/pedidos
```

Se deben tomar los paramtros de DEFAULTOFFSET  Y DEFAULTLIMIT desd el .env Ademas se deben agregar MAXOFFSET Y MAXLIMIT
