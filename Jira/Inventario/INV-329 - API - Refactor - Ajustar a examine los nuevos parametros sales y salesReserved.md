---
jira_key: "INV-329"
aliases: ["INV-329"]
summary: "API - Refactor - Ajustar a \"examine\" los nuevos parametros sales y salesReserved"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-19 17:55"
updated: "2026-01-23 12:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-329"
---

# INV-329: API - Refactor - Ajustar a "examine" los nuevos parametros sales y salesReserved

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-19 17:55 |
| Actualizado | 2026-01-23 12:28 |
| Etiquetas | ninguna |
| Jira | [INV-329](https://bluinc.atlassian.net/browse/INV-329) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

Según lo realizado en [link](https://bluinc.atlassian.net/browse/INV-328)  ajustaremos el recurso

```
GET /itemsStocks/examine?itemId=121556&type=salesReserved
```

```
GET /itemsStocks/examine?itemId=121556&type=sales
```

Para poder visualizar la cantidad especificada para cada tipo de concepto/filtro
