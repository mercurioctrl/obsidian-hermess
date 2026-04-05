---
jira_key: "NBWEB-169"
summary: "Revisar parametro Novedades para la home del sitio"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-05 11:23"
updated: "2022-06-26 21:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-169"
---

# NBWEB-169: Revisar parametro Novedades para la home del sitio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-05 11:23 |
| Actualizado | 2022-06-26 21:09 |
| Etiquetas | ninguna |
| Jira | [NBWEB-169](https://bluinc.atlassian.net/browse/NBWEB-169) |

## Descripción

Al ejecutar el recurso trae todos los productos, cuando en rrealidad deberia solo traer 10

```
GET /v1/?novedades=1
```

En la tabla de articulos, seguro hay una columna llamada ULTIMO_INGRESO ques e puede utilizar para este fin
