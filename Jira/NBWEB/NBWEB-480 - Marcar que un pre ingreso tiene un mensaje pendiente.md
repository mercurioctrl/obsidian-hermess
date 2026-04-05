---
jira_key: "NBWEB-480"
aliases: ["NBWEB-480"]
summary: "Marcar que un pre ingreso tiene un mensaje pendiente"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2022-08-29 13:07"
updated: "2022-11-25 10:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-480"
---

# NBWEB-480: Marcar que un pre ingreso tiene un mensaje pendiente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2022-08-29 13:07 |
| Actualizado | 2022-11-25 10:22 |
| Etiquetas | ninguna |
| Jira | [NBWEB-480](https://bluinc.atlassian.net/browse/NBWEB-480) |

## Relaciones

*Sin relaciones*

## Descripcion

Se trata de informarle al cliente que tiene un mensaje pendiente. para esto agregamos un campo que se llama ‘hasMessage’ en la cabecera de las postventas. Si este viene en true es que tiene un mensaje pendiente. pense en ponerle algo como un puntito azul o algo para que se de cuenta que algo tiene y tiene q ingresar para ver.

```
{{API_URL}}/v1/miCuenta/postventa?limit=50&offset=0
```

[adjunto]
