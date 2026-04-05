---
jira_key: "NBWEB-496"
aliases: ["NBWEB-496"]
summary: "API - Feat - Recurso de reenvió de correo con palabra clave"
status: "Code Review"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-07 08:53"
updated: "2022-11-07 12:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-496"
---

# NBWEB-496: API - Feat - Recurso de reenvió de correo con palabra clave

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-07 08:53 |
| Actualizado | 2022-11-07 12:45 |
| Etiquetas | ninguna |
| Jira | [NBWEB-496](https://bluinc.atlassian.net/browse/NBWEB-496) |

## Relaciones

- **Padre:** [[NBWEB-495 - API - Features especiales|NBWEB-495]] API - Features especiales
- **Subtarea:** [[NBWEB-506 - API - Refactor - Se debe enviar una notificacion a la gerencia|NBWEB-506]] API - Refactor - Se debe enviar una notificacion a la gerencia

## Descripcion

Este recurso solo puede ejecutarse con login de nivel administrativo

```
{{API_URL}}/v1/cms/resubmitKeyword
```

Recibe

```
[
{
  branch: '0002',
  order: '0000345',
}
]
```
