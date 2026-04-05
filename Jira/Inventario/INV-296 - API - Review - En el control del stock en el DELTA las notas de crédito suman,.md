---
jira_key: "INV-296"
aliases: ["INV-296"]
summary: "API  - Review - En el control del stock en el DELTA las notas de crédito suman, no restan"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-21 19:16"
updated: "2025-12-26 18:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-296"
---

# INV-296: API  - Review - En el control del stock en el DELTA las notas de crédito suman, no restan

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-21 19:16 |
| Actualizado | 2025-12-26 18:14 |
| Etiquetas | ninguna |
| Jira | [INV-296](https://bluinc.atlassian.net/browse/INV-296) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios
- **has action item:** [[INV-297]] APP - Review - En stock delta el parametro NC suma, en lugar de restar

## Descripcion

Es probable que al escribir [link](https://bluinc.atlassian.net/browse/INV-242)  me confundi yo, pero ahora que lo estoy probando podemos hacer la corrección

 Para todos los casos, cuando calculamos `stockDelta` el parámetro `creditNoteReturn`** suma en lugar de restar** (como hace actualmente por como se redacto la historia)
