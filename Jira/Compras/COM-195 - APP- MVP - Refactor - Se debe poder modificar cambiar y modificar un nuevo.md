---
jira_key: "COM-195"
aliases: ["COM-195"]
summary: "APP- MVP  - Refactor - Se debe poder modificar cambiar y modificar un nuevo atributo countryId asociado a las ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Low"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-08-05 07:53"
updated: "2025-09-30 10:16"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-195"
---

# COM-195: APP- MVP  - Refactor - Se debe poder modificar cambiar y modificar un nuevo atributo countryId asociado a las ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Low |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-05 07:53 |
| Actualizado | 2025-09-30 10:16 |
| Etiquetas | MVPLaset |
| Jira | [COM-195](https://bluinc.atlassian.net/browse/COM-195) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra
- **action item from:** [[COM-194 - API- MVP - Refactor - Se debe poder modificar cambiar y modificar un nuevo|COM-194]] API- MVP  - Refactor - Se debe poder modificar cambiar y modificar un nuevo atributo countryId asosiado a las ordenes

## Descripcion

Usando el repositorio permitiremos editar el parámetro `countryId` de una orden con el recurso [link](https://bluinc.atlassian.net/browse/COM-194) 

[adjunto]
Permitiremos elegir cualquier país usando el repositorio 

```
GET {API_URL}/v1/countries
```
