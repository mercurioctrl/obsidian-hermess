---
jira_key: "PED-843"
aliases: ["PED-843"]
summary: "API - Refactor - Agregar Peso y Dimensiones a cada item en reporte de stock"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-10-15 18:24"
updated: "2024-10-16 11:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-843"
---

# PED-843: API - Refactor - Agregar Peso y Dimensiones a cada item en reporte de stock

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-10-15 18:24 |
| Actualizado | 2024-10-16 11:06 |
| Etiquetas | ninguna |
| Jira | [PED-843](https://bluinc.atlassian.net/browse/PED-843) |

## Relaciones

- **Padre:** [[PED-213]] Reportes de ventas

## Descripcion

Se debe agregar los campos 

```
PESO_KG
LARGO_CM
ANCHO_CM
ALTO_CM
```

al reporte de STOCK. tomando el dato solo de la tabla articulo, en caso de que no existan valores deben quedar vacios para se completados pos los pm.
