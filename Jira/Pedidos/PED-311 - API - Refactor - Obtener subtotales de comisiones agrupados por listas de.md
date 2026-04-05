---
jira_key: "PED-311"
aliases: ["PED-311"]
summary: "API - Refactor - Obtener subtotales de comisiones agrupados por listas de precios  -> Agregar coeficientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-06 06:25"
updated: "2023-12-11 09:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-311"
---

# PED-311: API - Refactor - Obtener subtotales de comisiones agrupados por listas de precios  -> Agregar coeficientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-06 06:25 |
| Actualizado | 2023-12-11 09:57 |
| Etiquetas | ninguna |
| Jira | [PED-311](https://bluinc.atlassian.net/browse/PED-311) |

## Relaciones

- **Padre:** [[PED-242 - Pestaña Estadisticas|PED-242]] Pestaña Estadisticas
- **blocks:** [[PED-312 - APP - Refactor - Subtotales de comisiones|PED-312]] APP - Refactor - Subtotales de comisiones

## Descripcion

Agregaremos al objeto los coeficientes aplicados para cada tipo de lista

```
GET /v1/statistics/groupedCommision
```

```
{
    "applied_filters": {
        "sellerId": "8",
        "between": "7-10-2023_6-12-2023",
        "coefficient": 0.1
    },
    "comissions": {
        "A": {
            "total": 21014.932689999998,
            "count": 56,
            "coefficient": 0.2
        },
        "C": {
            "total": 949.51527,
            "count": 3,
            "coefficient": 0.3
        },
        "D": {
            "total": 150212.46636,
```
