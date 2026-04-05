---
jira_key: "NBWEB-618"
summary: "API - Feat - Leer hard token -> Agregar fecha de creacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-22 09:45"
updated: "2024-01-26 05:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-618"
---

# NBWEB-618: API - Feat - Leer hard token -> Agregar fecha de creacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-22 09:45 |
| Actualizado | 2024-01-26 05:28 |
| Etiquetas | ninguna |
| Jira | [NBWEB-618](https://bluinc.atlassian.net/browse/NBWEB-618) |

## Descripción

Usando la columna creada en [link](https://lioteam.atlassian.net/browse/NBWEB-616) agregaremos la fecha al objeto.

```
{{API_URL}}/v1/miCuenta/readToken
```

```
{
    "token": "fe5ba42e32632445a23580990a111662",
    "creationDate": "01/01/2024"
}
```
