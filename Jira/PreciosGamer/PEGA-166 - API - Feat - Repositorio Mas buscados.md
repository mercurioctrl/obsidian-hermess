---
jira_key: "PEGA-166"
aliases: ["PEGA-166"]
summary: "API - Feat - Repositorio \"Mas buscados\""
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-01-08 09:44"
updated: "2025-01-27 17:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-166"
---

# PEGA-166: API - Feat - Repositorio "Mas buscados"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-08 09:44 |
| Actualizado | 2025-01-27 17:32 |
| Etiquetas | ninguna |
| Jira | [PEGA-166](https://bluinc.atlassian.net/browse/PEGA-166) |

## Relaciones

- **Padre:** [[PEGA-1]] Bases y repositorios
- **has action item:** [[PEGA-169]] APP - Feat - Los mas buscados (sitio privado con token)

## Descripcion

Basándonos en una consulta similar a esta

```sql
SELECT keywords
    , count(*)
FROM [PEGA].[dbo].[searchQueries]
WHERE [date] BETWEEN '01-06-2025 00:00' AND '01-08-2025 00:00'
GROUP BY keywords
HAVING count(*) > 1
ORDER BY count(*) DESC
```

Obtendremos un objeto similar al siguiente

```
GET {API_URL}/v1/rankingSearch?between={intervaloDeFechas}&token={token}
```

Lo que mostraremos es la búsqueda de agrupada contando la cantidad de ocurrencias de la búsqueda en un intervalo `{intervaloDeFechas}` de fechas determinado.

Lleva token porque es informacion sensible, el token esta en el .env

Si `{intervaloDeFechas}` no esta presente, entonces muestro el ultimo mes.

**Devuelva**

```
[
  {
    "keywords": "placa_de_video",
    "occurrences": 883
  },
  {
    "keywords": "procesador",
    "occurrences": 869
  },
  {
    "keywords": "memoria",
    "occurrences": 818
  },
  {
    "keywords": "fuente",
    "occurrences": 815
  },
  {
    "keywords": "mother",
    "occurrences": 807
  },
  {
    "keywords": "ssd",
    "occurrences": 98
  },
  {
    "keywords": "monitor",
    "occurrences": 72
  },
  {
    "keywords": "gabinete",
    "occurrences": 52
  },
  {
    "keywords": "cooler",
    "occurrences": 48
  },
  {
    "keywords": "teclado",
    "occurrences": 38
  },
  {
    "keywords": "notebook",
    "occurrences": 31
  },
  {
    "keywords": "4060",
    "occurrences": 27
  },
  {
  
  ...
```
