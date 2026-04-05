---
jira_key: "PED-527"
aliases: ["PED-527"]
summary: "APP - Feat - Agregar un accionable para ver las comisiones directamente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-02-02 09:36"
updated: "2024-02-08 19:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-527"
---

# PED-527: APP - Feat - Agregar un accionable para ver las comisiones directamente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-02 09:36 |
| Actualizado | 2024-02-08 19:50 |
| Etiquetas | ninguna |
| Jira | [PED-527](https://bluinc.atlassian.net/browse/PED-527) |

## Relaciones

- **Padre:** [[PED-242 - Pestaña Estadisticas|PED-242]] Pestaña Estadisticas
- **is blocked by:** [[PED-533 - APP - Accionable para ver las comisiones directamente - Fechas no coincidentes|PED-533]] APP - Accionable para ver las comisiones directamente - Fechas no coincidentes

## Descripcion

En el DASHBOARD agregaremos un accionable en la siguiente posición

[adjunto]
Este accionable toma los parametros “vendedor” y “fecha” para hacer un salto a la seccion “comisiones”

```
{APP_URL}/comissions?currentPage=1&itemsPerPage=15&sellerId=8&between=01-01-2024_31-01-2024
```
