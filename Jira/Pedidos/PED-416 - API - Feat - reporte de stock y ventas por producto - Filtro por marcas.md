---
jira_key: "PED-416"
aliases: ["PED-416"]
summary: "API - Feat - reporte de stock y ventas por producto -> Filtro por marcas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-02 12:54"
updated: "2024-01-03 16:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-416"
---

# PED-416: API - Feat - reporte de stock y ventas por producto -> Filtro por marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-02 12:54 |
| Actualizado | 2024-01-03 16:36 |
| Etiquetas | ninguna |
| Jira | [PED-416](https://bluinc.atlassian.net/browse/PED-416) |

## Relaciones

- **Padre:** [[PED-213 - Reportes de ventas|PED-213]] Reportes de ventas
- **blocks:** [[PED-417 - APP - Feat - reporte de stock y ventas - filtro por marcas|PED-417]] APP - Feat - reporte de stock y ventas -> filtro por marcas

## Descripcion

Agregaremos un filtro de marca para afectar el reporte

```
GET /v1/reports/stocks?brandId={marca}
```
