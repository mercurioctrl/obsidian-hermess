---
jira_key: "PED-840"
aliases: ["PED-840"]
summary: "API - Refactor - Mostrar estadisticas de venta filtrando por string especifico"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-10-04 06:29"
updated: "2024-11-05 02:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-840"
---

# PED-840: API - Refactor - Mostrar estadisticas de venta filtrando por string especifico

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-04 06:29 |
| Actualizado | 2024-11-05 02:12 |
| Etiquetas | ninguna |
| Jira | [PED-840](https://bluinc.atlassian.net/browse/PED-840) |

## Relaciones

- **Padre:** [[PED-242 - Pestaña Estadisticas|PED-242]] Pestaña Estadisticas
- **has action item:** [[PED-841 - APP - Refactor - Filtrar estadisticas tambien por string si esta presente|PED-841]] APP - Refactor - Filtrar estadisticas tambien por string si esta presente
- **is blocked by:** [[PED-856 - API - Mostrar estadísticas de venta filtrando por string específico - Valores|PED-856]] API - Mostrar estadísticas de venta filtrando por string específico - Valores no coincidentes

## Descripcion

Modificaremos los recursos de estadística para que los mismos sean sensibles a un filtro por string, como ya lo son a marcas y categorías (busca en `articulo.cDetalle`)

```
GET /v1/statistics/totalSales
```

```
GET /v1/statistics/averageTicket
```

```
GET /v1/statistics/totalBilled
```

```
GET /v1/statistics/customerConversionRate
```

```
GET /v1/statistics/customerReactivationRate
```



[adjunto]
