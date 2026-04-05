---
jira_key: "NBE-213"
aliases: ["NBE-213"]
summary: "APP - Refactor - Minificar a un solo paso reducido al formulario de registro"
status: "Listo"
type: "Tarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-09 08:05"
updated: "2025-12-09 12:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBE-213"
---

# NBE-213: APP - Refactor - Minificar a un solo paso reducido al formulario de registro

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-09 08:05 |
| Actualizado | 2025-12-09 12:54 |
| Etiquetas | ninguna |
| Jira | [NBE-213](https://bluinc.atlassian.net/browse/NBE-213) |

## Relaciones

- **Padre:** [[NBE-211 - Mejoras de usabilidad para captar clientes|NBE-211]] Mejoras de usabilidad para captar clientes
- **relates to:** [[NBE-212 - API - Refactor - Reducir campos olbigatorioso en registro dado un parametro|NBE-212]] API - Refactor - Reducir campos olbigatorioso en registro dado un parametro para tal fin en las variables globales (.env)

## Descripcion

Refactorizar el formulario de registro para que ejecute una version reducida del recurso (segun la historia [link](https://bluinc.atlassian.net/browse/NBE-212) )

```
PUT /v1/registrationRequest
```

El mismo solo contara con

- Usuario


- correo


- clave



[adjunto]
