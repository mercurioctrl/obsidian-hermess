---
jira_key: "PEGA-109"
summary: "API - Feat - Crear repositorio en la base de datos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-12 08:50"
updated: "2024-09-16 10:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-109"
---

# PEGA-109: API - Feat - Crear repositorio en la base de datos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-12 08:50 |
| Actualizado | 2024-09-16 10:55 |
| Etiquetas | ninguna |
| Jira | [PEGA-109](https://bluinc.atlassian.net/browse/PEGA-109) |

## Descripción

Crearemos la tabla 

`PEGA.dbo.historicalCurrencyQuote`

con una estructura que albergue algo similar a esto


```json
{
  "id": 1,
  "currencyCode": "USD",
  "date": "2024-09-12",
  "buyRate": 350.50,
  "sellRate": 355.75,
  "averageRate": 353.13,
  "source": "String corto con la fuente",
  "createdAt": "2024-09-12T10:00:00"
}

```
