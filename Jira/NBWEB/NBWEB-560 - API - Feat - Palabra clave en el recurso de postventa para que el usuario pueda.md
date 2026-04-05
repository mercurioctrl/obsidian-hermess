---
jira_key: "NBWEB-560"
aliases: ["NBWEB-560"]
summary: "API - Feat - Palabra clave en el recurso de postventa para que el usuario pueda visualizar la palabra de retiro"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-07-19 12:27"
updated: "2023-07-19 13:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-560"
---

# NBWEB-560: API - Feat - Palabra clave en el recurso de postventa para que el usuario pueda visualizar la palabra de retiro

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-19 12:27 |
| Actualizado | 2023-07-19 13:05 |
| Etiquetas | ninguna |
| Jira | [NBWEB-560](https://bluinc.atlassian.net/browse/NBWEB-560) |

## Relaciones

- **Padre:** [[NBWEB-559]] Palabra clave visible por el usuario para el apartaado Mi cuenta > Postventa

## Descripcion

De la misma forma que se hizo para los pedidos, agregaremos en el recurso

```
{API_URL}/v1/miCuenta/postventa
```

el parametro `secretKey` para que el ususario pueda ver la palabra clave de retiro en el caso de que exista
