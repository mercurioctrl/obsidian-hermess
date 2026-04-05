---
jira_key: "PED-235"
aliases: ["PED-235"]
summary: "API - Feat - Generar reporte de venta para Marcas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-11-06 10:21"
updated: "2024-01-04 17:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-235"
---

# PED-235: API - Feat - Generar reporte de venta para Marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-06 10:21 |
| Actualizado | 2024-01-04 17:33 |
| Etiquetas | ninguna |
| Jira | [PED-235](https://bluinc.atlassian.net/browse/PED-235) |

## Relaciones

- **Padre:** [[PED-213]] Reportes de ventas
- **blocks:** [[PED-248]] APP - Feat - Agregar accionables para descargar reporte de ventas y de marcas
- **is blocked by:** [[PED-266]] API - Generar reporte de venta para Marcas - Incidencias varias

## Descripcion

```
GET {API_URL}/v1/reports/salesBrands
```

Basándonos en un repositorio similar (origen de los datos) al utilizado anteriormente ([link](https://lioteam.atlassian.net/browse/PED-215) ) se debe conseguir un reporte como el que se adjunto en ele ejemplo.

El mismo debe poder filtrar por

- Intervalo de fechas


- Marca
