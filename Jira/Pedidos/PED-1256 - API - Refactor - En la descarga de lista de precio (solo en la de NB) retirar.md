---
jira_key: "PED-1256"
aliases: ["PED-1256"]
summary: "API - Refactor - En la descarga de lista de precio (solo en la de NB) retirar ultimas columnas"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-14 07:11"
updated: "2026-01-14 11:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1256"
---

# PED-1256: API - Refactor - En la descarga de lista de precio (solo en la de NB) retirar ultimas columnas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-14 07:11 |
| Actualizado | 2026-01-14 11:53 |
| Etiquetas | ninguna |
| Jira | [PED-1256](https://bluinc.atlassian.net/browse/PED-1256) |

## Relaciones

- **Padre:** [[PED-191 - Descargar Listado de precios|PED-191]] Descargar Listado de precios

## Descripcion

Cuando ejecutamos el recurso

```
https://api2.orders.lio.red/v1/download/priceList?type=xlsx
```

Ocultaremos por ahora las columnas `F`, `G`

[adjunto]
Ojo, hay otro recurso que es `type=xlsxb` que es el de LASET, ese no hay que tocarlo
