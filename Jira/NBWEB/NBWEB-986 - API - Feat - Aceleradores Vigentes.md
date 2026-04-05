---
jira_key: "NBWEB-986"
aliases: ["NBWEB-986"]
summary: "API - Feat - Aceleradores Vigentes"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-28 08:32"
updated: "2025-07-29 10:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-986"
---

# NBWEB-986: API - Feat - Aceleradores Vigentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-28 08:32 |
| Actualizado | 2025-07-29 10:30 |
| Etiquetas | ninguna |
| Jira | [NBWEB-986](https://bluinc.atlassian.net/browse/NBWEB-986) |

## Relaciones

- **Padre:** [[NBWEB-978 - NB TRAVEL|NBWEB-978]] NB TRAVEL

## Descripcion

Obtendremos un repositorio para listar los aceleradores que se usan en [link](https://bluinc.atlassian.net/browse/NBWEB-754)  y que son los acelerados basándonos en la tabla `[NB_WEB].[dbo].[acelerators]`. El mismo podrá ser filtrado para saber cuales son los aceleradores Finalizados, Vigentes y próximos basándonos en la fecha de vencimiento e inicio. Para esto crearemos el siguiente recurso

```
GET {API_URL}/v1/miCuenta/acelerators?status={completed/current/upcoming}
```

```json
[
  {
    "id": 1,
    "txtMatch": " ",
    "acelerator": 1.0,
    "startDate": "2024-07-01T00:00:00",
    "endDate": "2024-11-15T18:30:00"
  },
  {
    "id": 2,
    "txtMatch": "notebook",
    "acelerator": 1.5,
    "startDate": "2024-07-03T00:00:00",
    "endDate": "2024-07-05T18:00:00"
  },
  {
    "id": 4,
    "txtMatch": "trust",
    "acelerator": 2.0,
    "startDate": "2024-07-15T00:00:00",
    "endDate": "2024-07-31T23:59:00"
  },
  ...
```
